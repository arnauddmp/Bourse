from playwright.sync_api import sync_playwright
from supabase import create_client, Client
from datetime import datetime
import os

# ⚡ Config Supabase
SUPABASE_URL = os.environ.get("SUPABASE_URL")      # ton URL Supabase
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")      # ta clé API Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Nom et URL du site à scraper
site_name = "apple"
site_url = "https://www.apple.com"

# Scraping Playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(site_url)
    title = page.title()
    browser.close()

print("Titre récupéré :", title)

# Préparer les données à insérer
data = {
    "site": site_name,
    "title": title,
    "last_update": datetime.now().isoformat()
}

# UPSERT sur Supabase
# La colonne "site" doit être unique dans la table "site_data"
response = supabase.table("site_data").upsert(data, on_conflict="site").execute()

if response.status_code in [200, 201]:
    print("Base Supabase mise à jour.")
else:
    print("Erreur :", response.data)