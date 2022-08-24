import time
from ..元素对象库.公共元素 import *
from ..元素对象库.首页对象库 import *
from ..基础操作.用户信息页面 import *
from ..基础操作.进入到操作位置 import *
from 自动化测试.基础操作.登录页面 import *
from HNtest.testcasesec.testcasesec import page
from HNtest.Secselenium.secdriver import Secdriver
from selenium.webdriver.common.keys import Keys

class 用户信息业务实现(page):
    def __init__(self,Secdriver = None):
        page.__init__(self,secdriver=Secdriver)
        self.用户信息页面=用户信息页面(Secdriver=Secdriver)
        self.滑块验证 = 滑块验证(Secdriver=self.driver)
        self.登录页面 = 登录页面(Secdriver=self.driver)
    def 数据准备(self):
        #创建用户18942178870 pw:user8870 name:user8870 绑定邮箱123456@qq.com
        self.用户信息页面.进入账号信息页面()
        self.用户信息页面.维护用户账号信息(电子邮箱='123456@qq.com',用户名='user8870',原密码="user@8870", 用户密码='user@8870')
        #创建用户17789371421 pw:user1421 name:user1421
        self.登录页面.退出登录()
        # self.登录页面.短信快捷登录(手机号='17789371421')
        self.登录页面.账号密码登录(账号='17789371421',密码='user@1421')
        self.用户信息页面.进入账号信息页面()
        self.用户信息页面.维护用户账号信息(用户名='user1421',原密码="user@1421", 用户密码='user@1421')
        # 注册账号2:18942178871 pw:user0000
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        # self.登录页面.短信快捷登录(手机号='18942178871')
        self.用户信息页面.进入账号信息页面()
        self.用户信息页面.维护用户账号信息(用户名='user8871',原密码="user@8871", 用户密码='user@0000')

    def 用户基本信息校验(self):
        self.用户信息页面.进入基本信息页面()
        #点击更换头像，选择非图片文件，点击确定
        self.用户信息页面.更换头像(文件路径=['TestData', 'FrontData', '用户信息', '头像2.txt'])
        if not self.wait(公共元素对象库.系统提示信息弹框.format("请上传图片类型"),3):
            raise AssertionError("头像上传非图片文件，系统未出现提示信息")
        #对用户昵称进行空值、超长校验
        time.sleep(3)
        self.click(公共元素对象库.输入框.format("用户昵称"))
        element=self.driver.getelement(公共元素对象库.输入框.format("用户昵称"))
        element.send_keys(Keys.CONTROL+'a')
        element.send_keys(Keys.BACKSPACE)
        self.move_to_by_pyautogui(公共元素对象库.输入框.format("用户昵称"))
        self.scroll_by_pyautogui(-30)
        self.click(用户信息对象库.账号信息对象库.保存)
        if not self.wait(公共元素对象库.输入框错误信息提示.format("请输入昵称"),3):
            raise AssertionError("用户昵称未空时点击保存，未出现对应的提示信息")
        self.clear(公共元素对象库.输入框.format("用户昵称"))
        self.send_keys(公共元素对象库.输入框.format("用户昵称"),"usernametoolongtest12345678")
        self.click(用户信息对象库.账号信息对象库.保存)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("操作失败"), 3):
            raise AssertionError("用户名昵称超长时点击保存，系统未出现提示信息")
        self.clear(公共元素对象库.输入框.format("用户昵称"))
        self.send_keys(公共元素对象库.输入框.format("用户昵称"), "user8870")
        self.move_to_by_pyautogui(公共元素对象库.输入框.format("用户昵称"))
        self.scroll_by_pyautogui(-30)
        self.click(用户信息对象库.账号信息对象库.保存)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("保存成功"), 3):
            raise AssertionError("用户名昵称超长时点击保存，系统未出现提示信息")
        #点击下拉列表，点击可以选择对应的国家
        self.click(公共元素对象库.列表框.format("国家"))
        if not self.wait(公共元素对象库.列表框选项.format("中国"),3):
            raise AssertionError("点击国家列表框，未发现对应的列表框选项")
        self.click(公共元素对象库.列表框选项.format("中国"))
        #输入对应合法信息后点击保存，系统提示保存成功
        #姓超长校验
        self.clear(用户信息对象库.基本信息对象库.姓输入框)
        self.send_keys(用户信息对象库.基本信息对象库.姓输入框, "usernametoolongtest12345678")
        self.move_to_by_pyautogui(公共元素对象库.输入框.format("用户昵称"))
        self.scroll_by_pyautogui(-30)
        self.click(用户信息对象库.账号信息对象库.保存)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("操作失败"), 3):
            raise AssertionError("用户姓名的姓超长时点击保存，系统未出现提示信息")
        self.clear(用户信息对象库.基本信息对象库.姓输入框)
        self.send_keys(用户信息对象库.基本信息对象库.姓输入框,"admin")
        # 名超长校验
        self.clear(用户信息对象库.基本信息对象库.名输入框)
        self.send_keys(用户信息对象库.基本信息对象库.名输入框, "usernametoolongtest12345678")
        self.move_to_by_pyautogui(公共元素对象库.输入框.format("用户昵称"))
        self.scroll_by_pyautogui(-30)
        self.click(用户信息对象库.账号信息对象库.保存)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("操作失败"), 3):
            raise AssertionError("用户姓名的名超长时点击保存，系统未出现提示信息")
        self.clear(用户信息对象库.基本信息对象库.名输入框)
        self.send_keys(用户信息对象库.基本信息对象库.名输入框, "admin")
        #职位名称超长校验
        self.clear(公共元素对象库.输入框.format("职位"))
        self.send_keys(公共元素对象库.输入框.format("职位"), "usernametoolonusernametoolongtest12345678usernametoolongtest12345678gtest12345678")
        self.move_to_by_pyautogui(公共元素对象库.输入框.format("用户昵称"))
        self.scroll_by_pyautogui(-30)
        self.click(用户信息对象库.账号信息对象库.保存)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("操作失败"), 3):
            raise AssertionError("用户名职位超长时点击保存，系统未出现提示信息")
        self.clear(公共元素对象库.输入框.format("职位"))
        self.send_keys(公共元素对象库.输入框.format("职位"), "用户职位")
        #用户办公电话超长校验
        self.clear(公共元素对象库.输入框.format("办公电话"))
        self.send_keys(公共元素对象库.输入框.format("办公电话"),"usernametoolongtest12345678usernametoolongtest12345678usernametoolongtest12345678gtest12345678")
        self.move_to_by_pyautogui(公共元素对象库.输入框.format("用户昵称"))
        self.scroll_by_pyautogui(-30)
        self.click(用户信息对象库.账号信息对象库.保存)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("操作失败"), 3):
            raise AssertionError("用户名办公电话超长时点击保存，系统未出现提示信息")
        self.clear(公共元素对象库.输入框.format("办公电话"))
        self.send_keys(公共元素对象库.输入框.format("办公电话"), "12345678901")
        #公司地址超长校验
        self.clear(公共元素对象库.输入框.format("办公地址"))
        self.send_keys(公共元素对象库.输入框.format("办公地址"),
                       "usernametoolonusernametoolongtest12345678usernametoolongtest12345678gtest12345678usernametoolongtest12345678gtest12345678")
        self.send_keys(公共元素对象库.输入框.format("办公地址"),
                       "usernametoolonusernametoolongtest12345678usernametoolongtest12345678gtest12345678usernametoolongtest12345678gtest12345678")
        self.move_to_by_pyautogui(公共元素对象库.输入框.format("用户昵称"))
        self.scroll_by_pyautogui(-30)
        self.click(用户信息对象库.账号信息对象库.保存)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("操作失败"), 3):
            raise AssertionError("用户名公司地址超长时点击保存，系统未出现提示信息")
        self.clear(公共元素对象库.输入框.format("办公地址"))
        self.send_keys(公共元素对象库.输入框.format("办公地址"), "办公地址")
        #公司名称超长校验
        self.clear(公共元素对象库.输入框.format("公司名称"))
        self.send_keys(公共元素对象库.输入框.format("公司名称"),
                       "usernametoolonusernametoolongtest12345678usernametoolongtest12345678gtest12345678usernametoolongtest12345678gtest12345678")
        self.move_to_by_pyautogui(公共元素对象库.输入框.format("用户昵称"))
        self.scroll_by_pyautogui(-30)
        self.click(用户信息对象库.账号信息对象库.保存)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("操作失败"), 3):
            raise AssertionError("用户名公司名称超长时点击保存，系统未出现提示信息")
        self.clear(公共元素对象库.输入框.format("公司名称"))
        self.send_keys(公共元素对象库.输入框.format("公司名称"), "公司名称")
        #城市超长校验
        self.clear(公共元素对象库.输入框.format("城市"))
        self.send_keys(公共元素对象库.输入框.format("城市"),
                       "usernametoolonusernametoolongtest12345678usernametoolongtest12345678gtest12345678usernametoolongtest12345678gtest12345678")
        self.move_to_by_pyautogui(公共元素对象库.输入框.format("用户昵称"))
        self.scroll_by_pyautogui(-30)
        self.click(用户信息对象库.账号信息对象库.保存)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("操作失败"), 3):
            raise AssertionError("用户名城市超长时点击保存，系统未出现提示信息")
        self.clear(公共元素对象库.输入框.format("城市"))
        self.send_keys(公共元素对象库.输入框.format("城市"), "城市")
        #省/市/自治区下拉校验
        self.click(公共元素对象库.列表框.format("省/直辖市/自治区"))
        if not self.wait(公共元素对象库.列表框选项.format("上海"), 3):
            raise AssertionError("点击省/直辖市/自治区列表框，未发现对应的列表框选项")
        self.click(公共元素对象库.列表框选项.format("上海"))
        #邮编校验
        self.clear(公共元素对象库.输入框.format("邮编"))
        self.send_keys(公共元素对象库.输入框.format("邮编"),"usernametoolongtest12345678usernametoolongtest12345678gtest12345678")
        self.move_to_by_pyautogui(公共元素对象库.输入框.format("用户昵称"))
        self.scroll_by_pyautogui(-30)
        self.click(用户信息对象库.账号信息对象库.保存)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("操作失败"), 3):
            raise AssertionError("用户名邮编超长时点击保存，系统未出现提示信息")
        self.clear(公共元素对象库.输入框.format("邮编"))
        self.send_keys(公共元素对象库.输入框.format("邮编"), "123456")
        #合法信息点击保存是否保存成功
        self.move_to_by_pyautogui(公共元素对象库.输入框.format("用户昵称"))
        self.scroll_by_pyautogui(-30)
        self.click(用户信息对象库.账号信息对象库.保存)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("保存成功"), 3):
            raise AssertionError("当用户信息输入合法时点击保存，系统未出现保存成功提示信息")

    def 用户切换手机号(self):
        self.用户信息页面.进入账号信息页面()
        # 手机号输入框处于不可编辑状态
        if not self.wait(用户信息对象库.账号信息对象库.非编辑状态手机号输入框,3):
            raise AssertionError("在账号信息页面未查看到处于非编辑状态的手机号输入框")
        #点击切换手机号按钮，弹出切换手机号弹窗
        self.click(用户信息对象库.账号信息对象库.切换手机号按钮)
        self.default_content()
        if not self.wait(用户信息对象库.账号信息对象库.切换手机号弹窗保存, 3):
            raise AssertionError("点击切换手机号按钮未弹出切换手机号弹窗")
        #手机号设置为已经注册的手机号，输入验证码点击保存
        self.clear(登录页对象库.手机号输入框)
        self.send_keys(登录页对象库.手机号输入框, "18942178870")
        self.click(登录页对象库.验证码按钮)
        self.default_content()
        self.滑块验证.滑块验证操作()
        self.wait(用户信息对象库.账号信息对象库.切换手机号弹窗保存, 3)
        self.clear(登录页对象库.验证码输入框)
        self.send_keys(登录页对象库.验证码输入框, "888888")
        self.click(用户信息对象库.账号信息对象库.切换手机号弹窗保存, 3)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("已被注册"),3):
            raise AssertionError("手机号设置为已经注册的手机号，输入验证码点击保存,未出现手机号已存在的提示信息")

    def 绑定邮箱(self):
        self.用户信息页面.进入账号信息页面()
        #空值校验
        if self.wait(用户信息对象库.账号信息对象库.绑定邮箱按钮,3):
            self.click(公共元素对象库.输入框.format("电子邮件"))
            element = self.driver.getelement(公共元素对象库.输入框.format("电子邮件"))
            element.send_keys(Keys.CONTROL + 'a')
            element.send_keys(Keys.BACKSPACE)
            self.click(用户信息对象库.账号信息对象库.绑定邮箱按钮)
            if not self.wait(公共元素对象库.系统提示信息弹框.format("请填写邮箱"),2):
                raise AssertionError("未填写电子邮箱，点击绑定电子邮箱，系统未给出提示")
            #非法值校验
            self.clear(公共元素对象库.输入框.format("电子邮件"))
            self.send_keys(公共元素对象库.输入框.format("电子邮件"),"123456@ddd")
            self.click(用户信息对象库.账号信息对象库.绑定邮箱按钮)
            if not self.wait(公共元素对象库.输入框错误信息提示.format("请输入正确的邮箱"),3):
                raise AssertionError("输入电子邮箱格式非法，点击绑定电子邮箱，系统未给出提示")
            #邮箱唯一性校验
            self.clear(公共元素对象库.输入框.format("电子邮件"))
            self.send_keys(公共元素对象库.输入框.format("电子邮件"), "123456@qq.com")
            self.click(用户信息对象库.账号信息对象库.绑定邮箱按钮)
            if not self.wait(公共元素对象库.系统提示信息弹框.format("当前邮箱123456@qq.com已被注册！"),3):
                raise AssertionError("输入已被绑定的邮箱，点击绑定邮箱，系统未给出提示")
        else:
            self.click(用户信息对象库.账号信息对象库.切换邮箱按钮)
            self.click(对话框对象库.对话框按钮.format("切换邮箱","保存"))
            if not self.wait(公共元素对象库.输入框错误信息提示.format("邮箱不能为空"), 2):
                raise AssertionError("未填写电子邮箱，保存电子邮箱，系统未给出提示")
            self.clear(公共元素对象库.输入框.format("新邮箱"))
            self.send_keys(公共元素对象库.输入框.format("新邮箱"), "123456@ddd")
            self.click(对话框对象库.对话框按钮.format("切换邮箱", "保存"))
            if not self.wait(公共元素对象库.输入框错误信息提示.format("请输入正确的邮箱"), 3):
                raise AssertionError("输入电子邮箱格式非法，点击绑定电子邮箱，系统未给出提示")
            # 邮箱唯一性校验
            self.clear(公共元素对象库.输入框.format("新邮箱"))
            self.send_keys(公共元素对象库.输入框.format("新邮箱"), "123456@qq.com")
            self.click(对话框对象库.对话框按钮.format("切换邮箱", "保存"))
            if not self.wait(公共元素对象库.系统提示信息弹框.format("已被注册"), 3):
                raise AssertionError("输入已被绑定的邮箱，点击绑定邮箱，系统未给出提示")


    def 用户名密码校验(self):
        self.用户信息页面.进入账号信息页面()
        #对用户名进行空值、超长、唯一性校验
        element = self.driver.getelement(公共元素对象库.输入框.format("用户名"))
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.BACKSPACE)
        self.click(用户信息对象库.账号信息对象库.保存)
        if not self.wait(公共元素对象库.输入框错误信息提示.format("用户名不能为空"),3):
            raise AssertionError("用户名为空时，点击保存，没有提示信息")
        self.clear(公共元素对象库.输入框.format("用户名"))
        self.send_keys(公共元素对象库.输入框.format("用户名"),"testusernametoolong1234567890testusernametoolong1234567890")
        self.send_keys(公共元素对象库.输入框.format("用户密码"), "user8870")
        self.send_keys(公共元素对象库.输入框.format("确认密码"), "user8870")
        self.click(用户信息对象库.账号信息对象库.保存)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("未知错误"), 3):
            raise AssertionError("用户名超长时，点击保存，没有提示信息")
        self.clear(公共元素对象库.输入框.format("用户名"))
        self.send_keys(公共元素对象库.输入框.format("用户名"), "user8870")
        self.click(用户信息对象库.账号信息对象库.保存)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("用户名已被注册，请更换用户名！"), 3):
            raise AssertionError("用户名输入已经被注册的用户名时，点击保存，没有提示信息")
        self.clear(公共元素对象库.输入框.format("用户名"))
        self.send_keys(公共元素对象库.输入框.format("用户名"), "user8871")
        #对密码进行空值、非法、一致性校验
        element = self.driver.getelement(公共元素对象库.输入框.format("用户密码"))
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.BACKSPACE)
        self.click(用户信息对象库.账号信息对象库.保存)
        if not self.wait(公共元素对象库.输入框错误信息提示.format("密码长度至少为8，至少含有一个字母和一个数字"), 3):
            raise AssertionError("密码为空时，点击保存，没有提示信息")
        self.clear(公共元素对象库.输入框.format("用户密码"))
        self.send_keys(公共元素对象库.输入框.format("用户密码"), "user")
        self.click(用户信息对象库.账号信息对象库.保存)
        if not self.wait(公共元素对象库.输入框错误信息提示.format("密码长度至少为8，至少含有一个字母和一个数字"), 3):
            raise AssertionError("密码未非法格式时，点击保存，没有提示信息")
        self.clear(公共元素对象库.输入框.format("用户密码"))
        self.send_keys(公共元素对象库.输入框.format("用户密码"), "user8871")
        self.clear(公共元素对象库.输入框.format("确认密码"))
        self.send_keys(公共元素对象库.输入框.format("确认密码"), "user8870")
        self.click(用户信息对象库.账号信息对象库.保存)
        if not self.wait(公共元素对象库.输入框错误信息提示.format("两次密码不一致"), 3):
            raise AssertionError("两次密码不一致时，点击保存，没有提示信息")
        #维护用户账号信息后，使用账号密码是否能登录
        self.clear(公共元素对象库.输入框.format("确认密码"))
        self.send_keys(公共元素对象库.输入框.format("确认密码"), "user8871")
        self.click(用户信息对象库.账号信息对象库.保存)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 3):
            raise AssertionError("所有信息合法，点击保存时，未出现保存成功提示")
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='user8871',密码='user8871')
        if not self.wait(首页对象库.项目,30):
            raise AssertionError("用户账号信息维护成功后，不能使用账号密码登录")




