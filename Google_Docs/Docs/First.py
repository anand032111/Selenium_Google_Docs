from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://docs.google.com")
driver.get_screenshot_as_file("/Users/priyamvadaanand/PycharmProjects/Selenium/image/img1.png")
driver.quit()
