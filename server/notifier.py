import json
import os 

# file where we save seen jobs
SEEN_JOBS_FILE = "seen_jobs.json"

def load_seen_jobs():
    if not os.path.exists(SEEN_JOBS_FILE):
        return []

    with open(SEEN_JOBS_FILE, "r") as f:
        try:
            seen_jobs = json.load(f)
        except json.JSONDecodeError:
            seen_jobs = []
    
def save_seen_jobs(job):
    # loads current list of jobs
    seen_jobs = load_seen_jobs()

    # appeands new job to list
    seen_jobs.append(job)

    # save the updated list back to the file 
    with open(SEEN_JOBS_FILE, "w") as file:
        json.dump(seen_jobs, file, indent=2)
