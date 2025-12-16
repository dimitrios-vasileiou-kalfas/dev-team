#!/usr/bin/env python
import sys
import warnings
from pathlib import Path

from dev_team.orchestrator import run_full_pipeline

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# WordPress Plugin Development Workflow
#
# This project uses a two-crew architecture:
# 1. Strategy Crew: Competitor analysis + Product roadmap
# 2. Development Crew: Architecture + Implementation + Testing
#
# Usage:
#   crewai run                    # Run full pipeline with checkpoint

def run():
    """
    Run the complete WordPress plugin development pipeline.

    This runs both crews with a human review checkpoint:
    1. Strategy Crew analyzes competitor and creates roadmap
    2. Wait for human approval (APPROVED.txt)
    3. Development Crew implements milestone features
    """
    competitor_path = "inputs/competitor-plugin"
    skeleton_path = "inputs/skeleton-plugin"

    # Verify input paths exist
    if not Path(competitor_path).exists():
        print(f"\n⚠️  ERROR: Competitor plugin not found at: {competitor_path}")
        print("   Please add your competitor plugin to this folder.\n")
        return

    if not Path(skeleton_path).exists():
        print(f"\n⚠️  ERROR: Skeleton plugin not found at: {skeleton_path}")
        print("   Please add your skeleton plugin to this folder.\n")
        return

    try:
        run_full_pipeline(
            competitor_path=competitor_path,
            skeleton_path=skeleton_path,
            milestone="milestone-1-mvp"
        )
    except Exception as e:
        raise Exception(f"An error occurred while running the pipeline: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    from dev_team.crews.strategy_crew import StrategyCrew

    inputs = {
        'competitor_plugin_path': 'inputs/competitor-plugin',
        'skeleton_plugin_path': 'inputs/skeleton-plugin'
    }
    try:
        StrategyCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    from dev_team.crews.strategy_crew import StrategyCrew

    try:
        StrategyCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    from dev_team.crews.strategy_crew import StrategyCrew

    inputs = {
        'competitor_plugin_path': 'inputs/competitor-plugin',
        'skeleton_plugin_path': 'inputs/skeleton-plugin'
    }
    
    try:
        StrategyCrew().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
