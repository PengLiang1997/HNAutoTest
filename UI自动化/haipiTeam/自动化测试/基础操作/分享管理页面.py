import time

import pyautogui
from HNtest import Pltest
from HNtest.testcasesec.testcasesec import page
from HNtest.Secselenium.secdriver import Secdriver
from ..元素对象库.公共元素 import *
from ..基础操作.公共操作 import *
from ..基础操作.登录页面 import *
from ..基础操作.进入到操作位置 import *
from ..元素对象库.项目 import *
from ..元素对象库.分享管理页 import *


class 分享管理页面(page):
    def __init__(self,Secdriver=None):
        page.__init__(self,secdriver=Secdriver)
        self.进入到操作位置 = 进入到操作位置(Secdriver=Secdriver)
        self.公共操作 = 公共操作(Secdriver=Secdriver)
        self.登录页面 = 登录页面(Secdriver=Secdriver)

    def 取消所有分享(self):
        self.click(分享管理对象库.全选复选框)
        self.click(分享管理对象库.批量取消分享)
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"),3)

    def 点击查看分享(self):
        pass

    def 改变分享状态(self):
        pass

    def 编辑过期时间(self):
        pass

    def 取消单个分享(self,分享内容名称):
        self.click(分享管理对象库.全选复选框)
        if self.wait(分享管理对象库.取消分享.format(分享内容名称),3):
            self.click(分享管理对象库.取消分享.format(分享内容名称))
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 3)

    def 批量取消分享(self):
        pass

    def 查看分享记录(self):
        pass

    def 清除所有访问记录(self):
        self.click(分享管理对象库.全选复选框)
        self.click(分享管理对象库.批量删除访问记录)
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 3)

    def 清除单个访问记录(self):
        pass

    def 批量清除访问记录(self):
        pass

    def 点击查看访问记录(self):
        pass