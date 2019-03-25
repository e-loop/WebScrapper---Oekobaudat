#!usr/bin/python
'''
@Creater = Anish Koyamparambath
@Company =  WeLOOP
@Title = WebScraping Oekobaudat EPD
@Objective = Automatic download of all the xml files(EPD Data) by using selenium in python with chrome headless browser
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# URL variable - For fetching the url and use it for automation.
URL = 'https://www.oekobaudat.de/datenbank/browser-oekobaudat.html'

# Options introduce the properties of the Pseudo chrome
options = webdriver.ChromeOptions()
options.add_argument('--safebrowsing-disable-download-protection')
options.add_argument('--safebrowsing-disable-extension-blacklist')
options.add_argument('--no-sandbox')
options.add_argument('--allow-unchecked-dangerous-downloads')
preferences = {'safebrowsing.enabled': 'false'}
options.add_experimental_option("prefs", preferences)

# Uncomment the below line if you want to use the chrome headless. DO NOT UNCOMMENT IF YOU WANT TO DOWNLOAD ANY FILE.
# options.add_argument('--headless')


# PTCD - Path to Chrome Driver in the User System
PTCD = 'Support/chromedriver.exe'

# Call the Chrome browser using Selenium WebDriver in a variable driver
driver = webdriver.Chrome(executable_path=PTCD, options=options)
result = driver.get(URL)

# tryclick is a variable which is used to check and stop iterative function in the below loop
tryclick = 10

# Close the pop up dialogue
try:
    click = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div[2]/a[1]')))
    click.click()
except:
    print('Pop up not available')


# Iterative loop starts here with the index value you should set
index = 1
while index:
    try:
        index = str(index)
        click1 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="c613"]/div/ul/li[' +index +']/a' )))
        driver.switch_to_active_element()
        driver.execute_script("arguments[0].scrollIntoView(true);", click1)
    except:
        tryclick = 0
    if tryclick != 0:
        click1.click()
        URL2 = driver.current_url
        index2 = 1
        while index2:
            try:
                index2 = str(index2)
                click2 = driver.find_element_by_xpath('//*[@id="c613"]/div/ul/li[' + index2 + ']/a')
                driver.execute_script("arguments[0].scrollIntoView(true);", click2)
            except:
                tryclick = 0
            if tryclick != 0:
                click2.click()
                URL3 = driver.current_url
                print(URL2)
                index3 = 1
                while index3:
                    try:
                        index3 = str(index3)
                        click3 = driver.find_element_by_xpath('//*[@id="c613"]/div/ul/li[' + index3 + ']/a')
                        driver.execute_script("arguments[0].scrollIntoView(true);", click3)
                    except:
                        tryclick = 0
                    if tryclick != 0:
                        click3.click()
                        print(URL3)
                        index4 = 1
                        while index4:
                            try:
                                index4 = str(index4)
                                click4 = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="c613"]/div/ul/li[' +index4 + ']/span/a[2]')))
                            except:
                                print('not working' +index4)
                                tryclick = 0
                            if tryclick != 0:
                                driver.execute_script("arguments[0].scrollIntoView(true);", click4)
                                click4.click()
                                index4 = int(index4)
                                index4 = index4 + 1
                            else:
                                index4 = False
                                index3 = int(index3)
                                index3 = index3 + 1
                                driver.get(URL3)
                                tryclick = 10
                    else:
                        index3 = False
                        index2 = int(index2)
                        index2 = index2+1
                        driver.get(URL2)
                        tryclick = 10

            else:
                index2 = False
                index = int(index)
                index = index + 1
                driver.get(URL)
                tryclick = 10
    break
Reply = input('Please enter if you want to exit or no:' )
if Reply == 'yes':
    driver.quit()
else:
    pass
