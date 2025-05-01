import time
from scraper import fetch_job_listings
from database import load_seen_jobs, save_seen_jobs
from notifier import send_notification
from config import SCRAPE_INTERVAL
from flask import Flask, jsonify, request
from recipients.recipients_util import save_phone_number
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# API route to receive a phone number from the frontend and save it
@app.route("/api/phone", methods=["POST"])
def add_phone_number():
    data = request.get_json()
    number = data.get("number")

    if not number:
        return jsonify({"error": "Phone number is required"}), 400
    
    save_phone_number(number)
    return jsonify({"message": "Phone number saved successfully"}), 200

# Main scraping loop: runs forever, checking for new jobs periodically
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
