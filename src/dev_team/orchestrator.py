#!/usr/bin/env python
"""
WordPress Plugin Development Orchestrator

Runs two crews sequentially with a human review checkpoint:
1. Strategy Crew: Competitor analysis + product roadmap
2. Development Crew: Architecture + Implementation + Testing

After Strategy Crew completes, you must review the analysis and create
an APPROVED.txt file before proceeding to development.
"""
from pathlib import Path
from dev_team.crews.strategy_crew import StrategyCrew
from dev_team.crews.development_crew import DevelopmentCrew


def run_strategy_phase(competitor_path: str, skeleton_path: str):
    """
    Run Strategy & Planning Crew

    Outputs:
    - outputs/analysis/market-research.md
    - outputs/analysis/technical-analysis.md
    - outputs/analysis/product-roadmap.md
    - outputs/analysis/milestones/*.md
    """
    print("\n" + "="*80)
    print("🎯 PHASE 1: STRATEGY & PLANNING")
    print("="*80)
    print("\nAnalyzing market, competitor plugin, and creating product roadmap...")
    print(f"Competitor: {competitor_path}")
    print(f"Skeleton: {skeleton_path}\n")

    inputs = {
        'competitor_plugin_path': competitor_path,
        'skeleton_plugin_path': skeleton_path
    }

    strategy_crew = StrategyCrew().crew()
    result = strategy_crew.kickoff(inputs=inputs)

    print("\n" + "="*80)
    print("✅ STRATEGY PHASE COMPLETE")
    print("="*80)
    print("\n📋 REVIEW REQUIRED:")
    print("   1. Check outputs/analysis/market-research.md")
    print("   2. Check outputs/analysis/technical-analysis.md")
    print("   3. Check outputs/analysis/product-roadmap.md")
    print("   4. Check outputs/analysis/milestones/")
    print("\n   If approved, create: outputs/analysis/APPROVED.txt")
    print("   Then run development phase.\n")

    return result


def run_development_phase(competitor_path: str, skeleton_path: str, milestone: str = "milestone-1-mvp"):
    """
    Run Development & QA Crew for a specific milestone

    Requires: outputs/analysis/APPROVED.txt must exist

    Outputs:
    - outputs/plugin/ (complete WordPress plugin structure)
    """
    # Check for approval
    approval_file = Path("outputs/analysis/APPROVED.txt")
    if not approval_file.exists():
        print("\n❌ ERROR: No approval found!")
        print("   Create outputs/analysis/APPROVED.txt after reviewing strategy outputs.")
        return None

    print("\n" + "="*80)
    print(f"🚀 PHASE 2: DEVELOPMENT - {milestone.upper()}")
    print("="*80)
    print(f"\nDeveloping milestone: {milestone}")
    print(f"Skeleton: {skeleton_path}\n")

    inputs = {
        'competitor_plugin_path': competitor_path,
        'skeleton_plugin_path': skeleton_path,
        'current_milestone': milestone
    }

    dev_crew = DevelopmentCrew().crew()
    result = dev_crew.kickoff(inputs=inputs)

    print("\n" + "="*80)
    print(f"✅ DEVELOPMENT COMPLETE - {milestone.upper()}")
    print("="*80)
    print("\n📦 Plugin generated at: outputs/plugin/")
    print("   Backend (PHP): outputs/plugin/includes/, outputs/plugin/src/")
    print("   Frontend (React): outputs/plugin/admin-react/")
    print("   Tests: outputs/plugin/tests/\n")

    return result


def run_full_pipeline(competitor_path: str, skeleton_path: str, milestone: str = "milestone-1-mvp"):
    """
    Run complete pipeline: Strategy → Review Checkpoint → Development

    Args:
        competitor_path: Path to competitor plugin folder
        skeleton_path: Path to skeleton plugin folder
        milestone: Which milestone to develop (default: milestone-1-mvp)
    """
    # Phase 1: Strategy
    strategy_result = run_strategy_phase(competitor_path, skeleton_path)

    # Human checkpoint
    print("\n" + "="*80)
    print("⏸️  HUMAN REVIEW CHECKPOINT")
    print("="*80)

    approval_file = Path("outputs/analysis/APPROVED.txt")

    if approval_file.exists():
        print("\n✅ Approval found - proceeding to development...")
    else:
        print("\nWaiting for approval...")
        while not approval_file.exists():
            input("\nPress Enter after creating APPROVED.txt (or Ctrl+C to exit)...")
            if not approval_file.exists():
                print("❌ APPROVED.txt not found. Please create it to continue.")

    # Phase 2: Development
    dev_result = run_development_phase(competitor_path, skeleton_path, milestone)

    print("\n" + "="*80)
    print("🎉 PIPELINE COMPLETE")
    print("="*80)
    print("\nYour WordPress plugin is ready at: outputs/plugin/")

    return dev_result


if __name__ == "__main__":
    # Example usage - update these paths
    competitor = "inputs/competitor-plugin"
    skeleton = "inputs/skeleton-plugin"

    # Verify paths exist
    if not Path(competitor).exists():
        print(f"⚠️  Competitor plugin not found: {competitor}")
        print("   Please add competitor plugin to inputs/competitor-plugin/")
        exit(1)

    if not Path(skeleton).exists():
        print(f"⚠️  Skeleton plugin not found: {skeleton}")
        print("   Please add skeleton plugin to inputs/skeleton-plugin/")
        exit(1)

    # Run pipeline
    run_full_pipeline(competitor, skeleton)

