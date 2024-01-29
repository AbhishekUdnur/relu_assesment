from selenium import webdriver
import time
from selenium.common.exceptions import StaleElementReferenceException

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.allrecipes.com/recipes/233/world-cuisine/asian/indian/")
receipes = driver.find_elements_by_class_name("card__detailsContainer")
for rec in receipes:
    name = rec.find_element_by_tag_name("h3").get_attribute("innerText")
    print(name)
loadmore = driver.find_element_by_id("category-page-list-related-load-more-button")
j = 0
try:
    while loadmore.is_displayed():
        loadmore.click()
        time.sleep(5)
        lrec = driver.find_elements_by_class_name("recipeCard__detailsContainer")
        newlist = lrec[j:]
        for rec in newlist:
            name = rec.find_element_by_tag_name("h3").get_attribute("innerText")
            print(name)
        j = len(lrec)+1
        time.sleep(5)
except StaleElementReferenceException:
    pass
driver.quit()