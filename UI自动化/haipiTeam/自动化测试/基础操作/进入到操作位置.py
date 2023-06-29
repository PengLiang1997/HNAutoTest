from HNtest.testcasesec.testcasesec import page
from HNtest.Secselenium.secdriver import Secdriver
from ..元素对象库.首页对象库 import *
from ..元素对象库.公共元素 import *
from ..元素对象库.设置页 import *
from ..元素对象库.分享管理页 import *


class 进入到操作位置(page):
    def __init__(self,Secdriver=None):
        page.__init__(self,secdriver=Secdriver)

    def 进入项目管理页(self):
        self.default_content()
        self.click(首页对象库.项目)

    def 进入收藏页(self):
        self.default_content()
        self.click(首页对象库.收藏)

    def 进入设置页(self):
        self.default_content()
        self.click(首页对象库.设置)

    def 进入生命周期工作区(self):
        self.default_content()
        self.click(首页对象库.设置)
        self.click(设置页对象库.生命周期页)

    def 进入版次工作区(self):
        self.default_content()
        self.click(首页对象库.设置)
        self.click(设置页对象库.版次页)

    def 进入属性工作区(self):
        self.default_content()
        self.click(首页对象库.设置)
        self.click(设置页对象库.属性页)


    def 进入搜索页(self):
        self.default_content()
        self.click(首页对象库.全局搜索)

    def 进入消息页(self):
        self.default_content()
        self.click(首页对象库.消息)

    def 进入用户信息页(self):
        self.default_content()
        self.click(首页对象库.用户)
        self.wait(首页对象库.用户信息,30)
        self.click(首页对象库.用户信息)

    def 进入用户首选项页(self):
        self.default_content()
        self.click(首页对象库.用户)
        self.wait(首页对象库.用户首选项, 30)
        self.click(首页对象库.用户首选项)

    def 进入我的分享页(self):
        self.default_content()
        self.click(首页对象库.分享)
        self.click(分享管理对象库.我的分享tab页)

    def 进入访问记录页(self):
        self.default_content()
        self.click(首页对象库.分享)
        self.click(分享管理对象库.访问记录tab页)

