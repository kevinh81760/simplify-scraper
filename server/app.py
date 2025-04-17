from scraper import fetch_job_listings
from database import load_seen_jobs, save_seen_jobs
from notifier import send_notification
from config import SCRAPE_INTERVAL
import time

def main():
    while True:
        print("Checking for new jobs")
        # fetches old and new jobs
        new_jobs = fetch_job_listings()
        old_jobs = load_seen_jobs()

        # checks if there are any new jobs 
        for job in new_jobs:
            if job not in old_jobs:
                # sends an sms message if there is 
                send_notification(f"New job posted: {job['title']}")

                # adds new jobs to seen jobs
                save_seen_jobs(job)

        # sleeps for 10 mins
        time.sleep(SCRAPE_INTERVAL)

if __name__ == "__main__":
    main()

        

            
