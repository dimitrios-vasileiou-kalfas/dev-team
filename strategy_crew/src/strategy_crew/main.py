#!/usr/bin/env python
import sys
import warnings
from pathlib import Path

from strategy_crew.crew import StrategyCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Strategy Crew - WordPress Plugin Analysis & Roadmap
#
# This crew analyzes competitor plugins and creates strategic roadmaps:
# 1. Competitor Analyst: Performs systematic technical analysis
# 2. Market Researcher: Identifies market gaps and niche opportunities
# 3. Product Manager: Creates milestone-based product roadmap with plugin naming
#
# Usage:
#   crewai run                    # Run strategy analysis

def run():
    """
    Run the Strategy & Planning crew to analyze competitor plugin and create roadmap.

    Outputs:
    - outputs/technical-analysis.md
    - outputs/market-research.md
    - outputs/product-roadmap.md
    - outputs/plugin-metadata.json (NEW: includes plugin name, slug, namespace)
    """
    # Paths relative to strategy_crew root (when running from strategy_crew/)
    competitor_path = "inputs/competitor-plugin"
    skeleton_path = "inputs/skeleton-plugin"

    # Verify input paths exist
    if not Path(competitor_path).exists():
        print(f"\n⚠️  ERROR: Competitor plugin not found at: {competitor_path}")
        print("   Please make sure symlinks are created in inputs/ folder.\n")
        return

    if not Path(skeleton_path).exists():
        print(f"\n⚠️  ERROR: Skeleton plugin not found at: {skeleton_path}")
        print("   Please make sure symlinks are created in inputs/ folder.\n")
        return

    inputs = {
        'competitor_plugin_path': competitor_path,
        'skeleton_plugin_path': skeleton_path
    }

    try:
        result = StrategyCrew().crew().kickoff(inputs=inputs)

        print("\n" + "="*80)
        print("✅ STRATEGY CREW COMPLETE")
        print("="*80)
        print("\n📋 Outputs created:")
        print("   - outputs/technical-analysis.md")
        print("   - outputs/market-research.md")
        print("   - outputs/product-roadmap.md")
        print("   - outputs/plugin-metadata.json")
        print("\n🎯 Next steps:")
        print("   1. Review the analysis and roadmap")
        print("   2. Use outputs as input for Architecture Crew")
        print("   3. Proceed with implementation\n")

        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
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
    try:
        StrategyCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'competitor_plugin_path': 'inputs/competitor-plugin',
        'skeleton_plugin_path': 'inputs/skeleton-plugin'
    }

    try:
        StrategyCrew().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

