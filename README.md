# extract-zoom-urls.py
Python script to extract URLs from Zoom chat logs and output them in CSV format.
## Requirements
- Python 3.9+
- No external dependencies (uses only standard library)

## Installation
Download the script to any folder in your path and make it executable
```bash
chown 755 extract-zoom-urls.py
```
## Usage
This script takes one or more Zoom chat log filenames as arguments and outputs CSV data to stdout.
### Basic usage
```bash
extract-zoom-urls.py filename.txt
```
### Multiple files
```bash
extract-zoom-urls.py file1.txt file2.txt *.txt
```
### Save to CSV file
```bash
extract-zoom-urls.py *.txt > urls.csv
```
### Help
Run with no arguments for usage information:
```bash
% extract-zoom-urls.py
Extract URLs from Zoom chat logs.
USAGE: extract-zoom-urls.py filename [filename...]
```
## Output Format
The script outputs CSV with three columns:
1) Filename (source chat log)
2) URL (extracted link)
3) Author (person who posted the URL)

### Example output
```csv
ERT Thu Wkshp 2 chat.txt,https://www.dickblick.com/products/nature-print-paper/,Kirk (they/them)
ERT Thu Wkshp 2 chat.txt,https://vimeo.com/user495806,John
ERT Thu Wkshp 2 chat.txt,https://www.youtube.com/watch?v=0t-tnN-moSY,Jennifer (she/her)
ERT Thu Wkshp 2 chat.txt,https://open.spotify.com/episode/3X9jFkCmbLN54ELGaU2W5K,Tyler (he/him)
```

## Notes

- The script assumes Zoom chat logs have timestamps in the first 15 characters of each line
- Files are read with UTF-8 encoding
- Error messages are written to stderr, not stdout, so they won't corrupt CSV output
- If a line contains multiple URLs, each one gets its own CSV row with same filename and author
