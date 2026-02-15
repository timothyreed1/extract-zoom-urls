#!/usr/bin/env python3
"""
Extract URLs from Zoom chat logs and output in CSV format.
Format: filename, url, author
"""

import sys
import os
import re
import csv
from typing import List

# Zoom chat log format has timestamps in first 15 characters (e.g., "09:23:45 From ")
TIMESTAMP_LENGTH = 15


def extract_urls_from_file(path: str, writer: csv.writer) -> None:
    """
    Extract URLs from a single Zoom chat log file.
    
    Args:
        path: Path to the Zoom chat log file
        writer: CSV writer to output results
    """
    try:
        with open(path, encoding='utf-8') as file:
            filename = os.path.basename(path)
            
            for line in file:
                # Skip lines that are too short to contain timestamp + content
                if len(line) <= TIMESTAMP_LENGTH:
                    continue
                
                content = line[TIMESTAMP_LENGTH:]
                urls = re.findall(r'(https?://[^\s]+)', content)
                
                if urls:
                    # Extract author name (text before first colon)
                    author_parts = content.split(':', 1)
                    author = author_parts[0].strip() if author_parts else "Unknown"
                    
                    # Write a row for each URL found on this line
                    for url in urls:
                        writer.writerow([filename, url, author])
                    
    except FileNotFoundError:
        print(f"Error: File not found: {path}", file=sys.stderr)
    except PermissionError:
        print(f"Error: Permission denied: {path}", file=sys.stderr)
    except Exception as e:
        print(f"Error processing {path}: {e}", file=sys.stderr)


def main(argv: List[str]) -> None:
    """
    Main function to process Zoom chat log files.
    
    Args:
        argv: Command line arguments
    """
    script = os.path.basename(argv[0])
    usage = f"Extract URLs from Zoom chat logs.\nUSAGE: {script} filename [filename...]"
    
    if len(argv) == 1:
        print(usage)
        sys.exit(1)
    
    writer = csv.writer(sys.stdout)
    
    for path in argv[1:]:
        extract_urls_from_file(path, writer)


if __name__ == "__main__":
    main(sys.argv)
