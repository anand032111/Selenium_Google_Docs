
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://docs.google.com")
driver.find_element_by_xpath("//input[@id='identifierId']").send_keys("testuser30071")
driver.find_element_by_class_name("VfPpkd-RLmnJb").click()
driver.get_screenshot_as_file("/Users/priyamvadaanand/PycharmProjects/Selenium/screenshots/googledocs/img1.png")
driver.implicitly_wait(2)
driver.find_element_by_xpath("//input[@name='password']").send_keys("Test@3007")
driver.find_element_by_xpath("//div[@id='passwordNext']//div[2]").click()
driver.get_screenshot_as_file("/Users/priyamvadaanand/PycharmProjects/Selenium/screenshots/googledocs/img2.png")
driver.find_element_by_xpath("//body/div/div/div/div/div/div/div/div/header[@id='gb']/div[2]/div//*[local-name()='svg']").click()
driver.find_element_by_xpath("//div[contains(text(),'Docs')]").click()
driver.get_screenshot_as_file("/Users/priyamvadaanand/PycharmProjects/Selenium/screenshots/googledocs/img3.png")
driver.find_element_by_css_selector("body.docs-gm.docs-homescreen-snackbar-enabled.docs-homescreen-material-bar-enabled.docs-homescreen-templates-enabled:nth-child(2) div.docs-homescreen-container.docs-homescreen-docs:nth-child(3) div.docs-homescreen-homescreenmain div.docs-homescreen-fcc-inlinecontainer.docs-homescreen-fcc-inlinecontainer-docked:nth-child(1) div.docs-homescreen-fcc-flex.docs-homescreen-fcc-flex-contracted div.docs-homescreen-fcc-flex-content-wrapper div.docs-homescreen-fcc-content div.docs-hs-tmp-sch.docs-hs-tmp-sch-swe.docs-hs-tmp-templatecontentholder div.docs-hs-tmp-sch-content div.docs-hs-tmp-templatecontentholder-inline div.docs-hs-tmp-sch.docs-hs-tmp-sch-content.docs-hs-tmp-sch-ns.docs-hs-tmp-alwaysvisiblecontentholder div.docs-hs-tmp-widthwrapper div.docs-homescreen-itemholder-content.docs-homescreen-templates-gallery div.docs-homescreen-grid-container.docs-homescreen-grid-container-horizontal.docs-hs-tmp-sc-showcase:nth-child(1) div.docs-homescreen-item-section div.docs-homescreen-templates-templateview.docs-homescreen-templates-templateview-showcase:nth-child(1) div.docs-homescreen-templates-templateview-preview.docs-homescreen-templates-templateview-preview-showcase > img:nth-child(1)").click()
driver.implicitly_wait(10)
driver.title
driver.find_element_by_class_name("kix-page-column").click()
driver.get_screenshot_as_file("/Users/priyamvadaanand/PycharmProjects/Selenium/screenshots/googledocs/img4.png")
driver.quit()
print("anand")