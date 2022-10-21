import win32con
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import win32gui
from HNtest import Pltest

class Secdriver(object):

    def __init__(self,url=None,browser="chrome"):
        try:
            if browser == "chrome":
                self.driver = webdriver.Chrome()
            elif browser == "firfox":
                self.driver = webdriver.Firefox()
            elif browser == "360":
                self.driver = webdriver.Chrome()
            if url:
                self.driver.get(url)
            else:
                self.driver.get(Pltest.testurl)
        except:
            raise TypeError("浏览器启动失败")



    ##############以下是对webdriver方法的重写######################
    def switch_to_default_content(self):
        '''
        切换到top window
        '''
        self.driver.switch_to.default_content()

    def swtich_to_window(self,name):
        '''
        根据句柄切换页面
        '''
        self.driver.switch_to.window(window_name=name)

    def switch_to_alert(self):
        '''
        切换到页面提示框
        :return:返回一个alert对象
        '''
        self.driver.switch_to.alert()

    def get(self,url):
        '''
        在当前窗口打开url
        '''
        self.driver.get(url)

    def back(self):
        '''
        浏览器回退一步操作
        '''
        self.driver.back()

    def forword(self):
        '''
        浏览器前进一步操作
        '''
        self.driver.forward()

    def close(self):
        '''
        关闭当前创建偶
        '''
        self.driver.close()

    def quite(self):
        '''
        关闭所有窗口并退出浏览器
        '''
        self.driver.quit()

    def refrsh(self):
        '''
        刷新当前页面
        '''
        self.driver.refresh()

    def maximize_window(self):
        '''
        最大化浏览器窗口
        '''
        self.driver.maximize_window()

    def minimize_window(self):
        '''
        最小化浏览器窗口
        '''
        self.driver.minimize_window()

    def implicitly_wait(self,otime):
        '''
        隐式等待
        '''
        self.driver.implicitly_wait(time_to_wait=otime)

    def window_handles(self):
        '''
        获取当前浏览器的句柄
        :return: 返回句柄列表
        '''
        self.driver.window_handles()

    def current_window_handle(self):
        '''
        返回当前窗口句柄
        '''
        self.driver.current_window_handle()

    def current_url(self):
        '''
        返回当前窗口的url
        :return:string
        '''
        self.driver.current_url()

    def current_title(self):
        '''
        返回当前窗口的标题
        '''
        self.driver.title()


    #####################以下为二次封装的方法###################

    #等待html稳定，增强脚本的稳定性
    def waithtml(self,otime=3):
        try:
            WebDriverWait(self.driver,otime).until(lambda driver: driver.execute_script('return document.readyState')=='complete')
        except exceptions.TimeoutException:
            pass

    def waitpagestable(self,checkpage):
        '''
        检查页面，等待到页面元素不发生变化
        :param checkpage: bool型，控制是否进行页面检查
        :return:
        '''
        if checkpage:
            starttime=time.time()
            source=self.driver.page_source
            while True:
                time.sleep(0.3)
                secsource=self.driver.page_source
                if secsource==source:
                    break
                else:
                    newtime=time.time()
                    if int(newtime)-int(starttime)>3:
                        break
                source=secsource

    def elementisVisable(self,element):
        '''
        判断元素在页面上是否可见
        :param element:
        :return:
        '''
        try:
            if not element.is_displayed():
                return False
            if not element.is_enabled():
                return False
        except:
            return False
        return True

    def wait_ele_disappear(self,xpath,otime):
        '''
        等待元素在页面上消失
        :param xpath: 元素定位的xpath
        :param otime: 等待消失时间
        :return:
        '''
        starttime=time.time()
        while True:
            elements=self.driver.find_elements(by=By.XPATH,value=xpath)
            for element in elements:
                if not self.elementisVisable(element):
                    elements.remove(element)
            if not elements:
                return True
            else:
                endtime=time.time()
                if int(endtime)-int(starttime)>=otime:
                    raise exceptions.NoSuchElementException(f'页面元素：{xpath}在{otime}s内未消失！')
                else:
                    time.sleep(0.3)

    def waitelement(self, value, by=By.XPATH, otime=30):
        '''
        等待页面元素出现
        :param value:
        :param by:
        :param otime:
        :return:
        '''
        try:
            self.getelement(value=value,by=by,otime=otime)
        except:
            return False
        else:
            return True

    def waitpopup(self,message,appear=2,disappear=30):
        '''
        等待加载弹窗的出现和消失
        :param message: 加载弹窗的提示信息
        :param appear: 弹窗出现信息
        :param disappear: 弹窗消失信息
        :return:
        '''
        popup=f"//*[contains(text(),'{message}')]"
        if self.waitelement(value=popup,otime=appear):
            self.waitelement(value=popup,otime=disappear)


    #浏览器常规操作
    def getelement(self,value,by=By.XPATH,otime=30,checkpage=True):
        '''
        获取xpath指定的非隐藏元素，如果有多个，默认返回收个元素
        :param value: 指定的xpath
        :param by: 指定value的类型，默认为xpath
        :param otime: 元素等待超时时间
        :return:
        '''
        self.waithtml(otime=1)
        self.waitpagestable(checkpage=checkpage)
        starttime=time.time()
        while True:
            visable_elements=[]
            elements=self.driver.find_elements(by=by,value=value)
            for element in elements:
                if self.elementisVisable(element):
                    visable_elements.append(element)
            if visable_elements:
                return visable_elements[0]
            else:
                nowtime=time.time()
                if int(nowtime)-int(starttime)>otime:
                    raise exceptions.NoSuchElementException(f'未找到xpath：{value}指向的页面元素')
                else:
                    time.sleep(0.3)

    def getelements(self,value,by=By.XPATH,otime=30,checkpage=True):
        '''
        返回xpath指向的所有非隐藏元素
        :param value:
        :param by:
        :param otime:
        :param checkpage:
        :return:
        '''
        self.waithtml(otime=1)
        self.waitpagestable(checkpage=checkpage)
        starttime = time.time()
        while True:
            visable_elements = []
            elements = self.driver.find_elements(by=by, value=value)
            for element in elements:
                if self.elementisVisable(element):
                    visable_elements.append(element)
            if visable_elements:
                return visable_elements
            else:
                nowtime = time.time()
                if int(nowtime) - int(starttime) > otime:
                    raise exceptions.NoSuchElementException(f'未找到xpath：{value}指向的页面元素')
                else:
                    time.sleep(0.3)

    def switch_to_window_byTitle(self,title,otime=30):
        '''
        根据页面title切换Window
        :param title: 页面标题
        :param otime: 等待时间（s）
        '''
        for clock in range(otime):
            for handle in self.driver.window_handles:
                self.driver.switch_to.window(handle)
                if self.driver.title==title:
                    return True
            time.sleep(1)
            clock+=1
        raise TimeoutError(f"未找到title为{title}的页面")

    def switch_to_new_window(self):
        '''
        跳转到最新的页面
        '''
        list=self.driver.window_handles
        self.driver.switch_to.window(list[-1])

    def scrollToBottom(self):
        '''
        滚动滚动条到最底部
        '''
        self.driver.execute_script("window.scrollTo(0, 99999)")

    def scrollToUp(self):
        '''
        滚动滚动条到最顶部
        '''
        self.driver.execute_script("window.scrollTo(0, 0)")


    #操作页面元素属性
    def addAttribute(self,element,attributeName,value):
        '''
        向网页里的标签中添加属性
        :param element: 页面元素
        :param attributeName: 属性名称
        :param value: 属性值
        :return:
        '''
        return self.driver.execute_script("arguments[0].%s=arguments[1]"% attributeName,element,value)

    def setAttribute(self,element,attributeName,value):
        '''
        修改网页里的标签属性
        :param element: 页面元素
        :param attributeName: 属性名称
        :param value: 属性值
        :return:
        '''
        return self.driver.execute_script("arguments[0].SetAttribute(arguments[1],arguments[2])",attributeName, element, value)

    def removeAttribute(self,element,attributeName):
        '''
        删除网页里的标签属性
        :param element: 页面元素
        :param attributeName: 属性名称
        :return:
        '''
        return self.driver.execute_script(f"arguments[0].removeAttribute(\"{attributeName}\")",element)

    def setText(self,element,text):
        '''
        设置网页里的标签文本
        :param element: 页面元素
        :param text: 文本内容
        :return:
        '''
        return self.driver.execute_script("arguments[0].innerHTML=arguments[1]",element,text)

    


    #其他操作
    def win_dialog(self,path):
        '''
        处理win下选择上传文件类的系统对话框，此类对话框类型为#32770
        :param path:需上传文件的绝对路径
        :return:
        '''
        time.sleep(3)
        dialog=win32gui.FindWindow('#32770','打开')
        ComboBoxEx32=win32gui.FindWindowEx(dialog,0,'ComboBoxEx32',None)
        ComboBox=win32gui.FindWindowEx(ComboBoxEx32,0,'ComboBox',None)
        Edit=win32gui.FindWindowEx(ComboBox,0,'Edit',None)
        button=win32gui.FindWindowEx(Edit,0,'Button',None)
        win32gui.SendMessage(Edit,win32con.WM_SETTEXT,None,path)
        win32gui.SendMessage(dialog,win32con.WM_COMMAND,1,button)
        time.sleep(2)

    def get_screenshot(self,path):
        '''
        对页面截图并保存到指定的目录
        :return:
        '''
        self.driver.get_screenshot_as_file(filename=path)