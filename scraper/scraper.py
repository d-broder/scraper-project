import csv
import json
from datetime import datetime, timezone

import requests

# URL of the API endpoint
API_URL = "https://api.netze-bw.de/rediservice/v1/measures"

# Required headers (replace subscription key with your actual key or load from env)
HEADERS = {
    "accept": "application/json, text/plain, */*",
    "ocp-apim-subscription-key": "902271fcdc0c44a4bf006d67cf00b763",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 " "(KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
}

OUTPUT_COLUMNS = [
    "scrape_datetime",
    "Startinterval",
    "Endinterval",
    "Stufe",
    "Anlagen",
]


def fetch_measures():
    """
    Perform a GET request to the API and return the parsed JSON list.
    Raises an HTTPError on bad responses.
    """
    response = requests.get(API_URL, headers=HEADERS)
    response.raise_for_status()
    return response.json()


def transform(measures):
    """
    Convert raw measure dicts into a list of flat dicts ready for CSV writing.
    - scrape_datetime: current UTC time in ISO 8601 without microseconds
    - Startinterval: measure['start'] in "DD.MM.YYYY, HH:mm Uhr" format
    - Endinterval: measure.get('end') in "DD.MM.YYYY, HH:mm Uhr" format or blank
    - Stufe: measure['level']
    - Anlagen: measure['deviceId']
    """
    # Format scrape_datetime to match the expected format
    now_iso = datetime.now(timezone.utc).replace(microsecond=0).strftime("%Y-%m-%dT%H:%M:%SZ")
    rows = []

    def format_timestamp(ts):
        if not ts:
            return ""
        dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
        return dt.strftime("%d.%m.%Y, %H:%M Uhr")

    for m in measures:
        rows.append(
            {
                "scrape_datetime": now_iso,
                "Startinterval": format_timestamp(m.get("start", "")),
                "Endinterval": format_timestamp(m.get("end", "")),
                "Stufe": m.get("level", ""),
                "Anlagen": m.get("deviceId", ""),
            }
        )
    return rows


def run(output_filepath):
    """
    Entry point for the scraper.
    1. Fetch data from API
    2. Transform it into tabular rows
    3. Write a CSV file to `output_filepath`
    """
    measures = fetch_measures()
    rows = transform(measures)

    with open(output_filepath, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=OUTPUT_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Scrape complete. {len(rows)} records written to {output_filepath}")
