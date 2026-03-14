from playwright.sync_api import sync_playwright
from supabase import create_client, Client
from datetime import datetime
import os



print("imports ok")

# Nom et URL du site à scraper
site_name = "Stellantis"
site_url = "https://www.google.com/finance/quote/STLAP:EPA?sa=X&ved=2ahUKEwjQyNH56p6TAxU7UaQEHTLqDhIQ3ecFKAN6BAgvEAQ"

# Scraping Playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    print("browser défini et lancé")
    page = browser.new_page()
    print("onglet ouvert")
    page.goto(site_url)
    print("allé sur le site")
    print(page.locator("div.YMlKec fxKbKc").count())
    text = page.locator("YMlKec fxKbKc").text_content()
    #valeur = page.locator("div.YMlKec fxKbKc").text_content()
    print(text)
    browser.close()
    print("browser fermé")


# Préparer les données à insérer
data = {
    "site": site_name,
    "last_update": datetime.now().isoformat()
}

