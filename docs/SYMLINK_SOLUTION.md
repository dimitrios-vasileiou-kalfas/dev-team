# Architecture Crew - Portable Paths Solution

## Problem Solved

CrewAI's Pydantic validation blocks path traversal attempts (`../../../`) in `output_file` paths, but we need to write to the shared `/outputs/architecture/` directory at the project root level.

## Solution: Symlink Approach

Instead of using path traversal or absolute paths, we use a **local symlink** that points to the shared outputs directory.

### Setup

```bash
cd architecture_crew
./setup_symlinks.sh
```

This creates:
- `architecture_crew/outputs` → symlink to `../outputs/architecture`

### How It Works

1. **crew.py** uses simple relative path:
   ```python
   self.outputs_dir = Path("outputs")  # No path traversal!
   ```

2. **Symlink** redirects to shared location:
   ```
   architecture_crew/outputs → ../outputs/architecture
   ```

3. **Files written** to `outputs/strategy-summary.md` actually go to:
   ```
   /dev-team/outputs/architecture/strategy-summary.md
   ```

### Benefits

✅ **No path traversal** - Uses simple relative path `outputs/`  
✅ **No hardcoded paths** - Symlink is relative, works anywhere  
✅ **Shared outputs** - All crews write to same location  
✅ **Portable** - Works on any machine after running setup script  

## Usage

### First Time Setup

```bash
cd architecture_crew
./setup_symlinks.sh
uv run crewai run
```

### Regular Usage

```bash
cd architecture_crew
uv run crewai run
```

**Important:** Always run from the `architecture_crew` directory, not from the project root!

## File Structure

```
dev-team/
├── architecture_crew/
│   ├── outputs/              # Symlink → ../outputs/architecture
│   ├── setup_symlinks.sh     # Setup script
│   └── src/
│       └── architecture_crew/
│           └── crew.py       # Uses Path("outputs")
└── outputs/
    └── architecture/         # Actual output location
        ├── strategy-summary.md
        ├── high-level-architecture.md
        └── folder-structure.json
```

## Comparison with Other Approaches

### ❌ Absolute Paths (Initial Attempt)
```python
output_file = '/Users/user/Projects/dev-team/outputs/...'
```
- Not portable across machines
- Hardcoded username
- CrewAI created nested directories literally

### ❌ Path Traversal (Second Attempt)
```python
output_file = '../../../outputs/architecture/...'
```
- Blocked by Pydantic validation
- Security feature prevents `..` in paths

### ✅ Symlink (Final Solution)
```python
output_file = 'outputs/strategy-summary.md'
```
- Simple relative path
- No path traversal
- Portable via setup script
- Works with Pydantic validation

## Troubleshooting

### Error: "No such file or directory: 'pyproject.toml'"
**Cause:** Running from wrong directory  
**Solution:** `cd architecture_crew` before running

### Error: "Path traversal attempts are not allowed"
**Cause:** Symlink not created  
**Solution:** Run `./setup_symlinks.sh`

### Outputs in wrong location
**Cause:** Symlink pointing to wrong target  
**Solution:** Delete symlink and re-run setup script
```bash
rm outputs
./setup_symlinks.sh
```

## For Other Crews

The same approach can be used for strategy_crew and other crews:

```bash
# In strategy_crew/
ln -s ../outputs/strategy outputs
```

Then in `strategy_crew/src/strategy_crew/crew.py`:
```python
self.outputs_dir = Path("outputs")
```

