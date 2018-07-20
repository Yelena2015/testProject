# coding=utf8

from appium import webdriver
import time,traceback



desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'test'
# desired_caps['app'] = r'e:\apk\toutiao.apk'
desired_caps['appPackage'] = 'io.manong.developerdaily'
desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.LaunchActivity'
desired_caps['unicodeKeyboard']  = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(2)

try:
    # -----------------

    driver.open_notifications()
    #
    # time.sleep(1)
    # eles = driver.find_elements_by_xpath('//com.android.systemui.statusbar.phone.TimeAxisWidgetEx//android.widget.TextView')
    #
    # for ele in eles:
    #     print ele.text


    time.sleep(2)
    driver.press_keycode(5)


    # -----------------

except:
    print traceback.format_exc()


raw_input('**** Press to quit..')
driver.quit()