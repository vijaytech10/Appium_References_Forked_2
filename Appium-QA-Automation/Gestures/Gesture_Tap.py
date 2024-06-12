from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
import time
## Defining Desired Capablities
desired_cap = {
  "deviceName": "Android Emulator",
  "platformName": "Android",
  "appPackage": "com.code2lead.kwad",
  "appActivity": "com.code2lead.kwad.MainActivity",
  "app": "C:\\Users\\BS726\\Desktop\\AppiumQA-Automation\\Demo APK\\Android_Demo_App.apk",
  "appWaitDuration": "20000"
}

## Invoking Appium
options = UiAutomator2Options().load_capabilities(desired_cap)
driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)

# Scroll to the "LOGIN" button
scrollable = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("LOGIN"))')

# Ensure that the "LOGIN" button is within the view
login_button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'text("LOGIN")')

# Get the location of the "LOGIN" button
location = login_button.location

# Calculate the tap coordinates based on the location of the "LOGIN" button
tap_x = location['x'] + login_button.size['width'] // 2
tap_y = location['y'] + login_button.size['height'] // 2

# Perform a tap using TouchAction
action = TouchAction(driver)
action.tap(None, tap_x, tap_y).perform()

# Add a sleep for demonstration purposes
time.sleep(30)

# Quit the Driver
driver.quit()