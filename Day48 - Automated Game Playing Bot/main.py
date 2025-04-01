from selenium import webdriver
from selenium.webdriver.common.by import By

#Keep Chrome browser open after program finishes (if not, it automatically closes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)  #We create a driver from the Chrome object
driver.get("https://appbrewery.github.io/instant_pot/") #This will open the webpage

#We want to find a certain element in a webpage, in this case, the price:
price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
#This gets them but ads an HTML element! we need to convert them to vlues we can use,
#aka get the Text content
print(f"Price is: ${price_dollar.text}.{price_cents.text}")

search_bar = driver.find_element(By.NAME, value="field-keywords")
print(search_bar)
#This gets you a selenium element like this:
#<selenium.webdriver.remote.webelement.WebElement (session="e4d222971086d676e97f658343271e60", element="f.2D340315E23FE60E3713AF3C780E4207.d.D37C6CFA855D21E15F3A81C5686FEEB4.e.15")>

#You can search by CSS, NAME, XPATH etc...tis last one being more reliable. Here an ex.:
#//*[@id="udemy"]/div[1]/div[1]/div/div[1]/main/div/div[2]/section/div/div[1]/div[1]/section

#driver.close() #this closes the a single tab, the active one
driver.quit() #this closes the whole browser, all Chrome ex..