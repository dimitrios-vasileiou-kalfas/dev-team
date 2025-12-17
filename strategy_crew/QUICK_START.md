# Quick Start: Running Strategy Crew

## Prerequisites Check

1. **Ollama Model**
   ```bash
   ollama pull qwen3:30b-instruct
   ollama list  # Verify it's installed
   ```

2. **Python Dependencies**
   ```bash
   cd strategy_crew
   uv pip install -e .
   # Or: pip install -e .
   ```

3. **Input Folders**
   ```bash
   ls -la inputs/
   # Should see:
   # competitor-plugin -> /path/to/dev-team/inputs/competitor-plugin
   # skeleton-plugin -> /path/to/dev-team/inputs/skeleton-plugin
   ```

## Run Strategy Crew

```bash
cd /Users/dimitrios.vasileiou-kalfas/Projects/my-projects/dev-team/strategy_crew
crewai run
```

## What Happens

The crew runs 3 tasks sequentially:

1. **analyze_competitor** (15-20 min)
   - Competitor Analyst reads all plugin files
   - Creates detailed technical analysis
   - Output: `outputs/technical-analysis.md`

2. **research_market** (5-8 min)
   - Market Researcher analyzes market gaps
   - Identifies niche opportunities
   - Output: `outputs/market-research.md`

3. **create_roadmap** (3-5 min)
   - Product Manager creates milestone roadmap
   - Defines plugin name, slug, namespace
   - Output: `outputs/product-roadmap.md`, `outputs/plugin-metadata.json`

**Total Time**: ~25-30 minutes

## Check Outputs

```bash
cd outputs/
ls -la
cat technical-analysis.md
cat market-research.md
cat product-roadmap.md
cat plugin-metadata.json  # NEW: Plugin naming
```

## Troubleshooting

### Error: "Competitor plugin not found"
```bash
# Recreate symlinks
cd strategy_crew/inputs/
ln -s ../../inputs/competitor-plugin competitor-plugin
ln -s ../../inputs/skeleton-plugin skeleton-plugin
```

### Error: "Model not found"
```bash
ollama pull qwen3:30b-instruct
```

### Crew runs but outputs empty
- Check `outputs/` folder was created
- Verify tasks.yaml has correct `output_file` paths
- Check agent LLM is running: `ollama ps`

## Next Steps After Completion

1. Review all markdown outputs
2. Check `plugin-metadata.json` for plugin name
3. Copy outputs to Architecture Crew inputs:
   ```bash
   # When Architecture Crew is ready:
   cp -r strategy_crew/outputs/* architecture_crew/inputs/strategy-outputs/
   ```

## Testing Without Full Run

### Test with smaller competitor plugin first
```bash
# Use a simple plugin for faster testing
cp -r /path/to/simple-plugin inputs/competitor-plugin/
crewai run
```

### Check individual task
```bash
# View task config
cat src/strategy_crew/config/tasks.yaml | grep -A 20 "analyze_competitor:"
```

---

**Quick Test** (5 min check):
```bash
cd strategy_crew
python -c "from strategy_crew.crew import StrategyCrew; print('✅ Import works')"
python -c "from strategy_crew.tools.custom_tool import FileReaderTool; print('✅ Tools work')"
ls inputs/competitor-plugin && echo "✅ Inputs linked"
```

