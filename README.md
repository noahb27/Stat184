# STAT184 – SAPA Data Cleaning Project

## Overview
This repository contains my STAT184 project focused on cleaning and preparing the SAPA (Synthetic Aperture Personality Assessment) dataset for further analysis. The project includes data extraction, metadata removal, row and column filtering, and the creation of a final cleaned dataset that can be merged with other personality data sources.

This repository demonstrates proper use of GitHub branching, issues, commits, documentation, and workflow management as required by the STAT184 course.

---

## Project Purpose
The primary goal of this project is to build a reproducible data-cleaning pipeline that:

1. Loads SAPA data exported from R.
2. Removes metadata and unnecessary fields.
3. Drops incomplete or low-quality responses.
4. Removes empty or non-informative columns.
5. Exports a cleaned CSV suitable for analysis or merging with other psychological datasets.

---

## Data Source
The SAPA dataset used in this project was originally obtained through R as an RData file and exported into a working format for Python.  
The raw files were included in the local project environment but large processed files (over 100MB) were excluded from GitHub to meet repository size constraints.

---

*Note: Large data files exceeding GitHub's 100MB limit were removed from Git tracking and stored locally.*

---

## Current Project Plan
A detailed plan is included in `PLAN.md`, but the main goals include:

- Develop the full SAPA data-cleaning pipeline.
- Maintain proper version control practices using `main` and `dev` branches.
- Use GitHub Issues to track tasks and documentation.
- Demonstrate appropriate commit messages and workflow management.
- Complete Activity #14 using Quarto and include both QMD and PDF outputs.

---

## How to Use This Repository

### 1. Clone the Repository
git clone https://github.com/noahb27/Stat184.git

cd Stat184


### 2. Install Dependencies
This project uses Python libraries:
- pandas
- numpy

Install them if needed:


pip install pandas numpy


### 3. Run the Cleaning Script


python Scripts/sapa_clean_from_r.py


The cleaned dataset will be produced in the `Processed/` directory (stored locally due to size constraints).

---

## Branching Workflow
This repository follows the STAT184 required workflow:

- **main** → stable branch  
- **dev** → active development branch  

All work is completed on `dev` and merged into `main` through pull requests.

---

## Issues & Documentation
GitHub Issues were used to track major tasks:

- Building initial repository structure  
- Implementing the SAPA cleaning script  
- Creating README & PLAN documentation  

Issues include labels, descriptions, and commits that reference or close them.

---

## Contact Information
**Noah Buranasombati**  
Email: *your PSU email here*

If you have questions about the project structure, workflow, or data-cleaning code, feel free to reach out.

---

## License
This project is for educational purposes as part of STAT184 at Penn State University.