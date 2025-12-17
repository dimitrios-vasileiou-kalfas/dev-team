
#!/bin/bash
# Setup symlinks for architecture_crew
# This script creates symlinks to shared directories to avoid path traversal issues

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Setting up symlinks for architecture_crew..."

# Create symlink to shared outputs
if [ ! -e "$SCRIPT_DIR/outputs" ]; then
    ln -s ../outputs/architecture "$SCRIPT_DIR/outputs"
    echo "✓ Created symlink: outputs -> ../outputs/architecture"
else
    echo "✓ Symlink already exists: outputs"
fi

# Create symlink to shared inputs
if [ ! -e "$SCRIPT_DIR/inputs" ]; then
    ln -s ../inputs "$SCRIPT_DIR/inputs"
    echo "✓ Created symlink: inputs -> ../inputs"
else
    echo "✓ Symlink already exists: inputs"
fi

echo "✅ Setup complete!"

