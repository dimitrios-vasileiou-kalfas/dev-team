# Plugin Architecture Documentation Template

Add this file to your skeleton plugin as `ARCHITECTURE.md` to help AI agents understand your structure.

---

# Plugin Architecture

## Overview

Brief description of your plugin's architecture and design philosophy.

## Folder Structure

```
skeleton-plugin/
├── wp-skeleton-plugin.php       # Main plugin file
├── includes/                     # [Describe purpose]
├── src/                          # [Describe purpose]
│   ├── admin/                    # [Describe purpose]
│   ├── frontend/                 # [Describe purpose]
│   └── api/                      # [Describe purpose]
├── admin-react/                  # [Describe purpose]
│   └── src/
│       ├── components/           # [Describe purpose]
│       ├── pages/                # [Describe purpose]
│       ├── hooks/                # [Describe purpose]
│       └── utils/                # [Describe purpose]
├── assets/
└── tests/
```

## Naming Conventions

### PHP
- **Namespace:** `YourPlugin\` (or none if not using namespaces)
- **Class prefix:** `YP_` (if not using namespaces)
- **Hook prefix:** `your_plugin_`
- **Function prefix:** `yp_` or `your_plugin_`

### JavaScript/React
- **Component naming:** PascalCase (e.g., `MyComponent.jsx`)
- **File naming:** kebab-case or PascalCase
- **Hook naming:** `use` prefix (e.g., `useAPI.js`)

## Architectural Patterns

### Backend (PHP)
- **Dependency Injection:** Constructor injection, no service container
- **Repository Pattern:** Used for database access (or: Not used, direct wpdb)
- **Service Layer:** Business logic in service classes (or: Logic in main classes)
- **Hook Registration:** Centralized in main class (or: Distributed per feature)

### Frontend (React)
- **State Management:** Context API (or: Redux, Zustand, etc.)
- **API Client:** Custom hooks using fetch (or: Axios, RTK Query)
- **Routing:** React Router v6 (or: No routing, single page)
- **Styling:** Material-UI sx prop (or: CSS modules, styled-components)

## Design Decisions

### Why We Organize This Way
Explain key architectural decisions:
- Why you chose this folder structure
- Why certain patterns are used
- Trade-offs you made
- Things to keep in mind when adding features

### Important Conventions
- How to register new hooks
- Where to add new REST API endpoints
- How to create new React components
- Testing requirements (unit tests required? E2E tests?)

## WordPress Integration

### Hooks & Filters
- Hook registration pattern: [Describe]
- Custom hooks naming: `{prefix}_{context}_{action}`
- Filter naming: `{prefix}_{context}_{what}`

### Database
- Custom tables prefix: `{wpdb->prefix}your_plugin_`
- Schema location: `includes/class-database.php`
- Migration approach: [Describe]

### REST API
- Base route: `/wp-json/your-plugin/v1/`
- Authentication: WordPress nonces + cookie auth
- Endpoint organization: One class per endpoint group

## React/MUI Setup

### Material-UI Theme
- Theme file: `admin-react/src/theme.js`
- Primary color: #your-color
- Custom components: [List any customized MUI components]

### Component Structure
- Smart components (pages): `admin-react/src/pages/`
- Dumb components: `admin-react/src/components/`
- Layout components: `admin-react/src/components/layout/`

### API Integration
- API client: `admin-react/src/utils/api.js`
- Custom hooks for API: `admin-react/src/hooks/useAPI.js`
- Error handling: [Describe approach]

## Testing

### PHP Testing (PHPUnit)
- Test location: `tests/php/`
- Naming: `test-{class-name}.php`
- Coverage goal: 80%+
- Mocking: Brain Monkey for WordPress functions

### JavaScript Testing (Jest)
- Test location: Co-located with components
- Naming: `ComponentName.test.jsx`
- Coverage goal: 80%+
- Library: React Testing Library

### E2E Testing (Playwright)
- Test location: `tests/e2e/`
- Naming: `feature-name.spec.js`
- Required: Critical user flows only

## Build & Development

### PHP Dependencies
- Managed by: Composer (or: No dependencies)
- Location: `composer.json`

### JavaScript Dependencies
- Managed by: npm
- Location: `admin-react/package.json`
- Build tool: Webpack (or: Vite, Parcel)
- Build command: `npm run build`
- Dev server: `npm start`

## Code Style

### PHP
- Standard: WordPress Coding Standards
- Linter: PHPCS with WordPress ruleset
- Formatting: PSR-12 (or: WordPress style)

### JavaScript/React
- Standard: ESLint + Prettier
- Config: `.eslintrc.js`
- Formatting: Prettier with 2-space indentation

## Security Considerations

- Nonce validation required for: All AJAX/REST requests
- Data sanitization: All user inputs
- Output escaping: All HTML output
- Capability checks: All admin actions

## Adding New Features

### Backend Feature
1. Create class in `src/{context}/class-{feature}.php`
2. Register hooks in class constructor or dedicated method
3. Write tests in `tests/php/test-{feature}.php`
4. Document public methods with PHPDoc

### Frontend Feature
1. Create component in `admin-react/src/components/{Feature}.jsx`
2. Create page if needed in `admin-react/src/pages/{Feature}.jsx`
3. Write tests `{Feature}.test.jsx`
4. Update routing if needed

### REST API Endpoint
1. Create controller in `src/api/class-{endpoint}-controller.php`
2. Register route in main plugin class
3. Add permission callbacks
4. Document in code comments

## Common Pitfalls

List common mistakes or things to avoid:
- Don't use global variables
- Don't directly access $wpdb without sanitization
- Don't skip nonce validation
- Don't forget to enqueue scripts properly
- [Add your specific gotchas]

## Resources

- [Link to your internal docs]
- [Coding standards document]
- [Design system / style guide]

---

**Note for AI Agents:** This document should be your PRIMARY reference when designing new features. Follow these patterns and conventions to ensure new code integrates seamlessly with the existing codebase.

