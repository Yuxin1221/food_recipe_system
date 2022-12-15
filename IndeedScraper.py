import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import json
import random
import sys
#specify driver path
DRIVER_PATH = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(executable_path = DRIVER_PATH)
driver2 = webdriver.Chrome(executable_path = DRIVER_PATH)

driver.get('https://indeed.com')
#search software engineer'
driver.implicitly_wait(random.randrange(10,13)*random.random())
search_job = driver.find_element(By.XPATH,'//*[@id="text-input-what"]')
search_job.send_keys(['software engineer'])

# #set display limit of 30 results per page
# display_limit = driver.find_element(By.XPATH,'//select[@id="limit"]//option[@value="30"]')
# display_limit.click()

#search for all location
driver.implicitly_wait(random.randrange(5)*random.random())
job_location = driver.find_element(By.XPATH,'//*[@id="text-input-where"]')
job_location.send_keys(Keys.COMMAND + "a")
job_location.send_keys(Keys.DELETE)
driver.implicitly_wait(random.randrange(10)*random.random())
job_location.send_keys(['United States'])
#

driver.implicitly_wait(random.randrange(10,20)*random.random())
#start search
search_button = driver.find_element(By.XPATH,'//*[@id="jobsearch"]/button')
search_button.click()

try:
    close_popup = driver.find_element(By.XPATH,'//*[@id="popover-x"]/button')
    close_popup.click()
except:
    close_popup = "None"


# let the driver wait 3 seconds to locate the element before exiting out

driver.implicitly_wait(random.randrange(10,20)*random.random())
for page in range(2000):
    try:
        close_popup = driver.find_element(By.XPATH, '//*[@id="popover-x"]/button')
        close_popup.click()
    except:
        close_popup = "None"

    jobIds = []
    titles = []
    companies = []
    locations = []
    links = []
    ratings = []
    salaries = []
    descriptions = []
    applyLinks = []
    jobTypes = []

    jobs = driver.find_elements(By.CLASS_NAME,'sponTapItem')


    for job in jobs:
        driver.implicitly_wait(random.randrange(10) * random.random())
        try:
            title = job.find_element(By.CLASS_NAME, 'jobTitle').text
        except:
            title = "None"
        titles.append(title)

        try:
            location = job.find_element(By.CLASS_NAME, 'companyLocation').text
        except:
            location = "None"
        locations.append(location)

        try:
            rating = job.find_element(By.CLASS_NAME, 'ratingLink').text
        except:
            rating = "None"
        ratings.append(rating)

        try:
            company = job.find_element(By.CLASS_NAME,'companyName').text
        except:
            company = "None"
        companies.append(company)
        links.append(job.get_attribute(name='href'))


    try:
        next_page = driver.find_element(By.XPATH, '//*[@id="resultsCol"]/nav/div/ul/li[7]/a')
    except:
        next_page = driver.find_element(By.XPATH, '//*[@id="resultsCol"]/nav/div/ul/li[6]/a')
    next_page.click()
    print("Page: {0}".format(page + 1))



    for link in links:
        driver2.implicitly_wait(random.randrange(10,25)*random.random())
        driver2.get(link)
        try:
            jd = driver2.find_element(By.CLASS_NAME,'jobsearch-jobDescriptionText').text
        except:
            jd = "None"
        descriptions.append(jd)
        try:
            al = driver2.find_element(By.ID,'applyButtonLinkContainer').get_attribute(name='href')
        except:
            al = None
        applyLinks.append(al)
        try:
            jt = driver2.find_element(By.CLASS_NAME,'jobsearch-JobMetadataHeader-item').text
        except:
            jt = "None"
        jobTypes.append(jt)





    for i in range(len(links)):
        title = titles[i].replace('/','_')
        company = companies[i].replace('/','_')
        JobData = {

                "Job_Title:": title,
                "Company_Name:": company,
                "Location":locations[i],
                "Employment_Type": jobTypes[i],
                "Job_Description":descriptions[i],
                "Job_Link":links[i],
                "Apply_Link":applyLinks[i],
            }
        json_object = json.dumps(JobData, indent=4)


        # Writing to sample.json
        with open("/Users/cchen/Desktop/university/computerScience/631/ScrapedData/{0}_{1}.json".format(title,company), "w") as outfile:
            outfile.write(json_object)



    driver.implicitly_wait(random.randrange(10,30)*random.random())

    if page == 25:
        driver.implicitly_wait(random.randrange(100))


