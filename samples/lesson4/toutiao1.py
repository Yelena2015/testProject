# coding=utf8

from appium import webdriver
import time,traceback



desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'test'
desired_caps['app'] = r'e:\apk\toutiao.apk'
desired_caps['appPackage'] = 'io.manong.developerdaily'
desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.LaunchActivity'
desired_caps['unicodeKeyboard']  = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)

try:
    # -----------------
    # xpath = u'//android.widget.TextView[@text="我的"]'
    # ele = driver.find_element_by_xpath(xpath)
    code = 'new UiSelector().resourceId("io.manong.developerdaily:id/tab_bar").childSelector(new UiSelector().className("android.widget.TextView").instance(3))'
    ele = driver.find_element_by_android_uiautomator(code)

    ele.click()

    time.sleep(1)

    code = u'new UiSelector().textMatches("^我的.*")'
    eles = driver.find_elements_by_android_uiautomator(code)
    for ele in eles:
        print ele.text



    # -----------------

except:
    print traceback.format_exc()


raw_input('**** Press to quit..')
driver.quit()