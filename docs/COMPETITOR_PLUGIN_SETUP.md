3# Competitor Plugin

Place your competitor WordPress plugin here for analysis.

## Setup Options

### Option 1: Symlink (Recommended) 🔗

Create a symlink to your local WordPress plugin installation:

```bash
# From project root
ln -s /absolute/path/to/competitor-plugin inputs/competitor-plugin

# Example:
ln -s ~/Projects/my-projects/other-plugins/elta-courier-voucher-for-woocommerce inputs/competitor-plugin
```

**Benefits:**
- ✅ Always in sync with your WordPress installation
- ✅ No duplication - saves disk space
- ✅ Changes reflect immediately
- ✅ Perfect for active development

**Remove and recreate symlink (if needed):**
```bash
# Remove old symlink
rm inputs/competitor-plugin

# Create new symlink
ln -s ~/Projects/my-projects/other-plugins/elta-courier-voucher-for-woocommerce inputs/competitor-plugin
```

**Verify symlink is working:**
```bash
# Check symlink exists and points to correct location
ls -la inputs/
# Should show: competitor-plugin -> /path/to/your/competitor-plugin

# Verify plugin files are accessible directly
ls inputs/competitor-plugin/
# Should show: plugin-name.php, includes/, assets/, etc.

# Check you can read the main plugin file
head -20 inputs/competitor-plugin/*.php
# Should show the WordPress plugin header
```

### Option 2: Copy Plugin Files (Fallback)

If symlinks don't work for your setup, copy the plugin:

```bash
# From project root
cp -r /path/to/competitor-plugin/* inputs/competitor-plugin/

# Or drag and drop files in Finder/Explorer
```

**Use this if:**
- You want a snapshot of a specific version
- Working with downloaded plugin (not local WordPress install)
- Symlinks aren't supported on your system

## What the AI Agents Will Analyze

### Market Researcher Agent 🔍
Analyzes from **business perspective**:
- User reviews and ratings
- Feature requests in support forums
- Pain points and complaints
- Market gaps and opportunities
- Niche markets (Greek eshops, healthcare, etc.)
- Regional needs (ELTA shipping, AADE myDATA, etc.)

### Competitor Analyst Agent 🔧
Analyzes from **technical perspective**:
- Code structure and architecture
- Code quality and technical debt
- Security implementations
- Performance bottlenecks
- Database design
- REST API structure
- React/JavaScript implementation
- Testing coverage

## Expected Plugin Structure

Any WordPress plugin structure works. Common examples:

### Standard WordPress Plugin
```
competitor-plugin/
├── plugin-name.php          # Main plugin file
├── includes/                # Core PHP functionality
├── admin/                   # Admin interface
├── public/                  # Public-facing code
├── assets/                  # CSS, JS, images
└── readme.txt              # WordPress readme
```

### Modern WordPress Plugin (with React)
```
competitor-plugin/
├── plugin-name.php
├── includes/                # Backend PHP
├── src/                     # Modern PHP structure
├── admin-react/            # React admin interface
├── assets/
└── tests/
```

The AI agents will automatically adapt to whatever structure your competitor uses!

## Troubleshooting

**Symlink shows as broken?**
- Check the absolute path is correct
- Ensure the target plugin exists
- Use `ls -la inputs/competitor-plugin` to verify

**Seeing nested folder structure?**
If you see `inputs/competitor-plugin/plugin-name/files` instead of `inputs/competitor-plugin/files`:
```bash
# This means you symlinked to a parent folder, not the plugin folder itself
# Fix it:
rm inputs/competitor-plugin
ln -s /path/to/actual/plugin-folder inputs/competitor-plugin

# Verify files are now at the top level:
ls inputs/competitor-plugin/
# Should show: plugin-name.php (not another folder)
```

**Permission issues?**
```bash
# Give read permissions
chmod -R a+r /path/to/competitor-plugin
```

**Want to change the plugin later?**
```bash
# Remove old symlink
rm inputs/competitor-plugin

# Create new symlink
ln -s /path/to/new-plugin inputs/competitor-plugin
```

**Test the symlink works for AI agents:**
```bash
# The agents will read files like this:
cat inputs/competitor-plugin/*.php | head -30
# Should show the plugin code directly
```

