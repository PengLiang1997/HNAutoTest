import time

from HNtest.testcasesec.testcasesec import page
from HNtest.Secselenium.secdriver import Secdriver
from ..元素对象库.用户信息 import *
from ..元素对象库.公共元素 import *
from .进入到操作位置 import *
from .公共操作 import *
from ..基础操作.滑块验证 import *


class 用户信息页面(page):
    def __init__(self,Secdriver=None):
        page.__init__(self,secdriver=Secdriver)
        self.滑块验证=滑块验证(Secdriver=self.driver)
        self.进入到操作位置=进入到操作位置(Secdriver=self.driver)
        self.公共操作 = 公共操作(Secdriver=self.driver)

    def 进入账号信息页面(self):
        self.default_content()
        self.进入到操作位置.进入用户信息页()
        self.click(用户信息对象库.账号信息)

    def 进入基本信息页面(self):
        self.default_content()
        self.进入到操作位置.进入用户信息页()
        self.click(用户信息对象库.基本信息)

    def 维护用户账号信息(self,手机号=None,验证码=None,电子邮箱=None,用户名=None,原密码=None,用户密码=None):
        if 手机号:
            self.切换手机号(手机号=手机号,验证码=验证码)
        if 电子邮箱:
            if self.wait(用户信息对象库.账号信息对象库.绑定邮箱按钮,3):
                self.clear(公共元素对象库.输入框.format("电子邮件"))
                self.send_keys(公共元素对象库.输入框.format("电子邮件"),电子邮箱)
                self.click(用户信息对象库.账号信息对象库.绑定邮箱按钮)
        if 用户名:
            if self.wait(公共元素对象库.输入框.format("用户名"),3):
                self.clear(公共元素对象库.输入框.format("用户名"))
                self.send_keys(公共元素对象库.输入框.format("用户名"),用户名)
        if 用户密码:
            self.click(用户信息对象库.账号信息对象库.修改密码按钮)
            self.wait(对话框对象库.弹框标题.format("修改密码"),3)
            self.send_keys(公共元素对象库.输入框.format("当前密码"), 原密码)
            self.send_keys(公共元素对象库.输入框.format("新密码"), 用户密码)
            self.send_keys(公共元素对象库.输入框.format("确认密码"), 用户密码)
            self.click(对话框对象库.弹框按钮.format("修改密码","保存"))
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 3)

    def 切换手机号(self,手机号,验证码):
        self.default_content()
        self.click(用户信息对象库.账号信息对象库.切换手机号按钮)
        self.default_content()
        self.wait(用户信息对象库.账号信息对象库.切换手机号弹窗保存,3)
        self.clear(登录页对象库.手机号输入框)
        self.send_keys(登录页对象库.手机号输入框, 手机号)
        self.click(登录页对象库.验证码按钮)
        self.default_content()
        self.滑块验证.滑块验证操作()
        self.wait(用户信息对象库.账号信息对象库.切换手机号弹窗保存,3)
        self.click(登录页对象库.验证码输入框)
        self.clear(登录页对象库.验证码输入框)
        self.send_keys(登录页对象库.验证码输入框, 验证码)
        self.click(用户信息对象库.账号信息对象库.切换手机号弹窗保存,3)

    def 维护用户基本信息(self,头像路径=None,用户昵称=None,国家=None,姓=None,名=None,职位=None,办公电话=None,公司地址=None,公司名称=None,城市=None,所在省=None,邮编=None):
        if 头像路径:
            self.更换头像(文件路径=头像路径)
        if 用户昵称:
            self.clear(公共元素对象库.输入框.format("用户昵称"))
            self.send_keys(公共元素对象库.输入框.format("用户昵称"),用户昵称)
        if 国家:
            self.click(公共元素对象库.列表框.format("国家"))
            self.click(公共元素对象库.列表框选项.format(国家))
        if 姓:
            self.clear(用户信息对象库.基本信息对象库.姓输入框)
            self.send_keys(用户信息对象库.基本信息对象库.姓输入框, 姓)
        if 名:
            self.clear(用户信息对象库.基本信息对象库.名输入框)
            self.send_keys(用户信息对象库.基本信息对象库.名输入框, 名)
        if 职位:
            self.clear(公共元素对象库.输入框.format("职位"))
            self.send_keys(公共元素对象库.输入框.format("职位"), 职位)
        if 办公电话:
            self.clear(公共元素对象库.输入框.format("办公电话"))
            self.send_keys(公共元素对象库.输入框.format("办公电话"), 办公电话)
        if 公司地址:
            self.clear(公共元素对象库.输入框.format("公司地址"))
            self.send_keys(公共元素对象库.输入框.format("公司地址"), 公司地址)
        if 公司名称:
            self.clear(公共元素对象库.输入框.format("公司名称"))
            self.send_keys(公共元素对象库.输入框.format("公司名称"), 公司名称)
        if 城市:
            self.clear(公共元素对象库.输入框.format("城市"))
            self.send_keys(公共元素对象库.输入框.format("城市"), 城市)
        if 所在省:
            self.click(公共元素对象库.列表框.format("省/直辖市/自治区"))
            self.click(公共元素对象库.列表框选项.format(所在省))
        if 邮编:
            self.clear(公共元素对象库.输入框.format("邮编"))
            self.send_keys(公共元素对象库.输入框.format("邮编"), 邮编)
        flage = True
        self.move_to_by_pyautogui(用户信息对象库.基本信息对象库.更改头像按钮, y_offset=0)
        while (flage):
            try:
                flage = False
                self.click(用户信息对象库.账号信息对象库.保存)
            except:
                flage = True
                self.scroll_by_pyautogui(-5)
        self.wait(公共元素对象库.系统提示信息弹框.format("保存成功"), 3)

    def 更换头像(self,文件路径):
        self.default_content()
        self.click(用户信息对象库.基本信息对象库.更改头像按钮)
        self.公共操作.win上传文件(文件路径=文件路径)



