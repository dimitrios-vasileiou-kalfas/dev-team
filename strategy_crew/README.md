# Strategy Crew - WordPress Plugin Analysis & Strategic Planning

This is the **Strategy Crew** - the first of three crews in the plugin development pipeline. It analyzes competitor plugins and creates strategic roadmaps including plugin naming and requirements.

## Purpose

The Strategy Crew performs comprehensive market research and technical analysis to define:
- **Technical Analysis**: Deep dive into competitor plugin code, architecture, and security
- **Market Research**: User needs, niche opportunities, and localization requirements  
- **Product Roadmap**: Milestone-based feature plan with plugin metadata (name, slug, namespace)

## Agents

1. **Competitor Analyst**: Systematic technical code analysis with file-by-file review
2. **Market Researcher**: Market gaps, niche identification, and regional opportunities
3. **Product Manager**: Synthesizes research into actionable milestone roadmap

## Setup

### Prerequisites

- Python 3.10+
- Ollama running with `qwen3:30b-instruct` model
- CrewAI installed

### Installation

From the `strategy_crew` directory:

```bash
# Install dependencies
uv pip install -e .

# Or with pip
pip install -e .
```

### Input Requirements

The crew expects two input folders (symlinked from parent dev-team project):

```
strategy_crew/
├── inputs/
│   ├── competitor-plugin/     # Symlink to ../inputs/competitor-plugin
│   └── skeleton-plugin/        # Symlink to ../inputs/skeleton-plugin
```

Symlinks should already be created. If not, run from `strategy_crew/` directory:

```bash
ln -s ../inputs/competitor-plugin inputs/competitor-plugin
ln -s ../inputs/skeleton-plugin inputs/skeleton-plugin
```

## Usage

### Run Strategy Analysis

From the `strategy_crew` directory:

```bash
crewai run
```

This will:
1. Analyze competitor plugin code systematically
2. Research market opportunities and user needs
3. Create milestone-based product roadmap
4. Generate plugin metadata (name, slug, namespace)

### Outputs

All outputs are saved to `outputs/`:

```
strategy_crew/outputs/
├── technical-analysis.md      # Technical analysis of competitor
├── market-research.md          # Market gaps and opportunities
├── product-roadmap.md          # Milestone-based roadmap
└── plugin-metadata.json        # NEW: Plugin name, slug, namespace, version
```

### plugin-metadata.json Structure

```json
{
  "name": "Secure ELTA Shipping Manager",
  "slug": "secure-elta-shipping",
  "namespace": "SecureELTA",
  "version": "1.0.0",
  "author": "Your Team"
}
```

## Configuration

### Models

Agents are configured to use Ollama models in `config/agents.yaml`:
- Market Researcher: `ollama/qwen3:30b-instruct`
- Competitor Analyst: `ollama/qwen3:30b-instruct` (temperature: 0.2, max_iter: 60)
- Product Manager: `ollama/qwen3:30b-instruct`

### Tasks

Tasks are defined in `config/tasks.yaml`:
- `analyze_competitor`: Technical analysis (output: outputs/technical-analysis.md)
- `research_market`: Market research (output: outputs/market-research.md, context: analyze_competitor)
- `create_roadmap`: Product roadmap (output: outputs/product-roadmap.md, context: both above)

## Next Steps

After the Strategy Crew completes:

1. **Review Outputs**: Check all generated markdown files
2. **Verify Plugin Metadata**: Confirm the chosen plugin name and slug
3. **Pass to Architecture Crew**: Use outputs as input for the next crew
4. **Continue Pipeline**: Architecture Crew → Development Crew

## Training & Testing

Train the crew with historical data:

```bash
crewai train <n_iterations> <filename>
```

Test crew performance:

```bash
crewai test <n_iterations> <eval_llm>
```

Replay specific task:

```bash
crewai replay <task_id>
```

## Troubleshooting

**Error: Competitor plugin not found**
- Verify symlink exists: `ls -la inputs/competitor-plugin`
- Recreate if needed: `ln -s ../inputs/competitor-plugin inputs/competitor-plugin`

**Error: Ollama model not found**
- Pull model: `ollama pull qwen3:30b-instruct`
- Verify running: `ollama list`

**Slow performance**
- Competitor Analyst has `max_iter: 60` to read all files thoroughly
- Expect 25-30 minutes for complete analysis
- This is intentional for comprehensive code review

## Integration with Other Crews

This is **Crew 1 of 3** in the plugin development pipeline:

```
Strategy Crew (this) → Architecture Crew → Development Crew
     ↓
  outputs/          →     inputs/        →     inputs/
```

The outputs from this crew become inputs for the Architecture Crew.

## License

Part of the dev-team multi-crew plugin development system.

