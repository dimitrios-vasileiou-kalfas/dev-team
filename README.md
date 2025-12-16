# WordPress Plugin Development Team (CrewAI)

An AI-powered development team for building WordPress plugins using CrewAI. This project uses a **two-crew architecture** with a human review checkpoint to analyze competitor plugins, create product roadmaps, and implement features using best practices.

## 🚀 Quick Start

```bash
# 1. Add your plugins
cp -r /path/to/competitor-plugin inputs/competitor-plugin/
cp -r /path/to/skeleton-plugin inputs/skeleton-plugin/

# 2. Install dependencies
crewai install

# 3. Add your API key to .env
echo "OPENAI_API_KEY=your_key_here" > .env

# 4. Run analysis (Crew 1 only - Development temporarily disabled)
crewai run

# 5. Review outputs in outputs/analysis/
```

**🎯 What You Get:** Market research, technical analysis, and strategic roadmap with niche/localization opportunities (Greek eshops, healthcare, etc.)

**⚠️ Current Status:**
- 🟢 **Crew 1 (Strategy & Planning):** ACTIVE - Runs when you execute `crewai run`
- 🔴 **Crew 2 (Development & QA):** DISABLED - Only analysis/planning will run
- 📖 To re-enable full pipeline, see [docs/CREW2_DISABLED.md](docs/CREW2_DISABLED.md)

> 📚 **Detailed Documentation:** See the [docs/](docs/) folder for comprehensive guides:
> - [Setup Guide](docs/SETUP_COMPLETE.md) - Getting started
> - [Complete Summary](docs/COMPLETE_SUMMARY.md) - Full overview  
> - [Niche Strategy](docs/NICHE_AND_LOCALIZATION_ENHANCED.md) - Market specialization
> - [Analysis Mode](docs/CREW2_DISABLED.md) - Current configuration (Dev crew disabled)

## 🏗️ Architecture

### Two-Crew Workflow

```
┌─────────────────────────────────────────────────────────────┐
│  CREW 1: STRATEGY & PLANNING                                │
│  ├─ Market Researcher Agent                                 │
│  ├─ Competitor Analyst Agent (Technical)                    │
│  └─ Product Manager Agent                                   │
│                                                              │
│  Output: Analysis reports & milestone-based roadmap         │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  👤 HUMAN REVIEW CHECKPOINT                                 │
│  Review analysis, approve roadmap, create APPROVED.txt      │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  CREW 2: DEVELOPMENT & QA                                   │
│  ├─ Software Architect Agent                                │
│  ├─ WordPress Backend Developer (PHP/OOP/SOLID)             │
│  ├─ React Frontend Developer (React/MUI)                    │
│  ├─ Code Reviewer Agent                                     │
│  └─ QA Engineer Agent (Playwright E2E)                      │
│                                                              │
│  Output: Working WordPress plugin with tests                │
└─────────────────────────────────────────────────────────────┘
```

## ✨ What Makes This Special

### 🎯 Niche Market Intelligence
Unlike generic analysis tools, this identifies **profitable specialization opportunities**:
- **Geographic niches**: Greek eshops need ELTA shipping + AADE myDATA integration
- **Vertical niches**: Healthcare needs HIPAA compliance, Real estate needs IDX/MLS
- **Regional gaps**: Missing payment gateways, shipping providers, tax systems

**Example:** Instead of building another generic WooCommerce plugin (€49/year), build "WooCommerce Greek Pack" with mandatory compliance features (€199/year, €2M+ market).

### 🌍 Localization Focus
Detects country-specific requirements competitors miss:
- Greek market: ELTA, Piraeus Bank, ΦΠΑ tax system, Skroutz marketplace
- German market: DHL, Deutsche Post, German invoicing standards
- Regional compliance: GDPR, AADE myDATA, HIPAA

### 🤖 Complete Automation
From market research → roadmap → code → tests → review. Each feature is:
- ✅ Designed with SOLID principles
- ✅ Implemented with WordPress best practices
- ✅ Tested (PHPUnit, Jest, Playwright E2E)
- ✅ Reviewed for security and quality

### 💡 Strategic Business Focus
Not just "what features exist" but "what market opportunities exist":
- User pain points with high demand
- Underserved segments with low competition
- Premium pricing opportunities (specialization = higher prices)
- First-mover advantages (compliance requirements)

## 📋 Agent Responsibilities

### Crew 1: Strategy & Planning

**1. Market Researcher**
- Analyzes user reviews, feedback, and feature requests
- Researches competitive landscape and market gaps
- Identifies user pain points and unmet needs
- Discovers high-value feature opportunities based on demand

**2. Competitor Analyst (Technical)**
- Analyzes competitor plugin code and architecture
- Identifies technical weaknesses and opportunities
- Evaluates code quality, security, and performance
- Proposes technical improvements and innovations

**3. Product Manager**
- Synthesizes market research + technical analysis
- Creates milestone-based roadmap (MVP → Parity → Differentiation)
- Prioritizes features by user impact × technical feasibility
- Defines acceptance criteria and success metrics

### Crew 2: Development & QA

**3. Software Architect**
- Designs plugin architecture (OOP/SOLID principles)
- Plans file structure respecting skeleton plugin
- Defines REST API endpoints and data flow

