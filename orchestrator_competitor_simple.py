#!/usr/bin/env python3
"""
Multi-Run Competitor Analyst - Simple Pattern

Runs ONLY the competitor_analyst agent 5 times using the task iteration pattern.

Usage:
    python orchestrator_competitor_simple.py
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from crewai import Agent, Task, Crew, Process
from dev_team.tools.custom_tool import FileReaderTool, DirectoryListTool, FindFilesTool
import yaml

def main():
    # Paths
    competitor_path = str(Path('inputs/competitor-plugin').resolve())
    skeleton_path = str(Path('inputs/skeleton-plugin').resolve())

    # Load configs
    with open('src/dev_team/config/agents.yaml') as f:
        agents_config = yaml.safe_load(f)

    with open('src/dev_team/config/strategy_tasks.yaml') as f:
        tasks_config = yaml.safe_load(f)

    # Create competitor_analyst agent
    agent_config = agents_config['competitor_analyst']

    competitor_analyst = Agent(
        role=agent_config['role'],
        goal=agent_config['goal'],
        backstory=agent_config['backstory'],
        llm=agent_config['llm'],
        max_iter=agent_config.get('max_iter', 60),
        verbose=agent_config.get('verbose', True),
        allow_delegation=agent_config.get('allow_delegation', False),
        tools=[
            DirectoryListTool(),
            FileReaderTool(),
            FindFilesTool()
        ]
    )

    # Get task config
    task_config = tasks_config['analyze_competitor']
    base_description = task_config['description']

    # Replace placeholders
    base_description = base_description.replace('{competitor_plugin_path}', competitor_path)
    base_description = base_description.replace('{skeleton_plugin_path}', skeleton_path)

    tasks = []

    # Create 5 tasks for the same agent
    print("\n" + "="*70)
    print("Creating 5 analysis tasks for competitor_analyst")
    print("="*70 + "\n")

    for i in range(5):
        task = Task(
            description=f"""
**ANALYSIS RUN {i+1}/5**

{base_description}

**Special Instructions for Run {i+1}:**
- This is run {i+1} of 5 independent analyses
- Focus on finding items that might be missed in other runs
- Be thorough - different runs may focus on different aspects
- Save output to outputs/analysis/run{i+1}-technical-analysis.md
            """,
            expected_output=task_config['expected_output'],
            agent=competitor_analyst,
            output_file=f'outputs/analysis/run{i+1}-technical-analysis.md'
        )
        tasks.append(task)
        print(f"✓ Created task {i+1}/5")

    # Create crew with all tasks
    print(f"\n{'='*70}")
    print("Creating crew with 1 agent and 5 tasks")
    print(f"{'='*70}\n")

    crew = Crew(
        agents=[competitor_analyst],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    # Run the crew
    print(f"\n{'='*70}")
    print("Starting 5 sequential analysis runs...")
    print(f"{'='*70}\n")

    result = crew.kickoff()

    print(f"\n{'='*70}")
    print("✓ All 5 runs complete!")
    print(f"{'='*70}\n")
    print("Output files:")
    for i in range(1, 6):
        print(f"  • outputs/analysis/run{i}-technical-analysis.md")
    print("\nNext step: Merge results with voting logic")
    print("Run: python merge_results.py")

if __name__ == '__main__':
    main()

