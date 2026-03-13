from playwright.sync_api import sync_playwright
from supabase import create_client, Client
from datetime import datetime
import os

print("imports ok")

# Nom et URL du site à scraper
site_name = "apple"
site_url = "https://www.apple.com"

# Scraping Playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    print("browser défini et lancé")
    page = browser.new_page()
    print("onglet ouvert")
    page.goto(site_url)
    print("allé sur le site")
    title = page.title()
    print("get title")
    browser.close()
    print("browser fermé")

print("Titre récupéré :", title)

# Préparer les données à insérer
data = {
    "site": site_name,
    "title": title,
    "last_update": datetime.now().isoformat()
}

