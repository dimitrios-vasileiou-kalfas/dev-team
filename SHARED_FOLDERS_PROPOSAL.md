# Multi-Crew Project Structure - Shared Folders Approach

## Current Problem

Right now we have:
```
strategy_crew/
├── inputs/            # Symlinks to root inputs
└── outputs/           # Strategy crew writes here
    └── *.md, *.json

architecture_crew/
├── inputs/
│   └── strategy-outputs/   # Must COPY from strategy_crew/outputs/
└── outputs/           # Architecture crew writes here
    └── specs/

development_crew/
├── inputs/
│   └── architecture-outputs/  # Must COPY from architecture_crew/outputs/
└── outputs/           # Final plugin code
```

**Issues:**
- ❌ Manual copying between crews
- ❌ Risk of outdated data
- ❌ Duplication of files
- ❌ Complex data flow

---

## Proposed Solution: Shared Root Folders

```
dev-team/                        # Root project
├── inputs/                      # SHARED inputs (READ by all crews)
│   ├── competitor-plugin/
│   └── skeleton-plugin/
│
├── outputs/                     # SHARED outputs (WRITE by all crews)
│   ├── strategy/                # Strategy crew writes here
│   │   ├── technical-analysis.md
│   │   ├── market-research.md
│   │   ├── product-roadmap.md
│   │   └── plugin-metadata.json
│   │
│   ├── architecture/            # Architecture crew writes here
│   │   ├── high-level-architecture.md
│   │   ├── folder-structure.json
│   │   └── specs/
│   │       ├── backend/*.md
│   │       └── frontend/*.md
│   │
│   └── implementation/          # Development crew writes here
│       └── {plugin-slug}/       # Final plugin code
│
├── strategy_crew/               # Crew 1
│   ├── src/strategy_crew/
│   │   ├── config/
│   │   │   ├── agents.yaml
│   │   │   └── tasks.yaml      # output_file: '../../../outputs/strategy/...'
│   │   ├── crew.py
│   │   └── main.py
│   └── README.md
│
├── architecture_crew/           # Crew 2
│   ├── src/architecture_crew/
│   │   ├── config/
│   │   │   ├── agents.yaml
│   │   │   └── tasks.yaml      # output_file: '../../../outputs/architecture/...'
│   │   ├── crew.py
│   │   └── main.py
│   └── README.md
│
└── development_crew/            # Crew 3 (TODO)
    └── ...
```

---

## Benefits

### 1. No Manual Copying ✅
- Architecture crew reads from `outputs/strategy/`
- Development crew reads from `outputs/architecture/`
- Everything automatic!

### 2. Single Source of Truth ✅
- Only one copy of each file
- No risk of outdated data
- Always current

### 3. Clear Data Flow ✅
```
inputs/competitor-plugin
    ↓ (read by)
Strategy Crew
    ↓ (writes to)
outputs/strategy/
    ↓ (read by)
Architecture Crew
    ↓ (writes to)
outputs/architecture/
    ↓ (read by)
Development Crew
    ↓ (writes to)
outputs/implementation/{plugin-slug}/
```

### 4. Easier Testing ✅
- Can run any crew independently
- Outputs stay in one place
- Easy to verify/debug

### 5. Better for Git ✅
- All outputs in one `outputs/` folder
- Easy to `.gitignore` all outputs
- Or commit them for versioning

---

## Implementation Changes Needed

### 1. Update Strategy Crew Tasks
Change `output_file` paths in `strategy_crew/src/strategy_crew/config/tasks.yaml`:

**Before:**
```yaml
output_file: 'outputs/technical-analysis.md'
```

**After:**
```yaml
output_file: '../../../outputs/strategy/technical-analysis.md'
```

### 2. Update Architecture Crew Tasks
Change `output_file` paths in `architecture_crew/src/architecture_crew/config/tasks.yaml`:

**Before:**
```yaml
output_file: 'outputs/high-level-architecture.md'
```

**After:**
```yaml
output_file: '../../../outputs/architecture/high-level-architecture.md'
```

### 3. Update Input Paths in Tasks

**Architecture Crew** reads strategy outputs:
```yaml
description: >
  Read: ../../../outputs/strategy/plugin-metadata.json
  Read: ../../../outputs/strategy/technical-analysis.md
  Read: ../../../outputs/strategy/market-research.md
  Read: ../../../outputs/strategy/product-roadmap.md
```

**Development Crew** reads architecture outputs:
```yaml
description: >
  Read: ../../../outputs/architecture/folder-structure.json
  Read: ../../../outputs/architecture/specs/backend/*.md
  Read: ../../../outputs/architecture/specs/frontend/*.md
```

### 4. Remove Local Input/Output Folders

Each crew no longer needs:
- ❌ `inputs/strategy-outputs/` (architecture_crew)
- ❌ `inputs/architecture-outputs/` (development_crew)
- ❌ `outputs/` (all crews - use shared root)

Keep only:
- ✅ Root `inputs/` folder (competitor-plugin, skeleton-plugin)
- ✅ Root `outputs/` folder (strategy, architecture, implementation)

---

