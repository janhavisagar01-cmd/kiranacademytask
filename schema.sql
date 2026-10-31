CREATE DATABASE IF NOT EXISTS recruitment_placement;
USE recruitment_placement;
CREATE TABLE IF NOT EXISTS candidates (
 candidate_id INT AUTO_INCREMENT PRIMARY KEY,
 full_name VARCHAR(100) NOT NULL, email VARCHAR(150) NOT NULL UNIQUE,
 qualification VARCHAR(100) NOT NULL, percentage DECIMAL(5,2) NOT NULL,
 passing_year INT NOT NULL, skills VARCHAR(500) DEFAULT '',
 backlogs INT NOT NULL DEFAULT 0, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS companies (
 company_id INT AUTO_INCREMENT PRIMARY KEY,
 company_name VARCHAR(150) NOT NULL UNIQUE, location VARCHAR(150) DEFAULT ''
);
CREATE TABLE IF NOT EXISTS jobs (
 job_id INT AUTO_INCREMENT PRIMARY KEY, company_id INT NOT NULL,
 job_title VARCHAR(150) NOT NULL, minimum_percentage DECIMAL(5,2) NOT NULL DEFAULT 0,
 maximum_backlogs INT NOT NULL DEFAULT 0, required_skills VARCHAR(500) DEFAULT '',
 status ENUM('Open','Closed') NOT NULL DEFAULT 'Open',
 FOREIGN KEY (company_id) REFERENCES companies(company_id)
);
CREATE TABLE IF NOT EXISTS applications (
 application_id INT AUTO_INCREMENT PRIMARY KEY, candidate_id INT NOT NULL, job_id INT NOT NULL,
 application_status ENUM('Applied','Shortlisted','Rejected','Selected') NOT NULL DEFAULT 'Applied',
 applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, UNIQUE KEY unique_candidate_job (candidate_id,job_id),
 FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id),
 FOREIGN KEY (job_id) REFERENCES jobs(job_id)
);
