# Ollama Model Configuration for AI Agents

## Model Assignment Summary

All AI agents are now configured with specific Ollama models optimized for their tasks.

### Crew 1: Strategy & Planning

| Agent | Model | Size | Reason |
|-------|-------|------|--------|
| **Market Researcher** | `ollama/qwen3:30b-instruct` | 18 GB | Best for analysis, reasoning, and understanding nuanced user feedback |
| **Competitor Analyst** | `ollama/qwen3-coder:30b` | 18 GB | Best for deep code analysis and technical understanding |
| **Product Manager** | `ollama/qwen3:30b-instruct` | 18 GB | Best for strategic thinking and synthesis |

### Crew 2: Development & QA

| Agent | Model | Size | Reason |
|-------|-------|------|--------|
| **Software Architect** | `ollama/qwen3-coder:30b` | 18 GB | Best for architecture design and system thinking |
| **WordPress Backend Dev** | `ollama/qwen2.5-coder:14b` | 9 GB | Good balance for PHP code generation |
| **React Frontend Dev** | `ollama/qwen2.5-coder:14b` | 9 GB | Good for React/JSX generation |
| **Code Reviewer** | `ollama/qwen3-coder:30b` | 18 GB | Needs deep analysis to catch subtle bugs |
| **QA Engineer** | `ollama/qwen2.5-coder:7b` | 4.7 GB | Sufficient for test generation, faster |

## Configuration Location

Models are configured in: `src/dev_team/config/agents.yaml`

Example:
```yaml
market_researcher:
  role: >
    WordPress Plugin Market Research...
  goal: >
    Research user needs...
  llm: ollama/qwen3:30b-instruct  # ← Model specified here
  backstory: >
    You're a product researcher...
```

## How to Change Models

### Option 1: Edit agents.yaml (Recommended)

Change the `llm` field for any agent:

```yaml
market_researcher:
  llm: ollama/qwen2.5-coder:14b  # Changed from qwen3:30b-instruct
```

### Option 2: Environment Variable (Global Override)

Set in `.env` file:
```bash
MODEL_NAME=ollama/qwen2.5-coder:14b
```

This will override all agents to use this model (not recommended for production).

## Model Selection Guide

### When to Use Large Models (30B)

**Use for:**
- Complex reasoning tasks
- Strategic planning
- Deep code analysis
- Thorough code reviews
- Architecture design

**Agents:**
- Market Researcher (needs to understand nuanced feedback)
- Competitor Analyst (needs to analyze complex codebases)
- Product Manager (needs strategic synthesis)
- Software Architect (needs system-level thinking)
- Code Reviewer (needs to catch subtle bugs)

### When to Use Medium Models (14B)

**Use for:**
- Code generation
- Standard development tasks
- Good balance of quality/speed

**Agents:**
- WordPress Backend Developer
- React Frontend Developer

### When to Use Small Models (7B)

**Use for:**
- Fast generation tasks
- Test writing
- Straightforward code

**Agents:**
- QA Engineer (test generation is more formulaic)

## Alternative Configurations

### Budget Configuration (Faster, Less VRAM)

If you want faster execution or have limited VRAM, use smaller models:

```yaml
# In agents.yaml, change all to:
llm: ollama/qwen2.5-coder:7b
```

**Pros:** ✅ Fast, ✅ Low VRAM (4.7 GB)
**Cons:** ⚠️ Lower quality output, ⚠️ May miss edge cases

### Premium Configuration (Best Quality)

For maximum quality (if you have the compute):

```yaml
# All agents use 30B models
market_researcher:
  llm: ollama/qwen3:30b-instruct

competitor_analyst:
  llm: ollama/qwen3-coder:30b

# ... all others use qwen3-coder:30b
```

**Pros:** ✅ Best quality, ✅ Catches more issues
**Cons:** ⚠️ Slow, ⚠️ High VRAM (18 GB per agent)

### Balanced Configuration (Current)

The current setup balances quality and performance:
- Large models (30B) for complex tasks
- Medium models (14B) for code generation
- Small models (7B) for simple tasks

This is **recommended for production use**.

## Installing Additional Models

If you want to try other models:

```bash
# Install DeepSeek Coder (excellent for code)
ollama pull deepseek-coder-v2:16b

# Install CodeLlama (strong code understanding)
ollama pull codellama:34b

# Install Llama 3.1 (best reasoning)
ollama pull llama3.1:70b

# Install Mistral (good general purpose)
ollama pull mistral-large
```

Then update `agents.yaml`:
```yaml
competitor_analyst:
  llm: ollama/deepseek-coder-v2:16b
```

## Performance Considerations

### VRAM Requirements

**Current Configuration:**
- 3 agents × 18 GB (30B models) = 54 GB
- 2 agents × 9 GB (14B models) = 18 GB
- 1 agent × 4.7 GB (7B model) = 4.7 GB
- **Total if all run simultaneously:** ~76.7 GB VRAM

**Sequential Execution:**
Only one agent runs at a time, so peak VRAM = 18 GB (largest model).

### Speed Comparison

On typical hardware:
- 7B models: ~50 tokens/sec
- 14B models: ~25 tokens/sec
- 30B models: ~10 tokens/sec

**Current configuration optimizes for:**
- Analysis quality (30B for strategy crew)
- Development speed (14B for dev crew)
- Test generation speed (7B for QA)

## Testing Your Configuration

Verify models are available:

```bash
# List installed models
ollama list

# Test a model
ollama run qwen3:30b-instruct "Hello"

# Check if all configured models exist
ollama list | grep "qwen3:30b-instruct"
ollama list | grep "qwen3-coder:30b"
ollama list | grep "qwen2.5-coder:14b"
ollama list | grep "qwen2.5-coder:7b"
```

## Troubleshooting

**Model not found error?**
```bash
# Install missing model
ollama pull qwen3:30b-instruct
```

**Out of memory?**
- Use smaller models (14B or 7B)
- Close other applications
- Ensure only one agent runs at a time (default behavior)

**Slow generation?**
- Use smaller models for faster iteration
- Consider GPU acceleration
- Reduce context window size

## Model Updates

When new models are released:

1. Pull the new model:
   ```bash
   ollama pull qwen3.5:30b-instruct
   ```

2. Update `agents.yaml`:
   ```yaml
   market_researcher:
     llm: ollama/qwen3.5:30b-instruct
   ```

3. Test the configuration:
   ```bash
   crewai run
   ```

## Summary

✅ **Current setup is optimized** for quality/performance balance
✅ **Models configured in YAML** for easy management
✅ **Can be customized per agent** based on your needs
✅ **Sequential execution** keeps VRAM manageable

The configuration uses your available models efficiently! 🎯

