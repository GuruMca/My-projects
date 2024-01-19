from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

opt = Options()
opt.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opt)
url = "https://www.flightradar24.com/data/airports/pnq"
driver.get(url)
driver.maximize_window()
states = ["Bengaluru", "Delhi", "Goa", "Chandigarh", "Hyderabad", "Nagpur", "Dubai"]
driver.find_element(By.LINK_TEXT, "Arrivals").click()
rows = driver.find_elements(By.CSS_SELECTOR, '[data-date="Friday, Jan 19"]')
for row in rows:
    for state in states:
        capturedText = row.find_element(By.XPATH, "//td[3]/div/span")
        if state == capturedText.text:
            print(capturedText, row.find_element(By.XPATH, "//td[7]").text)

