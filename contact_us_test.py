from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from locators import locator
from csv import reader
import random
from selenium.webdriver.support.ui import Select
import os


#! create a chrom driver obj
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)
driver.get("http://automationpractice.com/")
driver.maximize_window()

with open('contact_us_TestData.csv') as csvfile:
    csvreader = reader(csvfile, delimiter=';')
    for row in csvreader:
        # ?1- Click Contact-us
        assert driver.find_element(*locator["contact_us"]).is_displayed()
        driver.find_element(*locator["contact_us"]).click()

        assert driver.title == "Contact us - My Store"

        # ?2- pick subject heading
        select = Select(driver.find_element(*locator['subject_heading']))
        select.select_by_value(row[0])

        # ?3- fill-in Email Address
        driver.find_element(
            *locator["email"]).send_keys(str(random.randint(0, 1000000)) + row[1])

        # ?4- fill-in Order refrence
        driver.find_element(
            *locator["order_refrence"]).send_keys(str(random.randint(0, 1000000)) + row[2])

        # ?5- Attach a File
        driver.find_element(
            *locator["attach_file_button"]).send_keys(os.getcwd() + "/image.png")

        # ?6- Fill-in the Message
        driver.find_element(*locator["message"]).send_keys(row[3])

        # ?7- Submit The Message
        driver.find_element(*locator["submit_message_btn"]).click()

# driver.quit()
