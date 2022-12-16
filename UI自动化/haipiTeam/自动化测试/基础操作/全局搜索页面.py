import time

import pyautogui

from HNtest.testcasesec.testcasesec import page
from HNtest.Secselenium.secdriver import Secdriver
from ..元素对象库.公共元素 import *
from ..基础操作.公共操作 import *
from ..基础操作.登录页面 import *
from ..基础操作.进入到操作位置 import *
from ..元素对象库.全局搜索 import *

class 全局搜索页面(page):
    def __init__(self,Secdriver=None):
        page.__init__(self,secdriver=Secdriver)
        self.进入到操作位置 = 进入到操作位置(Secdriver=Secdriver)
        self.公共操作 = 公共操作(Secdriver=Secdriver)
        self.登录页面 = 登录页面(Secdriver=Secdriver)

    def 搜索文件(self, 搜索条件):
        self.clear(全局搜索对象库.搜索框)
        self.send_keys(全局搜索对象库.搜索框,搜索条件)
        self.click(全局搜索对象库.搜索按钮)
        time.sleep(3)