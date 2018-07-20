# coding=utf8
from appium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import traceback
 
desired_caps = {}
desired_caps['platformName'] = 'Android'  #测试平台
desired_caps['platformVersion'] = '6.0'   #平台版本,不能写错
desired_caps['deviceName'] = 'test'    #设备名称，多设备时需区分
# desired_caps['app'] = 'e:\\toutiao.apk'  #app package名
desired_caps['appPackage'] = 'io.manong.developerdaily'  #app package名
desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.LaunchActivity' #app默认Activity
desired_caps['unicodeKeyboard']  = True  # 一定要有该参数，否则unicode 输入的中文无效
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #启动Remote RPC

try:
    print 1
    driver.implicitly_wait(10)


    driver.find_element_by_id("io.manong.developerdaily:id/tab_bar_plus").click()
    print driver.page_source

    time.sleep(1)
    driver.find_element_by_id("io.manong.developerdaily:id/btn_email").click()
    time.sleep(1)


    ele = driver.find_element_by_id("io.manong.developerdaily:id/edt_email")
    print ele

    ele.send_keys('jcyrss@163.com')
    ele = driver.find_element_by_id("io.manong.developerdaily:id/edt_password")
    ele.send_keys('sdfsdf')

    time.sleep(2)
    driver.find_element_by_id('io.manong.developerdaily:id/btn_login').click()

    # eles = driver.find_elements_by_xpath("//android.widget.TextView")
    # for ele in eles:
    #     print ele.get_attribute('text')

except:
    print traceback.format_exc()


raw_input('**** Press to quit..')
driver.quit()


# if __name__ == '__main__':
#     print 1
#     pass