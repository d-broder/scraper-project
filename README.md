# Redispatch Data Scraper

This project is a Python-based scraper designed to extract data from the paginated tables available at [Netze BW Redispatch](https://www.netze-bw.de/stromeinspeisung/redispatch). The scraper fetches data via an API and outputs it in a structured CSV format. **Selenium is not used in this project.**

## Features

-   Extracts data from the API endpoint.
-   Handles paginated data.
-   Outputs data in a CSV file with the following columns:
    -   `scrape_datetime`: Timestamp of when the scrape was executed (ISO 8601 format).
    -   `Startinterval`: Start interval of the data (formatted as `DD.MM.YYYY, HH:mm Uhr`).
    -   `Endinterval`: End interval of the data (can be blank).
    -   `Stufe`: Integer value representing the level.
    -   `Anlagen`: String identifier for the device.

## Requirements

-   Python 3.8 or higher.
-   Required Python packages are listed in `requirements.txt`.

## Installation

1. Clone the repository to your local machine.
2. Install the required dependencies by running:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the scraper, use the following command:

```bash
python -m scraper <output_csv_file>
```

Replace `<output_csv_file>` with the desired path and filename for the output CSV file.

### Example

```bash
python -m scraper data/sample.csv
```

This will save the scraped data to `data/sample.csv`.

## Project Structure

-   `scraper/`: Contains the source code for the scraper.
    -   `scraper.py`: Main scraper logic. The `run` function is the entry point for the scraper.
    -   `__main__.py`: Entry point for running the scraper as a module.
-   `data/`: Directory for storing output data.
    -   `sample.csv`: Example output file.
-   `history/`: Directory for manually generated historical files.
-   `requirements.txt`: List of required Python packages.

## Output Format

The scraper outputs a CSV file with the following columns:

| Column Name       | Data Type | Example Value           | Comments                                                   |
| ----------------- | --------- | ----------------------- | ---------------------------------------------------------- |
| `scrape_datetime` | Timestamp | `1997-08-29T06:14:00Z`  | ISO 8601 format timestamp of when the scrape was executed. |
| `Startinterval`   | Timestamp | `27.04.2025, 13:45 Uhr` |                                                            |
| `Endinterval`     | Timestamp | `27.04.2025, 13:45 Uhr` | This value can be blank or `-`.                            |
| `Stufe`           | Integer   | `60`                    |                                                            |
| `Anlagen`         | String    | `C1001`                 |                                                            |
