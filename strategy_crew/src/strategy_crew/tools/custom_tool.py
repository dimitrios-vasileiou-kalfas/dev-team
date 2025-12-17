from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import os
from pathlib import Path


class FileReaderInput(BaseModel):
    """Input schema for FileReaderTool."""
    file_path: str = Field(..., description="Relative or absolute path to the file to read")


class FileReaderTool(BaseTool):
    name: str = "read_file"
    description: str = (
        "Reads the contents of a file. Use this to read plugin code files, configuration files, "
        "documentation, etc. Provide the file path relative to the plugin directory or absolute path."
    )
    args_schema: Type[BaseModel] = FileReaderInput

    def _run(self, file_path: str) -> str:
        try:
            # Handle both relative and absolute paths
            if not os.path.isabs(file_path):
                # Try relative to current working directory
                file_path = os.path.join(os.getcwd(), file_path)

            if not os.path.exists(file_path):
                return f"Error: File not found: {file_path}"

            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # Limit output size to prevent context overflow
            max_chars = 50000
            if len(content) > max_chars:
                return f"{content[:max_chars]}\n\n[FILE TRUNCATED - Total size: {len(content)} chars]"

            return content
        except Exception as e:
            return f"Error reading file: {str(e)}"


class DirectoryListInput(BaseModel):
    """Input schema for DirectoryListTool."""
    directory_path: str = Field(..., description="Path to directory to list")
    recursive: bool = Field(default=False, description="Whether to list recursively")


class DirectoryListTool(BaseTool):
    name: str = "list_directory"
    description: str = (
        "Lists files and directories in a given path. Use this to explore plugin structure, "
        "find configuration files, locate source code, etc. Set recursive=True to see full tree."
    )
    args_schema: Type[BaseModel] = DirectoryListInput

    def _run(self, directory_path: str, recursive: bool = False) -> str:
        try:
            if not os.path.isabs(directory_path):
                directory_path = os.path.join(os.getcwd(), directory_path)

            if not os.path.exists(directory_path):
                return f"Error: Directory not found: {directory_path}"

            if not os.path.isdir(directory_path):
                return f"Error: Path is not a directory: {directory_path}"

            result = []

            if recursive:
                for root, dirs, files in os.walk(directory_path):
                    level = root.replace(directory_path, '').count(os.sep)
                    indent = ' ' * 2 * level
                    result.append(f"{indent}{os.path.basename(root)}/")
                    subindent = ' ' * 2 * (level + 1)
                    for file in sorted(files):
                        result.append(f"{subindent}{file}")
            else:
                items = sorted(os.listdir(directory_path))
                for item in items:
                    item_path = os.path.join(directory_path, item)
                    if os.path.isdir(item_path):
                        result.append(f"{item}/")
                    else:
                        size = os.path.getsize(item_path)
                        result.append(f"{item} ({size} bytes)")

            return "\n".join(result) if result else "Directory is empty"
        except Exception as e:
            return f"Error listing directory: {str(e)}"


class FindFilesInput(BaseModel):
    """Input schema for FindFilesTool."""
    directory_path: str = Field(..., description="Directory to search in")
    pattern: str = Field(..., description="File pattern to match (e.g., '*.php', 'readme.*')")


class FindFilesTool(BaseTool):
    name: str = "find_files"
    description: str = (
        "Finds files matching a pattern in a directory and its subdirectories. "
        "Use this to locate specific file types (e.g., all PHP files, config files, test files)."
    )
    args_schema: Type[BaseModel] = FindFilesInput

    def _run(self, directory_path: str, pattern: str) -> str:
        try:
            if not os.path.isabs(directory_path):
                directory_path = os.path.join(os.getcwd(), directory_path)

            if not os.path.exists(directory_path):
                return f"Error: Directory not found: {directory_path}"

            from pathlib import Path
            matches = list(Path(directory_path).rglob(pattern))

            if not matches:
                return f"No files matching '{pattern}' found in {directory_path}"

            result = [str(match.relative_to(directory_path)) for match in matches]
            return "\n".join(sorted(result))
        except Exception as e:
            return f"Error finding files: {str(e)}"

