# This is a basic website scraper
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

website = "https://www.thesun.co.uk/sport/football/"
path = "C:/Users/AH0514/OneDrive - Mubea/Desktop/chromedriver-win64/chromedriver.exe"

#headless mode ie without opening a browser window
options = Options()
options.add_argument("--headless=new")

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

containers = driver.find_elements("xpath", '//div[@class="teaser__copy-container"]')
Titles = []
Subitles = []
Links = []

for container in containers:
    try:
        Title = container.find_element(By.XPATH, './/span').text
    except:
        Title = None
    try:
        Subitle = container.find_element(By.XPATH, './/h3').text
    except:
        Subitle = None
    try:
        Link = container.find_element(By.XPATH, './/a').get_attribute("href")
    except:
        Link = None
    Titles.append(Title)
    Subitles.append(Subitle)
    Links.append(Link)
    
my_dict = {
    "Title": Titles,
    "Subitle": Subitles,
    "Link": Links
}
    
df_headline = pd.DataFrame(my_dict)
df_headline.to_csv("headlines-headless.csv")
driver.quit()