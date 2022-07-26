from HNtest.testcasesec.testcasesec import TestCaseSec
import HNtest.Secselenium.secdriver as secdriver
from HNtest.BeautifulReport.BeautifulReport import add_to_report
from 自动化测试.完全业务实现.登录页业务实现 import *

class Test_登录页(TestCaseSec):
    @classmethod
    def setUp(cls):
        cls.driver=secdriver.Secdriver()
        cls.driver.driver.maximize_window()
        cls.登录页=登录页(Secdriver=cls.driver)

    @classmethod
    def tearDown(cls):
        cls.driver.quite()

    @add_to_report
    def test_00_数据准备(self):
        self.登录页.数据准备()

    @add_to_report
    def test_01_手机号验证码校验(self):
        '''
        用例编号：dly_030、dly_031、dly_032、dly_033、dly_034
        用例描述：
                1、点击下拉按钮，可以查看并选择对应区域号码
                2、对手机号进行空值和非法值校验
                3、对验证码进行空值和非法值校验
                4、手机号为空或非法是点击获取验证码按钮
                5、正确手机号验证码登录系统
        @author:彭亮
        '''
        self.登录页.手机号验证码校验()

    @add_to_report
    def test_02_账号密码校验(self):
        '''
        用例编号：dly_001、dly_002、dly_003、dly_004、dly_005、dly_013
        用例描述：
                1、点击账号密码登录，当前页面跳转至账号密码登录页面
                2、对账号进行空值、超长、非法值校验
                3、对密码进行空值，非法值校验
                4、输入有效账号密码，点击登录后关闭人机验证弹窗
                5、点击短信快捷登录，当前页面跳转至短信快捷登录页面
                6、错误密码登录系统
        @author:彭亮
        '''
        self.登录页.账号密码校验()

    @add_to_report
    def test_03_重置密码手机号验证码校验(self):
        '''
        用例编号：dly_014、dly_015、dly_016、dly_017、dly_018、dly_019
        用例描述：
                1、对手机号进行空值和非法值校验
                2、对验证码进行空值和非法值校验
                3、手机号合法，点击获取验证码按钮
                4、手机号为空或非法是点击获取验证码按钮
                5、点击忘记密码按钮进入重置密码页面
        @author:彭亮
        '''
        self.登录页.重置密码手机号验证码校验()

    @add_to_report
    def test_04_重置密码密码输入校验(self):
        '''
        用例编号：dly_022、dly_024、dly_026
        用例描述：
                1、输入没有注册过的手机号进行重置密码
                2、手机号合法，验证码合法，点击重置密码
                3、对密码进行空值，非法值和一致性校验
                4、输入有效的密码，点击提交
                5、点击短信快捷登录，当前页面跳转至短信快捷登录页面
                6、使用重置后的密码登录，查看是否能正常登录
            @author:彭亮
        '''
        self.登录页.重置密码密码输入校验()

    @add_to_report
    def test_05_重置密码登录验证(self):
        '''
        用例编号：dly_025、dly_028、dly_027
        用例描述：
                1、输入有效的密码，点击提交
                2、点击短信快捷登录，当前页面跳转至短信快捷登录页面
                3、使用重置后的密码登录，查看是否能正常登录
            @author:彭亮
        '''
        self.登录页.重置密码登录验证()