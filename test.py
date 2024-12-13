import os
import json
from playwright.sync_api import sync_playwright

# Paths to store cookies and browser context
COOKIE_PATH = "cookies.json"


def load_cookies(context, path=COOKIE_PATH):
    """Load cookies into the browser context."""
    if os.path.exists(path):
        with open(path, "r") as cookie_file:
            cookies = json.load(cookie_file)
            context.add_cookies(cookies)


def login_and_scrape(url):
    with sync_playwright() as p:
        # Launch browser in headless mode (you can set headless=False for debugging)
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        # Load cookies if they exist
        load_cookies(context)

        # Open the LeetCode login page
        page = context.new_page()
        page.goto(url)
        page.wait_for_timeout(999999999)

        # Close the browser
        browser.close()


if __name__ == "__main__":
    login_and_scrape("https://leetcode.com/studyplan/top-sql-50/")
