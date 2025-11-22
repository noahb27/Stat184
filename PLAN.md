# Project and Repository Plan – STAT184 SAPA Cleaning

## 1. Project Goals
The purpose of this project is to build a reproducible data-cleaning workflow for the SAPA psychological assessment dataset. The project focuses on preparing the data for analysis by removing metadata, handling low-quality or incomplete entries, removing empty columns, and producing a cleaned CSV file suitable for merging with other datasets.

### Primary Goals:
- Load SAPA data exported from R.
- Remove unnecessary metadata and identifiers.
- Filter out incomplete or invalid rows.
- Remove fully empty or non-informative columns.
- Produce a cleaned dataset stored locally in the `Processed/` directory.
- Document the entire workflow using Quarto for Activity #14.

---

## 2. Repository Goals
This repository demonstrates proper GitHub workflow as required for STAT184.  
The goals for maintaining the repository include:

- Using a `main` branch as the stable version of the project.
- Conducting all development work in a `dev` branch.
- Tracking tasks and progress through GitHub Issues.
- Creating meaningful commits referencing Issues.
- Producing pull requests to merge changes from `dev` into `main`.
- Following documentation standards using README.md and PLAN.md.

---

## 3. Needs
To complete the project and maintain the repository successfully, the following are required:

### Technical Needs:
- Python (with pandas and numpy)
- RStudio for exporting the raw SAPA data
- Git and GitHub for version control
- Quarto to render Activity14.qmd into PDF

### Project Needs:
- Raw SAPA dataset
- Cleaning pipeline script (`sapa_clean_from_r.py`)
- Documentation files (README.md and PLAN.md)
- Folder structure: Scripts, Raw, Processed

---

## 4. Steps

### Steps for the Project
1. Load the raw SAPA file exported from R.
2. Identify and remove metadata columns.
3. Apply row filters to remove low-quality or incomplete responses.
4. Identify and remove empty or non-informative columns.
5. Export the cleaned dataset to the `Processed` directory.
6. Test the script to ensure it runs end-to-end.
7. Document and summarize results using Quarto in Activity14.qmd.

---

### Steps for Maintaining the Repository
1. Clone the repository and set up `main` and `dev` branches.
2. Create Issues for major tasks such as project structure, cleaning script, and documentation.
3. Do all development work on the `dev` branch.
4. Make meaningful commits with messages that reference and close Issues.
5. Push commits regularly to keep the dev branch updated.
6. Submit a pull request from `dev` → `main` once development tasks are complete.
7. Continue updating documentation and maintaining the repo as needed.

---

## 5. Summary
This PLAN.md outlines the structure and responsibilities of both the project and the repository.  
It ensures that the project meets both the technical data-cleaning requirements and the GitHub workflow expectations for STAT184.
