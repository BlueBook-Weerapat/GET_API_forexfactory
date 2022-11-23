from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("https://finviz.com/forex_performance.ashx")
    table = driver.find_element(By.CLASS_NAME, "table-light")
    for row in table.find_elements(By.TAG_NAME, "tr"):
        row_data = list(filter(None, [td.text for td in row.find_elements(By.TAG_NAME, "td")]))
        if row_data == []:
            continue
        print(row_data)
except Exception as e:
    print(e)
finally:
    driver.quit()