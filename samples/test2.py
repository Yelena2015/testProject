# coding=utf8
from appium import webdriver
import time
 
desired_caps = {}
desired_caps['platformName'] = 'Android'  #测试平台
desired_caps['platformVersion'] = '6.0'   #平台版本,不能写错
desired_caps['deviceName'] = 'm3_note'    #设备名称，多设备时需区分
desired_caps['app'] = 'e:\\toutiao.apk'  #app package名
desired_caps['appPackage'] = 'com.ximalaya.ting.android'  #app package名
desired_caps['appActivity'] = '.activity.MainActivity' #app默认Activity
desired_caps['unicodeKeyboard']  = True  # 一定要有该参数，否则unicode 输入的中文无效
dr = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #启动Remote RPC

dr.implicitly_wait(10)

elem = dr.find_element_by_id('com.ximalaya.ting.android:id/search')
elem.click()
elem = dr.find_element_by_id('com.ximalaya.ting.android:id/search_et')
elem.send_keys(u'红楼梦')


raw_input('press to quit')
dr.quit()

# elem = dr.find_element_by_id('so.ofo.labofo:id/verify_code_button')
# elem.click()
#
#
# vc = raw_input('input validatecode')
# elem = dr.find_element_by_id('so.ofo.labofo:id/verify_code')
# elem.send_keys(vc)
#
#
#
# elem = dr.find_element_by_id('so.ofo.labofo:id/sign_in_button')
# elem.click()


#WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.ID, "io.manong.developerdaily:id/progressText")))
time.sleep(3)
#print 2
#driver.swipe(start_x=75, start_y=800, end_x=75, end_y=0, duration=800)
time.sleep(1)

#print 3
#driver.swipe(start_x=75, start_y=800, end_x=75, end_y=0, duration=800)
time.sleep(1)
#print 4

#driver.swipe(start_x=75, start_y=800, end_x=75, end_y=0, duration=800)
#print 5

#raw_input('press to quit')
#driver.quit()