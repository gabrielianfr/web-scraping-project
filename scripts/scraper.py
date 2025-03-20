import requests
from bs4 import BeautifulSoup
import json
import config
from utils import save_data

# Mendapatkan konten halaman
def fetch_page(url):
    headers = {
        'User-Agent': config.USER_AGENT
    }
    response = requests.get(url, headers=headers)
    return response.text

# Melakukan scraping pada halaman
def scrape_data():
    page_content = fetch_page(config.TARGET_URL)
    soup = BeautifulSoup(page_content, 'html.parser')

    # Contoh scraping: ambil semua elemen h2 dengan class 'title'
    titles = soup.find_all('h2', class_='title')
    data = []

    for title in titles:
        data.append({
            'title': title.get_text(),
            'link': title.find('a')['href']
        })
    
    # Simpan data yang sudah di-scrape
    save_data(data)

# Fungsi utama
if __name__ == "__main__":
    scrape_data()
    print("Scraping selesai.")
