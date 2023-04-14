import time

from HNtest.testcasesec.testcasesec import page
from HNtest.Secselenium.secdriver import Secdriver
from ..元素对象库.公共元素 import *
from ..基础操作.公共操作 import *
from ..基础操作.登录页面 import *
from ..基础操作.进入到操作位置 import *
from ..元素对象库.项目 import *

class 生命周期管理页面(page):
    def __init__(self, Secdriver=None):
        page.__init__(self, secdriver=Secdriver)
        self.进入到操作位置 = 进入到操作位置(Secdriver=Secdriver)
        self.公共操作 = 公共操作(Secdriver=Secdriver)
        self.登录页面 = 登录页面(Secdriver=Secdriver)

    def 进入新增生命周期弹框(self,生命周期名称,描述=None):
        self.click(设置页对象库.生命周期管理工作区.新增)
        self.wait(对话框对象库.弹框标题.format("新增生命周期"))
        self.send_keys(公共元素对象库.输入框.format("名称"),生命周期名称)
        if 描述:
            self.send_keys(公共元素对象库.文本框.format("描述"),描述)

    def 删除生命周期(self,生命周期名称):
        if self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format(生命周期名称), 3):
            self.click(设置页对象库.生命周期管理工作区.生命周期列表复选框.format(生命周期名称))
            self.click(设置页对象库.生命周期管理工作区.删除)
            self.wait(对话框对象库.对话框标题.format("提示"),3)
            self.click(对话框对象库.弹框按钮.format("提示", "确定"))
            self.wait(公共元素对象库.系统提示信息弹框.format("删除成功"),3)

    def 删除所有生命周期(self):
        namelist=[]
        list=self.driver.getelements("//table//tr/td[2]//span[1]")
        syslist=self.driver.getelements('//table//tr/td[2]//span[text()="系统"]/preceding-sibling::span')
        if len(list)>len(syslist):
            for name in syslist:
                namelist.append(name.text)
            self.click(设置页对象库.生命周期管理工作区.设置默认单选框.format(namelist[0]))
            self.click(设置页对象库.生命周期管理工作区.生命周期列表全选按钮)
            for sysname in namelist:
                self.click(设置页对象库.生命周期管理工作区.生命周期列表复选框.format(sysname))
            self.click(设置页对象库.生命周期管理工作区.删除)
            self.wait(对话框对象库.对话框标题.format("提示"), 3)
            self.click(对话框对象库.弹框按钮.format("提示", "确定"))
            self.wait(公共元素对象库.系统提示信息弹框.format("删除成功"), 3)

    def 添加生命周期节点(self,节点名称,节点描述=None):
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框,节点名称)
        if 节点描述:
            self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点描述输入框, 节点描述)
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)

    def 设置升版流程(self,节点名称,开始节点,结束节点):
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format(节点名称))
        self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format(开始节点,结束节点))


class 版次管理页面(page):
    def __init__(self, Secdriver=None):
        page.__init__(self, secdriver=Secdriver)
        self.进入到操作位置 = 进入到操作位置(Secdriver=Secdriver)
        self.公共操作 = 公共操作(Secdriver=Secdriver)
        self.登录页面 = 登录页面(Secdriver=Secdriver)

    def 进入新增版次弹框(self,版次名称,描述=None):
        self.click(设置页对象库.版次管理工作区.新增)
        self.wait(对话框对象库.弹框标题.format("新增"))
        self.send_keys(公共元素对象库.输入框.format("名称"), 版次名称)
        if 描述:
            self.send_keys(公共元素对象库.文本框.format("描述"), 描述)

    def 删除版次(self,版次名称):
        if self.wait(设置页对象库.版次管理工作区.版次名称.format(版次名称), 3):
            self.click(设置页对象库.版次管理工作区.版次复选框.format(版次名称))
            self.click(设置页对象库.版次管理工作区.删除)
            self.wait(对话框对象库.对话框标题.format("提示"),3)
            self.click(对话框对象库.弹框按钮.format("提示", "确定"))
            self.wait(公共元素对象库.系统提示信息弹框.format("删除成功"),3)

    def 删除所有版次(self):
        namelist = []
        list = self.driver.getelements("//table//tr/td[2]//span[1]")
        syslist = self.driver.getelements('//table//tr/td[2]//span[text()="系统"]/preceding-sibling::span')
        if len(list) > len(syslist):
            for name in syslist:
                namelist.append(name.text)
            self.click(设置页对象库.版次管理工作区.是否默认单选框.format(namelist[0]))
            self.click(设置页对象库.生命周期管理工作区.生命周期列表全选按钮)
            for sysname in namelist:
                self.click(设置页对象库.版次管理工作区.版次复选框.format(sysname))
            self.click(设置页对象库.版次管理工作区.删除)
            self.wait(对话框对象库.对话框标题.format("提示"), 3)
            self.click(对话框对象库.弹框按钮.format("提示", "确定"))
            self.wait(公共元素对象库.系统提示信息弹框.format("删除成功"), 3)

    def 添加版次节点(self,节点名称):
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        self.wait(设置页对象库.版次管理工作区.版次内容输入框, 3)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框,节点名称)
        self.click(设置页对象库.版次管理工作区.保存版次节点)


