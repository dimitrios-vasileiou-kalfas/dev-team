# Skeleton Plugin

Place your skeleton WordPress plugin here. This serves as the **foundation** for the new plugin that will be built.

## Setup Options

### Option 1: Symlink (Recommended) 🔗

Create a symlink to your local skeleton plugin:

```bash
# From project root
ln -s /absolute/path/to/your/skeleton-plugin inputs/skeleton-plugin

# Example:
ln -s ~/Projects/wp-skeleton-plugin inputs/skeleton-plugin
```

**Benefits:**
- ✅ Always in sync with your skeleton template
- ✅ Update once, use everywhere
- ✅ No duplication
- ✅ Perfect for maintaining your plugin template

**Verify symlink:**
```bash
ls -la inputs/skeleton-plugin  # Should show -> /path/to/skeleton
```

### Option 2: Copy Plugin Files (Fallback)

Copy your skeleton plugin:

```bash
# From project root
cp -r /path/to/skeleton-plugin/* inputs/skeleton-plugin/

# Or drag and drop in Finder/Explorer
```

**Use this if:**
- You want to version this specific skeleton setup
- Working with a one-time template
- Symlinks aren't supported

## What Is a Skeleton Plugin?

A **skeleton plugin** is your base WordPress plugin template with:
- ✅ Basic plugin structure set up
- ✅ React + Material-UI admin interface configured
- ✅ Build tools and configuration files
- ✅ Testing setup (PHPUnit, Jest, Playwright)
- ✅ Code organization you prefer

The AI agents will **respect this structure** and build on top of it.

## Expected Skeleton Structure

Your skeleton should have this structure (as described in your requirements):

```
skeleton-plugin/
├── wp-skeleton-plugin.php       # Main plugin file
│                                 # - Plugin header
│                                 # - Activation/deactivation hooks
│
├── includes/                     # Core PHP functionality & hooks
│   ├── class-plugin.php          # Main plugin class
│   ├── class-activator.php       # Activation logic
│   └── class-deactivator.php     # Deactivation logic
│
├── src/                          # Modern WordPress development
│   ├── admin/                    # Admin-specific PHP classes
│   │   └── class-admin.php
│   ├── frontend/                 # Public-facing PHP
│   │   └── class-public.php
│   └── blocks/                   # Gutenberg blocks (PHP part)
│       └── block-registration.php
│
├── admin-react/                  # React admin interface ⚛️
│   ├── src/
│   │   ├── components/           # Reusable React components
│   │   │   └── HelloWorld.jsx
│   │   ├── pages/                # Admin page components
│   │   │   └── Dashboard.jsx
│   │   ├── hooks/                # Custom React hooks
│   │   │   └── useAPI.js
│   │   ├── utils/                # JavaScript utilities
│   │   │   └── helpers.js
│   │   ├── App.jsx               # Main app component
│   │   └── index.jsx             # Entry point
│   ├── public/                   # Static assets
│   ├── build/                    # Built React app (gitignored)
│   ├── package.json              # React dependencies
│   └── webpack.config.js         # Build configuration
│
├── assets/                       # Plugin assets
│   ├── css/                      # Stylesheets (SCSS/CSS)
│   ├── js/                       # Vanilla JS (if needed)
│   └── images/                   # Images & icons
│
├── build/                        # WordPress build output (gitignored)
│
├── languages/                    # Translation files (.pot, .po, .mo)
│
├── tests/                        # Plugin tests
│   ├── php/                      # PHPUnit tests
│   │   └── test-sample.php
│   ├── js/                       # Jest tests
│   │   └── sample.test.js
│   └── e2e/                      # Playwright E2E tests
│       └── sample.spec.js
│
├── Dockerfile.admin-react        # Docker for React dev
├── composer.json                 # PHP dependencies
├── phpunit.xml                   # PHPUnit configuration
└── README.md                     # Documentation
```

## How AI Agents Use the Skeleton

**✨ The AI agents will automatically understand your skeleton plugin structure!**

### Recommended: Add Architecture Documentation 📄

For best results, add an `ARCHITECTURE.md` file to your skeleton plugin root describing:
- Folder structure and organization
- Naming conventions (namespaces, prefixes)
- Architectural patterns (DI, repository pattern, etc.)
- Design decisions and rationale
- Coding standards

**Template available:** See `docs/ARCHITECTURE_TEMPLATE.md` in this project for a complete template.

**Benefits:**
- ✅ Faster and more accurate understanding
- ✅ Agents know *why* certain patterns exist
- ✅ Better integration with existing code
- ✅ Documents your architecture for humans too!

### Fallback: Code Analysis

If no documentation exists, agents will analyze your actual code:
- 📁 Read folder organization
- 🏗️ Study architectural patterns
- 📝 Identify naming conventions
- 🎨 Understand coding style
- ⚛️ Analyze React setup and MUI theme
- 🧪 Review testing patterns

Then they design and build features that seamlessly integrate with YOUR existing codebase.

### Software Architect Agent 🏗️
- Respects your folder structure
- Designs features to fit your organization
- Plans where new classes/components go
- Maintains your architectural patterns

### WordPress Backend Developer 💻
- Works ONLY in PHP files:
  - `includes/`
  - `src/admin/`
  - `src/frontend/`
  - `src/blocks/`
- Never touches `admin-react/`
- Follows your existing PHP patterns

### React Frontend Developer ⚛️
- Works ONLY in `admin-react/` folder
- Never touches PHP files
- Follows your React setup
- Uses your existing MUI theme
- Matches your component patterns

## Key Principles

### Separation of Concerns
- **Backend devs** → PHP files only
- **Frontend devs** → React files only
- Clean separation, no conflicts

### Modular Architecture
Your skeleton sets the pattern:
- OOP classes in `includes/`
- Modern PHP in `src/`
- React components in `admin-react/src/components/`
- Pages in `admin-react/src/pages/`

### SOLID Principles
The architect ensures:
- Single Responsibility
- Open/Closed
- Liskov Substitution
- Interface Segregation
- Dependency Inversion

## Minimum Requirements

Your skeleton must have:
- ✅ Valid WordPress plugin header in main PHP file
- ✅ Basic folder structure (includes/, src/, admin-react/)
- ✅ React setup with package.json
- ✅ Material-UI configured
- ✅ At least one "Hello World" example

The AI will build on top of this foundation!

## Troubleshooting

**Symlink shows as broken?**
```bash
# Verify path
ls -la inputs/skeleton-plugin

# Recreate if needed
rm inputs/skeleton-plugin
ln -s /correct/path/to/skeleton inputs/skeleton-plugin
```

**Want to update your skeleton?**
- With symlink: Just update the original, changes reflect immediately
- With copy: Copy again to refresh

**Testing skeleton structure?**
```bash
# Check main file exists
cat inputs/skeleton-plugin/wp-skeleton-plugin.php | head -n 20

# Check React setup
cat inputs/skeleton-plugin/admin-react/package.json

# Check folder structure
tree -L 2 inputs/skeleton-plugin
```

