import functools
import os.path
import random
import sys
import time
import traceback
from ..Secselenium.secdriver import Secdriver
import pyautogui as pyautogui

import Demos.FileSecurityTest
from .border import BorderPoints
from ..config import Config
import unittest as unittest
from ..Secselenium.secdriver import Secdriver as driver
from selenium.webdriver.common.action_chains import ActionChains as AC
from HNtest.BeautifulReport.BeautifulReport import *
from selenium.webdriver.common.keys import Keys

#全局变量，保存图片名称
imgName_list=[]

class ParametrizedTestCase(unittest.TestCase):
    '''
    对unittest进行参数化
    '''
    def __init__(self,methodName="runTest",param=None):
        super(ParametrizedTestCase,self).__init__(methodName)
        self.param=param

    def parametrize(self,param,className,functionName):
        '''
        创建一个包含从给定子类中获取的所有测试的套件，并将参数“param”传递给它们
        '''
        testloader=unittest.TestLoader()
        testsuite=unittest.TestSuite()
        testnames=testloader.getTestCaseNames(className)
        for name in testnames:
            if not functionName:
                testsuite.addTest(className(name,param=param))
            else:
                if name==functionName:
                    testsuite.addTest(className(name,param=param))
        return testsuite

class TestCaseSec(ParametrizedTestCase):
    '''
    继承unittest基类与参数化类，集成了截图和保存到对应目录功能
    '''
    @classmethod
    def setUp(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    #用于测试此类的初始化方法是否被正常执行
    @classmethod
    def setUpClass(cls):
        return 'NoclassconFunction'

    # @classmethod
    # def savedriver(cls):
    #     '''
    #     保存脚本运行出错时浏览器页面
    #     :return:
    #     '''
    #     if Config.keepwindows()==True:
    #         exec(f'cls.driver{int(round(time.time()*1000))}')

    def get_screenshot(self,funcname=None,cv=None,picname=None):
        '''
        截取图片并将图片保存到测试报告的目录中
        :param funcname: 测试方法名称
        :param cv: 控制流程分支
        :param picname: 截图名称
        :param win: 控制流程分支
        :return: 返回图片的相对路径
        '''
        message=traceback.extract_stack()
        # 项目路径
        projectdir=sys.path[0]
        # report_dir=os.path.join(projectdir,'report')
        report_dir = projectdir+'\\report'
        #生成最新报告的文件夹
        if os.path.exists(report_dir):
            for i,x,name in os.walk(report_dir):
                if x[-1]=="pic":
                    new_reportName=x[-2]
                else:
                    new_reportName = x[-1]
                projectdir=os.path.join(report_dir,new_reportName,'img')
                if not os.path.exists(projectdir):
                    os.mkdir(projectdir)
                break
        else:
            projectdir=os.path.join(os.path.dirname(projectdir),'opencv_img')
            if not os.path.exists(projectdir):
                os.mkdir(projectdir)
        pid=os.getpid()
        randomInt=random.randint(10000000,99999999)

        #message[-2][2]时调用这个函数的函数的名称
        if not funcname:
            funcname=message[-2][2]

        path=os.path.join(projectdir,self.__module__+'.'+self.__class__.__name__+'.'+funcname+'_'+str(randomInt)+'_'+str(pid)+'.png')
        #截图
        global imgName_list
        img_name=self.__module__+'.'+self.__class__.__name__+'.'+funcname+'_'+str(randomInt)+'_'+str(pid)+'.png'
        if not cv :
            imgName_list.append(img_name)
            try:
                self.driver.get_screenshot(path=path)
            except:
                raise RuntimeError('测试类里面没有driver变量')
            return path
        elif cv:
            cv_name="cv_"+self.__module__+'.'+self.__class__.__name__+'.'+funcname+'_'+str(randomInt)+'_'+str(pid)+f'{picname}hhh.png'
            cv_path=os.path.join(projectdir,cv_name)
            self.driver.get_screenshot(path=cv_path)
            return cv_path

def wsht(func):
    '''
    测试用例执行失败或报错截图
    :param func:
    :return:
    '''
    @functools.wraps(func)
    def screenshot(self:TestCaseSec):
        try:
            res=func(self)
        except Exception as e:
            if isinstance(e,unittest.SkipTest):
                raise
            self.get_screenshot(funcname=func.__name__,picname='flage')
            raise e
        else:
            return res
    return screenshot

class page():
    '''
    页面对象封装类，封装常用的页面方法
    '''
    def __init__(self,secdriver:Secdriver=None):
        self.driver=secdriver

    def click(self, xpath, otime=30):
        self.driver.getelement(value=xpath,otime=otime).click()

    def double_click(self,xpath,otime=30):
        AC(self.driver.driver).double_click(self.driver.getelement(value=xpath,otime=otime)).perform()

    def move_to_element(self,xpath,otime=30):
        AC(self.driver.driver).move_to_element(self.driver.getelement(value=xpath,otime=otime)).perform()

    def context_click(self,xpath,otime=30):
        AC(self.driver.driver).context_click(self.driver.getelement(value=xpath,otime=otime)).perform()

    def clear(self,xpath,otime=30):
        self.driver.getelement(value=xpath, otime=otime).clear()

    def clear_by_key(self,xpath):
        self.send_keys(xpath, Keys.CONTROL + 'a')
        self.send_keys(xpath, Keys.BACKSPACE)

    def send_keys(self,xpath,key,otime=30):
        self.driver.getelement(value=xpath, otime=otime).send_keys(key)

    def click_index(self,xpath,index=0,otime=30):
        '''
        根据index索引点击元素
        :param xpath:
        :param index:
        :param otime:
        :return:
        '''
        self.driver.getelements(value=xpath, otime=otime)[index].click()

    def double_click_index(self,xpath,index=0,otime=30):
        '''
        根据index索引双击元素
        :param xpath:
        :param index:
        :param otime:
        :return:
        '''
        AC(self.driver.driver).double_click(self.driver.getelements(value=xpath, otime=otime)[index]).perform()

    def context_click_index(self,xpath,index=0,otime=30):
        '''
        根据index索引右击元素
        :param xpath:
        :param index:
        :param otime:
        :return:
        '''
        AC(self.driver.driver).context_click(self.driver.getelements(value=xpath,otime=otime)[index]).perform()

    def clear_index(self,xpath,index=0,otime=30):
        '''
        根据index索引清理元素
        :param xpath:
        :param index:
        :param otime:
        :return:
        '''
        self.driver.getelements(value=xpath, otime=otime)[index].clear()

    def send_keys_index(self,xpath,index,key,otime=30):
        '''
        根据index索引向元素输入数据
        :param xpath:
        :param index:
        :param key:
        :param otime:
        :return:
        '''
        self.driver.getelements(value=xpath, otime=otime)[index].send_keys(key)

    def drag_and_drop_to_element(self,srpath,tgpath,srBorderpoint=BorderPoints.CENTER,tgBorderpoint=BorderPoints.CENTER,otime=30):
        '''
        拖拽页面元素到目标元素位置
        :param srpath: 需要拖拽的元素
        :param thpath: 目标元素
        :param drBorderpoint: 需要拖拽的元素的拖拽部位
        :param tgBorderpoint: 拖拽到目标元素的目标部位
        :param otime: 定位超时时间
        :return:
        '''
        srElement=self.driver.getelement(srpath,otime=otime)
        srSize=srElement.size
        tgElement = self.driver.getelement(tgpath, otime=otime)
        tgSize = tgElement.size
        action=AC(self.driver.driver)
        action.move_to_element(srElement)
        if srBorderpoint==1:
            action.move_by_offset(-srSize["width"]/2,-srSize["height"]/2)
        elif srBorderpoint==2:
            action.move_by_offset(0,-srSize["height"]/2)
        elif srBorderpoint==3:
            action.move_by_offset(-srSize["width"]/2,-srSize["height"]/2)
        elif srBorderpoint==4:
            action.move_by_offset(-srSize["width"]/2,0)
        elif srBorderpoint==5:
            pass
        elif srBorderpoint==6:
            action.move_by_offset(-srSize["width"]/2,0)
        elif srBorderpoint==7:
            action.move_by_offset(-srSize["width"]/2,-srSize["height"]/2)
        elif srBorderpoint==8:
            action.move_by_offset(0,-srSize["height"]/2)
        elif srBorderpoint==9:
            action.move_by_offset(-srSize["width"]/2,-srSize["height"]/2)
        elif srBorderpoint==10:
            action.move_by_offset(0,-srSize["height"]/4)
        elif srBorderpoint==11:
            action.move_by_offset(0,-srSize["height"]/4)
        elif srBorderpoint==12:
            action.move_by_offset(-srSize["width"]/4,0)
        elif srBorderpoint==13:
            action.move_by_offset(-srSize["width"]/4,0)
        elif srBorderpoint==14:
            action.move_by_offset(-srSize["width"]/4,-srSize["height"]/4)
        elif srBorderpoint==15:
            action.move_by_offset(-srSize["width"]/4,-srSize["height"]/4)
        elif srBorderpoint==16:
            action.move_by_offset(-srSize["width"]/4,-srSize["height"]/4)
        elif srBorderpoint==17:
            action.move_by_offset(-srSize["width"]/4,-srSize["height"]/4)
        else:
            raise Exception('参数错误：srBorderpoint')
        action.click_and_hold()
        action.move_by_offset(tgElement)
        if tgBorderpoint==1:
            action.move_by_offset(-tgSize["width"]/2,-tgSize["height"]/2)
        elif tgBorderpoint==2:
            action.move_by_offset(0,-tgSize["height"]/2)
        elif tgBorderpoint==3:
            action.move_by_offset(-tgSize["width"]/2,-tgSize["height"]/2)
        elif tgBorderpoint==4:
            action.move_by_offset(-tgSize["width"]/2,0)
        elif tgBorderpoint==5:
            pass
        elif tgBorderpoint==6:
            action.move_by_offset(-tgSize["width"]/2,0)
        elif tgBorderpoint==7:
            action.move_by_offset(-tgSize["width"]/2,-tgSize["height"]/2)
        elif tgBorderpoint==8:
            action.move_by_offset(0,-tgSize["height"]/2)
        elif tgBorderpoint==9:
            action.move_by_offset(-tgSize["width"]/2,-tgSize["height"]/2)
        elif tgBorderpoint==10:
            action.move_by_offset(0,-tgSize["height"]/4)
        elif tgBorderpoint==11:
            action.move_by_offset(0,-tgSize["height"]/4)
        elif tgBorderpoint==12:
            action.move_by_offset(-tgSize["width"]/4,0)
        elif tgBorderpoint==13:
            action.move_by_offset(-tgSize["width"]/4,0)
        elif tgBorderpoint==14:
            action.move_by_offset(-tgSize["width"]/4,-tgSize["height"]/4)
        elif tgBorderpoint==15:
            action.move_by_offset(-tgSize["width"]/4,-tgSize["height"]/4)
        elif tgBorderpoint==16:
            action.move_by_offset(-tgSize["width"]/4,-tgSize["height"]/4)
        elif tgBorderpoint==17:
            action.move_by_offset(-tgSize["width"]/4,-tgSize["height"]/4)
        else:
            raise Exception('参数错误：tgBorderpoint')
        action.release().perform()

    def drag_and_drop_by_offset(self,srpath,offset_x,offset_y,borderpoint=BorderPoints.CENTER,otime=30):
        '''
        拖拽页面元素到指定坐标位置
        :param srxpath: 被做拽元素xpath
        :param offset_x: 目标坐标的x坐标
        :param offset_y: 目标坐标的y坐标
        :param borderpoint: 元素的拖拽位置
        :param otime: 元素等待超时时间
        :return:
        '''
        srElement = self.driver.getelement(srpath, otime=otime)
        srSize = srElement.size
        action = AC(self.driver.driver)
        action.move_to_element(srElement)
        if borderpoint==1:
            action.move_by_offset(-srSize["width"]/2,-srSize["height"]/2)
        elif borderpoint==2:
            action.move_by_offset(0,-srSize["height"]/2)
        elif borderpoint==3:
            action.move_by_offset(-srSize["width"]/2,-srSize["height"]/2)
        elif borderpoint==4:
            action.move_by_offset(-srSize["width"]/2,0)
        elif borderpoint==5:
            pass
        elif borderpoint==6:
            action.move_by_offset(-srSize["width"]/2,0)
        elif borderpoint==7:
            action.move_by_offset(-srSize["width"]/2,-srSize["height"]/2)
        elif borderpoint==8:
            action.move_by_offset(0,-srSize["height"]/2)
        elif borderpoint==9:
            action.move_by_offset(-srSize["width"]/2,-srSize["height"]/2)
        elif borderpoint==10:
            action.move_by_offset(0,-srSize["height"]/4)
        elif borderpoint==11:
            action.move_by_offset(0,-srSize["height"]/4)
        elif borderpoint==12:
            action.move_by_offset(-srSize["width"]/4,0)
        elif borderpoint==13:
            action.move_by_offset(-srSize["width"]/4,0)
        elif borderpoint==14:
            action.move_by_offset(-srSize["width"]/4,-srSize["height"]/4)
        elif borderpoint==15:
            action.move_by_offset(-srSize["width"]/4,-srSize["height"]/4)
        elif borderpoint==16:
            action.move_by_offset(-srSize["width"]/4,-srSize["height"]/4)
        elif borderpoint==17:
            action.move_by_offset(-srSize["width"]/4,-srSize["height"]/4)
        else:
            raise Exception('参数错误：borderpoint')
        action.click_and_hold().move_by_offset(offset_x,offset_y).release().perform()

    def default_content(self):
        '''
        跳转到dom主目录下
        :return:
        '''
        self.driver.switch_to_default_content()

    def switch_frame(self,xpath='//iframe',num=1,otime=30):
        '''
        iframe切换
        :param xpath:
        :param num:
        :param otime:
        :return:
        '''
        for i in range(num):
            self.driver.driver.switch_to.frame(self.driver.getelement(value=xpath,otime=otime))

    def wait(self,xpath,otime=3):
        return self.driver.waitelement(value=xpath,otime=otime)

    def waitdisappear(self,xpath,otime):
        return self.driver.wait_ele_disappear(xpath=xpath,otime=otime)

    def waitpopup(self, message, appear=2, disappear=30):
        '''
        等待加载弹窗的出现和消失
        :param message: 加载弹窗的提示信息
        :param appear: 弹窗出现信息
        :param disappear: 弹窗消失信息
        :return:
        '''
        popup = f"//*[contains(text(),'{message}')]"
        if self.wait(xpath=popup, otime=appear):
            self.waitdisappear(xpath=popup, otime=disappear)

    def switch_to_window_byTagName(self,TagName):
        self.driver.switch_to_window_byTitle(title=TagName)

    def switch_to_new_window(self):
        self.driver.switch_to_new_window()

    def new_imgdir(self,info=None):
        '''
        创建一个路径，用来存放单个用例所有的错误截图
        :param info:
        :return:
        '''
        projectdir=sys.path[0]
        reportdir=os.path.join(projectdir,'report')
        if os.path.exists(reportdir):
            for i,x,name in os.walk(reportdir):
                new_reportName=x[-1]
                projectdir=os.path.join(reportdir,new_reportName,'img')
                break
        else:
            raise EOFError('report目录不存在')
        random_int=random.randint(1,99999)
        if info:
            img_name=str(random_int)+'_'+info+'.png'
        else:
            img_name = str(random_int) + '.png'
        img_path=os.path.join(projectdir,img_name)
        return img_path

    def get_screenshot(self,path=None,info=None):
        '''
        截图并保存到指定路径
        :param path:
        :param info:
        :return:
        '''
        if path:
            self.driver.get_screenshot(path=path)
        if info:
            self.driver.get_screenshot(path=self.new_imgdir(info=info))

    def addAttribute(self, element, attributeName, value):
        return self.driver.addAttribute(element=element,attributeName=attributeName,value=value)

    def setAttribute(self, element, attributeName, value):
        return self.driver.setAttribute(element=element,attributeName=attributeName,value=value)

    def removeAttribute(self, element, attributeName, value):
        return self.driver.removeAttribute(element=element,attributeName=attributeName)

    def move_to_by_pyautogui(self,xpath,x_offset=0,y_offset=0):
        element=self.driver.getelement(xpath)
        location=element.location
        x=location['x']
        y=location['y']
        pyautogui.moveTo(x=x*1.25+x_offset*1.25, y=y*1.25+y_offset*1.25)
        print(f"x坐标时{location['x']},y坐标是{location['y']}")

    def scroll_by_pyautogui(self,clicks):
        pyautogui.scroll(clicks)

