import requests
from bs4 import BeautifulSoup
from config import GITHUB_REPO_URL, USER_AGENT

def fetch_job_listings():
    headers = {
        "User-Agent": USER_AGENT
    }

    # holds the pages html element
    response = requests.get(GITHUB_REPO_URL, headers=headers)
    response.raise_for_status()

    # parses raw html to a navigational tree structure
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []

    # finds all table rows skipping the header
    rows  = soup.find_all("tr")[1:]

    for row in rows:
        # retrieves table data
        cells = row.find_all("td")
    
        # skip rows that don't have 4 headers
        if len(cells) < 4:
            continue

        # extracts company name and role
        company = cells[0].get_text(strip=True)
        role = cells[1].get_text(strip=True)

        # extracts application link
        apply_link_tag = cells[3].find('a')

        # grabs the href if it exists
        if apply_link_tag:
            application_link = apply_link_tag['href']
        else:
            application_link = None

        job = {
            "company": company,
            "role": role,
            "link": application_link
        }

        jobs.append(job)
    
    return jobs

        




