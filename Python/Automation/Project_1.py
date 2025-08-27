# This is a basic website scraper
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

website = "https://www.thesun.co.uk/sport/football/"
path = "C:/Users/AH0514/OneDrive - Mubea/Desktop/chromedriver-win64/chromedriver.exe"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')
Titles = []
Subitles = []
Links = []

for container in containers:
    Title = container.find_element(by="xpath", value='//div[@class="teaser__copy-container"]/a/span').text
    Subitle = container.find_element(by="xpath", value='//div[@class="teaser__copy-container"]/a/h3').text
    Link = container.find_element(by="xpath", value='//div[@class="teaser__copy-container"]/a').get_attribute("href")
    Titles.append(Title)
    Subitles.append(Subitle)
    Links.append(Link)
    
my_dict = {
    "Title": Titles,
    "Subitle": Subitles,
    "Link": Links
}
    
df_headline = pd.DataFrame(my_dict)
df_headline.to_csv("headlines.csv", index=False)
driver.quit()
    