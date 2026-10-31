def check_eligibility(candidate, job):
    reasons = []

    if float(candidate["percentage"]) < float(job["minimum_percentage"]):
        reasons.append("Percentage below minimum requirement")

    if int(candidate["backlogs"]) > int(job["maximum_backlogs"]):
        reasons.append("Too many backlogs")

    required = {
        s.strip().lower()
        for s in (job.get("required_skills") or "").replace(",", " ").split()
    }

    available = {
        s.strip().lower()
        for s in (candidate.get("skills") or "").replace(",", " ").split()
    }

    missing = required - available

    if missing:
        reasons.append(
            "Missing skills: " + ", ".join(sorted(missing))
        )

    return not reasons, reasons