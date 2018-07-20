# coding=utf8

from appium import webdriver
import time,traceback



desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'test'
desired_caps['app'] = r'e:\apk\toutiao.apk'
desired_caps['appPackage'] = 'io.manong.developerdaily'
desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.LaunchActivity'
desired_caps['unicodeKeyboard']  = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
print driver.session_id
driver.implicitly_wait(10)

try:
    # -----------------

    driver.find_element_by_class_name("android.widget.ImageButton")

    time.sleep(1)

    xpath="//*[@resource-id='io.manong.developerdaily:id/tab_bar']/android.widget.LinearLayout[1]/android.widget.RelativeLayout[4]/android.widget.LinearLayout[1]/android.widget.TextView[1]"

    ele = driver.find_element_by_xpath(xpath)

    print ele.text

    ele.click()




    # -----------------

except:
    print traceback.format_exc()


raw_input('**** Press to quit..')
driver.quit()