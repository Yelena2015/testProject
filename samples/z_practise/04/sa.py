# coding=utf8
from appium import webdriver
import time
import traceback


desired_caps = {}
desired_caps['platformName'] = 'Android'  #测试平台
desired_caps['platformVersion'] = '5.1'   #平台版本,不能写错
desired_caps['deviceName'] = 'test'    #设备名称，多设备时需区分
desired_caps['app'] = r'e:\apk\HiSpace.apk'  #app 文件 名，指定了要安装的app 在电脑上的路径
desired_caps['appPackage'] = 'com.huawei.appmarket'  #app package名,指定了要运行的app
desired_caps['appActivity'] = 'com.huawei.appmarket.MainActivity' #app默认Activity
desired_caps['unicodeKeyboard']  = True  # 一定要有该参数，否则unicode 输入的中文无效
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 60
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps) #启动Remote RPC
driver.implicitly_wait(10)

try:
    # ------------------------------
    code = u'new UiSelector().resourceId("com.huawei.appmarket:id/tabLayout").childSelector(new UiSelector().text("排行"))'
    driver.find_element_by_android_uiautomator(code).click()

    code = u'new UiSelector().text("总榜")'
    boardTotal = driver.find_element_by_android_uiautomator(code)
    destPosY= boardTotal.location['y']

    driver.implicitly_wait(1)
    code = u'new UiSelector().text("口碑最佳")'
    while True:
        driver.swipe(400, destPosY+80 ,400,destPosY,1000)
        eles = driver.find_elements_by_android_uiautomator(code)
        # 没有找到口碑最佳
        if not eles:
            continue

        # 找到了
        ele = eles[0]
        y1 = ele.location['y']

        driver.swipe(400,y1, 400,destPosY,3000)
        break



    driver.implicitly_wait(10)


    tvs = []
    eles = driver.find_elements_by_class_name('android.widget.TextView')
    for ele in eles:
        tvs.append(ele.text)


    tvsStr = '|||'.join(tvs)

    pos1 = tvsStr.find(u'口碑最佳|||')
    targetStr = tvsStr[pos1:]

    def getName(No):
        tp1 = targetStr.find(No + '|||')
        tp2 = targetStr.find('|||',tp1+4)
        return targetStr[tp1+4:tp2]

    print '\n\n ====== result is ========='
    print getName('1')
    print getName('2')
    print getName('3')


    # ------------------------------

except:
    print traceback.format_exc()


raw_input('**** Press to quit..')
driver.quit()