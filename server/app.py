import time
from scraper import fetch_job_listings
from database import load_seen_jobs, save_seen_jobs
from notifier import send_notification
from config import SCRAPE_INTERVAL

def main():
    while True:
        print("Checking for new jobs...")

        new_jobs = fetch_job_listings()
        old_jobs = load_seen_jobs()

        # Create set of identifiers based on company + role
        seen_keys = set(f"{job['company']} - {job['role']}" for job in old_jobs)

        for job in new_jobs:
            key = f"{job['company']} - {job['role']}"
            if key not in seen_keys:
                #send_notification(f"New job posted: {key}")
                print(f"Saving new job: {key}")
                save_seen_jobs(job)
        time.sleep(SCRAPE_INTERVAL)

if __name__ == "__main__":
    main()
