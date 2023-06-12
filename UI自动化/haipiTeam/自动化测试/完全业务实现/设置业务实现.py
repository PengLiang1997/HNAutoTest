import os.path
import random
import time

from ..基础操作.用户信息页面 import *
from ..基础操作.登录页面 import *
from ..基础操作.滑块验证 import *
from ..基础操作.项目页面 import *
from ..元素对象库.公共元素 import *
from ..基础操作.设置页面 import *
from HNtest.testcasesec.testcasesec import page

class 生命周期管理工作区(page):
    def __init__(self,Secdriver = None):
        page.__init__(self,secdriver=Secdriver)
        self.滑块验证=滑块验证(Secdriver=Secdriver)
        self.公共操作 = 公共操作(Secdriver=Secdriver)
        self.生命周期管理页面 = 生命周期管理页面(Secdriver=Secdriver)
        self.项目页面 = 项目页面(Secdriver=Secdriver)
        self.用户信息页面 = 用户信息页面(Secdriver=Secdriver)
        self.项目管理页面 = 项目管理页面(Secdriver=Secdriver)
        self.进入到操作位置 = 进入到操作位置(Secdriver=Secdriver)

    def 数据准备(self):
        self.项目管理页面.删除所有项目()
        self.进入到操作位置.进入生命周期工作区()
        self.生命周期管理页面.删除所有生命周期()

    def 新增生命周期(self):
        self.进入到操作位置.进入生命周期工作区()
        if self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format("test2"),3):
            self.click(设置页对象库.生命周期管理工作区.生命周期列表复选框.format("test2"))
            self.click(设置页对象库.生命周期管理工作区.删除)
            self.click(对话框对象库.弹框按钮.format("提示","确定"))
        if not self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format("test1"),3):
            self.click(设置页对象库.生命周期管理工作区.新增)
            self.wait(对话框对象库.弹框标题.format("新增生命周期"), 3)
            self.send_keys(公共元素对象库.输入框.format("名称"),"test1")
            self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
            self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框,"11")
            self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
            self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
            self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
            self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
            self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("22"))
            self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("22","11"))
            self.click(对话框对象库.弹框按钮.format("新增生命周期","确定"))
       #点击新增，弹出新增生命周期对话框
        self.click(设置页对象库.生命周期管理工作区.新增)
        self.default_content()
        if not self.wait(对话框对象库.弹框标题.format("新增生命周期"),3):
            raise AssertionError("点击新增生命周期，未出现新增生命周期弹窗")
        #对生命周期名称进行空值、重名、超长校验
        #空值校验
        self.click(公共元素对象库.输入框.format("名称"))
        self.click(对话框对象库.弹框按钮.format("新增生命周期","确定"))
        if not self.wait(公共元素对象库.输入框错误信息提示.format("名称不能为空"),3):
            raise AssertionError("对生命周期名称进行空值校验，没有出现名称不能为空的提示信息")
        #重名
        self.send_keys(公共元素对象库.输入框.format("名称"), "test1")
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("22"))
        self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("22", "11"))
        self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("存在同名模板"),3):
            raise AssertionError("生命周期可以重名创建")
        # #超长校验
        # self.clear(公共元素对象库.输入框.format("名称"))
        # self.send_keys(公共元素对象库.输入框.format("名称"), "123456789012345678901234567890123456789012345612345678907890")
        # self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
        # if not self.wait(公共元素对象库.系统提示信息弹框.format("参数检验失败"), 3):
        #     raise AssertionError("生命周期名称超长是，系统未给出对应的提示信息")

    def 生命周期节点管理(self):
        self.进入到操作位置.进入生命周期工作区()
        self.生命周期管理页面.删除生命周期('test2')
        self.click(设置页对象库.生命周期管理工作区.新增)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新增生命周期"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test2")
        #点击新增生命周期节点，生命周期节点列表中新增一行空白生命周期节点
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        if not self.wait(设置页对象库.生命周期管理工作区.生命周期节点名称输入框,3):
            raise AssertionError("点击添加生命周期节点按钮，未添加新的生命周期节点")
        #对节点名称进行超长校验、重名校验、空值校验
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("节点名称不能为空"),3):
            raise AssertionError("当生命周期节点名称为空时，点击保存可以保存生命周期节点成功！")
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("节点名称不能重复"),3):
            raise AssertionError("当生命周期节点名称重复时，点击保存未出现生命周期节点名称不能为空的提示！")
        # self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456")
        # self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        # if not self.wait(公共元素对象库.系统提示信息弹框.format("操作失败"), 3):
        #     raise AssertionError("当生命周期节点名称超长时，点击保存未出现生命周期节点名称过长的提示！")
        # #对输入内容进行空值校验和超长校验
        # self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        # self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
        # self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点描述输入框.format("123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456"))
        # self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        # if not self.wait(公共元素对象库.系统提示信息弹框.format("未知错误"), 3):
        #     raise AssertionError("当生命周期节点名称超长时，点击保存未出现生命周期节点描述过长的提示！")
        #点击生命周期节点行，点击删除按钮，生命周期行被删除
        time.sleep(2)
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
        self.click(设置页对象库.生命周期管理工作区.删除生命周期节点)
        if self.wait(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"),3):
            raise AssertionError("进行删除生命周期节点操作后，在生命周期节点列表仍然能查看到被删除的生命周期节点")
        #点击生命周期节点行，点击上移按钮，节点行上移一行，点击下移按钮，节点行下移一行
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
        self.click(设置页对象库.生命周期管理工作区.下移生命周期节点)
        text=self.driver.getelement('//div[text()="生命周期节点"]/following-sibling::div//tr[1]/td[1]//span').text
        if text=="11":
            raise AssertionError("点击下移生命周期节点，但是生命周期节点并未下移")
        self.click(设置页对象库.生命周期管理工作区.上移生命周期节点)
        text = self.driver.getelement('//div[text()="生命周期节点"]/following-sibling::div//tr[1]/td[1]//span').text
        if text != "11":
            raise AssertionError("点击上移生命周期节点，但是生命周期节点并未上移")

    def 编辑生命周期节点(self):
        self.进入到操作位置.进入生命周期工作区()
        self.生命周期管理页面.删除生命周期('test2')
        self.click(设置页对象库.生命周期管理工作区.新增)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新增生命周期"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test2")
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        #点击生命周期节点行的编辑按钮，生命周期行进入编辑状态
        self.click(设置页对象库.生命周期管理工作区.编辑生命周期节点按钮.format("11"))
        if not self.wait(设置页对象库.生命周期管理工作区.生命周期节点名称输入框,3) or not\
            self.wait(设置页对象库.生命周期管理工作区.生命周期节点描述输入框,3):
            raise AssertionError("点击编辑生命周期节点按钮，生命周期节点未进入编辑状态")
        #对节点名称进行超长校验、重名校验、空值校验
        # self.clear(设置页对象库.生命周期管理工作区.生命周期节点名称输入框)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框,Keys.CONTROL+'a')
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框,Keys.BACKSPACE)
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("节点名称不能为空"), 3):
            raise AssertionError("当生命周期节点名称为空时，点击保存可以保存生命周期节点成功！")
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框,'11')
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("节点名称不能重复"), 3):
            raise AssertionError("当生命周期节点名称重复时，点击保存未出现生命周期节点名称不能为空的提示！")
        # self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框,
        #                "123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456")
        # self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        # self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
        # if not self.wait(公共元素对象库.系统提示信息弹框.format("操作失败"), 3):
        #     raise AssertionError("当生命周期节点名称超长时，点击保存未出现生命周期节点名称过长的提示！")
        # #对输入内容进行空值校验和超长校验
        # self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        # self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "33")
        # self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点描述输入框.format(
        #     "123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789011"))
        # self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点描述输入框.format(
        #     "123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789011"))
        # self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        # if not self.wait(公共元素对象库.系统提示信息弹框.format("操作失败"), 3):
        #     raise AssertionError("当生命周期节点名称超长时，点击保存未出现生命周期节点描述过长的提示！")

    def 升版设置(self):
        self.进入到操作位置.进入生命周期工作区()
        self.生命周期管理页面.删除生命周期('test2')
        self.click(设置页对象库.生命周期管理工作区.新增)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新增生命周期"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test2")
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "33")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "44")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("22"))
        #点击生命周期节点，右侧节点流程显示当前节点与上级节点的流程和当前节点与下级节点的流程
        if not self.wait(设置页对象库.生命周期管理工作区.开始节点和结束节点.format("22","11"),3) or not \
            self.wait(设置页对象库.生命周期管理工作区.开始节点和结束节点.format("22","33"),3) or not \
            self.wait(设置页对象库.生命周期管理工作区.开始节点和结束节点.format("22","44"),3):
            raise AssertionError("点击查看节点流程，跨节点的节点流程显示不全")
        #不选择跨节点，右侧节点流程中不出现跨节点流程，选择跨节点，右侧节点流程出现跨节点流程
        self.click(公共元素对象库.单选按钮.format("是否跨节点"))
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("22"))
        if self.wait(设置页对象库.生命周期管理工作区.开始节点和结束节点.format("22","44"),3):
            raise AssertionError("点击查看节点流程，不勾选是否跨节点按钮，但是却显示跨节点流程")
        #生命周期中不设置升版流程，点击保存，提示没有选择升版流程
        self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("升版选项必须选择一位"),3):
            raise AssertionError("生命周期中没有勾选升版流程，点击保存，未出现对应的提示信息")
        #设置升版流程，项目生命周期经过此流程时，项目进行升版
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
        self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("11","22"))
        self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="升版测试")
        self.项目管理页面.创建空白项目(项目名称="升版测试",生命周期名称="test2")
        self.项目管理页面.点击进入项目(项目名称="升版测试")
        self.项目页面.上传单个文件(目录路径=['升版测试'], 文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'])
        self.项目页面.改变文件状态(目录路径=['升版测试'],文件名='检入检出素材.txt',状态名称='22')
        if not self.wait('//div[contains(@class,"pane-two")]//tr[1]/td[5]//span[text()="B"]',3):
            raise AssertionError("设置升版流程，项目生命周期经过此流程时，项目并没有进行升版")
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="升版测试")

    def 保存新增生命周期(self):
        self.进入到操作位置.进入生命周期工作区()
        self.生命周期管理页面.删除生命周期('test2')
        # 设置生命周期属性后，关闭新增生命周期界面，生命周期属性不能被保存
        self.click(设置页对象库.生命周期管理工作区.新增)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新增生命周期"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test2")
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
        self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("11", "22"))
        self.click(对话框对象库.关闭弹框.format("新增生命周期"))
        if self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format("test2"), 3):
            raise AssertionError("创建生命周期时关闭创建界面，被关闭的生命周期被保存")
        #设置生命周期属性后，新增生命周期界面点击取消，生命周期属性不能被保存
        self.click(设置页对象库.生命周期管理工作区.新增)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新增生命周期"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test2")
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
        self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("11", "22"))
        self.click(对话框对象库.弹框按钮.format("新增生命周期", "取消"))
        if self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format("test2"), 3):
            raise AssertionError("创建生命周期时点击取消，被取消的生命周期被保存")
        #设置生命周期属性后，新增生命周期界面点击确定，生命周期属性可以被保存
        self.click(设置页对象库.生命周期管理工作区.新增)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新增生命周期"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test2")
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
        self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("11", "22"))
        self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"),3)
        if not self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format("test2"), 3):
            raise AssertionError("创建生命周期时点击确定，生命周期未被保存")

    def 编辑生命周期(self):
        self.进入到操作位置.进入生命周期工作区()
        self.生命周期管理页面.删除生命周期('test2')
        self.click(设置页对象库.生命周期管理工作区.新增)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新增生命周期"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test2")
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
        self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("11", "22"))
        self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        if not self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format("test1"), 3):
            self.click(设置页对象库.生命周期管理工作区.新增)
            self.default_content()
            self.wait(对话框对象库.弹框标题.format("新增生命周期"), 3)
            self.send_keys(公共元素对象库.输入框.format("名称"), "test1")
            self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
            self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
            self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
            self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
            self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
            self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
            self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
            self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("11", "22"))
            self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
            self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        # 不选择任何生命周期，点击编辑，提示请选择需要修改的数据。
        self.driver.refrsh()
        self.click(设置页对象库.生命周期管理工作区.编辑)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("请选择需要修改的数据"),3):
            raise AssertionError("没有选择生命周期，点击编辑按钮，为出现提示信息")
        #选择生命周期后，点击编辑，进入编辑生命周期界面
        self.click(设置页对象库.生命周期管理工作区.生命周期名称.format("test2"))
        self.click(设置页对象库.生命周期管理工作区.编辑)
        if not self.wait(对话框对象库.弹框标题.format("编辑生命周期"), 3):
            raise AssertionError("选择生命周期后点击编辑，未弹出编辑生命周期的界面")
        #对生命周期名称进行空值、重名、超长校验
        # 空值校验
        self.click(公共元素对象库.输入框.format("名称"))
        self.send_keys(公共元素对象库.输入框.format("名称"),Keys.CONTROL + 'a')
        self.send_keys(公共元素对象库.输入框.format("名称"), Keys.BACKSPACE)
        self.click(对话框对象库.弹框按钮.format("编辑生命周期", "确定"))
        if not self.wait(公共元素对象库.输入框错误信息提示.format("名称不能为空"), 3):
            raise AssertionError("对生命周期名称进行空值校验，没有出现名称不能为空的提示信息")
        # 重名
        self.send_keys(公共元素对象库.输入框.format("名称"), "test1")
        self.click(对话框对象库.弹框按钮.format("编辑生命周期", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("存在同名模板"), 3):
            raise AssertionError("生命周期可以重名创建")
        # # 超长校验
        # self.clear(公共元素对象库.输入框.format("名称"))
        # self.send_keys(公共元素对象库.输入框.format("名称"), "123456789012345678901234567890123456789012345612345678907890")
        # self.click(对话框对象库.弹框按钮.format("编辑生命周期", "确定"))
        # if not self.wait(公共元素对象库.系统提示信息弹框.format("操作失败"), 3):
        #     raise AssertionError("生命周期名称超长是，系统未给出对应的提示信息")

    def 编辑生命周期界面生命周期节点管理(self):
        self.进入到操作位置.进入生命周期工作区()
        self.生命周期管理页面.删除生命周期('test2')
        self.生命周期管理页面.删除生命周期('test1')
        self.click(设置页对象库.生命周期管理工作区.新增)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新增生命周期"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test2")
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "33")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
        self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("11", "22"))
        self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        self.click(设置页对象库.生命周期管理工作区.新增)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新增生命周期"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test1")
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
        self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("11", "22"))
        self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        #点击新增生命周期节点，生命周期节点列表中新增一行空白生命周期节点
        self.click(设置页对象库.生命周期管理工作区.生命周期名称.format("test2"))
        self.click(设置页对象库.生命周期管理工作区.编辑)
        self.wait(对话框对象库.弹框标题.format("编辑生命周期"), 3)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        if not self.wait(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, 3):
            raise AssertionError("点击添加生命周期节点按钮，未添加新的生命周期节点")
        # 对节点名称进行超长校验、重名校验、空值校验
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("节点名称不能为空"), 3):
            raise AssertionError("当生命周期节点名称为空时，点击保存可以保存生命周期节点成功！")
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("节点名称不能重复"), 3):
            raise AssertionError("当生命周期节点名称重复时，点击保存未出现生命周期节点名称不能为空的提示！")
        # self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框,
        #                "123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456")
        # self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        # if not self.wait(公共元素对象库.系统提示信息弹框.format("未知错误"), 3):
        #     raise AssertionError("当生命周期节点名称超长时，点击保存未出现生命周期节点名称过长的提示！")
        # 对输入内容进行空值校验和超长校验
        # self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        # self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
        # self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点描述输入框.format(
        #     "123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456"))
        # self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        # if not self.wait(公共元素对象库.系统提示信息弹框.format("未知错误"), 3):
        #     raise AssertionError("当生命周期节点名称超长时，点击保存未出现生命周期节点描述过长的提示！")
        # 点击生命周期节点行，点击删除按钮，生命周期行被删除
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("33"))
        self.click(设置页对象库.生命周期管理工作区.删除生命周期节点)
        if self.wait(设置页对象库.生命周期管理工作区.生命周期节点名称.format("33"), 3):
            raise AssertionError("进行删除生命周期节点操作后，在生命周期节点列表仍然能查看到被删除的生命周期节点")
        # 点击生命周期节点行，点击上移按钮，节点行上移一行，点击下移按钮，节点行下移一行
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
        self.click(设置页对象库.生命周期管理工作区.下移生命周期节点)
        text = self.driver.getelement('//div[text()="生命周期节点"]/following-sibling::div//tr[1]/td[1]//span').text
        if text == "11":
            raise AssertionError("点击下移生命周期节点，但是生命周期节点并未下移")
        self.click(设置页对象库.生命周期管理工作区.上移生命周期节点)
        text = self.driver.getelement('//div[text()="生命周期节点"]/following-sibling::div//tr[1]/td[1]//span').text
        if text != "11":
            raise AssertionError("点击上移生命周期节点，但是生命周期节点并未上移")

    def 编辑生命周期界面编辑生命周期节点(self):
        self.进入到操作位置.进入生命周期工作区()
        self.生命周期管理页面.删除生命周期('test2')
        self.click(设置页对象库.生命周期管理工作区.新增)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新增生命周期"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test2")
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
        self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("11", "22"))
        self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        self.click(设置页对象库.生命周期管理工作区.生命周期名称.format("test2"))
        self.click(设置页对象库.生命周期管理工作区.编辑)
        self.wait(对话框对象库.弹框标题.format("编辑生命周期"), 3)
        # 点击生命周期节点行的编辑按钮，生命周期行进入编辑状态
        self.click(设置页对象库.生命周期管理工作区.编辑生命周期节点按钮.format("11"))
        if not self.wait(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, 3) or not \
                self.wait(设置页对象库.生命周期管理工作区.生命周期节点描述输入框, 3):
            raise AssertionError("点击编辑生命周期节点按钮，生命周期节点未进入编辑状态")
        # 对节点名称进行超长校验、重名校验、空值校验
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, Keys.CONTROL + 'a')
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, Keys.BACKSPACE)
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮2)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("节点名称不能为空"), 3):
            raise AssertionError("当生命周期节点名称为空时，点击保存可以保存生命周期节点成功！")
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮2)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("节点名称不能重复"), 3):
            raise AssertionError("当生命周期节点名称重复时，点击保存未出现生命周期节点名称不能为空的提示！")
        # self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框,
        #                "123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456")
        # self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        # if not self.wait(公共元素对象库.系统提示信息弹框.format("未知错误"), 3):
        #     raise AssertionError("当生命周期节点名称超长时，点击保存未出现生命周期节点名称过长的提示！")
        # 对输入内容进行空值校验和超长校验
        # self.clear(设置页对象库.生命周期管理工作区.生命周期节点名称输入框)
        # self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "33")
        # self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点描述输入框.format(
        #     "123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456"))
        # self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        # if not self.wait(公共元素对象库.系统提示信息弹框.format("未知错误"), 3):
        #     raise AssertionError("当生命周期节点名称超长时，点击保存未出现生命周期节点描述过长的提示！")

    def 编辑生命周期界面编辑升版流程(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="升版测试")
        self.进入到操作位置.进入生命周期工作区()
        self.生命周期管理页面.删除生命周期('test3')
        self.click(设置页对象库.生命周期管理工作区.新增)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新增生命周期"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test3")
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "33")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "44")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
        self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("11", "22"))
        self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
        self.click(设置页对象库.生命周期管理工作区.生命周期名称.format("test3"))
        self.click(设置页对象库.生命周期管理工作区.编辑)
        self.wait(对话框对象库.弹框标题.format("编辑生命周期"), 3)
        # 不选择跨节点，右侧节点流程中不出现跨节点流程，选择跨节点，右侧节点流程出现跨节点流程
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("22"))
        if not self.wait(设置页对象库.生命周期管理工作区.开始节点和结束节点.format("22", "11"), 3) or not \
                self.wait(设置页对象库.生命周期管理工作区.开始节点和结束节点.format("22", "33"), 3) or not \
                self.wait(设置页对象库.生命周期管理工作区.开始节点和结束节点.format("22", "44"), 3):
            raise AssertionError("点击查看节点流程，跨节点的节点流程显示不全")
        self.click(公共元素对象库.单选按钮.format("是否跨节点"))
        if self.wait(设置页对象库.生命周期管理工作区.开始节点和结束节点.format("22", "44"), 3):
            raise AssertionError("点击查看节点流程，不勾选是否跨节点按钮，但是却显示跨节点流程")
        # # 设置升版流程，项目生命周期经过此流程时，项目进行升版
        # self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
        # self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("11", "22"))
        self.click(对话框对象库.弹框按钮.format("编辑生命周期", "取消"))
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.创建空白项目(项目名称="升版测试", 生命周期名称="test3")
        self.项目管理页面.点击进入项目(项目名称="升版测试")
        self.项目页面.上传单个文件(目录路径=['升版测试'], 文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'])
        self.项目页面.改变文件状态(目录路径=['升版测试'], 文件名='检入检出素材.txt', 状态名称='22')
        if not self.wait('//div[contains(@class,"pane-two")]//tr[1]/td[5]//span[text()="B"]', 3):
            raise AssertionError("设置升版流程，项目生命周期经过此流程时，项目并没有进行升版")
        #如果生命周期已经被使用，再编辑升版流程，系统会给出对应的提示
        self.进入到操作位置.进入生命周期工作区()
        self.click(设置页对象库.生命周期管理工作区.生命周期名称.format("test3"))
        self.click(设置页对象库.生命周期管理工作区.编辑)
        self.wait(对话框对象库.弹框标题.format("编辑生命周期"), 3)
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
        self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("11", "44"))
        self.click(对话框对象库.弹框按钮.format("编辑生命周期", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("生命周期模版已被使用，不可修改！"),3):
            raise AssertionError("生命周期已经被使用，再编辑升版流程，系统会未给出对应的提示")

    def 编辑生命周期界面保存生命周期(self):
        self.进入到操作位置.进入生命周期工作区()
        self.生命周期管理页面.删除生命周期('test4')
        self.click(设置页对象库.生命周期管理工作区.新增)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新增生命周期"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test4")
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
        self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("11", "22"))
        self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        self.click(设置页对象库.生命周期管理工作区.生命周期名称.format("test4"))
        self.click(设置页对象库.生命周期管理工作区.编辑)
        self.wait(对话框对象库.弹框标题.format("编辑生命周期"), 3)
        # 设置生命周期属性后，关闭新增生命周期界面，生命周期属性不能被保存
        self.clear(公共元素对象库.输入框.format("名称"))
        self.send_keys(公共元素对象库.输入框.format("名称"), "test41")
        self.click(对话框对象库.关闭弹框.format("编辑生命周期"))
        if self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format("test41"), 3):
            raise AssertionError("创建生命周期时关闭创建界面，被关闭的生命周期被保存")
        # 设置生命周期属性后，新增生命周期界面点击取消，生命周期属性不能被保存
        self.click(设置页对象库.生命周期管理工作区.编辑)
        self.wait(对话框对象库.弹框标题.format("编辑生命周期"), 3)
        self.clear(公共元素对象库.输入框.format("名称"))
        self.send_keys(公共元素对象库.输入框.format("名称"), "test41")
        self.click(对话框对象库.弹框按钮.format("编辑生命周期", "取消"))
        if self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format("test41"), 3):
            raise AssertionError("创建生命周期时点击取消，被取消的生命周期被保存")
        # 设置生命周期属性后，新增生命周期界面点击确定，生命周期属性可以被保存
        self.click(设置页对象库.生命周期管理工作区.编辑)
        self.wait(对话框对象库.弹框标题.format("编辑生命周期"), 3)
        self.clear(公共元素对象库.输入框.format("名称"))
        self.send_keys(公共元素对象库.输入框.format("名称"), "test41")
        self.click(对话框对象库.弹框按钮.format("编辑生命周期", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        if not self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format("test41"), 3):
            raise AssertionError("创建生命周期时点击确定，生命周期未被保存")

    def 复制生命周期(self):
        self.进入到操作位置.进入生命周期工作区()
        self.生命周期管理页面.删除生命周期('test5')
        self.click(设置页对象库.生命周期管理工作区.新增)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新增生命周期"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test5")
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "33")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "44")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
        self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("11", "22"))
        self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
        #不选择生命周期，点击复制，系统给出对应的提示信息
        self.driver.refrsh()
        self.click(设置页对象库.生命周期管理工作区.复制)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("请选择需要复制的数据"),3):
            raise AssertionError("未选择生命周期点击复制，系统未给出相应的提示信息")
        #择生命周期后，点击复制，进入复制生命周期界面
        self.click(设置页对象库.生命周期管理工作区.生命周期名称.format("test5"))
        self.click(设置页对象库.生命周期管理工作区.复制)
        if not self.wait(对话框对象库.弹框标题.format("复制生命周期"), 3):
            raise AssertionError("选择生命周期后点击复制，未弹出复制生命周期界面")
        #对生命周期名称进行空值、重名、超长校验
        # 空值校验
        self.send_keys(公共元素对象库.输入框.format("名称"), Keys.CONTROL + 'a')
        self.send_keys(公共元素对象库.输入框.format("名称"), Keys.BACKSPACE)
        self.click(对话框对象库.弹框按钮.format("复制生命周期", "确定"))
        if not self.wait(公共元素对象库.输入框错误信息提示.format("名称不能为空"), 3):
            raise AssertionError("对生命周期名称进行空值校验，没有出现名称不能为空的提示信息")
        # 重名
        self.clear(公共元素对象库.输入框.format("名称"))
        self.send_keys(公共元素对象库.输入框.format("名称"), "test5")
        self.click(对话框对象库.弹框按钮.format("复制生命周期", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("存在同名模板"), 3):
            raise AssertionError("生命周期可以重名创建")
        # 超长校验
        # self.clear(公共元素对象库.输入框.format("名称"))
        # self.send_keys(公共元素对象库.输入框.format("名称"), "123456789012345678901234567890123456789012345612345678907890")
        # self.click(对话框对象库.弹框按钮.format("复制生命周期", "确定"))
        # if not self.wait(公共元素对象库.系统提示信息弹框.format("参数检验失败"), 3):
        #     raise AssertionError("生命周期名称超长是，系统未给出对应的提示信息")
        #复制生命周期界面，编辑生命周期名称，点击确定，可以复制成功
        self.clear(公共元素对象库.输入框.format("名称"))
        self.send_keys(公共元素对象库.输入框.format("名称"), "test51")
        self.click(对话框对象库.弹框按钮.format("复制生命周期", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"),3)
        if not self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format("test51"),3):
            raise AssertionError("在复制生命周期界面，编辑生命周期名称后点击复制，没有复制成功")

    def 复制生命周期界面生命周期节点管理(self):
        self.进入到操作位置.进入生命周期工作区()
        self.生命周期管理页面.删除生命周期('test5')
        self.click(设置页对象库.生命周期管理工作区.新增)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新增生命周期"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test5")
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "33")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
        self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("11", "22"))
        self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        # 点击新增生命周期节点，生命周期节点列表中新增一行空白生命周期节点
        self.click(设置页对象库.生命周期管理工作区.生命周期名称.format("test5"))
        self.click(设置页对象库.生命周期管理工作区.复制)
        self.wait(对话框对象库.弹框标题.format("复制生命周期"), 3)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        if not self.wait(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, 3):
            raise AssertionError("点击添加生命周期节点按钮，未添加新的生命周期节点")
        # 对节点名称进行超长校验、重名校验、空值校验
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("节点名称不能为空"), 3):
            raise AssertionError("当生命周期节点名称为空时，点击保存可以保存生命周期节点成功！")
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("节点名称不能重复"), 3):
            raise AssertionError("当生命周期节点名称重复时，点击保存未出现生命周期节点名称不能为空的提示！")
        # self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框,
        #                "123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456")
        # self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        # if not self.wait(公共元素对象库.系统提示信息弹框.format("未知错误"), 3):
        #     raise AssertionError("当生命周期节点名称超长时，点击保存未出现生命周期节点名称过长的提示！")
        # 对输入内容进行空值校验和超长校验
        # self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        # self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
        # self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点描述输入框.format(
        #     "123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456"))
        # self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        # if not self.wait(公共元素对象库.系统提示信息弹框.format("未知错误"), 3):
        #     raise AssertionError("当生命周期节点名称超长时，点击保存未出现生命周期节点描述过长的提示！")
        # 点击生命周期节点行，点击删除按钮，生命周期行被删除
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("33"))
        self.click(设置页对象库.生命周期管理工作区.删除生命周期节点)
        if self.wait(设置页对象库.生命周期管理工作区.生命周期节点名称.format("33"), 3):
            raise AssertionError("进行删除生命周期节点操作后，在生命周期节点列表仍然能查看到被删除的生命周期节点")
        # 点击生命周期节点行，点击上移按钮，节点行上移一行，点击下移按钮，节点行下移一行
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
        self.click(设置页对象库.生命周期管理工作区.下移生命周期节点)
        text = self.driver.getelement('//div[text()="生命周期节点"]/following-sibling::div//tr[1]/td[1]//span').text
        if text == "11":
            raise AssertionError("点击下移生命周期节点，但是生命周期节点并未下移")
        self.click(设置页对象库.生命周期管理工作区.上移生命周期节点)
        text = self.driver.getelement('//div[text()="生命周期节点"]/following-sibling::div//tr[1]/td[1]//span').text
        if text != "11":
            raise AssertionError("点击上移生命周期节点，但是生命周期节点并未上移")

    def 复制生命周期界面编辑生命周期节点(self):
        self.进入到操作位置.进入生命周期工作区()
        self.生命周期管理页面.删除生命周期('test5')
        self.click(设置页对象库.生命周期管理工作区.新增)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新增生命周期"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test5")
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
        self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("11", "22"))
        self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        self.click(设置页对象库.生命周期管理工作区.生命周期名称.format("test5"))
        self.click(设置页对象库.生命周期管理工作区.复制)
        self.wait(对话框对象库.弹框标题.format("复制生命周期"), 3)
        # 点击生命周期节点行的编辑按钮，生命周期行进入编辑状态
        self.click(设置页对象库.生命周期管理工作区.编辑生命周期节点按钮.format("11"))
        if not self.wait(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, 3) or not \
                self.wait(设置页对象库.生命周期管理工作区.生命周期节点描述输入框, 3):
            raise AssertionError("点击编辑生命周期节点按钮，生命周期节点未进入编辑状态")
        # 对节点名称进行超长校验、重名校验、空值校验
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, Keys.CONTROL + 'a')
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, Keys.BACKSPACE)
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮2)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("节点名称不能为空"), 3):
            raise AssertionError("当生命周期节点名称为空时，点击保存可以保存生命周期节点成功！")
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮2)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("节点名称不能重复"), 3):
            raise AssertionError("当生命周期节点名称重复时，点击保存未出现生命周期节点名称不能为空的提示！")
        # self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框,
        #                "123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456")
        # self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        # if not self.wait(公共元素对象库.系统提示信息弹框.format("未知错误"), 3):
        #     raise AssertionError("当生命周期节点名称超长时，点击保存未出现生命周期节点名称过长的提示！")
        # # 对输入内容进行空值校验和超长校验
        # self.clear(设置页对象库.生命周期管理工作区.生命周期节点名称输入框)
        # self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "33")
        # self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点描述输入框.format(
        #     "123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456"))
        # self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        # if not self.wait(公共元素对象库.系统提示信息弹框.format("未知错误"), 3):
        #     raise AssertionError("当生命周期节点名称超长时，点击保存未出现生命周期节点描述过长的提示！")

    def 复制生命周期界面编辑升版流程(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="升版测试")
        self.进入到操作位置.进入生命周期工作区()
        self.生命周期管理页面.删除生命周期('test6')
        self.click(设置页对象库.生命周期管理工作区.新增)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新增生命周期"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test6")
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "33")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "44")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
        self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("11", "22"))
        self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
        self.click(设置页对象库.生命周期管理工作区.生命周期名称.format("test6"))
        self.click(设置页对象库.生命周期管理工作区.复制)
        self.wait(对话框对象库.弹框标题.format("复制生命周期"), 3)
        # 不选择跨节点，右侧节点流程中不出现跨节点流程，选择跨节点，右侧节点流程出现跨节点流程
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("22"))
        if not self.wait(设置页对象库.生命周期管理工作区.开始节点和结束节点.format("22", "11"), 3) or not \
                self.wait(设置页对象库.生命周期管理工作区.开始节点和结束节点.format("22", "33"), 3) or not \
                self.wait(设置页对象库.生命周期管理工作区.开始节点和结束节点.format("22", "44"), 3):
            raise AssertionError("点击查看节点流程，跨节点的节点流程显示不全")
        self.click(公共元素对象库.单选按钮.format("是否跨节点"))
        if self.wait(设置页对象库.生命周期管理工作区.开始节点和结束节点.format("22", "44"), 3):
            raise AssertionError("点击查看节点流程，不勾选是否跨节点按钮，但是却显示跨节点流程")
        # 设置升版流程，项目生命周期经过此流程时，项目进行升版
        self.click(对话框对象库.弹框按钮.format("复制生命周期", "取消"))
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.创建空白项目(项目名称="升版测试", 生命周期名称="test6")
        self.项目管理页面.点击进入项目(项目名称="升版测试")
        self.项目页面.上传单个文件(目录路径=['升版测试'], 文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'])
        self.项目页面.改变文件状态(目录路径=['升版测试'], 文件名='检入检出素材.txt', 状态名称='22')
        if not self.wait('//div[contains(@class,"pane-two")]//tr[1]/td[5]//span[text()="B"]', 3):
            raise AssertionError("设置升版流程，项目生命周期经过此流程时，项目并没有进行升版")
        # 如果生命周期已经被使用，再编辑升版流程，系统会给出对应的提示
        self.进入到操作位置.进入生命周期工作区()
        self.click(设置页对象库.生命周期管理工作区.生命周期名称.format("test6"))
        self.click(设置页对象库.生命周期管理工作区.编辑)
        self.wait(对话框对象库.弹框标题.format("编辑生命周期"), 3)
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
        self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("11", "44"))
        self.click(对话框对象库.弹框按钮.format("编辑生命周期", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("生命周期模版已被使用，不可修改！"), 3):
            raise AssertionError("生命周期已经被使用，再编辑升版流程，系统会未给出对应的提示")

    def 复制生命周期界面保存生命周期(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="升版测试")
        self.项目管理页面.删除项目(项目名称="系统默认生命周期")
        self.进入到操作位置.进入生命周期工作区()
        self.生命周期管理页面.删除生命周期('test7')
        self.click(设置页对象库.生命周期管理工作区.新增)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新增生命周期"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test7")
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
        self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("11", "22"))
        self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        self.click(设置页对象库.生命周期管理工作区.生命周期名称.format("test7"))
        self.click(设置页对象库.生命周期管理工作区.复制)
        self.wait(对话框对象库.弹框标题.format("复制生命周期"), 3)
        # 设置生命周期属性后，关闭新增生命周期界面，生命周期属性不能被保存
        self.clear(公共元素对象库.输入框.format("名称"))
        self.send_keys(公共元素对象库.输入框.format("名称"), "test71")
        self.click(对话框对象库.关闭弹框.format("复制生命周期"))
        if self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format("test71"), 3):
            raise AssertionError("复制生命周期时关闭创建界面，被关闭的生命周期被保存")
        # 设置生命周期属性后，新增生命周期界面点击取消，生命周期属性不能被保存
        self.click(设置页对象库.生命周期管理工作区.复制)
        self.wait(对话框对象库.弹框标题.format("复制生命周期"), 3)
        self.clear(公共元素对象库.输入框.format("名称"))
        self.send_keys(公共元素对象库.输入框.format("名称"), "test71")
        self.click(对话框对象库.弹框按钮.format("复制生命周期", "取消"))
        if self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format("test71"), 3):
            raise AssertionError("复制生命周期时点击取消，被取消的生命周期被保存")
        # 设置生命周期属性后，新增生命周期界面点击确定，生命周期属性可以被保存
        self.click(设置页对象库.生命周期管理工作区.复制)
        self.wait(对话框对象库.弹框标题.format("复制生命周期"), 3)
        self.clear(公共元素对象库.输入框.format("名称"))
        self.send_keys(公共元素对象库.输入框.format("名称"), "test71")
        self.click(对话框对象库.弹框按钮.format("复制生命周期", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        if not self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format("test71"), 3):
            raise AssertionError("复制生命周期时点击确定，生命周期未被保存")

    def 删除单个生命周期(self):
        self.进入到操作位置.进入生命周期工作区()
        if not self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format("delete1"), 3):
            self.click(设置页对象库.生命周期管理工作区.新增)
            self.default_content()
            self.wait(对话框对象库.弹框标题.format("新增生命周期"), 3)
            self.send_keys(公共元素对象库.输入框.format("名称"), "delete1")
            self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
            self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
            self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
            self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
            self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
            self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
            self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
            self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("11", "22"))
            self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
            self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        #不选择生命周期，点击删除，系统给出对应提示
        self.driver.refrsh()
        self.click(设置页对象库.生命周期管理工作区.删除)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("未选中需要删除的数据"), 3):
            raise AssertionError("不选择生命周期，点击删除，未出现对应的提示信息")
        #勾选单个生命周期，点击删除，弹出删除提示对话框
        self.click(设置页对象库.生命周期管理工作区.生命周期列表复选框.format("delete1"))
        self.click(设置页对象库.生命周期管理工作区.删除)
        if not self.wait(对话框对象库.对话框标题.format("提示"),3):
            raise AssertionError("勾选单个生命周期，点击删除，系统未弹出删除确认对话框")
        #关闭删除提示对话框，查看生命周期是否被删除
        self.click(对话框对象库.关闭对话框.format("提示"))
        if not self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format("delete1"), 3):
            raise AssertionError("点击关闭删除确认对话框，被选择的生命周期被删除")
        #点击取消删除提示对话框，查看生命周期是否被删除
        self.click(设置页对象库.生命周期管理工作区.删除)
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示","取消"))
        if not self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format("delete1"), 3):
            raise AssertionError("点击取消删除确认对话框，被选择的生命周期被删除")
        #点击确定删除提示对话框，查看生命周期是否被删除
        self.click(设置页对象库.生命周期管理工作区.删除)
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示","确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("删除成功"),3)
        if self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format("delete1"), 3):
            raise AssertionError("点击确定删除确认对话框，被选择的生命周期未被删除")

    def 批量删除生命周期(self):
        self.进入到操作位置.进入生命周期工作区()
        if not self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format("delete1"), 3):
            self.click(设置页对象库.生命周期管理工作区.新增)
            self.default_content()
            self.wait(对话框对象库.弹框标题.format("新增生命周期"), 3)
            self.send_keys(公共元素对象库.输入框.format("名称"), "delete1")
            self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
            self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
            self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
            self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
            self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
            self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
            self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
            self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("11", "22"))
            self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
            self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        if not self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format("delete2"), 3):
            self.click(设置页对象库.生命周期管理工作区.新增)
            self.default_content()
            self.wait(对话框对象库.弹框标题.format("新增生命周期"), 3)
            self.send_keys(公共元素对象库.输入框.format("名称"), "delete2")
            self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
            self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
            self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
            self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
            self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
            self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
            self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
            self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("11", "22"))
            self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
            self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        #勾选多个生命周期，点击删除，弹出删除提示对话框
        self.click(设置页对象库.生命周期管理工作区.生命周期列表复选框.format("delete1"))
        self.click(设置页对象库.生命周期管理工作区.生命周期列表复选框.format("delete2"))
        self.click(设置页对象库.生命周期管理工作区.删除)
        if not self.wait(对话框对象库.对话框标题.format("提示"), 3):
            raise AssertionError("勾选多个生命周期，点击删除，系统未弹出删除确认对话框")
        #关闭删除提示对话框，查看生命周期是否被删除
        self.click(对话框对象库.关闭对话框.format("提示"))
        if not self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format("delete1"), 3) or\
                not self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format("delete2"), 3):
            raise AssertionError("点击关闭删除确认对话框，被选择的生命周期被删除")
        #点击取消删除提示对话框，查看生命周期是否被删除
        self.click(设置页对象库.生命周期管理工作区.删除)
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示","取消"))
        if not self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format("delete1"), 3)or\
                not self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format("delete2"), 3):
            raise AssertionError("点击取消删除确认对话框，被选择的生命周期被删除")
        #当勾选的生命周期中含有系统生命周期时，删除按钮不可用
        self.click(设置页对象库.生命周期管理工作区.生命周期列表复选框.format("系统默认生命周期"))
        if not self.wait('//div[@class="life_cycle_btns comm_bgc"]//button[@disabled="disabled"]/span[text()="删除"]',3):
            raise AssertionError("当勾选的生命周期中含有系统生命周期时，删除按钮应该不可用")
        #点击确定删除提示对话框，查看生命周期是否被删除
        self.driver.refrsh()
        self.click(设置页对象库.生命周期管理工作区.生命周期列表复选框.format("delete1"))
        self.click(设置页对象库.生命周期管理工作区.生命周期列表复选框.format("delete2"))
        self.click(设置页对象库.生命周期管理工作区.删除)
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示","确定"))
        if self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format("delete1"), 3) or \
                self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format("delete2"), 3):
            raise AssertionError("点击确认删除确认对话框，被选择的生命周期未被删除")

    def 设置默认生命周期(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="升版测试")
        self.项目管理页面.删除项目(项目名称="系统默认生命周期")
        self.进入到操作位置.进入生命周期工作区()
        self.生命周期管理页面.删除生命周期('test7')
        self.click(设置页对象库.生命周期管理工作区.新增)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新增生命周期"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test7")
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
        self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("11", "22"))
        self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        #点击生命周期列表中的生命周期，生命周期节点列表显示改生命周期下的生命周期节点
        self.click(设置页对象库.生命周期管理工作区.生命周期名称.format("test7"))
        if not self.wait(设置页对象库.生命周期管理工作区.生命周期节点.format("11"),3) or \
            not self.wait(设置页对象库.生命周期管理工作区.生命周期节点.format("22"),3):
            raise AssertionError("点击生命周期，在生命周期明细中并未查看到生命周期下的所有节点")
        #点击对应的生命周期节点，节点流程列表显示该节点对应的节点流程
        self.click(设置页对象库.生命周期管理工作区.生命周期节点.format("11"))
        if not self.wait(设置页对象库.生命周期管理工作区.节点流程.format("11","22"),3):
            raise AssertionError("点击生命周期节点，节点流程列表未显示该节点下的节点流程")
        #勾选生命周期列表，生命周期行的是否默认单选按钮，设置对应的生命周期为默认生命周期
        self.click(设置页对象库.生命周期管理工作区.设置默认单选框.format("test7"))
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="默认生命周期")
        self.click(项目管理对象库.创建新项目)
        self.wait(创建项目页面.页面名称, 3)
        self.click(创建项目页面.创建空白项目)
        self.wait(对话框对象库.弹框标题.format("项目名称"), 3)
        self.clear(公共元素对象库.输入框.format("项目名称"))
        self.send_keys(公共元素对象库.输入框.format("项目名称"), "默认生命周期")
        self.click(创建项目页面.提交按钮)
        self.default_content()
        self.wait(项目设置页面.项目成员tab页, 3)
        self.click(公共元素对象库.列表框.format("生命周期"))
        if not self.wait('//ul/li[contains(@class,"dropdown__item selected")]/span[text()="test7"]',3):
            raise AssertionError("设置test7未默认生命周期，创建新项目，项目的生命周期未默认选择test7")


