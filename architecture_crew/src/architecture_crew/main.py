#!/usr/bin/env python
import sys
import warnings
from pathlib import Path

from architecture_crew.crew import ArchitectureCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Architecture Crew - WordPress Plugin System Design
#
# This crew designs the complete system architecture:
# 1. Reads strategy outputs (analysis, research, roadmap)
# 2. Designs high-level architecture
# 3. Creates complete folder structure (JSON)
# 4. Generates backend class specifications
# 5. Generates frontend component specifications
#
# Usage:
#   crewai run                    # Run architecture design

def run():
    """
    Run the Architecture Crew to design the plugin system.

    Prerequisites:
    - Strategy crew outputs must exist in ../outputs/strategy/
    - Skeleton plugin must be accessible via inputs/skeleton-plugin/

    Outputs (in shared folder):
    - ../outputs/architecture/strategy-summary.md
    - ../outputs/architecture/high-level-architecture.md
    - ../outputs/architecture/folder-structure.json
    - ../outputs/architecture/specs/backend/*.md
    - ../outputs/architecture/specs/frontend/*.md
    """
    # Compute project root dynamically
    # main.py is at: architecture_crew/src/architecture_crew/main.py
    # Go up 3 levels to reach dev-team root
    project_root = Path(__file__).parent.parent.parent.parent

    # Verify strategy outputs exist (in shared folder)
    strategy_outputs_path = project_root / "outputs" / "strategy"
    if not strategy_outputs_path.exists():
        print(f"\n⚠️  ERROR: Strategy outputs not found at: {strategy_outputs_path}")
        print("   Please run Strategy Crew first:")
        print(f"   cd {project_root}/strategy_crew && crewai run")
        return

    # Check for required files (in shared folder)
    required_files = [
        strategy_outputs_path / "plugin-metadata.json",
        strategy_outputs_path / "technical-analysis.md",
        strategy_outputs_path / "market-research.md",
        strategy_outputs_path / "product-roadmap.md"
    ]

    missing_files = []
    for file_path in required_files:
        if not file_path.exists():
            missing_files.append(file_path)

    if missing_files:
        print(f"\n⚠️  ERROR: Missing required input files:")
        for file in missing_files:
            print(f"   - {file}")
        print("\n   Run Strategy Crew first to generate these files:")
        print(f"   cd {project_root}/strategy_crew && crewai run")
        return

    # Verify skeleton plugin exists
    skeleton_path = project_root / "inputs" / "skeleton-plugin"
    if not skeleton_path.exists():
        print(f"\n⚠️  ERROR: Skeleton plugin not found at: {skeleton_path}")
        print("   Please create symlink:")
        print(f"   cd {project_root}/inputs && ln -s ~/Projects/my-projects/wp-plugin-skeleton skeleton-plugin")
        return

    inputs = {
        'strategy_outputs_path': str(strategy_outputs_path),
        'skeleton_plugin_path': str(skeleton_path)
    }

    try:
        print("\n" + "="*80)
        print("🏗️  ARCHITECTURE CREW - STARTING")
        print("="*80)
        print("\nDesigning plugin architecture...")
        print(f"Strategy inputs: {strategy_outputs_path}")
        print(f"Skeleton plugin: {skeleton_path}\n")

        result = ArchitectureCrew().crew().kickoff(inputs=inputs)

        print("\n" + "="*80)
        print("✅ ARCHITECTURE CREW COMPLETE")
        print("="*80)
        print("\n📋 Outputs created:")
        print("   - ../outputs/architecture/strategy-summary.md")
        print("   - ../outputs/architecture/high-level-architecture.md")
        print("   - ../outputs/architecture/folder-structure.json")
        print("   - ../outputs/architecture/specs/backend/*.md")
        print("   - ../outputs/architecture/specs/frontend/*.md")
        print("\n🎯 Next steps:")
        print("   1. Review high-level architecture")
        print("   2. Verify folder-structure.json is valid JSON")
        print("   3. Check backend and frontend specs are detailed")
        print("   4. Use outputs as input for Development Crew\n")

        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'strategy_outputs_path': '../outputs/strategy',
        'skeleton_plugin_path': '../inputs/skeleton-plugin'
    }
    try:
        ArchitectureCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        ArchitectureCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'strategy_outputs_path': '../outputs/strategy',
        'skeleton_plugin_path': '../inputs/skeleton-plugin'
    }

    try:
        ArchitectureCrew().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

