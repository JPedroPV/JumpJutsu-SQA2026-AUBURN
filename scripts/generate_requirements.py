# TODO: Task 1; Modify this script to generat expected_structure.json
# scripts/generate_requirements.py
import json
import re
import argparse

# ---------- Arguments ----------
parser = argparse.ArgumentParser(description="Generate requirement JSON from CFR Markdown")
parser.add_argument("--input", "-i", required=True, help="Input Markdown file (.md)")
parser.add_argument("--output", "-o", required=True, help="Output JSON file")
parser.add_argument("--cfr", "-c", required=True, help="CFR section (e.g., 21 CFR 117.130)")
args = parser.parse_args()

INPUT_MD = args.input
OUTPUT_JSON = args.output
# Get output directory from OUTPUT_JSON to ensure expected_structure.json is saved in the same location
last_sep_index = max(OUTPUT_JSON.rfind("/"), OUTPUT_JSON.rfind("\\"))
OUTPUT_DIR = OUTPUT_JSON[:last_sep_index + 1] if last_sep_index != -1 else ""
CFR_SECTION = args.cfr

# ---------- Read File ----------
with open(INPUT_MD, "r") as f:
    lines = [line.strip() for line in f if line.strip()]

requirements = []
current_req = None

# ---------- Parse ----------
for line in lines:

    # Capture REQ ID
    req_match = re.search(r"→\s*(REQ-[\d\.]+-\d+)", line)
    if req_match:
        current_req = req_match.group(1)
        continue

    # Capture atomic rules
    atomic_match = re.match(r"^(.*?)\s*→\s*([A-Z]\d*)$", line)
    if atomic_match and current_req:
        description = atomic_match.group(1).strip()
        suffix = atomic_match.group(2)

        requirement_id = f"{current_req}{suffix}"

        # Parent logic
        if len(suffix) == 1:
            parent = current_req
        else:
            parent = f"{current_req}{suffix[0]}"

        requirements.append({
            "requirement_id": requirement_id,
            "description": description,
            "source": CFR_SECTION,
            "parent": parent
        })

# Keep 10 atomic rules (for testing purposes)
requirements = requirements[:10]

# ---------- Save ----------
with open(OUTPUT_JSON, "w") as f:
    json.dump(requirements, f, indent=2)

print(f"Saved {len(requirements)} requirements → {OUTPUT_JSON}")

# Generating expected_structure.json
expected_structure = {}
for req in requirements:
    if req["requirement_id"][:-1] in expected_structure:
        if req["requirement_id"][-1:] not in expected_structure[req["requirement_id"][:-1]]:
            expected_structure[req["requirement_id"][:-1]].append(req["requirement_id"][-1:])
    else:
        expected_structure[req["requirement_id"][:-1]] = [req["requirement_id"][-1:]]

with open(f"{OUTPUT_DIR}expected_structure.json", "w") as f:
    json.dump(expected_structure, f, indent=2)