class 版次管理工作区(page):
    def __init__(self,Secdriver = None):
        page.__init__(self,secdriver=Secdriver)
        self.滑块验证=滑块验证(Secdriver=Secdriver)
        self.公共操作 = 公共操作(Secdriver=Secdriver)
        self.版次管理页面 = 版次管理页面(Secdriver=Secdriver)
        self.项目页面 = 项目页面(Secdriver=Secdriver)
        self.用户信息页面 = 用户信息页面(Secdriver=Secdriver)
        self.项目管理页面 = 项目管理页面(Secdriver=Secdriver)
        self.进入到操作位置 = 进入到操作位置(Secdriver=Secdriver)

    def 数据准备(self):
        self.项目管理页面.删除所有项目()
        self.进入到操作位置.进入版次工作区()
        self.版次管理页面.删除所有版次()

    def 新增版次(self):
        self.进入到操作位置.进入版次工作区()
        self.版次管理页面.删除版次(版次名称='test')
        # 点击新增按钮，出现新增版次界面
        self.click(设置页对象库.版次管理工作区.新增)
        if not self.wait(对话框对象库.弹框标题.format("新增"), 3):
            raise AssertionError("点击新增版次，未弹出新增版次界面")
        # 对版次名称进行空值、超长、重名校验
        #空值
        self.click(对话框对象库.弹框按钮.format("新增", "确定"))
        if not self.wait(公共元素对象库.输入框错误信息提示.format("名称不能为空"),3):
            raise AssertionError("版次名称为空，点击保存系统未给出对应的提示信息")
        #超长
        self.send_keys(公共元素对象库.输入框.format("名称"),"12345678901234567890123456789012345678901234561234567890789012345612345678907890")
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框,"C")
        time.sleep(3)
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        self.click(对话框对象库.弹框按钮.format("新增", "确定"))
        if not self.wait(公共元素对象库.输入框错误信息提示.format("名称不能超过50个字"),3):
            raise AssertionError("版次名称超长是点击保存，系统未给出对应的提示信息")
        #重名
        self.clear(公共元素对象库.输入框.format("名称"))
        self.send_keys(公共元素对象库.输入框.format("名称"), "test")
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框,"A")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        self.click(对话框对象库.弹框按钮.format("新增", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"))
        self.click(设置页对象库.版次管理工作区.新增)
        self.wait(对话框对象库.弹框标题.format("新增"), 3)
        self.click(公共元素对象库.输入框.format("名称"))
        self.send_keys(公共元素对象库.输入框.format("名称"), "test")
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "A")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        self.click(对话框对象库.弹框按钮.format("新增", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("版次定义名称已经存在"),3):
            raise AssertionError("当创建的版次名称重复时，系统未给出对应的提示信息")

    def 新增版次界面版次节点管理(self):
        self.进入到操作位置.进入版次工作区()
        self.版次管理页面.删除版次(版次名称='test')
        self.click(设置页对象库.版次管理工作区.新增)
        self.wait(对话框对象库.弹框标题.format("新增"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test")
        #点击新增版次按钮，版次节点列表新增一行版次
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        if not self.wait(设置页对象库.版次管理工作区.版次内容输入框,3):
            raise AssertionError("点击新增版次节点按钮，未查看到新增的一行版次节点")
        #对版次内容进行空值，超长，重名校验
        #空值
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("版次不可为空"),3):
            raise AssertionError("版次节点为空时，点击保存版次节点，没有查看到提示信息")
        #重名
        self.clear(设置页对象库.版次管理工作区.版次内容输入框)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "A")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        self.wait(设置页对象库.版次管理工作区.版次内容输入框, 3)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "A")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        self.click(对话框对象库.弹框按钮.format("新增", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("版次定义详情内容不能重复"), 3):
            raise AssertionError("当创建的版次节点名称重复时，系统未给出对应的提示信息")
        #点击版次节点行，点击删除按钮，版次行被删除
        self.click(设置页对象库.版次管理工作区.版次内容.format("A"))
        self.click(设置页对象库.版次管理工作区.删除版次节点)
        版次=self.driver.getelements(设置页对象库.版次管理工作区.版次内容.format("A"))
        if len(版次)!=1:
            raise AssertionError("选择版次节点后点击删除，版次节点没有被删除")
        #第一行节点不能上移，最后一行节点不能下移
        # self.click(设置页对象库.版次管理工作区.版次内容.format("A"))
        # if not self.wait(设置页对象库.版次管理工作区.置灰_上移版次节点,3) or not self.wait(设置页对象库.版次管理工作区.置灰_下移版次节点,3):
        #     raise AssertionError("第一行可以上移，最后一行可以下移")
        #点击版次节点行，点击上移按钮，节点行上移一行，点击下移按钮，节点行下移一行
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        self.wait(设置页对象库.版次管理工作区.版次内容输入框, 3)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "B")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        self.click(设置页对象库.版次管理工作区.版次内容.format("A"))
        self.click(设置页对象库.版次管理工作区.下移版次节点)
        index1=self.driver.getelement('//tr/td//span[text()="A"]/ancestor::tr/td[1]/div/div').text
        if index1=='1':
            raise AssertionError("对版次节点进行下移操作，版次节点并未下移")
        self.click(设置页对象库.版次管理工作区.版次内容.format("A"))
        self.click(设置页对象库.版次管理工作区.上移版次节点)
        index1 = self.driver.getelement('//tr/td//span[text()="A"]/ancestor::tr/td[1]/div/div').text
        if index1 != '1':
            raise AssertionError("对版次节点进行上移操作，版次节点并未上移")
        #不保存节点，点击保存，系统给出对应提示
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        self.wait(设置页对象库.版次管理工作区.版次内容输入框, 3)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "C")
        self.click(对话框对象库.弹框按钮.format("新增", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("添加的版次未保存"),3):
            raise AssertionError("不保存版次节点，点击保存版次，系统未给出版次未保存的提示信息")

    def 新增版次界面编辑版次节点(self):
        self.进入到操作位置.进入版次工作区()
        self.版次管理页面.删除版次(版次名称='test')
        self.click(设置页对象库.版次管理工作区.新增)
        self.wait(对话框对象库.弹框标题.format("新增"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test")
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        self.wait(设置页对象库.版次管理工作区.版次内容输入框, 3)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "A")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        #点击版次节点行编辑按钮，版次节点行进入编辑状态
        self.click(设置页对象库.版次管理工作区.编辑版次节点按钮.format("A"))
        if not self.wait(设置页对象库.版次管理工作区.版次内容输入框, 3):
            raise AssertionError("点击版次节点编辑按钮，版次节点未进入编辑状态")
        #对版次内容进行空值，超长，重名校验
        # 空值
        self.clear_by_key(设置页对象库.版次管理工作区.版次内容输入框)
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("版次不可为空"), 3):
            raise AssertionError("版次节点为空时，点击保存版次节点，没有查看到提示信息")
        # 重名
        self.clear(设置页对象库.版次管理工作区.版次内容输入框)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "A")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        self.wait(设置页对象库.版次管理工作区.版次内容输入框, 3)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "A")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        self.click(对话框对象库.弹框按钮.format("新增", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("版次定义详情内容不能重复"), 3):
            raise AssertionError("当创建的版次节点名称重复时，系统未给出对应的提示信息")

    def 新增版次界面保存版次(self):
        self.进入到操作位置.进入版次工作区()
        self.版次管理页面.删除版次(版次名称='test')
        self.click(设置页对象库.版次管理工作区.新增)
        self.wait(对话框对象库.弹框标题.format("新增"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test")
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        self.wait(设置页对象库.版次管理工作区.版次内容输入框, 3)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "A")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        #设置版次属性后，关闭新增版次界面，版次属性不能被保存
        self.click(对话框对象库.关闭弹框.format("新增"))
        if self.wait(设置页对象库.版次管理工作区.版次名称.format("test"), 3):
            raise AssertionError("新增版次时，点击关闭新增界面，新增的版次被保存")
        #设置版次属性后，新增版次界面点击取消，版次属性不能被保存
        self.click(设置页对象库.版次管理工作区.新增)
        self.wait(对话框对象库.弹框标题.format("新增"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test")
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        self.wait(设置页对象库.版次管理工作区.版次内容输入框, 3)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "A")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        self.click(对话框对象库.弹框按钮.format("新增", "取消"))
        if self.wait(设置页对象库.版次管理工作区.版次名称.format("test"), 3):
            raise AssertionError("新增版次时，点击取消，新增的版次被保存")
        #设置版次属性后，新增版次界面点击确定，版次属性可以被保存
        self.click(设置页对象库.版次管理工作区.新增)
        self.wait(对话框对象库.弹框标题.format("新增"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test")
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        self.wait(设置页对象库.版次管理工作区.版次内容输入框, 3)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "A")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        self.click(对话框对象库.弹框按钮.format("新增", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"),3)
        if not self.wait(设置页对象库.版次管理工作区.版次名称.format("test"), 3):
            raise AssertionError("新增版次时，点击确定保存按钮，新增的版次未被保存")

    def 编辑版次(self):
        self.进入到操作位置.进入版次工作区()
        self.版次管理页面.删除版次(版次名称='test')
        self.click(设置页对象库.版次管理工作区.新增)
        self.wait(对话框对象库.弹框标题.format("新增"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test")
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        self.wait(设置页对象库.版次管理工作区.版次内容输入框, 3)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "A")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        self.click(对话框对象库.弹框按钮.format("新增", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"))
        #不选择任何版次，点击编辑，提示请选择需要修改的数据。
        self.driver.refrsh()
        self.进入到操作位置.进入版次工作区()
        self.click(设置页对象库.版次管理工作区.编辑)
        self.click(设置页对象库.版次管理工作区.编辑)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("请选择需要修改的数据"),3):
            raise AssertionError("不选择任何版次，点击编辑按钮，系统给出对应的提示")
        #选择版次后，点击编辑，进入编辑版次界面
        self.click(设置页对象库.版次管理工作区.版次名称.format("test"))
        self.click(设置页对象库.版次管理工作区.编辑)
        if not self.wait(对话框对象库.弹框标题.format("编辑"), 3):
            raise AssertionError("选择版次，点击编辑按钮，未弹出编辑版次界面")
        #对版次名称进行空值、重名、超长校验
        # 空值
        self.clear_by_key(公共元素对象库.输入框.format("名称"))
        self.click(对话框对象库.弹框按钮.format("编辑", "确定"))
        if not self.wait(公共元素对象库.输入框错误信息提示.format("名称不能为空"), 3):
            raise AssertionError("版次名称为空，点击保存系统未给出对应的提示信息")
        # 超长
        self.send_keys(公共元素对象库.输入框.format("名称"), "123456789012345678901234567890123456789012345612345678907890")
        self.click(对话框对象库.弹框按钮.format("编辑", "确定"))
        if not self.wait(公共元素对象库.输入框错误信息提示.format("名称不能超过50个字"),3):
            raise AssertionError("版次名称超长是点击保存，系统未给出对应的提示信息")
        # 重名
        self.clear(公共元素对象库.输入框.format("名称"))
        self.send_keys(公共元素对象库.输入框.format("名称"), "test")
        self.click(对话框对象库.弹框按钮.format("编辑", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"))
        self.click(设置页对象库.版次管理工作区.新增)
        self.wait(对话框对象库.弹框标题.format("新增"), 3)
        self.click(公共元素对象库.输入框.format("名称"))
        self.send_keys(公共元素对象库.输入框.format("名称"), "test")
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "A")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        self.click(对话框对象库.弹框按钮.format("编辑", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("版次定义名称已经存在"), 3):
            raise AssertionError("当创建的版次名称重复时，系统未给出对应的提示信息")

    def 编辑版次界面版次管理(self):
        self.进入到操作位置.进入版次工作区()
        self.版次管理页面.删除版次(版次名称='test')
        self.click(设置页对象库.版次管理工作区.新增)
        self.wait(对话框对象库.弹框标题.format("新增"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test")
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        self.wait(设置页对象库.版次管理工作区.版次内容输入框, 3)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "A")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        self.click(对话框对象库.弹框按钮.format("新增", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        self.click(设置页对象库.版次管理工作区.版次名称.format("test"))
        self.click(设置页对象库.版次管理工作区.编辑)
        self.wait(对话框对象库.弹框标题.format("编辑"), 3)
        # #第一行节点不能上移，最后一行节点不能下移
        try:
            self.click(设置页对象库.版次管理工作区.版次内容.format("A"))
        except:
            self.click_index(xpath=设置页对象库.版次管理工作区.版次内容.format("A"),index=1)
        # if not self.wait(设置页对象库.版次管理工作区.置灰_上移版次节点,3) or \
        #     not self.wait(设置页对象库.版次管理工作区.置灰_下移版次节点,3):
        #     raise AssertionError("第一行可以上移，最后一行可以下移")
        #点击新增版次按钮，版次节点列表新增一行版次
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        if not self.wait(设置页对象库.版次管理工作区.版次内容输入框, 3):
            raise AssertionError("点击新增版次节点按钮，未查看到新增的一行版次节点")
        # 对版次内容进行空值，超长，重名校验
        # 空值
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("版次不可为空"), 3):
            raise AssertionError("版次节点为空时，点击保存版次节点，没有查看到提示信息")
        # 重名
        self.clear_by_key(设置页对象库.版次管理工作区.版次内容输入框)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "A")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        self.click(对话框对象库.弹框按钮.format("编辑", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("版次定义详情内容不能重复"), 3):
            raise AssertionError("当创建的版次节点名称重复时，系统未给出对应的提示信息")
        对象列表=self.driver.getelements(设置页对象库.版次管理工作区.版次内容.format("A"))
        对象列表[0].click()
        self.click(设置页对象库.版次管理工作区.删除版次节点)
        ##点击版次节点行，点击上移按钮，节点行上移一行，点击下移按钮，节点行下移一行
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        self.wait(设置页对象库.版次管理工作区.版次内容输入框, 3)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "B")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        self.click(设置页对象库.版次管理工作区.版次内容.format("A"))
        self.click(设置页对象库.版次管理工作区.下移版次节点)
        index1=self.driver.getelement('//div[@aria-label="编辑"]//tr/td//span[text()="A"]/ancestor::tr/td[1]/div/div').text
        if index1=='1':
            raise AssertionError("对版次节点进行下移操作，版次节点并未下移")
        self.click(设置页对象库.版次管理工作区.版次内容.format("A"))
        self.click(设置页对象库.版次管理工作区.上移版次节点)
        index1 = self.driver.getelement('//div[@aria-label="编辑"]//tr/td//span[text()="A"]/ancestor::tr/td[1]/div/div').text
        if index1 != '1':
            raise AssertionError("对版次节点进行上移操作，版次节点并未上移")
        # 点击版次节点行，点击删除按钮，版次行被删除
        self.click(设置页对象库.版次管理工作区.版次内容.format("A"))
        self.click(设置页对象库.版次管理工作区.删除版次节点)
        if self.wait(设置页对象库.版次管理工作区.版次内容.format("A"),3):
            raise AssertionError("进行版次节点删除操作后，节点没有被删除")

    def 编辑版次界面编辑版次节点(self):
        self.进入到操作位置.进入版次工作区()
        self.版次管理页面.删除版次(版次名称='test')
        self.click(设置页对象库.版次管理工作区.新增)
        self.wait(对话框对象库.弹框标题.format("新增"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test")
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        self.wait(设置页对象库.版次管理工作区.版次内容输入框, 3)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "A")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        self.click(对话框对象库.弹框按钮.format("新增", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        self.click(设置页对象库.版次管理工作区.版次名称.format("test"))
        self.click(设置页对象库.版次管理工作区.编辑)
        self.wait(对话框对象库.弹框标题.format("编辑"), 3)
        #点击版次节点行编辑按钮，版次节点行进入编辑状态
        self.click(设置页对象库.版次管理工作区.编辑版次节点按钮.format("A"))
        if not self.wait(设置页对象库.版次管理工作区.版次内容输入框, 3):
            raise AssertionError("点击版次节点编辑按钮，版次节点未进入编辑状态")
        # 对版次内容进行空值，超长，重名校验
        # 空值
        self.clear_by_key(设置页对象库.版次管理工作区.版次内容输入框)
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("版次不可为空"), 3):
            raise AssertionError("版次节点为空时，点击保存版次节点，没有查看到提示信息")
        # 重名
        self.clear(设置页对象库.版次管理工作区.版次内容输入框)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "A")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        self.wait(设置页对象库.版次管理工作区.版次内容输入框, 3)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "A")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        self.click(对话框对象库.弹框按钮.format("编辑", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("版次定义详情内容不能重复"), 3):
            raise AssertionError("当创建的版次节点名称重复时，系统未给出对应的提示信息")

    def 编辑版次界面保存版次(self):
        self.进入到操作位置.进入版次工作区()
        self.版次管理页面.删除版次(版次名称='test')
        self.版次管理页面.删除版次(版次名称='test1')
        self.click(设置页对象库.版次管理工作区.新增)
        self.wait(对话框对象库.弹框标题.format("新增"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test")
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        self.wait(设置页对象库.版次管理工作区.版次内容输入框, 3)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "A")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        self.click(对话框对象库.弹框按钮.format("新增", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        self.click(设置页对象库.版次管理工作区.版次名称.format("test"))
        self.click(设置页对象库.版次管理工作区.编辑)
        self.wait(对话框对象库.弹框标题.format("编辑"), 3)
        #设置版次属性后，关闭新增版次界面，版次属性不能被保存
        self.clear(公共元素对象库.输入框.format("名称"))
        self.send_keys(公共元素对象库.输入框.format("名称"), "test1")
        self.click(对话框对象库.关闭弹框.format("编辑"))
        if self.wait(设置页对象库.版次管理工作区.版次名称.format("test1"), 3):
            raise AssertionError("编辑版次时，点击关闭新编辑界面，编辑的版次被保存")
        # 设置版次属性后，新增版次界面点击取消，版次属性不能被保存
        self.click(设置页对象库.版次管理工作区.版次名称.format("test"))
        self.click(设置页对象库.版次管理工作区.编辑)
        self.wait(对话框对象库.弹框标题.format("编辑"), 3)
        self.clear(公共元素对象库.输入框.format("名称"))
        self.send_keys(公共元素对象库.输入框.format("名称"), "test1")
        self.click(对话框对象库.弹框按钮.format("编辑", "取消"))
        if self.wait(设置页对象库.版次管理工作区.版次名称.format("test1"), 3):
            raise AssertionError("编辑版次时，点击取消，编辑的版次被保存")
        # 设置版次属性后，新增版次界面点击确定，版次属性可以被保存
        self.click(设置页对象库.版次管理工作区.版次名称.format("test"))
        self.click(设置页对象库.版次管理工作区.编辑)
        self.wait(对话框对象库.弹框标题.format("编辑"), 3)
        self.clear(公共元素对象库.输入框.format("名称"))
        self.send_keys(公共元素对象库.输入框.format("名称"), "test1")
        self.click(对话框对象库.弹框按钮.format("编辑", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("编辑成功"), 3)
        if not self.wait(设置页对象库.版次管理工作区.版次名称.format("test1"), 3):
            raise AssertionError("编辑版次时，点击确定保存按钮，编辑的版次未被保存")

    def 删除单个版次(self):
        self.进入到操作位置.进入版次工作区()
        self.版次管理页面.删除版次(版次名称='test')
        self.click(设置页对象库.版次管理工作区.新增)
        self.wait(对话框对象库.弹框标题.format("新增"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test")
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        self.wait(设置页对象库.版次管理工作区.版次内容输入框, 3)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "A")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        self.click(对话框对象库.弹框按钮.format("新增", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        #勾选单个版次，点击删除，弹出删除提示对话框
        self.click(设置页对象库.版次管理工作区.版次复选框.format("test"))
        self.click(设置页对象库.版次管理工作区.删除)
        if not self.wait(对话框对象库.对话框标题.format("提示"),3):
            raise AssertionError("勾选单个版次，点击删除，系统未弹出删除确认对话框")
        #关闭删除提示对话框，查看版次是否被删除
        self.click(对话框对象库.关闭对话框.format("提示"))
        if not self.wait(设置页对象库.版次管理工作区.版次名称.format("test"),3):
            raise AssertionError("点击关闭删除确认对话框，被选择的版次被删除")
        #点击取消删除提示对话框，查看版次是否被删除
        self.click(设置页对象库.版次管理工作区.删除)
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示","取消"))
        if not self.wait(设置页对象库.版次管理工作区.版次名称.format("test"), 3):
            raise AssertionError("点击取消删除确认对话框，被选择的版次被删除")
        #点击确定删除提示对话框，查看版次是否被删除
        self.driver.refrsh()
        self.进入到操作位置.进入版次工作区()
        self.click(设置页对象库.版次管理工作区.版次复选框.format("test"))
        self.click(设置页对象库.版次管理工作区.删除)
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if self.wait(设置页对象库.版次管理工作区.版次名称.format("test"), 3):
            raise AssertionError("点击确定删除确认对话框，被选择的版次未被删除")

    def 批量删除版次(self):
        self.进入到操作位置.进入版次工作区()
        self.版次管理页面.删除版次(版次名称='test')
        self.click(设置页对象库.版次管理工作区.新增)
        self.wait(对话框对象库.弹框标题.format("新增"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test")
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        self.wait(设置页对象库.版次管理工作区.版次内容输入框, 3)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "A")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        self.click(对话框对象库.弹框按钮.format("新增", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        self.版次管理页面.删除版次(版次名称='test1')
        self.click(设置页对象库.版次管理工作区.新增)
        self.wait(对话框对象库.弹框标题.format("新增"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test1")
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        self.wait(设置页对象库.版次管理工作区.版次内容输入框, 3)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "A")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        self.click(对话框对象库.弹框按钮.format("新增", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        #勾选多个版次，点击删除，弹出删除提示对话框
        self.click(设置页对象库.版次管理工作区.版次复选框.format("test"))
        self.click(设置页对象库.版次管理工作区.版次复选框.format("test1"))
        self.click(设置页对象库.版次管理工作区.删除)
        if not self.wait(对话框对象库.对话框标题.format("提示"), 3):
            raise AssertionError("勾选单个版次，点击删除，系统未弹出删除确认对话框")
        #关闭删除提示对话框，查看版次是否被删除、
        self.click(对话框对象库.关闭对话框.format("提示"))
        if not self.wait(设置页对象库.版次管理工作区.版次名称.format("test"), 3) or\
                not self.wait(设置页对象库.版次管理工作区.版次名称.format("test1"), 3):
            raise AssertionError("点击关闭删除确认对话框，被选择的版次被删除")
        #点击取消删除提示对话框，查看版次是否被删除
        self.driver.refrsh()
        self.进入到操作位置.进入版次工作区()
        self.click(设置页对象库.版次管理工作区.版次复选框.format("test"))
        self.click(设置页对象库.版次管理工作区.版次复选框.format("test1"))
        self.click(设置页对象库.版次管理工作区.删除)
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "取消"))
        if not self.wait(设置页对象库.版次管理工作区.版次名称.format("test"), 3)or\
                not self.wait(设置页对象库.版次管理工作区.版次名称.format("test1"), 3):
            raise AssertionError("点击取消删除确认对话框，被选择的版次被删除")
        # #当勾选的版次中含有系统版次时，删除按钮不可用
        # self.driver.refrsh()
        # self.进入到操作位置.进入版次工作区()
        # self.click(设置页对象库.版次管理工作区.版次复选框.format("test"))
        # self.click(设置页对象库.版次管理工作区.版次复选框.format("test1"))
        # self.click(设置页对象库.版次管理工作区.版次复选框.format("系统默认版次"))
        # if not self.wait(设置页对象库.版次管理工作区.置灰_删除,3):
        #     raise AssertionError("当勾选的版次中含有系统版次时，删除按钮没有被置灰")

    def 设置默认版次(self):
        self.进入到操作位置.进入版次工作区()
        self.版次管理页面.删除版次(版次名称='test2')
        self.click(设置页对象库.版次管理工作区.新增)
        self.wait(对话框对象库.弹框标题.format("新增"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test2")
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        self.wait(设置页对象库.版次管理工作区.版次内容输入框, 3)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "A")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        self.wait(设置页对象库.版次管理工作区.版次内容输入框, 3)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "B")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        self.click(对话框对象库.弹框按钮.format("新增", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        #点击版次列表中的版次，版次明细列表显示该版次下的版次节点
        self.click(设置页对象库.版次管理工作区.版次名称.format("test2"))
        if not self.wait(设置页对象库.版次管理工作区.版次明细节点.format("A"),3) or\
            not self.wait(设置页对象库.版次管理工作区.版次明细节点.format("B"),3):
            raise AssertionError("点击版次，版次明细中未显示该版次下的所有版次节点")
        #勾选版次列表，版次行的是否默认单选按钮，设置对应的版次为默认版次
        self.click(设置页对象库.版次管理工作区.是否默认单选框.format("test2"))
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="默认版次")
        self.click(项目管理对象库.创建新项目)
        self.wait(创建项目页面.页面名称, 3)
        self.click(创建项目页面.创建空白项目)
        self.wait(对话框对象库.弹框标题.format("项目名称"), 3)
        self.clear(公共元素对象库.输入框.format("项目名称"))
        self.send_keys(公共元素对象库.输入框.format("项目名称"), "默认版次")
        self.click(创建项目页面.提交按钮)
        self.default_content()
        self.wait(项目设置页面.项目成员tab页, 3)
        self.click(公共元素对象库.列表框.format("版次"))
        if not self.wait('//ul/li[contains(@class,"dropdown__item selected")]/span[text()="test2"]', 3):
            raise AssertionError("设置test2为默认版次，创建新项目，项目的版次未默认选择test2")


class 属性管理工作区(page):
    def __init__(self,Secdriver = None):
        page.__init__(self,secdriver=Secdriver)
        self.滑块验证=滑块验证(Secdriver=Secdriver)
        self.公共操作 = 公共操作(Secdriver=Secdriver)
        self.属性管理页面 = 属性管理页面(Secdriver=Secdriver)
        self.项目页面 = 项目页面(Secdriver=Secdriver)
        self.用户信息页面 = 用户信息页面(Secdriver=Secdriver)
        self.项目管理页面 = 项目管理页面(Secdriver=Secdriver)
        self.进入到操作位置 = 进入到操作位置(Secdriver=Secdriver)

    def 数据准备(self):
        self.项目管理页面.删除所有项目()
        self.进入到操作位置.进入属性工作区()
        self.属性管理页面.删除所有属性系统()

    def 新增属性系统(self):
        self.进入到操作位置.进入属性工作区()
        self.属性管理页面.删除属性系统(属性系统名称="test")
        #点击属性列表属性新增按钮，属性列表新增一行属性系统，属性系统处于编辑状态
        self.click(设置页对象库.属性管理工作区.新增)
        if not self.wait(设置页对象库.属性管理工作区.属性系统名称输入框,3):
            raise AssertionError("点击新增属性系统，属性系统列表未新增一行属性系统")
        #对属性系统名称进行空值、超长、重名校验
        #空值
        self.click(设置页对象库.属性管理工作区.属性系统保存按钮)
        if not self.wait('//table[@class="el-table__body"]//tr/td[2]//input[@placeholder="请输入属性名称"]',3):
            raise AssertionError("属性系统名称未空时，点击保存，未出现属性系统名称不能为空的提示信息")

        #重名
            # 输入合法信息，点击保存按钮，可以正常保存，属性系统编辑状态消失
        self.clear(设置页对象库.属性管理工作区.属性系统名称输入框)
        self.send_keys(设置页对象库.属性管理工作区.属性系统名称输入框,"test")
        self.click(设置页对象库.属性管理工作区.属性系统保存按钮)
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"))
        if self.wait(设置页对象库.属性管理工作区.属性系统名称输入框, 3):
            raise AssertionError("点击保存属性系统，属性系统列表中新增的属性系统行的编辑状态未改变")
        self.click(设置页对象库.属性管理工作区.新增)
        self.wait(设置页对象库.属性管理工作区.属性系统名称输入框, 3)
        self.send_keys(设置页对象库.属性管理工作区.属性系统名称输入框, "test")
        self.click(设置页对象库.属性管理工作区.属性系统保存按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("存在同名的属性模板定义！"),3):
            raise AssertionError("属性系统名称重复时，点击保存，未出现属性系统名称重复的提示信息")
        # #对属性系统描述进行超长校验
        # self.clear(设置页对象库.属性管理工作区.属性系统名称输入框)
        # self.send_keys(设置页对象库.属性管理工作区.属性系统名称输入框, "test0")
        # self.send_keys(设置页对象库.属性管理工作区.属性系统描述输入框, "test")
        # self.click(设置页对象库.属性管理工作区.属性系统保存按钮)
        # self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"))

    def 编辑属性系统(self):
        self.进入到操作位置.进入属性工作区()
        self.属性管理页面.批量删除属性系统(属性系统名称列表=["test","test1","test2"])
        self.属性管理页面.创建属性系统(属性系统名称="test")
        self.属性管理页面.创建属性系统(属性系统名称="test1")
        self.driver.refrsh()
        self.进入到操作位置.进入属性工作区()
        #不选择属性系统，点击编辑按钮，提示没有要修改的数据
        self.click(设置页对象库.属性管理工作区.编辑)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("请选择需要修改的数据"),3):
            raise AssertionError("不选择任何属性系统，点击编辑按钮，系统未给出对应的提示信息")
        #点击属性系统，点击编辑按钮，被选中的属性系统处于编辑状态
        self.click(设置页对象库.属性管理工作区.属性系统名称.format("test"))
        self.click(设置页对象库.属性管理工作区.编辑)
        if not self.wait(设置页对象库.属性管理工作区.属性系统名称输入框,3):
            raise AssertionError("点击编辑属性系统，属性系统未进入编辑状态")
        #对属性系统名称进行空值、超长、重名校验
        # 空值
        self.clear_by_key(设置页对象库.属性管理工作区.属性系统名称输入框)
        self.click(设置页对象库.属性管理工作区.属性系统保存按钮)
        if not self.wait('//table[@class="el-table__body"]//tr/td[2]//input[@placeholder="请输入属性名称"]', 3):
            raise AssertionError("属性系统名称未空时，点击保存，未出现属性系统名称不能为空的提示信息")

        # 重名
        # 输入合法信息，点击保存按钮，可以正常保存，属性系统编辑状态消失
        self.clear(设置页对象库.属性管理工作区.属性系统名称输入框)
        self.send_keys(设置页对象库.属性管理工作区.属性系统名称输入框, "test2")
        self.click(设置页对象库.属性管理工作区.属性系统保存按钮)
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"))
        if self.wait(设置页对象库.属性管理工作区.属性系统名称输入框, 3):
            raise AssertionError("点击保存属性系统，属性系统列表中新增的属性系统行的编辑状态未改变")
        if not self.wait(设置页对象库.属性管理工作区.属性系统名称.format("test2"), 3):
            raise AssertionError("编辑属性系统后，点击保存，编辑的属性系统未被保存")
        self.click(设置页对象库.属性管理工作区.属性系统名称.format("test2"))
        self.click(设置页对象库.属性管理工作区.编辑)
        self.wait(设置页对象库.属性管理工作区.属性系统名称输入框, 3)
        self.clear(设置页对象库.属性管理工作区.属性系统名称输入框)
        self.send_keys(设置页对象库.属性管理工作区.属性系统名称输入框, "test1")
        self.click(设置页对象库.属性管理工作区.属性系统保存按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("存在同名的属性模板定义！"), 3):
            raise AssertionError("编辑属性系统，属性系统名称重复时，点击保存，未出现属性系统名称重复的提示信息")

    def 删除单个属性系统(self):
        self.进入到操作位置.进入属性工作区()
        self.属性管理页面.删除属性系统(属性系统名称="test")
        self.属性管理页面.创建属性系统(属性系统名称="test")
        #勾选单个非系统属性系统，点击删除、弹出删除提示对话框
        self.click(设置页对象库.属性管理工作区.删除)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("请选择需要删除的数据"),3):
            raise AssertionError("未勾选任何属性系统，点击删除，未出现需要选择属性系统的提示信息")
        self.click(设置页对象库.属性管理工作区.属性系统复选框.format("test"))
        self.click(设置页对象库.属性管理工作区.删除)
        if not self.wait(对话框对象库.对话框标题.format("提示"), 3):
            raise AssertionError("勾选单个属性系统，点击删除，系统未弹出删除确认对话框")
        #关闭删除提示对话框，查看属性系统是否被删除
        self.click(对话框对象库.关闭对话框.format("提示"))
        if not self.wait(设置页对象库.属性管理工作区.属性系统名称.format("test"),3):
            raise AssertionError("关闭删除确认对话框，属性系统被删除")
        #点击取消删除提示对话框，查看属性系统是否被删除
        self.driver.refrsh()
        self.进入到操作位置.进入属性工作区()
        self.click(设置页对象库.属性管理工作区.属性系统复选框.format("test"))
        self.click(设置页对象库.属性管理工作区.删除)
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "取消"))
        if not self.wait(设置页对象库.属性管理工作区.属性系统名称.format("test"), 3):
            raise AssertionError("点击取消删除确认对话框，属性系统被删除")
        #点击确定删除提示对话框，查看属性系统是否被删除
        self.driver.refrsh()
        self.进入到操作位置.进入属性工作区()
        self.click(设置页对象库.属性管理工作区.属性系统复选框.format("test"))
        self.click(设置页对象库.属性管理工作区.删除)
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if self.wait(设置页对象库.属性管理工作区.属性系统名称.format("test"), 3):
            raise AssertionError("点击确定删除确认对话框，属性系统为被删除")
        #系统属性系统不可删除
        self.click(设置页对象库.属性管理工作区.属性系统复选框.format("系统"))
        if not self.wait(设置页对象库.属性管理工作区.置灰_删除按钮,3):
            raise AssertionError("勾选删除系统属性，系统属性不可以被删除")

    def 批量删除属性系统(self):
        self.进入到操作位置.进入属性工作区()
        self.属性管理页面.批量删除属性系统(属性系统名称列表=["test", "test1", "test2"])
        self.属性管理页面.创建属性系统(属性系统名称="test")
        self.属性管理页面.创建属性系统(属性系统名称="test1")
        self.属性管理页面.创建属性系统(属性系统名称="test2")
        #勾选多个非系统属性系统，点击删除，弹出删除提示对话框
        self.click(设置页对象库.属性管理工作区.属性系统复选框.format("test"))
        self.click(设置页对象库.属性管理工作区.属性系统复选框.format("test1"))
        self.click(设置页对象库.属性管理工作区.属性系统复选框.format("test2"))
        self.click(设置页对象库.属性管理工作区.删除)
        if not self.wait(对话框对象库.对话框标题.format("提示"), 3):
            raise AssertionError("勾选单个属性系统，点击删除，系统未弹出删除确认对话框")
        #关闭删除提示对话框，查看属性系统是否被删除
        self.click(对话框对象库.关闭对话框.format("提示"))
        if not self.wait(设置页对象库.属性管理工作区.属性系统名称.format("test"), 3) or\
                not self.wait(设置页对象库.属性管理工作区.属性系统名称.format("test1"), 3) or\
                not self.wait(设置页对象库.属性管理工作区.属性系统名称.format("test2"), 3):
            raise AssertionError("关闭删除确认对话框，属性系统被删除")
        #点击取消删除提示对话框，查看属性系统是否被删除
        self.driver.refrsh()
        self.进入到操作位置.进入属性工作区()
        self.click(设置页对象库.属性管理工作区.属性系统复选框.format("test"))
        self.click(设置页对象库.属性管理工作区.属性系统复选框.format("test1"))
        self.click(设置页对象库.属性管理工作区.属性系统复选框.format("test2"))
        self.click(设置页对象库.属性管理工作区.删除)
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "取消"))
        if not self.wait(设置页对象库.属性管理工作区.属性系统名称.format("test"), 3) or \
                not self.wait(设置页对象库.属性管理工作区.属性系统名称.format("test1"), 3) or \
                not self.wait(设置页对象库.属性管理工作区.属性系统名称.format("test2"), 3):
            raise AssertionError("点击取消删除确认对话框，属性系统被删除")
        #点击确定删除提示对话框，查看属性系统是否被删除
        self.driver.refrsh()
        self.进入到操作位置.进入属性工作区()
        self.click(设置页对象库.属性管理工作区.属性系统复选框.format("test"))
        self.click(设置页对象库.属性管理工作区.属性系统复选框.format("test1"))
        self.click(设置页对象库.属性管理工作区.属性系统复选框.format("test2"))
        self.click(设置页对象库.属性管理工作区.删除)
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if self.wait(设置页对象库.属性管理工作区.属性系统名称.format("test"), 3) or \
                self.wait(设置页对象库.属性管理工作区.属性系统名称.format("test1"), 3) or \
                self.wait(设置页对象库.属性管理工作区.属性系统名称.format("test2"), 3):
            raise AssertionError("点击确定删除确认对话框，属性系统未被删除")

    def 属性系统添加属性(self):
        self.进入到操作位置.进入属性工作区()
        self.属性管理页面.删除属性系统(属性系统名称="test")
        self.属性管理页面.创建属性系统(属性系统名称="test")
        self.click(设置页对象库.属性管理工作区.属性系统名称.format("test"))
        #点击添加属性，属性列表新增一行属性
        self.click(设置页对象库.属性管理工作区.添加属性)
        if not self.wait(设置页对象库.属性管理工作区.属性类别输入框.format("1"),3):
            raise AssertionError("点击添加属性按钮，属性列表未新增一行属性")
        #对属性类别，属性名称进行空值校验
        self.click(设置页对象库.属性管理工作区.行保存按钮.format("1"))
        if not self.wait('//table[@class="el-table__body"]//tr[1]/td[3]//input[@placeholder="请输入属性类别"]',3):
            raise AssertionError("属性类别为空时，点击保存属性，没有给出对应的提示信息")
        if not self.wait('//table[@class="el-table__body"]//tr[1]/td[4]//input[@placeholder="请输入属性名称"]',3):
            raise AssertionError("属性名称为空时，点击保存属性，没有给出对应的提示信息")

    def 导入属性模板(self):
        self.进入到操作位置.进入属性工作区()
        self.属性管理页面.删除属性系统(属性系统名称="test")
        self.属性管理页面.创建属性系统(属性系统名称="test")
        self.click(设置页对象库.属性管理工作区.属性系统名称.format("test"))
        # 点击下载模板，属性模板可以正常下载
        self.click(设置页对象库.属性管理工作区.下载模板)
        downpath = self.公共操作.检查文件是否下载完成()
        filepath = downpath + '\property_template.xlsx'
        time.sleep(4)
        print(filepath)
        if not os.path.exists(filepath):
            raise AssertionError("在下载目录下未查看到下载的模板文件")
        ##正确填写模板，使用导入属性，可以正常导入
        self.click(设置页对象库.属性管理工作区.导入属性)
        self.公共操作.win上传文件(文件路径=['TestData','FrontData','项目页','项目属性模板表.xlsx'])
        if not self.wait(设置页对象库.属性管理工作区.行删除按钮.format("1"), 3):
            raise AssertionError("导入填写的属性模板后，未查看到导入的属性")
        #当属性模板列表中填写非法值时，导入属性，会出现相应的提示
        self.driver.refrsh()
        self.进入到操作位置.进入属性工作区()
        self.click(设置页对象库.属性管理工作区.属性系统名称.format("test"))
        self.click(设置页对象库.属性管理工作区.导入属性)
        self.公共操作.win上传文件(文件路径=['TestData', 'FrontData', '项目页', '项目属性模板表1.xlsx'])
        if not self.wait(公共元素对象库.系统提示信息弹框.format("导入的文件中存在为空列"),3):
            raise AssertionError("导入的项目模板中存在不合法的数据，系统未给出对应的提示信息")

    def 编辑属性(self):
        self.进入到操作位置.进入属性工作区()
        self.属性管理页面.删除属性系统(属性系统名称="test")
        self.属性管理页面.创建属性系统(属性系统名称="test")
        self.click(设置页对象库.属性管理工作区.属性系统名称.format("test"))
        self.click(设置页对象库.属性管理工作区.添加属性)
        self.wait(设置页对象库.属性管理工作区.属性类别输入框.format("1"), 3)
        self.send_keys(设置页对象库.属性管理工作区.属性类别输入框.format("1"),"kind")
        self.send_keys(设置页对象库.属性管理工作区.属性名称输入框.format("1"), "name")
        self.click(设置页对象库.属性管理工作区.行保存按钮.format("1"))
        #点击编辑属性，属性进入编辑状态
        self.click(设置页对象库.属性管理工作区.行保存按钮.format("1"))
        if not self.wait(设置页对象库.属性管理工作区.属性类别输入框.format("1"),3):
            raise AssertionError("点击编辑属性行，属性行未进入编辑状态")
        #对属性类别，属性名称进行空值校验
        self.clear_by_key(设置页对象库.属性管理工作区.属性类别输入框.format("1"))
        self.click(设置页对象库.属性管理工作区.行保存按钮.format("1"))
        if not self.wait(设置页对象库.属性管理工作区.属性类别输入框.format("1"),3):
            raise AssertionError("属性类型为空时，点击保存按钮，该属性可以保存")
        self.clear(设置页对象库.属性管理工作区.属性名称输入框.format("1"))
        self.click(设置页对象库.属性管理工作区.行保存按钮.format("1"))
        if not self.wait(设置页对象库.属性管理工作区.属性名称输入框.format("1"), 3):
            raise AssertionError("属性名称为空时，点击保存按钮，该属性可以保存")

        #在属性列表中编辑属性的属性后，不点击保存，编辑的属性不会保存
        self.clear(设置页对象库.属性管理工作区.属性类别输入框.format("1"))
        self.clear(设置页对象库.属性管理工作区.属性名称输入框.format("1"))
        self.send_keys(设置页对象库.属性管理工作区.属性类别输入框.format("1"),'test1')
        self.send_keys(设置页对象库.属性管理工作区.属性名称输入框.format("1"),'test1')
        self.click(设置页对象库.属性管理工作区.属性系统名称.format("系统"))
        self.click(设置页对象库.属性管理工作区.属性系统名称.format("test"))
        if self.wait('//div[@class="el-card__body"]//table[@class="el-table__body"]//tr[1]/td[3]//span[text()="test1"]',3):
            raise AssertionError("编辑属性时，未点击保存，属性信息被保存")

    def 删除单个属性(self):
        self.进入到操作位置.进入属性工作区()
        self.属性管理页面.删除属性系统(属性系统名称="test")
        self.属性管理页面.创建属性系统(属性系统名称="test")
        self.click(设置页对象库.属性管理工作区.属性系统名称.format("test"))
        self.属性管理页面.添加属性(服务类别="A",属性类型="A",属性名称="A")
        #属性列表中，点击删除属性行操作，出现属性删除提示框
        self.click(设置页对象库.属性管理工作区.行删除按钮.format("1"))
        if not self.wait(设置页对象库.属性管理工作区.删除对话框,3):
            raise AssertionError("点击删除单个属性，未查看到删除确认对话框")
        #属性删除提示框点击取消，被删除属性不会被删除
        self.click(设置页对象库.属性管理工作区.删除取消按钮)
        if not self.wait(设置页对象库.属性管理工作区.行删除按钮.format("1"),3):
            raise AssertionError("点击删除单个属性，点击取消删除确认对话框后，该属性被删除")
        #属性删除提示框点击确定，被删除属性会被删除
        self.click(设置页对象库.属性管理工作区.行删除按钮.format("1"))
        self.wait(设置页对象库.属性管理工作区.删除对话框, 3)
        self.click(设置页对象库.属性管理工作区.删除确认按钮)
        if self.wait(设置页对象库.属性管理工作区.行删除按钮.format("1"), 3):
            raise AssertionError("点击删除单个属性，点击确认删除确认对话框后，该属性未被删除")

    def 批量删除属性(self):
        self.进入到操作位置.进入属性工作区()
        self.属性管理页面.删除属性系统(属性系统名称="test")
        self.属性管理页面.创建属性系统(属性系统名称="test")
        self.click(设置页对象库.属性管理工作区.属性系统名称.format("test"))
        self.属性管理页面.添加属性(服务类别="A",属性类型="A", 属性名称="A")
        self.属性管理页面.添加属性(服务类别="B",属性类型="B", 属性名称="B")
        self.属性管理页面.添加属性(服务类别="C",属性类型="C", 属性名称="C")
        #勾选多个属性，点击批量删除，出现属性删除提示框
        self.click(设置页对象库.属性管理工作区.属性行复选框.format("1"))
        self.click(设置页对象库.属性管理工作区.属性行复选框.format("2"))
        self.click(设置页对象库.属性管理工作区.属性行复选框.format("3"))
        self.click(设置页对象库.属性管理工作区.删除属性)
        if not self.wait(设置页对象库.属性管理工作区.删除对话框, 3):
            raise AssertionError("批量删除属性，点击删除，未查看到删除确认对话框")
        #属性删除提示框点击取消，被删除属性不会被删除
        self.click(设置页对象库.属性管理工作区.删除取消按钮)
        if not self.wait(设置页对象库.属性管理工作区.行删除按钮.format("1"), 3) or\
                not self.wait(设置页对象库.属性管理工作区.行删除按钮.format("2"), 3) or\
                not self.wait(设置页对象库.属性管理工作区.行删除按钮.format("3"), 3):
            raise AssertionError("批量删除属性，点击取消删除确认对话框后，属性被删除")
        #属性删除提示框点击确定，被删除属性会被删除
        self.click(设置页对象库.属性管理工作区.删除属性)
        self.wait(设置页对象库.属性管理工作区.删除对话框, 3)
        self.click(设置页对象库.属性管理工作区.删除确认按钮)
        if self.wait(设置页对象库.属性管理工作区.行删除按钮.format("1"), 3) or \
                self.wait(设置页对象库.属性管理工作区.行删除按钮.format("2"), 3) or \
                self.wait(设置页对象库.属性管理工作区.行删除按钮.format("3"), 3):
            raise AssertionError("批量删除属性，点击确认删除确认对话框后，属性未被删除")



