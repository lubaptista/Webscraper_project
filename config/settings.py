SETTINGS = {
    "BASE_URL": "https://webscraper.io/test-sites/tables",
    "USER_AGENTS": [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    ],
    "HEADERS": {
        "Accept-Language": "en-US,en;q=0.9"
    },
    "REQUEST_TIMEOUT": 10,
    "RETRY_COUNT": 3,
    "RETRY_DELAY": 2,
    "DOWNLOAD_DELAY": 1,
    "CSS_SELECTORS": {
        "TABLE": "table",
        "ROWS": "tbody tr",
        "COLUMNS": "td",
    },
}
