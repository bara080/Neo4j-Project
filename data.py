# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import os

# # Source info
# source = "our_world_in_data"

# # Create directory for source
# os.makedirs(source, exist_ok=True)

# # Scrape
# url = "https://ourworldindata.org/environment"
# response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")

# # Extract dataset links
# data_links = []
# for link in soup.find_all("a", href=True):
#     href = link['href']
#     if href.endswith(".csv") or href.endswith(".xlsx"):
#         data_links.append(href)

# # Save
# df = pd.DataFrame(data_links, columns=["dataset_link"])
# print("  Done with Beautiful Soup")
# df.to_csv(f"{source}/datasets.csv", index=False)


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import os
import time

# Setup
source = "our_world_in_data"
os.makedirs(source, exist_ok=True)

driver_path = "/usr/bin/chromedriver"  # Adjust if different
service = Service(driver_path)
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=options)

# Load dynamic content
driver.get("https://ourworldindata.org/environment")
time.sleep(5)

# Extract links
links = driver.find_elements(By.TAG_NAME, "a")
data_links = [l.get_attribute("href") for l in links if l.get_attribute("href") and (".csv" in l.get_attribute("href") or ".xlsx" in l.get_attribute("href"))]

# Save
df = pd.DataFrame(data_links, columns=["dataset_link"])
df.to_csv(f"{source}/datasets.csv", index=False)
print("  Done with Selenium")

driver.quit()
