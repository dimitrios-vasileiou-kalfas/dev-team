"""
Main CrewAI entry point for Strategy & Planning Crew

This file is used by `crewai` CLI commands (train, replay, test).
For full pipeline execution, use: python src/dev_team/orchestrator.py

The project uses a two-crew architecture:
- This file: Strategy Crew (Competitor analysis + Market research + Product roadmap)
- crews/development_crew.py: Development Crew (Architecture + Implementation + Testing)

Configuration:
- Uses ollama/qwen2.5-coder:14b models (configured in agents.yaml)
- Sequential execution with task dependencies
- Outputs to outputs/analysis/
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from dev_team.tools.custom_tool import FileReaderTool, DirectoryListTool, FindFilesTool


@CrewBase
class DevTeam():
    """
    Strategy & Planning Crew (Main entry point for CrewAI CLI)

    This matches the StrategyCrew but is named DevTeam for CLI compatibility.

    Agents:
    - Market Researcher: Analyzes user needs, market gaps, niche opportunities
    - Competitor Analyst: Analyzes competitor plugin technically
    - Product Manager: Creates milestone-based roadmap

    Execution Order:
    1. analyze_competitor (identifies what the product does)
    2. research_market (product-specific market research)
    3. create_roadmap (synthesizes into actionable roadmap)
    """

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/strategy_tasks.yaml'

    @agent
    def market_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['market_researcher'],
            verbose=True
        )

    @agent
    def competitor_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['competitor_analyst'],
            tools=[
                DirectoryListTool(),
                FileReaderTool(),
                FindFilesTool()
            ],
            verbose=True
        )

    @agent
    def product_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['product_manager'],
            verbose=True
        )

    @task
    def analyze_competitor(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_competitor'],
        )

    @task
    def research_market(self) -> Task:
        return Task(
            config=self.tasks_config['research_market'],
            context=[self.analyze_competitor()]  # Uses competitor analysis as context
        )

    @task
    def create_roadmap(self) -> Task:
        return Task(
            config=self.tasks_config['create_roadmap'],
            context=[self.analyze_competitor(), self.research_market()]  # Uses both as context
        )

    @crew
    def crew(self) -> Crew:
        """
        Creates the Strategy & Planning crew with enhanced configuration

        Configuration:
        - Process: Sequential (tasks run in order with dependencies)
        - Memory: Enabled (agents remember context)
        - Cache: Enabled (avoid redundant LLM calls)
        - Verbose: Full output for transparency
        """
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            memory=True,  # Enable memory for better context retention
            cache=True,   # Enable caching to save on LLM calls
            max_rpm=10,   # Rate limit: max 10 requests per minute to Ollama
        )
