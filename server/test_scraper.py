from scraper import fetch_job_listings

def test_scraper():
    jobs = fetch_job_listings()

    print(f"Found {len(jobs)} jobs:")
    for job in jobs:
        print(job)

if __name__ == "__main__":
    test_scraper()
