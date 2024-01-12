import random
import time

from ..基础操作.用户信息页面 import *
from ..基础操作.登录页面 import *
from ..基础操作.滑块验证 import *
from ..元素对象库.登录页 import *
from ..元素对象库.公共元素 import *
from HNtest.testcasesec.testcasesec import page
from HNtest.Secselenium.secdriver import Secdriver

class 登录页(page):
    def __init__(self,Secdriver = None):
        page.__init__(self,secdriver=Secdriver)
        self.滑块验证=滑块验证(Secdriver=Secdriver)
        self.登录页面 = 登录页面(Secdriver=Secdriver)
        self.用户信息页面 = 用户信息页面(Secdriver=Secdriver)

    def 数据准备(self):
        # # 注册账号1:18942178870 pw:user8870
        # self.登录页面.短信快捷登录(手机号='18942178870')
        # self.用户信息页面.进入账号信息页面()
        # self.用户信息页面.维护用户账号信息(用户密码='user8870',原密码='user8870')
        # #注册账号2:18942178871 pw:user0000
        # self.登录页面.退出登录()
        # self.登录页面.短信快捷登录(手机号='18942178871')
        # self.用户信息页面.进入账号信息页面()
        # self.用户信息页面.维护用户账号信息(用户密码='user0000',原密码='user8871')
        pass

    def 手机号验证码校验(self):
        self.default_content()
        #点击下拉按钮，可以查看并选择对应区域号码
        self.click(公共元素对象库.手机号地区列表框)
        if not self.wait(公共元素对象库.手机号地区列表框选项.format("中国(+86)"),3):
            raise AssertionError("手机区域号码列表框选项显示错误，未查看到对应的区域号码")
        self.click(公共元素对象库.手机号地区列表框选项.format("中国(+86)"))
        #对手机号进行空值和非法值校验
        self.click(登录页对象库.开始使用)
        if not self.wait(公共元素对象库.输入框错误信息提示.format("请输入正确的手机号"),3):
            raise AssertionError("对手机号进行空值校验，未给出相应提示信息")
        self.click(登录页对象库.验证码按钮)
        if self.wait(人机验证弹窗对象库.弹窗标题,3):
            raise AssertionError("手机号为空，可以进行人机验证")
        self.clear(登录页对象库.手机号输入框)
        self.send_keys(登录页对象库.手机号输入框, '189421788701')
        self.click(登录页对象库.开始使用)
        if not self.wait(公共元素对象库.输入框错误信息提示.format("请输入正确的手机号"), 3):
            raise AssertionError("对手机号进行非法值校验，未给出相应提示信息")
        self.click(登录页对象库.验证码按钮)
        if self.wait(人机验证弹窗对象库.弹窗标题, 3):
            raise AssertionError("手机号非法，可以进行人机验证")
        #对验证码进行空值和非法值校验
        self.clear(登录页对象库.手机号输入框)
        self.send_keys(登录页对象库.手机号输入框, '18942178870')
        self.click(登录页对象库.开始使用)
        if not self.wait(公共元素对象库.输入框错误信息提示.format("验证码不能为空"), 3):
            raise AssertionError("对验证码进行空值校验，未给出相应提示信息")
        self.clear(登录页对象库.验证码输入框)
        self.send_keys(登录页对象库.验证码输入框, '888890')
        self.click(登录页对象库.开始使用)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("手机验证码不存在或已过期，请重新输入验证码")):
            raise AssertionError("未进行滑块验证操作，直接登录，未给出相应的提示信息")
        self.click(登录页对象库.验证码按钮)
        self.default_content()
        self.滑块验证.滑块验证操作()
        self.clear(登录页对象库.验证码输入框)
        self.send_keys(登录页对象库.验证码输入框, '888880')
        self.click(登录页对象库.开始使用)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("手机验证码错误，请输入正确的验证码！")):
            raise AssertionError("输入错误的验证码，点击登录，未给出相应的提示信息")
        #输入正确值登录
        time.sleep(60)
        self.clear(登录页对象库.手机号输入框)
        self.send_keys(登录页对象库.手机号输入框,'18942178870')
        self.click(登录页对象库.验证码按钮)
        self.default_content()
        self.滑块验证.滑块验证操作()
        self.clear(登录页对象库.验证码输入框)
        self.send_keys(登录页对象库.验证码输入框,'888888')
        self.click(登录页对象库.开始使用)
        self.default_content()
        if not self.wait('//div[@id="project"]',3):
            raise AssertionError("输入正确手机号和验证码，未进入到项目首页")

    def 账号密码校验(self):
        self.default_content()
        #点击账号密码登录，当前页面跳转至账号密码登录页面
        self.click(登录页对象库.账号密码登录)
        if not self.wait(登录页对象库.账号输入框,3):
            raise AssertionError("在短信快捷登录页点击账号密码登录按钮，登录页未切换到账号密码登录页")
        #对账号进行空值、超长、非法值校验
        self.click(登录页对象库.登录按钮)
        if not self.wait(公共元素对象库.输入框错误信息提示.format("用户名或邮箱不能为空"),3):
            raise AssertionError("账号为空时，点击登录，未给出相应的提示")
        #账号密码校验已移除
        # self.clear(登录页对象库.账号输入框)
        # self.send_keys(登录页对象库.账号输入框, 'user887user8870user8870user8870user8870user8870user8870user8870user8870user8870user8870user8870user8870user88700')
        # self.click(登录页对象库.登录按钮)
        # if not self.wait(公共元素对象库.输入框错误信息提示.format("用户名为4到16位(字母，数字，下划线，不能以下划线开头或结尾)"), 3):
        #     raise AssertionError("账号超长时，点击登录，未给出相应的提示")
        # self.clear(登录页对象库.账号输入框)
        # self.send_keys(登录页对象库.账号输入框,'@##￥')
        # self.click(登录页对象库.登录按钮)
        # if not self.wait(公共元素对象库.输入框错误信息提示.format("用户名为4到16位(字母，数字，下划线，不能以下划线开头或结尾)")):
        #     raise AssertionError("账号非法时，点击登录，未给出相应的提示")
        #对密码进行空值，非法值校验
        self.clear(登录页对象库.账号输入框)
        self.send_keys(登录页对象库.账号输入框,'user8870')
        self.click(登录页对象库.登录按钮)
        if not self.wait(公共元素对象库.输入框错误信息提示.format("请输入密码"), 3):
            raise AssertionError("密码为空时，点击登录，未给出相应的提示")
        # 账号密码校验已移除
        # self.clear(登录页对象库.密码输入框)
        # self.send_keys(登录页对象库.密码输入框, 'user')
        # self.click(登录页对象库.登录按钮)
        # if not self.wait(公共元素对象库.输入框错误信息提示.format("密码必须包含字母，数字和特殊字符，且在8-18位之间"), 3):
        #     raise AssertionError("密码为非法格式时，点击登录，未给出相应的提示")
        #输入有效账号密码，点击登录后关闭人机验证弹窗
        self.clear(登录页对象库.密码输入框)
        self.send_keys(登录页对象库.密码输入框, 'user@8870')
        self.click(登录页对象库.登录按钮)
        self.default_content()
        self.wait(人机验证弹窗对象库.弹窗标题,3)
        self.click(人机验证弹窗对象库.关闭弹窗)
        if self.wait('//div[@id="project"]',3):
            raise AssertionError("账号密码登录，未进行人机验证就进入了项目首页")
        #错误密码登录系统
        self.clear(登录页对象库.密码输入框)
        self.send_keys(登录页对象库.密码输入框, 'user@8871')
        self.click(登录页对象库.登录按钮)
        self.default_content()
        self.滑块验证.滑块验证操作()
        if not self.wait(公共元素对象库.系统提示信息弹框.format("用户名或密码错误,请重新输入")):
            raise AssertionError("账号密码登录，登录密码错误，为出现提示信息")

    def 重置密码手机号验证码校验(self):
        self.default_content()
        self.click(登录页对象库.账号密码登录)
        #点击忘记密码按钮进入重置密码页面
        self.click(登录页对象库.忘记密码)
        self.default_content()
        if not self.wait(登录页对象库.忘记密码对象库.重置密码弹窗标题,3):
            raise AssertionError("点击忘记密码按钮，未跳转到重置密码弹框")
        # 点击下拉按钮，可以查看并选择对应区域号码
        self.click(公共元素对象库.手机号地区列表框)
        if not self.wait(公共元素对象库.手机号地区列表框选项.format("中国(+86)"), 3):
            raise AssertionError("手机区域号码列表框选项显示错误，未查看到对应的区域号码")
        self.click(公共元素对象库.手机号地区列表框选项.format("中国(+86)"))
        # 对手机号进行空值和非法值校验
        self.click(登录页对象库.忘记密码对象库.重置密码按钮)
        if not self.wait(公共元素对象库.输入框错误信息提示.format("请输入正确的手机号"), 3):
            raise AssertionError("对手机号进行空值校验，未给出相应提示信息")
        self.click(登录页对象库.验证码按钮)
        if self.wait(人机验证弹窗对象库.弹窗标题, 3):
            raise AssertionError("手机号为空，可以进行人机验证")
        self.clear(登录页对象库.手机号输入框)
        self.send_keys(登录页对象库.手机号输入框, '189421788701')
        self.click(登录页对象库.忘记密码对象库.重置密码按钮)
        if not self.wait(公共元素对象库.输入框错误信息提示.format("请输入正确的手机号"), 3):
            raise AssertionError("对手机号进行非法值校验，未给出相应提示信息")
        self.click(登录页对象库.验证码按钮)
        if self.wait(人机验证弹窗对象库.弹窗标题, 3):
            raise AssertionError("手机号非法，可以进行人机验证")
        # 对验证码进行空值和非法值校验
        self.clear(登录页对象库.手机号输入框)
        self.send_keys(登录页对象库.手机号输入框, '18942178870')
        self.click(登录页对象库.忘记密码对象库.重置密码按钮)
        if not self.wait(公共元素对象库.输入框错误信息提示.format("验证码不能为空"), 3):
            raise AssertionError("对验证码进行空值校验，未给出相应提示信息")
        self.clear(登录页对象库.验证码输入框)
        self.send_keys(登录页对象库.验证码输入框, '888890')
        self.click(登录页对象库.验证码按钮)
        self.default_content()
        self.滑块验证.滑块验证操作()
        self.click(登录页对象库.忘记密码对象库.重置密码按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("手机验证码错误，请输入正确的验证码！"), 3):
            raise AssertionError("对验证码进行非法值校验，未给出相应的提示信息")
        #手机号合法，点击获取验证码按钮
        time.sleep(61)
        self.click(登录页对象库.验证码按钮)
        if not self.wait(人机验证弹窗对象库.弹窗标题, 3):
            raise AssertionError("手机号合法，点击验证码按钮，未打开人机验证弹窗")

    def 重置密码密码输入校验(self):
        #输入没有注册过的手机号进行重置密码
        # 手机号合法，验证码合法，点击重置密码
        self.default_content()
        self.click(登录页对象库.账号密码登录)
        self.click(登录页对象库.忘记密码)
        self.default_content()
        self.wait(登录页对象库.忘记密码对象库.重置密码弹窗标题, 3)
        self.click(公共元素对象库.手机号地区列表框)
        self.click(公共元素对象库.手机号地区列表框选项.format("中国(+86)"))
        self.clear(登录页对象库.手机号输入框)
        self.send_keys(登录页对象库.手机号输入框, '18942177771')
        self.click(登录页对象库.验证码按钮)
        self.default_content()
        self.滑块验证.滑块验证操作()
        self.click(登录页对象库.验证码输入框)
        self.clear(登录页对象库.验证码输入框)
        self.send_keys(登录页对象库.验证码输入框, '888888')
        self.click(登录页对象库.忘记密码对象库.重置密码按钮)
        if not self.wait(登录页对象库.忘记密码对象库.密码输入框,3):
            raise AssertionError("输入合法的手机号和验证码，点击重置密码，未进入到设置新密码页面")
        #对密码进行空值，非法值和一致性校验
        #密码格式校验已移除
        # self.click(登录页对象库.忘记密码对象库.提交按钮)
        # if not self.wait(公共元素对象库.输入框错误信息提示.format("密码必须包含字母，数字和特殊字符，且在8-18位之间"), 3):
        #     raise AssertionError("对密码输入框进行空值校验，未出现对应的提示")
        # self.clear(登录页对象库.忘记密码对象库.密码输入框)
        # self.send_keys(登录页对象库.忘记密码对象库.密码输入框,"user")
        # self.click(登录页对象库.忘记密码对象库.提交按钮)
        # if not self.wait(公共元素对象库.输入框错误信息提示.format("密码必须包含字母，数字和特殊字符，且在8-18位之间"), 3):
        #     raise AssertionError("对密码输入框进行非法值校验，未出现对应的提示")
        self.clear(登录页对象库.忘记密码对象库.密码输入框)
        self.send_keys(登录页对象库.忘记密码对象库.密码输入框, "user@7771")
        self.clear(登录页对象库.忘记密码对象库.确认密码输入框)
        self.send_keys(登录页对象库.忘记密码对象库.确认密码输入框, "user")
        self.click(登录页对象库.忘记密码对象库.提交按钮)
        if not self.wait(公共元素对象库.输入框错误信息提示.format("两次密码不一致"), 3):
            raise AssertionError("对密码输入框进行一致性校验，未出现对应的提示")
        self.clear(登录页对象库.忘记密码对象库.确认密码输入框)
        self.send_keys(登录页对象库.忘记密码对象库.确认密码输入框, "user@7771")
        self.click(登录页对象库.忘记密码对象库.提交按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("用户不存在"), 3):
            raise AssertionError("输入没有注册过的手机号进行重置密码，系统未出现对应的提示")

    def 重置密码登录验证(self):
        self.default_content()
        self.click(登录页对象库.账号密码登录)
        self.click(登录页对象库.忘记密码)
        self.default_content()
        self.wait(登录页对象库.忘记密码对象库.重置密码弹窗标题, 3)
        self.click(公共元素对象库.手机号地区列表框)
        self.click(公共元素对象库.手机号地区列表框选项.format("中国(+86)"))
        self.clear(登录页对象库.手机号输入框)
        self.send_keys(登录页对象库.手机号输入框, '18942178871')
        self.click(登录页对象库.验证码按钮)
        self.default_content()
        self.滑块验证.滑块验证操作()
        self.click(登录页对象库.验证码输入框)
        self.clear(登录页对象库.验证码输入框)
        self.send_keys(登录页对象库.验证码输入框, '888888')
        self.click(登录页对象库.忘记密码对象库.重置密码按钮)
        self.clear(登录页对象库.忘记密码对象库.密码输入框)
        #输入有效的密码，点击提交
        num = random.randint(1000, 9999)
        self.send_keys(登录页对象库.忘记密码对象库.密码输入框, "user@"+str(num))
        self.clear(登录页对象库.忘记密码对象库.确认密码输入框)
        self.send_keys(登录页对象库.忘记密码对象库.确认密码输入框, "user@"+str(num))
        self.click(登录页对象库.忘记密码对象库.提交按钮)
        self.default_content()
        if not self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 5):
            raise AssertionError("密码重置成功，系统未给出对应提示")
        self.default_content()
        if not self.wait(登录页对象库.短信快捷登录,3):
            raise AssertionError("密码重置成功，页面未自动跳转到账号密码登录页")
        #点击短信快捷登录，当前页面跳转至短信快捷登录页面
        self.click(登录页对象库.短信快捷登录)
        self.default_content()
        if not self.wait(登录页对象库.账号密码登录,3):
            raise AssertionError("在账号密码登录页点击短信快捷登录按钮，页面自动跳转到短信快捷登录页")
        self.click(登录页对象库.账号密码登录)
        #使用重置后的密码登录，查看是否能正常登录
        self.clear(登录页对象库.账号输入框)
        self.send_keys(登录页对象库.账号输入框, '18942178871')
        self.clear(登录页对象库.密码输入框)
        self.send_keys(登录页对象库.密码输入框, "user@"+str(num))
        self.click(登录页对象库.登录按钮)
        self.default_content()
        self.滑块验证.滑块验证操作()
        self.default_content()
        if not self.wait('//div[@id="project"]', 5):
            raise AssertionError("被重置的密码无法登录到系统")





