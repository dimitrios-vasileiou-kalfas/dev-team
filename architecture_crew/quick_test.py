#!/usr/bin/env python3
"""
Quick interactive tool tester
Run specific tool tests without the full crew
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from architecture_crew.tools.custom_tool import (
    FileWriterTool,
    FileReaderTool,
    DirectoryListTool,
    FindFilesTool
)


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Test architecture crew tools")
    parser.add_argument("tool", choices=["write", "read", "list", "find"],
                       help="Tool to test")
    parser.add_argument("args", nargs="*", help="Tool arguments")

    args = parser.parse_args()

    if args.tool == "write":
        if len(args.args) < 2:
            print("Usage: python quick_test.py write <file_path> <content>")
            return 1
        tool = FileWriterTool()
        result = tool._run(file_path=args.args[0], content=" ".join(args.args[1:]))
        print(result)

    elif args.tool == "read":
        if len(args.args) < 1:
            print("Usage: python quick_test.py read <file_path>")
            return 1
        tool = FileReaderTool()
        result = tool._run(file_path=args.args[0])
        print(result)

    elif args.tool == "list":
        if len(args.args) < 1:
            print("Usage: python quick_test.py list <directory_path> [--recursive]")
            return 1
        tool = DirectoryListTool()
        recursive = "--recursive" in args.args
        dir_path = args.args[0]
        result = tool._run(directory_path=dir_path, recursive=recursive)
        print(result)

    elif args.tool == "find":
        if len(args.args) < 2:
            print("Usage: python quick_test.py find <directory_path> <pattern>")
            return 1
        tool = FindFilesTool()
        result = tool._run(directory_path=args.args[0], pattern=args.args[1])
        print(result)

    return 0


if __name__ == "__main__":
    sys.exit(main())

