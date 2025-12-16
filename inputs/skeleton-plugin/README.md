# Skeleton Plugin

Place your skeleton WordPress plugin here. This serves as the foundation for the new plugin.

## Expected Structure

```
skeleton-plugin/
├── wp-skeleton-plugin.php       # Main plugin file
├── includes/                    # Core PHP functionality & hooks
├── src/                         # Modern WordPress development structure
│   ├── admin/                   # Admin-specific PHP classes & logic
│   ├── frontend/                # Public-facing PHP functionality  
│   └── blocks/                  # Gutenberg blocks (can include React)
├── admin-react/                 # React admin interface
│   ├── src/                     # React components & pages
│   │   ├── components/          # Reusable React components
│   │   ├── pages/               # Admin page components
│   │   ├── hooks/               # Custom React hooks
│   │   └── utils/               # JavaScript utilities
│   ├── public/                  # Static assets
│   ├── build/                   # Built React app (gitignored)
│   └── package.json             # React dependencies
├── assets/                      # Plugin assets
│   ├── css/                     # Stylesheets (SCSS/CSS)
│   ├── js/                      # Vanilla JS (if needed)
│   └── images/                  # Images & icons
├── build/                       # WordPress build output (gitignored)
├── languages/                   # Translation files
├── tests/                       # Plugin tests
├── Dockerfile.admin-react       # Docker config for React dev
└── README.md                    # Documentation
```

The Software Architect will respect this structure and make modifications as needed while maintaining the organizational pattern.

