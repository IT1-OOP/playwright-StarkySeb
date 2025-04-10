import os
import urllib.parse
from playwright.sync_api import sync_playwright, expect

def test_page_title():

    cesta = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src/index.html"))
    cesta = urllib.parse.unquote(cesta) 

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  
        page = browser.new_page()
        page.goto(f"file://{cesta}")
        page.wait_for_load_state("load")  
        nadpis = page.locator("h1").first
        expect(nadpis).to_be_visible()

        browser.close()