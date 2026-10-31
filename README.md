# Recruitment & Placement Management System

Python + MySQL console project for candidate records, company/job listings, eligibility checks, and applications.

## Setup
1. Connect to `Local instance MySQL80` in MySQL Workbench.
2. Open `schema.sql` and click the lightning-bolt Execute button.
3. Edit `config.py`; replace `YOUR_MYSQL_PASSWORD` with your MySQL password.
4. In VS Code terminal, open this folder and run:
   `pip install -r requirements.txt`
   `python main.py`

## Menu
1. Add candidate
2. Add company and job
3. List candidates
4. List jobs
5. Apply for job (checks percentage, backlogs, and required skills)
6. View applications
7. Update application status

Note: Workbench is the interface; MySQL Server must also be installed and running.
