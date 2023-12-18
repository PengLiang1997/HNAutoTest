from HNtest.testcasesec.testcasesec import page
from HNtest.Secselenium.secdriver import Secdriver
from ..元素对象库.登录页 import *
from ..元素对象库.首页对象库 import *
from ..元素对象库.公共元素 import *
from ..基础操作.滑块验证 import *


class 登录页面(page):
    def __init__(self,Secdriver=None):
        page.__init__(self,secdriver=Secdriver)
        self.滑块验证=滑块验证(Secdriver=self.driver)


    def 短信快捷登录(self,手机号,验证码=888888):
        self.default_content()
        self.clear(登录页对象库.手机号输入框)
        self.send_keys(登录页对象库.手机号输入框,手机号)
        self.click(登录页对象库.验证码按钮)
        self.default_content()
        self.滑块验证.滑块验证操作()
        self.wait(登录页对象库.开始使用, 30)
        self.clear(登录页对象库.验证码输入框)
        self.send_keys(登录页对象库.验证码输入框,验证码)
        self.click(登录页对象库.开始使用)
        self.default_content()

    def 账号密码登录(self,账号,密码):
        self.driver.refrsh()
        self.default_content()
        if self.wait(对话框对象库.对话框标题.format("确认注销"),3):
            self.click(对话框对象库.对话框按钮.format("确认注销","重新登录"))
        # self.click(登录页对象库.账号密码登录)
        self.click(登录页对象库.账号输入框)
        self.clear(登录页对象库.账号输入框)
        self.send_keys(登录页对象库.账号输入框,账号)
        self.click(登录页对象库.密码输入框)
        self.clear(登录页对象库.密码输入框)
        self.send_keys(登录页对象库.密码输入框, 密码)
        self.click(登录页对象库.登录按钮)
        self.default_content()
        self.滑块验证.滑块验证操作()
        self.default_content()

    def 忘记密码(self,手机号,验证码,新密码):
        self.default_content()
        self.click(登录页对象库.账号密码登录)
        self.wait(登录页对象库.忘记密码,30)
        self.click(登录页对象库.忘记密码)
        self.wait(登录页对象库.忘记密码对象库.重置密码弹窗标题,30)
        self.clear(登录页对象库.手机号输入框)
        self.send_keys(登录页对象库.手机号输入框,手机号)
        self.click(登录页对象库.验证码按钮)
        self.default_content()
        self.滑块验证.滑块验证操作()
        self.wait(登录页对象库.验证码输入框, 30)
        self.clear(登录页对象库.验证码输入框)
        self.send_keys(登录页对象库.验证码输入框, 验证码)
        self.click(登录页对象库.忘记密码对象库.重置密码按钮)
        self.clear(登录页对象库.忘记密码对象库.密码输入框)
        self.send_keys(登录页对象库.忘记密码对象库.密码输入框,新密码)
        self.clear(登录页对象库.忘记密码对象库.确认密码输入框)
        self.send_keys(登录页对象库.忘记密码对象库.确认密码输入框, 新密码)
        self.click(登录页对象库.忘记密码对象库.提交按钮)
        self.default_content()
        self.wait(公共元素对象库.系统提示信息弹框.format("重置成功,请重新登录"),30)

    def 退出登录(self):
        self.default_content()
        self.click(首页对象库.用户)
        self.wait(首页对象库.退出, 30)
        self.click(首页对象库.退出)
        self.default_content()



