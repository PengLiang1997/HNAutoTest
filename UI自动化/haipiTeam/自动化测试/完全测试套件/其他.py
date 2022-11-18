from HNtest.testcasesec.testcasesec import TestCaseSec
import HNtest.Secselenium.secdriver as secdriver
from HNtest.BeautifulReport.BeautifulReport import add_to_report
from 自动化测试.完全业务实现.其他业务实现 import *
from 自动化测试.基础操作.登录页面 import *

class Test_其他操作(TestCaseSec):
    @classmethod
    def setUp(cls):
        cls.driver=secdriver.Secdriver()
        cls.driver.driver.maximize_window()
        cls.其他操作=其他操作(Secdriver=cls.driver)
        cls.登录页=登录页面(Secdriver=cls.driver)
        # cls.登录页.短信快捷登录(手机号='18942178870')
        cls.登录页.账号密码登录(账号='18942178870', 密码='user@8870')

    @classmethod
    def tearDown(cls):
        cls.driver.quite()

    @add_to_report
    def test_00_创建目录引用文件再删除(self):
        '''
        模板环境，目录F1下有A , B两个文件、B引用A，先创建目录F1 ，然后上传A，再上传B（引用A），再删除目录F1， 循环再来一次
        author:黄超
        '''
        self.其他操作.创建目录再删除()