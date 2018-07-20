# coding=utf8
from appium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import traceback
 
desired_caps = {}
desired_caps['platformName'] = 'Android'  #测试平台
desired_caps['platformVersion'] = '5.1'   #平台版本,不能写错
desired_caps['deviceName'] = 'test'    #设备名称，多设备时需区分
desired_caps['app'] = r'e:\apk\wv.apk'  #app package名
desired_caps['appPackage'] = 'com.example.jcy.wvtest'  #app package名
desired_caps['appActivity'] = '.MainActivity' #app默认Activity
desired_caps['unicodeKeyboard']  = True  # 一定要有该参数，否则unicode
desired_caps['resetKeyboard']  = True  # 一定要有该参数，否则unicode 输入的中文无效
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #启动Remote RPC

driver.implicitly_wait(10)
try:
    # -----------------------
    time.sleep(3)
    print driver.contexts
    print driver.current_context

    driver.switch_to.context(u'WEBVIEW_com.example.jcy.wvtest')
    driver.find_element_by_css_selector('#index-kw').send_keys(u'松勤')
    driver.find_element_by_id('index-bn').click()

    driver.switch_to.context(u'NATIVE_APP')


    # -----------------------

except:
    print traceback.format_exc()


raw_input('**** Press to quit..')
driver.quit()