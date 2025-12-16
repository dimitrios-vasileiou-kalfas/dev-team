# Symlink Setup & Documentation-First Architecture ✅

## What Was Changed

### 1. Input Plugins Now Use Symlinks 🔗

Both `inputs/competitor-plugin/` and `inputs/skeleton-plugin/` are now designed to be **symlinked** to your local WordPress plugin folders.

#### Setup Instructions

```bash
# From project root
ln -s /absolute/path/to/wordpress/wp-content/plugins/competitor-plugin inputs/competitor-plugin
ln -s /absolute/path/to/your/skeleton-plugin inputs/skeleton-plugin

# Example:
ln -s ~/Sites/wordpress/wp-content/plugins/woocommerce-shipping inputs/competitor-plugin
ln -s ~/Projects/my-skeleton-plugin inputs/skeleton-plugin
```

#### Benefits
- ✅ Always in sync with your source plugins
- ✅ No duplication, saves disk space
- ✅ Changes reflect immediately
- ✅ Perfect for active development

#### Git Configuration
Updated `.gitignore` to:
- Ignore the symlinked folders completely
- Keep only the README.md files in each folder
- Prevent committing actual plugin code

### 2. AI Agents Use Documentation-First Approach 📄

The **Software Architect** agent now follows this workflow:

#### Step 1: Search for Documentation (Primary)
Looks for architecture documentation in skeleton plugin:
- `ARCHITECTURE.md` (root folder)
- `STRUCTURE.md`
- `README.md` with architecture section
- `docs/architecture.md` or `docs/structure.md`

If found, uses documentation to understand:
- Folder structure and organization
- Naming conventions (namespaces, prefixes, hooks)
- Architectural patterns (DI, repository, etc.)
- Design decisions and rationale
- Coding standards

#### Step 2: Code Analysis (Fallback)
If documentation doesn't exist or is incomplete:
- Analyzes folder structure
- Studies existing classes and patterns
- Reviews naming conventions
- Checks configuration files (package.json, composer.json)
- Identifies coding style

#### Step 3: Design Features
Creates architecture that seamlessly integrates with existing patterns.

### 3. Architecture Template Provided 📋

Created `docs/ARCHITECTURE_TEMPLATE.md` - a comprehensive template for documenting your skeleton plugin.

**Copy this to your skeleton plugin:**
```bash
cp docs/ARCHITECTURE_TEMPLATE.md /path/to/your/skeleton-plugin/ARCHITECTURE.md
# Then customize it for your plugin
```

**What it includes:**
- Folder structure explanation
- Naming conventions (PHP, JS, hooks)
- Architectural patterns used
- Design decisions and rationale
- WordPress integration patterns
- React/MUI setup details
- Testing requirements
- Build & development setup
- Code style guides
- Security considerations
- How to add new features
- Common pitfalls to avoid

## Updated Files

### Configuration Files
- ✅ `src/dev_team/config/agents.yaml` - Updated `software_architect` agent
- ✅ `src/dev_team/config/tasks.yaml` - Updated `design_architecture`, `implement_backend`, `implement_frontend` tasks
- ✅ `.gitignore` - Updated to handle symlinked folders properly

### Documentation Files
- ✅ `inputs/competitor-plugin/README.md` - Added symlink setup instructions
- ✅ `inputs/skeleton-plugin/README.md` - Added symlink setup + architecture documentation guidance
- ✅ `docs/ARCHITECTURE_TEMPLATE.md` - NEW: Complete template for skeleton plugin documentation
- ✅ `docs/README.md` - Added ARCHITECTURE_TEMPLATE to index

## Benefits of This Approach

### Symlinks
1. **Efficiency** - No file duplication
2. **Consistency** - Always working with latest code
3. **Simplicity** - One source of truth
4. **Flexibility** - Easy to switch plugins (just relink)

### Documentation-First
1. **Speed** - Reading docs is faster than analyzing code
2. **Accuracy** - Docs explain *intent* and *why*, not just *what*
3. **Context** - Understanding design decisions leads to better integration
4. **Fallback** - Code analysis still works if docs missing

