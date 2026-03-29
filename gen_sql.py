import os

SQL_FILE = '/home/runner/work/FOCUS-MAS-Init/FOCUS-MAS-Init/EDF Empty Step 8 1 A VISION-MSSQL-8.6-9.0.2-NoVLS Github PURE  Part 2a.sql'

with open(SQL_FILE, 'r') as f:
    existing_lines = f.readlines()

# We'll reconstruct the file, keeping everything up to (but not including) the final DB_UPDATE_HISTORY section
# Find the line index of SECTION 16
section16_idx = None
for i, line in enumerate(existing_lines):
    if 'SECTION 16: DB_UPDATE_HISTORY' in line:
        section16_idx = i
        break

print(f"Section 16 starts at line {section16_idx}")
base_content = ''.join(existing_lines[:section16_idx])
final_content = ''.join(existing_lines[section16_idx:])
print("Base split OK")
