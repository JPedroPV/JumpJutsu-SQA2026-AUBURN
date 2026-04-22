#TODO: Task 2; Take in requirements.json and generates test_cases.json
import json
import os

requirementsPath = os.path.join("outputs","requirements.json")
structurePath = os.path.join("outputs","expected_structure.json")
testCasesPath = os.path.join("outputs","test_cases.json")


def openJSON(inputPath):
    with open(inputPath,"r") as f:
        output = json.load(f)
        f.close()
    return output

requirements = openJSON(requirementsPath)
structures = openJSON(structurePath)

#get the structures into a more usable form
structsToUse = []
for item, key in structures.items():
    for thing in key:
        structsToUse.append(f"{item}{thing}")

#combine the requirements with its defintion
test_cases = []
req_lookup = {req["requirement_id"]: req["description"] for req in requirements}
for i in range(1,len(structsToUse)+1):
    test_cases.append({
        "test_case_id": f"TC-{i:03d}",   # formats as TC-001, TC-002, etc.
        "requirement_id": structsToUse[i-1],
        "description": req_lookup[structsToUse[i-1]]
    })

    print(f"{structsToUse[i-1]}, ID {i-1}")

# save output to file
with open(testCasesPath, "w") as f:
    json.dump(test_cases, f, indent=2)