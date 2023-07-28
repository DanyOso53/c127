from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time 
import pandas as pd 

scrap_url="https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser= webdriver.Chrome()
browser.get(scrap_url)
planets_data = []

def scrap ():
    for i in range(0,10):
        print(f"Extrayendo página{i+1}...")
        soap = BeautifulSoup(browser.page_source,"html.parser")
        for ultag in soap.find_all("ul",attrs={"class","exoplanet"}):
            li_tags= ultag.find_all("li")
            temporal= []
            for index,etiquetali in enumerate(li_tags):
                if index == 0 :
                    temporal.append(etiquetali.find_all("a")[0].contents[0])
                else: 
                    try: temporal.append(etiquetali.contents[0])
                    except: temporal.append("")
            planets_data.append(temporal)
        browser.find_element( by=By.XPATH ,value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()



scrap ()


headers =  ["name","light_years_from_earth","planet_mass","stellar magnitude","discovery_date"]
planets_data_frame = pd.DataFrame(planets_data,columns=headers)
planets_data_frame.to_csv("scrapdata.csv",index = True, index_label="id")