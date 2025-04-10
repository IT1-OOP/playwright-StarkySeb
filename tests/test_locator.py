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
        w3odkaz = page.locator("#w3odkaz")

        expect(nadpis).to_be_visible()
        expect(w3odkaz).to_be_visible()

        expect(page.locator("p")).to_be_visible()
        expect(page.locator(".container")).to_be_visible()
        expect(page.locator("text=text nejaky")).to_be_visible()
        expect(w3odkaz).to_be_visible()

        w3odkaz.click()

        browser.close()