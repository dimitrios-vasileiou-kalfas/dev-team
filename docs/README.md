# Documentation

This folder contains detailed documentation about the WordPress Plugin Development Team project.

## Quick Reference

| Document | Description |
|----------|-------------|
| [SETUP_COMPLETE.md](SETUP_COMPLETE.md) | Complete setup guide and what was configured |
| [COMPLETE_SUMMARY.md](COMPLETE_SUMMARY.md) | Full project overview with all 8 agents and workflow |
| [ARCHITECTURE_SPECIFICATION_WORKFLOW.md](ARCHITECTURE_SPECIFICATION_WORKFLOW.md) | How Software Architect bridges PM vision with development |
| [COMPETITOR_PLUGIN_SETUP.md](COMPETITOR_PLUGIN_SETUP.md) | How to set up competitor plugin (symlink or copy) |
| [SKELETON_PLUGIN_SETUP.md](SKELETON_PLUGIN_SETUP.md) | How to set up skeleton plugin (symlink or copy) |
| [ARCHITECTURE_TEMPLATE.md](ARCHITECTURE_TEMPLATE.md) | Template for documenting your skeleton plugin architecture |
| [SYMLINK_AND_ARCHITECTURE_APPROACH.md](SYMLINK_AND_ARCHITECTURE_APPROACH.md) | How to use symlinks and documentation-first approach |
| [PLATFORM_AGNOSTIC_ANALYSIS.md](PLATFORM_AGNOSTIC_ANALYSIS.md) | Why competitor analyst works with any platform (WordPress, Shopify, etc.) |
| [OLLAMA_MODEL_CONFIGURATION.md](OLLAMA_MODEL_CONFIGURATION.md) | Ollama model selection and configuration for each agent |
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

### ARCHITECTURE_TEMPLATE.md
Template for documenting your skeleton plugin:
- Comprehensive architecture documentation template
- Copy to your skeleton plugin as `ARCHITECTURE.md`
- Helps AI agents understand your structure faster
- Documents folder organization, patterns, conventions
- Improves code generation quality

### SYMLINK_AND_ARCHITECTURE_APPROACH.md
Complete guide to symlinks and documentation-first approach:
- How to set up symlinks for input plugins
- Why symlinks are better than copying
- How AI agents use documentation-first approach
- Benefits of documenting your skeleton architecture
- Troubleshooting symlink issues
- Migration guide from old approach

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

