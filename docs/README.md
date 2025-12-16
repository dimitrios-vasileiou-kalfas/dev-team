# Documentation

This folder contains detailed documentation about the WordPress Plugin Development Team project.

## Quick Reference

| Document | Description |
|----------|-------------|
| [SETUP_COMPLETE.md](SETUP_COMPLETE.md) | Complete setup guide and what was configured |
| [COMPLETE_SUMMARY.md](COMPLETE_SUMMARY.md) | Full project overview with all 8 agents and workflow |
| [MARKET_RESEARCHER_ADDED.md](MARKET_RESEARCHER_ADDED.md) | Details about the Market Researcher agent addition |
| [NICHE_AND_LOCALIZATION_ENHANCED.md](NICHE_AND_LOCALIZATION_ENHANCED.md) | Niche market & localization focus explanation |
| [CREW2_DISABLED.md](CREW2_DISABLED.md) | How to run analysis-only mode (Development disabled) |

## Start Here

**New to the project?** → Read [SETUP_COMPLETE.md](SETUP_COMPLETE.md)

**Want the full picture?** → Read [COMPLETE_SUMMARY.md](COMPLETE_SUMMARY.md)

**Interested in the niche strategy?** → Read [NICHE_AND_LOCALIZATION_ENHANCED.md](NICHE_AND_LOCALIZATION_ENHANCED.md)

**Only want analysis?** → Read [CREW2_DISABLED.md](CREW2_DISABLED.md)

## Document Details

### SETUP_COMPLETE.md
Your getting started guide. Explains:
- The 8 AI agents and their roles
- Project structure
- How to run the pipeline
- Expected outputs
- Next steps

### COMPLETE_SUMMARY.md
The comprehensive overview covering:
- Full architecture (2 crews, 8 agents)
- Complete workflow
- Real-world examples
- Strategic advantages
- Quick start commands

### MARKET_RESEARCHER_ADDED.md
Explains the Market Researcher agent:
- What it does (user needs, market gaps, feature demand)
- Why it was added (business perspective, not just technical)
- How it works with other agents
- Example insights it provides

### NICHE_AND_LOCALIZATION_ENHANCED.md
Deep dive into niche market strategy:
- Why niche specialization matters
- Examples (Greek eshops, healthcare, real estate)
- Regional opportunities (Greek market, German market, etc.)
- How the agent identifies niches
- Strategic positioning examples
- Revenue opportunities

### CREW2_DISABLED.md
How to use analysis-only mode:
- Run only Strategy & Planning crew
- Skip development temporarily
- Perfect for market validation
- How to re-enable full pipeline

## Project Architecture

```
WordPress Plugin AI Development Team
├── Crew 1: Strategy & Planning
│   ├── Market Researcher (User needs, niches, localization)
│   ├── Competitor Analyst (Technical analysis)
│   └── Product Manager (Roadmap & milestones)
│
└── Crew 2: Development & QA
    ├── Software Architect (Architecture design)
    ├── WordPress Backend Dev (PHP implementation)
    ├── React Frontend Dev (React/MUI implementation)
    ├── Code Reviewer (Quality assurance)
    └── QA Engineer (Testing & validation)
```

## Quick Commands

```bash
# Run analysis only (Crew 1)
crewai run

# Run full pipeline (both crews)
python src/dev_team/orchestrator.py

# Train the crew
crewai train

# Test the crew
crewai test
```

## Contributing

When adding new documentation:
1. Create the markdown file in this `docs/` folder
2. Add an entry to this README
3. Update the Quick Reference table
4. Keep it organized and accessible

---

**For more information, see the main [README.md](../README.md) in the project root.**

