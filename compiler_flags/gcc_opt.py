import re
from collections import defaultdict

# Input file
INPUT_FILE = "test/gcc_simple_opt.txt"

# Regex to match structured diagnostic lines
structured_re = re.compile(
    r'^(.*?):(\d+):(\d+):\s+(note|missed|remark|optimized):\s+(.*)$'
)

# Storage structures
structured = defaultdict(list)
unstructured = []

with open(INPUT_FILE, 'r') as f:
    for line in f:
        stripped = line.strip()
        if not stripped:
            continue  # skip empty lines
        match = structured_re.match(stripped)
        if match:
            filename, lineno, col, opt_type, message = match.groups()
            structured[opt_type].append({
                'file': filename,
                'line': int(lineno),
                'column': int(col),
                'message': message
            })
        else:
            unstructured.append(stripped)

# Display structured diagnostics
print("\n=== Structured Optimization Messages ===")
for opt_type, entries in structured.items():
    print(f"\n{opt_type.upper()} ({len(entries)}):")
    for entry in entries:
        print(f"{entry['file']}:{entry['line']}:{entry['column']} - {entry['message']}")

# Display unstructured logs
if unstructured:
    print("\n=== Unstructured Log Messages ===")
    for line in unstructured:
        print(line)
