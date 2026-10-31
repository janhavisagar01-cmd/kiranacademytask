from db import execute
from eligibility import check_eligibility

def show(rows):
    if not rows:
        print("No records found.")
    else:
        for row in rows:
            print(row)

def add_candidate():
    name = input("Full name: ").strip()
    email = input("Email: ").strip()
    qualification = input("Qualification: ").strip()
    percentage = float(input("Percentage: "))
    year = int(input("Passing year: "))
    skills = input("Skills (comma-separated): ").strip()
    backlogs = int(input("Current backlogs: "))
    execute("INSERT INTO candidates (full_name,email,qualification,percentage,passing_year,skills,backlogs) VALUES (%s,%s,%s,%s,%s,%s,%s)",
            (name,email,qualification,percentage,year,skills,backlogs))
    print("Candidate added.")

def add_company_job():
    company = input("Company name: ").strip()
    location = input("Location: ").strip()
    try:
        execute("INSERT INTO companies (company_name,location) VALUES (%s,%s)", (company,location))
    except Exception:
        pass
    rows = execute("SELECT company_id FROM companies WHERE company_name=%s", (company,), True)
    if not rows:
        print("Could not find company.")
        return
    title = input("Job title: ").strip()
    minimum = float(input("Minimum percentage: "))
    max_backlogs = int(input("Maximum allowed backlogs: "))
    skills = input("Required skills (comma-separated): ").strip()
    execute("INSERT INTO jobs (company_id,job_title,minimum_percentage,maximum_backlogs,required_skills) VALUES (%s,%s,%s,%s,%s)",
            (rows[0]["company_id"],title,minimum,max_backlogs,skills))
    print("Job added.")

def list_candidates():
    show(execute("SELECT * FROM candidates ORDER BY candidate_id DESC", fetch=True))

def list_jobs():
    show(execute("SELECT j.job_id,c.company_name,j.job_title,j.minimum_percentage,j.maximum_backlogs,j.required_skills,j.status FROM jobs j JOIN companies c ON j.company_id=c.company_id ORDER BY j.job_id DESC", fetch=True))

def apply_for_job():
    cid = int(input("Candidate ID: "))
    jid = int(input("Job ID: "))
    candidates = execute("SELECT * FROM candidates WHERE candidate_id=%s", (cid,), True)
    jobs = execute("SELECT * FROM jobs WHERE job_id=%s AND status='Open'", (jid,), True)
    if not candidates or not jobs:
        print("Candidate/job not found or job closed.")
        return
    eligible, reasons = check_eligibility(candidates[0], jobs[0])
    if not eligible:
        print("Not eligible:", "; ".join(reasons))
        return
    execute("INSERT INTO applications (candidate_id,job_id) VALUES (%s,%s)", (cid,jid))
    print("Application submitted.")

def list_applications():
    show(execute("SELECT a.application_id,ca.full_name,j.job_title,c.company_name,a.application_status,a.applied_at FROM applications a JOIN candidates ca ON a.candidate_id=ca.candidate_id JOIN jobs j ON a.job_id=j.job_id JOIN companies c ON j.company_id=c.company_id ORDER BY a.application_id DESC", fetch=True))

def update_application():
    app_id = int(input("Application ID: "))
    status = input("Status (Applied/Shortlisted/Rejected/Selected): ").strip().title()
    if status not in {"Applied","Shortlisted","Rejected","Selected"}:
        print("Invalid status.")
        return
    execute("UPDATE applications SET application_status=%s WHERE application_id=%s", (status,app_id))
    print("Status updated.")

def main():
    actions = {
        "1": ("Add candidate", add_candidate),
        "2": ("Add company and job", add_company_job),
        "3": ("List candidates", list_candidates),
        "4": ("List jobs", list_jobs),
        "5": ("Apply for job (eligibility check)", apply_for_job),
        "6": ("View applications", list_applications),
        "7": ("Update application status", update_application),
    }
    while True:
        print("\n=== Recruitment & Placement Management System ===")
        for key, item in actions.items():
            print(f"{key}. {item[0]}")
        print("0. Exit")
        choice = input("Choose option: ").strip()
        if choice == "0":
            break
        if choice not in actions:
            print("Invalid option.")
            continue
        try:
            actions[choice][1]()
        except Exception as exc:
            print("Operation failed:", exc)
            print("Check config.py, schema.sql, and your MySQL connection.")

if __name__ == "__main__":
    main()