**4. WordPress Backend Developer**
- Implements PHP backend (includes/, src/)
- Follows WordPress coding standards
- Writes PHPUnit + Brain Monkey tests

**5. React Frontend Developer**
- Implements admin UI (admin-react/ folder)
- Uses React + Material-UI best practices
- Writes Jest tests (100% coverage goal)

**6. Code Reviewer**
- Reviews backend and frontend code
- Identifies security issues, SOLID violations, bugs
- Suggests improvements and refactoring

**7. QA Engineer**
- Runs test coverage analysis
- Writes Playwright E2E tests
- Validates backend ↔ frontend integration

## 🚀 Quick Start

### Installation

Ensure you have Python >=3.10 <3.14 installed.

```bash
# Install dependencies
crewai install

# Or manually
pip install uv
uv sync
```

### Setup

1. **Add your API key** to `.env`:
```bash
OPENAI_API_KEY=your_key_here
```

2. **Add input plugins**:
```bash
# Add competitor plugin
cp -r /path/to/competitor-plugin inputs/competitor-plugin/

# Add skeleton plugin (your base WordPress plugin)
cp -r /path/to/skeleton-plugin inputs/skeleton-plugin/
```

3. **Run the pipeline**:
```bash
crewai run
```

## 📂 Project Structure

```
dev-team/
├── inputs/
│   ├── competitor-plugin/       # Competitor WordPress plugin
│   └── skeleton-plugin/         # Your base plugin structure
│
├── outputs/
│   ├── analysis/                # Strategy Crew outputs
│   │   ├── market-research.md
│   │   ├── technical-analysis.md
│   │   ├── product-roadmap.md
│   │   ├── milestones/
│   │   │   ├── milestone-1-mvp.md
│   │   │   ├── milestone-2-parity.md
│   │   │   └── milestone-3-differentiation.md
│   │   └── APPROVED.txt         # Create this after review
│   │
│   └── plugin/                  # Development Crew outputs
│       ├── wp-skeleton-plugin.php
│       ├── includes/            # Backend PHP (Core)
│       ├── src/                 # Backend PHP (Modern)
│       │   ├── admin/
│       │   ├── frontend/
│       │   └── blocks/
│       ├── admin-react/         # Frontend React/MUI
│       │   ├── src/
│       │   │   ├── components/
│       │   │   ├── pages/
│       │   │   ├── hooks/
│       │   │   └── utils/
│       │   └── package.json
│       ├── assets/
│       └── tests/
│
└── src/
    └── dev_team/
        ├── config/
        │   ├── agents.yaml      # All 7 agent definitions
        │   └── tasks.yaml       # All task definitions
        ├── crews/
        │   ├── strategy_crew.py
        │   └── development_crew.py
        ├── orchestrator.py      # Runs both crews
        └── main.py
```

## 🔄 Workflow

### Full Pipeline (Recommended)

```bash
# Run both crews with human checkpoint
crewai run
```

**Steps:**
1. Strategy Crew analyzes competitor and creates roadmap
2. Review `outputs/analysis/` files
3. Create `outputs/analysis/APPROVED.txt` when ready
4. Development Crew implements Milestone 1 (MVP)
5. Review generated plugin in `outputs/plugin/`

### Run Crews Separately

```bash
# Phase 1: Strategy only
python src/dev_team/orchestrator.py

# After approval, Phase 2: Development only
# (After creating APPROVED.txt)
python -c "from dev_team.orchestrator import run_development_phase; run_development_phase('inputs/competitor-plugin', 'inputs/skeleton-plugin')"
```

## 🎯 Milestones

The product roadmap defines 3 milestones:

1. **Milestone 1: MVP** - Core features for basic functionality
2. **Milestone 2: Parity** - Match competitor's capabilities
3. **Milestone 3: Differentiation** - Unique features

Each milestone is developed separately. After Milestone 1, review the plugin, approve, then proceed to Milestone 2.

## 🧪 Testing

Generated plugin includes:
- **PHPUnit tests** (backend) with Brain Monkey for WordPress mocking
- **Jest tests** (frontend) with React Testing Library
- **Playwright E2E tests** for complete workflows

## 🛠️ Customization

### Modify Agents

Edit `src/dev_team/config/agents.yaml` to customize:
- Agent roles and goals
- Backstories and expertise
- Tools and capabilities

### Modify Tasks

Edit `src/dev_team/config/tasks.yaml` to customize:
- Task descriptions and requirements
- Expected outputs
- Context dependencies

### Modify Workflow

Edit `src/dev_team/orchestrator.py` to:
- Change checkpoint behavior
- Add additional crews
- Customize milestone iteration

## 📚 Documentation

- [CrewAI Documentation](https://docs.crewai.com)
- [WordPress Plugin Handbook](https://developer.wordpress.org/plugins/)
- [React Documentation](https://react.dev)
- [Material-UI Documentation](https://mui.com)

## 🤝 Support

For issues or questions:
- [CrewAI GitHub](https://github.com/joaomdmoura/crewai)
- [CrewAI Discord](https://discord.com/invite/X4JWnZnxPb)

## 📝 License

MIT License - see LICENSE file for details
