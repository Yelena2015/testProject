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
    code = u'new UiSelector().text("发现").className("android.widget.TextView")'
    driver.find_element_by_android_uiautomator(code).click()
    time.sleep(2)

    driver.implicitly_wait(1)
    while True:
        driver.swipe(400,800,400,300,2000)

        code = u'new UiSelector().text("已经全部加载完毕").className("android.widget.TextView")'
        eles = driver.find_elements_by_android_uiautomator(code)
        if eles:
            break

    driver.implicitly_wait(10)
    # -----------------

except:
    print traceback.format_exc()


raw_input('**** Press to quit..')
driver.quit()