## Workflow Example

### For New Users

1. **Clone the project**
   ```bash
   git clone your-repo
   cd dev-team
   ```

2. **Create symlinks**
   ```bash
   ln -s ~/Sites/wordpress/wp-content/plugins/competitor inputs/competitor-plugin
   ln -s ~/Projects/skeleton inputs/skeleton-plugin
   ```

3. **Add architecture docs to skeleton** (recommended)
   ```bash
   cp docs/ARCHITECTURE_TEMPLATE.md ~/Projects/skeleton/ARCHITECTURE.md
   # Edit to match your skeleton structure
   ```

4. **Run analysis**
   ```bash
   crewai install
   echo "OPENAI_API_KEY=your_key" > .env
   crewai run
   ```

### How AI Agents Work

```
┌─────────────────────────────────────────┐
│ Software Architect Agent                │
├─────────────────────────────────────────┤
│ 1. Look for ARCHITECTURE.md            │
│    ├─ Found? Use as primary reference  │
│    └─ Not found? Analyze code          │
│                                         │
│ 2. Understand:                          │
│    ├─ Folder organization               │
│    ├─ Naming conventions                │
│    ├─ Architectural patterns            │
│    └─ Design decisions                  │
│                                         │
│ 3. Design features that integrate       │
│    seamlessly with existing patterns    │
└─────────────────────────────────────────┘
```

## Troubleshooting

### Symlink Issues

**Broken symlink?**
```bash
# Check if it exists
ls -la inputs/competitor-plugin

# Should show: inputs/competitor-plugin -> /path/to/plugin

# If broken, recreate
rm inputs/competitor-plugin
ln -s /correct/path inputs/competitor-plugin
```

**Permission denied?**
```bash
chmod -R a+r /path/to/plugin
```

**Symlink not working on Windows?**
Use junction points or directory symbolic links:
```cmd
mklink /D inputs\competitor-plugin C:\path\to\plugin
```

### Architecture Documentation

**Don't have time to write full docs?**
Even a minimal ARCHITECTURE.md helps:
```markdown
# Architecture

## Structure
- includes/ - Core WordPress hooks
- src/ - Modern namespaced PHP (PSR-4)
- admin-react/ - React admin with MUI

## Conventions
- Namespace: MyPlugin\
- Hook prefix: my_plugin_
```

**Already have README.md?**
Add an "Architecture" section to your existing README instead of creating a separate file.

## Migration from Old Approach

If you had copied plugins before:

1. **Remove old copies**
   ```bash
   rm -rf inputs/competitor-plugin/*
   rm -rf inputs/skeleton-plugin/*
   ```

2. **Create symlinks**
   ```bash
   ln -s /path/to/competitor inputs/competitor-plugin
   ln -s /path/to/skeleton inputs/skeleton-plugin
   ```

3. **Verify**
   ```bash
   ls -la inputs/
   # Both should show as symlinks (->)
   ```

## Best Practices

### For Skeleton Plugin Maintainers

1. **Create ARCHITECTURE.md** - Use the template in `docs/ARCHITECTURE_TEMPLATE.md`
2. **Keep it updated** - When you change patterns, update the docs
3. **Be specific** - Don't just list folders, explain *why* they exist
4. **Include examples** - Show code snippets of your patterns
5. **Document gotchas** - Warn about common mistakes

### For AI Agent Users

1. **Provide good skeleton** - Clean, well-organized code
2. **Add documentation** - Even minimal docs help significantly
3. **Use symlinks** - Keeps everything in sync
4. **Review outputs** - Agents follow your patterns, but verify results
5. **Iterate** - If output doesn't match your style, update your docs

## Summary

✅ **Symlinks** - Efficient, consistent, no duplication
✅ **Documentation-first** - Faster, more accurate understanding
✅ **Template provided** - Easy to document your skeleton
✅ **Fallback available** - Works even without docs
✅ **Better integration** - AI agents respect your patterns

This approach ensures AI agents understand and respect your existing codebase structure! 🎯