## Directory Structure After Changes

```
dev-team/
├── inputs/                           # SHARED - All crews read from here
│   ├── competitor-plugin/
│   └── skeleton-plugin/
│
├── outputs/                          # SHARED - All crews write here
│   ├── strategy/
│   │   ├── technical-analysis.md
│   │   ├── market-research.md
│   │   ├── product-roadmap.md
│   │   ├── plugin-metadata.json
│   │   └── milestones/
│   │
│   ├── architecture/
│   │   ├── strategy-summary.md
│   │   ├── high-level-architecture.md
│   │   ├── database-schema.md
│   │   ├── api-contracts.md
│   │   ├── folder-structure.json
│   │   └── specs/
│   │       ├── backend/
│   │       │   ├── class-core.md
│   │       │   ├── class-soap-client.md
│   │       │   └── ...
│   │       └── frontend/
│   │           ├── component-voucher-form.md
│   │           └── ...
│   │
│   └── implementation/
│       └── {plugin-slug}/            # Final plugin
│           ├── {plugin-slug}.php
│           ├── includes/
│           ├── admin/
│           └── ...
│
├── strategy_crew/                    # Crew 1 - No local outputs!
│   ├── src/strategy_crew/
│   │   ├── config/
│   │   │   └── tasks.yaml           # Points to ../../../outputs/strategy/
│   │   └── ...
│   └── README.md
│
├── architecture_crew/                # Crew 2 - No local inputs/outputs!
│   ├── src/architecture_crew/
│   │   ├── config/
│   │   │   └── tasks.yaml           # Reads: ../../../outputs/strategy/
│   │   │                            # Writes: ../../../outputs/architecture/
│   │   └── ...
│   └── README.md
│
├── development_crew/                 # Crew 3 - No local inputs!
│   ├── src/development_crew/
│   │   ├── config/
│   │   │   └── tasks.yaml           # Reads: ../../../outputs/architecture/
│   │   │                            # Writes: ../../../outputs/implementation/
│   │   └── ...
│   └── README.md
│
├── docs/                             # Documentation
├── knowledge/                        # Shared knowledge
└── README.md                         # Root documentation
```

---

## Workflow With Shared Folders

### Step 1: Run Strategy Crew
```bash
cd strategy_crew
crewai run
# Outputs go to: ../outputs/strategy/
```

### Step 2: Run Architecture Crew
```bash
cd ../architecture_crew
crewai run
# Reads from: ../outputs/strategy/
# Writes to: ../outputs/architecture/
```

### Step 3: Run Development Crew
```bash
cd ../development_crew
crewai run
# Reads from: ../outputs/architecture/
# Writes to: ../outputs/implementation/{plugin-slug}/
```

**No manual copying needed!** 🎉

---

## Migration Steps

### 1. Create Root Output Folders
```bash
cd dev-team
mkdir -p outputs/strategy outputs/architecture outputs/implementation
```

### 2. Update Strategy Crew
```bash
# Update tasks.yaml to use ../../../outputs/strategy/
```

### 3. Update Architecture Crew
```bash
# Update tasks.yaml to read from ../../../outputs/strategy/
# Update tasks.yaml to write to ../../../outputs/architecture/
```

### 4. Remove Old Folders
```bash
# Remove local crew folders (after confirming new structure works)
rm -rf strategy_crew/outputs/
rm -rf architecture_crew/inputs/strategy-outputs/
rm -rf architecture_crew/outputs/
```

### 5. Update Documentation
- Update all READMEs
- Update ARCHITECTURE_CREW_COMPLETE.md
- Update STRATEGY_CREW_COMPLETE.md

---

## Git Configuration

Add to `.gitignore`:
```
# Shared outputs (generated by crews)
outputs/strategy/
outputs/architecture/
outputs/implementation/

# Or commit them for version control:
# !outputs/strategy/*.md
# !outputs/architecture/folder-structure.json
```

---

## Advantages Summary

| Aspect | Old Approach | New Approach |
|--------|--------------|--------------|
| **File Location** | Crew-specific | Shared root folders |
| **Data Flow** | Manual copying | Automatic (relative paths) |
| **Duplication** | Yes (multiple copies) | No (single source) |
| **Maintenance** | Complex | Simple |
| **Testing** | Hard (stale data risk) | Easy (always current) |
| **Git Tracking** | Multiple folders | Single outputs/ folder |
| **Clarity** | Scattered | Centralized |

---

## Recommendation

**✅ YES, implement shared folders at root level!**

**Why:**
1. Eliminates manual copying
2. Reduces duplication
3. Clearer data flow
4. Easier to maintain
5. Better for testing
6. More intuitive structure

**When to implement:**
- ✅ **Now** - Before running crews extensively
- ✅ Before creating Development Crew
- ✅ While structure is still flexible

---

## Next Steps

1. ✅ Create root `outputs/` structure
2. ✅ Update Strategy Crew task paths
3. ✅ Update Architecture Crew task paths
4. ✅ Test full pipeline
5. ✅ Update documentation
6. ✅ Remove old crew-specific folders

Would you like me to implement these changes now?

