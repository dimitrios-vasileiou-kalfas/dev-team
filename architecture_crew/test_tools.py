#!/usr/bin/env python3
"""
Test script for architecture_crew tools
Tests FileWriterTool, FileReaderTool, DirectoryListTool, and FindFilesTool
without running the entire crew.
"""

import sys
from pathlib import Path

# Add the src directory to Python path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from architecture_crew.tools.custom_tool import (
    FileWriterTool,
    FileReaderTool,
    DirectoryListTool,
    FindFilesTool
)


def test_file_writer_tool():
    """Test writing files with FileWriterTool"""
    print("\n" + "="*60)
    print("Testing FileWriterTool")
    print("="*60)

    tool = FileWriterTool()

    # Test 1: Write a simple file
    print("\n[Test 1] Writing a test file...")
    result = tool._run(
        file_path="outputs/test-file.md",
        content="# Test Document\n\nThis is a test file created by FileWriterTool.\n"
    )
    print(f"Result: {result}")

    # Test 2: Write to a nested directory (auto-create parents)
    print("\n[Test 2] Writing to nested directory...")
    result = tool._run(
        file_path="outputs/specs/backend/test-class.md",
        content="# Test Class Specification\n\nThis tests directory creation.\n"
    )
    print(f"Result: {result}")

    # Test 3: Write multiple files (simulating backend specs)
    print("\n[Test 3] Writing multiple backend spec files...")
    specs = [
        ("class-core.md", "# Core Class\n\nMain initialization class."),
        ("class-loader.md", "# Loader Class\n\nHook management class."),
        ("class-api.md", "# API Class\n\nExternal API integration class.")
    ]

    for filename, content in specs:
        result = tool._run(
            file_path=f"outputs/specs/backend/{filename}",
            content=content
        )
        print(f"  ✓ {filename}: {result}")


def test_file_reader_tool():
    """Test reading files with FileReaderTool"""
    print("\n" + "="*60)
    print("Testing FileReaderTool")
    print("="*60)

    tool = FileReaderTool()

    # Read the test file we just created
    print("\n[Test 1] Reading test file...")
    result = tool._run(file_path="outputs/test-file.md")
    print(f"Content: {result[:100]}...")

    # Read a strategy file
    print("\n[Test 2] Reading plugin metadata...")
    result = tool._run(file_path="../outputs/strategy/plugin-metadata.json")
    print(f"Content: {result[:200]}...")


def test_directory_list_tool():
    """Test listing directories with DirectoryListTool"""
    print("\n" + "="*60)
    print("Testing DirectoryListTool")
    print("="*60)

    tool = DirectoryListTool()

    # List outputs directory
    print("\n[Test 1] Listing outputs directory...")
    result = tool._run(directory_path="outputs", recursive=False)
    print(result)

    # List outputs/specs recursively
    print("\n[Test 2] Listing outputs/specs recursively...")
    result = tool._run(directory_path="outputs/specs", recursive=True)
    print(result)


def test_find_files_tool():
    """Test finding files with FindFilesTool"""
    print("\n" + "="*60)
    print("Testing FindFilesTool")
    print("="*60)

    tool = FindFilesTool()

    # Find all .md files in outputs
    print("\n[Test 1] Finding all .md files in outputs...")
    result = tool._run(directory_path="outputs", pattern="*.md")
    print(result)

    # Find all .json files
    print("\n[Test 2] Finding all .json files...")
    result = tool._run(directory_path="../outputs/strategy", pattern="*.json")
    print(result)


def cleanup_test_files():
    """Clean up test files created during testing"""
    print("\n" + "="*60)
    print("Cleanup (optional)")
    print("="*60)

    import shutil
    test_dir = Path("outputs/specs")
    test_file = Path("outputs/test-file.md")

    if test_dir.exists():
        print(f"To remove test files, run: rm -rf {test_dir}")
    if test_file.exists():
        print(f"To remove test file, run: rm {test_file}")


def main():
    """Run all tool tests"""
    print("\n🧪 Architecture Crew Tools Test Suite")
    print("="*60)

    try:
        # Test each tool
        test_file_writer_tool()
        test_file_reader_tool()
        test_directory_list_tool()
        test_find_files_tool()

        print("\n" + "="*60)
        print("✅ All tests completed successfully!")
        print("="*60)

        cleanup_test_files()

    except Exception as e:
        print(f"\n❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())

