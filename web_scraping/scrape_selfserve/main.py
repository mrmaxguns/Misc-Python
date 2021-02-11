"""Scrape the AISD grades website"""

SITE = "https://grades.austinisd.org/selfserve/EntryPointSignOnAction.do?parent=false"

from getpass import getpass
import time
import random
import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def main():
    """Scrape and print grades"""
    # Get auth information
    username = input("Username: ").strip()
    password = getpass("Password: ")

    # Setup
    driver = webdriver.Firefox()
    driver.get(SITE)
    _delay()

    # Authenticate
    un_form = driver.find_element_by_id("userLoginId")
    _delay_send_keys(un_form, username)
    pw_form = driver.find_element_by_id("userPassword")
    _delay_send_keys(pw_form, password)
    pw_form.send_keys(Keys.ENTER)
    _delay()

    # Go to tab
    grades_tab = driver.find_element_by_id("tabs-3_TAB")
    grades_tab.click()
    _delay()

    # Get headers
    #header_table = driver.find_element_by_id("tableHeaderTable")

    # Quit the window
    driver.quit()


def _delay():
    """Delay the code to avoid suspicion"""
    time.sleep(random.randint(5, 10))


def _delay_send_keys(element, *keys):
    """Send keys with a delay like a normal person would"""
    for keygroup in keys:
        for key in keygroup:
            element.send_keys(key)
            time.sleep(random.randint(5, 50) / 100)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