class 属性管理页面(page):
    def __init__(self, Secdriver=None):
        page.__init__(self, secdriver=Secdriver)
        self.进入到操作位置 = 进入到操作位置(Secdriver=Secdriver)
        self.公共操作 = 公共操作(Secdriver=Secdriver)
        self.登录页面 = 登录页面(Secdriver=Secdriver)

    def 创建属性系统(self,属性系统名称,属性系统描述=None):
        self.click(设置页对象库.属性管理工作区.新增)
        self.wait(设置页对象库.属性管理工作区.属性系统名称输入框, 3)
        self.send_keys(设置页对象库.属性管理工作区.属性系统名称输入框, 属性系统名称)
        if 属性系统描述:
            self.send_keys(设置页对象库.属性管理工作区.属性系统描述输入框,属性系统描述)
        self.click(设置页对象库.属性管理工作区.属性系统保存按钮)
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"))

    def 删除属性系统(self,属性系统名称):
        if self.wait(设置页对象库.属性管理工作区.属性系统名称.format(属性系统名称), 3):
            self.click(设置页对象库.属性管理工作区.属性系统复选框.format(属性系统名称))
            self.click(设置页对象库.属性管理工作区.删除)
            self.wait(对话框对象库.对话框标题.format("提示"),3)
            self.click(对话框对象库.弹框按钮.format("提示", "确定"))
            self.wait(公共元素对象库.系统提示信息弹框.format("删除成功"),3)

    def 批量删除属性系统(self,属性系统名称列表):
        for 属性系统名称 in 属性系统名称列表:
            if self.wait(设置页对象库.属性管理工作区.属性系统名称.format(属性系统名称), 3):
                self.click(设置页对象库.属性管理工作区.属性系统复选框.format(属性系统名称))
        self.click(设置页对象库.属性管理工作区.删除)
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.弹框按钮.format("提示", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("删除成功"), 3)

    def 删除所有属性系统(self):
        namelist = []
        list = self.driver.getelements('//div[@class="attr_main_t"]//table//tr/td[2]/div/span[1]')
        syslist = self.driver.getelements('//div[@class="attr_main_t"]//table//tr/td[2]/div/span[text()="系统"]/preceding-sibling::span')
        if len(list) > len(syslist):
            for name in syslist:
                namelist.append(name.text)
            self.click(设置页对象库.版次管理工作区.是否默认单选框.format(namelist[0]))
            self.click(设置页对象库.属性管理工作区.属性系统全选复选框)
            for sysname in namelist:
                self.click(设置页对象库.属性管理工作区.属性系统复选框.format(sysname))
            self.click(设置页对象库.属性管理工作区.删除)
            self.wait(对话框对象库.对话框标题.format("提示"), 3)
            self.click(对话框对象库.弹框按钮.format("提示", "确定"))
            self.wait(公共元素对象库.系统提示信息弹框.format("删除成功"), 3)

    def 添加属性(self,服务类别,属性类型,属性名称,描述=None):
        self.click(设置页对象库.属性管理工作区.添加属性)
        self.wait(设置页对象库.属性管理工作区.属性类别输入框.format("last()"), 3)
        self.send_keys(设置页对象库.属性管理工作区.服务类别输入框.format("last()"), 服务类别)
        self.send_keys(设置页对象库.属性管理工作区.属性类别输入框.format("last()"), 属性类型)
        self.send_keys(设置页对象库.属性管理工作区.属性名称输入框.format("last()"), 属性名称)
        if 描述:
            self.send_keys(设置页对象库.属性管理工作区.属性描述输入框.format("last()"), 描述)
        self.click(设置页对象库.属性管理工作区.行保存按钮.format("last()"))