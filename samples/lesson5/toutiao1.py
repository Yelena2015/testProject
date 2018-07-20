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

    code = 'new UiSelector().resourceId("io.manong.developerdaily:id/tab_bar").childSelector(new UiSelector().className("android.widget.TextView").instance(3))'
    ele = driver.find_element_by_android_uiautomator(code)

    ele.click()

    time.sleep(2)

    driver.start_activity('com.huawei.appmarket',
                          'com.huawei.appmarket.MainActivity',
                          )

    ele = driver.find_element_by_id('com.huawei.appmarket:id/banner')



    time.sleep(2)
    # -----------------

except:
    print traceback.format_exc()


raw_input('**** Press to quit..')
driver.quit()