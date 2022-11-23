from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())



# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# chromeDriverPath = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
# userdatadir = 'C:/Users/Weera/AppData/Local/Google/Chrome/User Data'
# chromeOptions = webdriver.ChromeOptions() 
# chromeOptions.add_argument(f"--user-data-dir={userdatadir}") #Path to your chrome profile
# driver = webdriver.Chrome(chromeDriverPath, options=chromeOptions) 





try:
    driver.get("https://www.forexfactory.com/calendar?day=nov23.2022")
    # Get the table
    table = driver.find_element(By.CLASS_NAME, "calendar__table")
    # Iterate over each table row
    for row in table.find_elements(By.TAG_NAME, "tr"):
        # list comprehension to get each cell's data and filter out empty cells
        row_data = list(filter(None,[td.text for td in row.find_elements(By.TAG_NAME, "td")]))
        data = list(filter(None,[td.get_attribute("class") for td in row.find_elements(By.TAG_NAME, "td")]))


        def fun(variable):
            letters = [
            'calendar__cell calendar__impact impact calendar__impact calendar__impact--holiday',
            'calendar__cell calendar__impact impact calendar__impact calendar__impact--low',
            'calendar__cell calendar__impact impact calendar__impact calendar__impact--medium',
            'calendar__cell calendar__impact impact calendar__impact calendar__impact--high'
            ]
            if (variable in letters):
                return True
            else:
                return False
        filtered = filter(fun, data)
        for s in filtered:
            if(s =='calendar__cell calendar__impact impact calendar__impact calendar__impact--holiday'):{ print("\033[37m {}\033[00m" .format('holiday'))}
            if(s =='calendar__cell calendar__impact impact calendar__impact calendar__impact--low'):{ print("\033[93m {}\033[00m" .format('low'))}
            if(s =='calendar__cell calendar__impact impact calendar__impact calendar__impact--medium'):{ print("\033[33m {}\033[00m" .format('medium'))}
            if(s =='calendar__cell calendar__impact impact calendar__impact calendar__impact--high'):{print("\033[91m {}\033[00m" .format('high'))}

        if row_data == []:
            continue
        if data == []:
            continue
        print(row_data)

except Exception as e:
    print(e)
finally:
    driver.quit()