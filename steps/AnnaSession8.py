from behave import step
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@step('I would like to open "{pagename}" page')
def open_page(context, pagename):
    if pagename == 'Provitolizer':
        context.driver.get("https://profitolizer.com/")
    elif pagename == 'Google':
        context.driver.get("https://google.com/")
    elif pagename == 'Provitolizer Login':
        context.driver.get("https://app.profitolizer.com/#/login")
    elif pagename == 'BestBuy':
        context.driver.get("https://bestbuy.com/")
    else:
        assert pagename in context.driver.title, f"Page {pagename} not found"


@step('AV verify page title as "{str_title}"')
def verify_title(context,str_title):
   actual_title = context.driver.title
   print(f"Actual title of the page is {actual_title}")
   assert context.driver.title == str_title, f" Title mismatch {actual_title} != {str_title}"


@step('AV click on "{xpath_of_element}" element')
def click_element(context, xpath_of_element):
   element = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_of_element)))
   element.click()


@step('AV type "{text}" to an element with xpath "{text_xpath}"')
def type_text(context, text, text_xpath):
   context.driver.find_element(By.XPATH, text_xpath).send_keys(text)


@then("I add new project")
def add_new_project(context):
    xpath = {
        'project': "//div[./label[text()='Project Name']]//input",
        'start_date': "//input[@placeholder='Start date']",
        'description': "//div[./label[text()='Project description']]//textarea",
        'dimension': "//span[text()='Period Dimension']",
        'duration': "//span[text()='",
    }
    for row in context.table:
        from steps.steps import type_text
        from steps.steps import click_element
        type_text(context, row[0], xpath['project'])
        type_text(context, row[1], xpath['start_date'])
        type_text(context, row[2], xpath['description'])
        click_element(context, xpath['dimension'])
        sleep(1)
        click_element(context, f"//li/span[text()='{row[3]}']")
        sleep(1)
        click_element(context, f"{xpath['duration']}{row[4]}']")
        sleep(1)
        #//li/span[text()='Month']
        #//span[text()='2 Years']
        #//button[text()=" Save"][not(contains(@class,"me-2"))]
        context.driver.find_element(By.XPATH, '//button[text()=" Save"][not(contains(@class,"me-2"))]').click()