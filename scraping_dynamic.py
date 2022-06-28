import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Install Webdriver (We can also address chrome driver file directory but this way is quicker, personally)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# The link that will be scraped
driver.get('https://www.tokopedia.com/p/komputer-laptop/media-penyimpanan-data')

# Add JavaScript Executor to scroll all items on the page
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

# Locating the web page elements using CSS selector of the info I want to scrape (name and price of the product)
product_name = driver.find_elements(By.CSS_SELECTOR, value='span.css-1bjwylw')
product_price = driver.find_elements(By.CSS_SELECTOR, value='span.css-o5uqvq')

# Make empty lists of name and price product
list_product = []
list_price = []

# Loop to scrape all the informations of all items on the page
for i in range(len(product_name)):
    list_product.append(product_name[i].text)

for j in range(len(product_price)):
   list_price.append(product_price[j].text)

# This is not necessary but I think it's better to close the unnecessary webpage once it's done
driver.quit()

# Put the products names and prices to a DataFrame
df = pd.DataFrame(columns=['product', 'price'])
df['product'] = pd.DataFrame(list_product)
df['price'] = list_price
print(df)

## Make a csv out of the dataframe

# Save the csv
df.to_csv('C:/Users/hp/Documents/Data Science/Personal Project/Scraping/scraping_dynamic/scrape.csv', sep='\t')