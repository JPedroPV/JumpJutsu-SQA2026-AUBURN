# JumpJustsu-SQA2026

## Project Overview

This project is for the SQA Verification & Validation assignment using 21 CFR 117.130.

The GitHub Actions tab should show a full green passing workflow when everything is working correctly.

---

## Important Note About the outputs Folder

There may be no files inside the `outputs/` folder when the repository is first opened.

This is expected because the output files are generated when the scripts run. The `outputs/` folder contains generated files, not hand-written source code.

If the TA wants to directly view the generated JSON files, they can clone the repository and run the scripts locally using the commands below.

---

## How to Check the Project

The TA can check the project in two ways:

1. Check the GitHub Actions run.
2. Clone the repository and run the scripts locally to generate the output files.

---

## Option 1: Check GitHub Actions

1. Open the GitHub repository.
2. Click the **Actions** tab.
3. Open the latest workflow run named:

```yaml
github-actions-JumpJustsu-SQA2026
```

4. Confirm that the run is green.

A green run means GitHub Actions successfully:

- Generated `outputs/requirements.json`
- Generated `outputs/expected_structure.json`
- Generated `outputs/test_cases.json`
- Ran verification
- Ran validation

The generated output files are created inside the GitHub Actions runner during the workflow. They may not appear permanently in the repository unless they are committed.

---

## Option 2: Generate and View the Output Files Locally

If the TA wants to directly view the generated JSON files, they can clone the repository and run the scripts manually.

From the root of the cloned repository, run:

```bash
python scripts/generate_requirements.py -i "Input CFR File/CFR-117.130.md" -o "outputs/requirements.json" -c "21 CFR 117.130"
python scripts/generate_test_cases.py
python scripts/verify.py
python scripts/validate.py
```

The scripts should be run from the root project folder because the paths are written relative to the repository root.

After running the commands, the `outputs/` folder should contain:

```text
requirements.json
expected_structure.json
test_cases.json
```

The important files to check are:

```text
outputs/requirements.json
outputs/expected_structure.json
outputs/test_cases.json
```

If `verify.py` and `validate.py` both pass, the project is working correctly.
