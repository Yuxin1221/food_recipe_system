from recipe_scrapers import scrape_me
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

DRIVER_PATH = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(executable_path = DRIVER_PATH)
url = 'https://www.foodnetwork.com/recipes/recipes-a-z/'

IndexSuffixList = ['123','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','xyz']

links = []
count = 0



for idx in IndexSuffixList:
    driver.get(url+idx)
    for i in range(1,1000):
        try:
            driver.get(url+idx+"/p/{0}".format(i))
            count+=1
            recipes = driver.find_elements(By.CLASS_NAME, 'm-PromoList__a-ListItem')
            for r in recipes:
                x = r.find_element_by_tag_name('a')
                y = x.get_attribute("href")
                links.append(y)
                with open("/631_Linkedin_Project/links.json",
                          "a") as outfile:
                    outfile.write(y+'\n')
            recipes[0].click()
        except:
            break


print(len(links))









# scraper = scrape_me('https://www.foodnetwork.com/recipes/1-2-3-lasagna-3644969',wild_mode=True)
#
# # Q: What if the recipe site I want to extract information from is not listed below?
# # A: You can give it a try with the wild_mode option! If there is Schema/Recipe available it will work just fine.
#
# print(scraper.title(),
# scraper.total_time(),
# scraper.yields(),
# scraper.ingredients(),
# scraper.instructions(),
# scraper.image(),
# scraper.host(),
# scraper.links(),
# scraper.nutrients())

