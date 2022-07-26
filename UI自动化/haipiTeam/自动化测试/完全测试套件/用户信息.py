from HNtest.testcasesec.testcasesec import TestCaseSec
import HNtest.Secselenium.secdriver as secdriver
from HNtest.BeautifulReport.BeautifulReport import add_to_report
from 自动化测试.完全业务实现.用户信息业务实现 import *
from 自动化测试.基础操作.登录页面 import *

class Test_用户信息(TestCaseSec):
    @classmethod
    def setUp(cls):
        cls.driver=secdriver.Secdriver()
        cls.driver.driver.maximize_window()
        cls.用户信息=用户信息业务实现(Secdriver=cls.driver)
        cls.登录页=登录页面(Secdriver=cls.driver)
        cls.登录页.短信快捷登录(手机号='18942178870')

    @classmethod
    def tearDown(cls):
        cls.driver.quite()

    @add_to_report
    def test_00_数据准备(self):
        self.用户信息.数据准备()

    @add_to_report
    def test_01_用户基本信息校验(self):
        '''
        用例编号：yhxx_001~yhxx_013
        用例描述：
                1、点击更换头像，选择头像图片，点击确定
                2、点击更换头像，选择非图片文件，点击确定
                3、对用户昵称进行空值、超长校验
                4、点击下拉列表，点击可以选择对应的国家
                5、输入对应信息后点击保存，系统提示保存成功
        @author:彭亮
        '''
        self.用户信息.用户基本信息校验()

    @add_to_report
    def test_02_用户切换手机号(self):
        '''
        用例编号：yhxx_014、yhxx_015、yhxx_026
        用例描述：
                1、手机号输入框处于不可编辑状态
                2、点击切换手机号按钮，弹出切换手机号弹窗
                3、手机号设置为已经注册的手机号，输入验证码点击保存
        @author:彭亮
        '''
        self.用户信息.用户切换手机号()

    @add_to_report
    def test_03_绑定邮箱(self):
        '''
        用例编号：yhxx_027
        用例描述：
                1、对电子邮件进行空值和非法值校验和唯一性校验
        @author:彭亮
        '''
        self.用户信息.绑定邮箱()

    @add_to_report
    def test_04_用户名密码校验(self):
        '''
        用例编号：yhxx_028~yhxx_033
        用例描述：
                1、对用户名进行空值、超长、唯一性校验
                2、对密码进行空值、非法、一致性校验
                3、维护用户账号信息后，使用账号密码是否能登录
        @author:彭亮
        '''
        self.登录页.退出登录()
        self.登录页.短信快捷登录(手机号='18942178871')
        self.用户信息.用户名密码校验()




