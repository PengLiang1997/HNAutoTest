from HNtest.testcasesec.testcasesec import TestCaseSec
import HNtest.Secselenium.secdriver as secdriver
from HNtest.BeautifulReport.BeautifulReport import add_to_report
from 自动化测试.完全业务实现.收藏业务实现 import *
from 自动化测试.基础操作.登录页面 import *

class Test_收藏页面(TestCaseSec):
    @classmethod
    def setUp(cls):
        cls.driver=secdriver.Secdriver()
        cls.driver.driver.maximize_window()
        cls.收藏页面=收藏页面(Secdriver=cls.driver)
        cls.登录页=登录页面(Secdriver=cls.driver)
        # cls.登录页.短信快捷登录(手机号='18942178870')
        cls.登录页.账号密码登录(账号='18942178870',密码='user@8870')

    @classmethod
    def tearDown(cls):
        cls.driver.quite()

    @add_to_report
    def test_00_数据准备(self):
        self.收藏页面.数据准备()

    @add_to_report
    def test_01_收藏过滤显示(self):
        '''
        用例编号：
        用例描述：
                1、点击过滤条件列表，点击所有收藏，收藏列表显示部收藏的资源
                2、点击过滤条件列表，点击收藏的项目，收藏列表显示收藏的项目资源
                3、点击过滤条件列表，点击收藏的目录，收藏列表显示收藏的文件目录
                4、点击过滤条件列表，点击收藏的文件，收藏列表显示收藏的文件
        @author:彭亮
        '''
        self.收藏页面.收藏过滤显示()

    @add_to_report
    def test_02_资源行操作(self):
        '''
        用例编号：
        用例描述：
                1、点击资源行操作中的查看按钮，可以查看到收藏的资源
                2、点击收藏的项目的行操作中的取消收藏按钮，提示取消收藏成功
                3、点击收藏的目录的行操作中的取消收藏按钮，提示取消收藏成功
                4、点击收藏的文件的行操作中的取消收藏按钮，提示取消收藏成功
        @author:彭亮
        '''
        self.收藏页面.资源行操作()

