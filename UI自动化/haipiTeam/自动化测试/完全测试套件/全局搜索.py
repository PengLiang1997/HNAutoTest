from HNtest.testcasesec.testcasesec import TestCaseSec
import HNtest.Secselenium.secdriver as secdriver
from HNtest.BeautifulReport.BeautifulReport import add_to_report
from 自动化测试.完全业务实现.全局搜索业务实现 import *
from 自动化测试.基础操作.登录页面 import *


class Test_全局搜索(TestCaseSec):
    @classmethod
    def setUp(cls):
        cls.driver=secdriver.Secdriver()
        cls.driver.driver.maximize_window()
        cls.全局搜索工作区=全局搜索工作区(Secdriver=cls.driver)
        cls.登录页=登录页面(Secdriver=cls.driver)
        # cls.登录页.短信快捷登录(手机号='18942178870')
        cls.登录页.账号密码登录(账号='18942178870', 密码='user@8870')

    @classmethod
    def tearDown(cls):
        cls.driver.quite()

    @add_to_report
    def test_00_数据准备(self):
        self.全局搜索工作区.数据准备()

    @add_to_report
    def test_01_文件搜索(self):
        '''
        用例编号：
        用例描述：
                1、搜索框不输入任何条件，点击搜索，不出现搜索结果
                2、输入文件名称，点击搜索，可以搜索到指定文件
                3、如果多个项目或目录存在相同的文件，输入文件名搜索后，会展示全部符合搜索条件的文件
                4、搜索框输入文件名称、格式、版次、生命周期节点，检入检出状态、自定义属性等条件，搜索结果列表展示所有符合搜索条件的文件
                5、文件搜索支持组合条件搜索
                6、点击搜索结构列表中的文件名称，页面自动跳转到对应文件的项目目录下
                7、文件搜索结果列表显示文件名称、文件类型、文件大小、目录路径、版本、版次、生命周期状态列
        @author:彭亮
        '''
        self.全局搜索工作区.文件搜索()

    @add_to_report
    def test_02_目录搜索(self):
        '''
        用例编号：
        用例描述：
                1、输入目录名称，点击搜索,搜索结果列表显示对应的文件目录
                2、目录搜索支持目录名称模糊匹配
                3、目录搜索支持目录创建人为搜索条件
                4、目录搜索支持目录名和创建人条件组合搜索
                5、点击搜索结果列表中的文件目录名称，页面跳转到对应的项目文件目录中
                6、如果多个项目或目录存在相同的文件目录，输入文件目录名搜索后，会展示全部符合搜索条件的文件目录
                7、目录搜索结果列表显示文件目录名称、创建人、目录路径列
        @author:彭亮
        '''
        self.全局搜索工作区.目录搜索()

    @add_to_report
    def test_03_项目搜索(self):
        '''
        用例编号：
        用例描述：
                1、在搜索框中输入项目名，点击搜索，可以搜索到对应的项目
                2、项目搜索支持项目名称模糊匹配
                3、项目搜索创建人作为搜索条件进行搜索
                4、项目搜索支持项目名称和创建人组合搜索
                5、当前用户加入的项目也可以被搜索到
                6、点击搜索结果列表中的项目名称，页面跳转到对应的项目页面
                7、项目搜索结果列表显示项目名称、项目描述、创建人、项目大小、团队名称
                8、如果同时存在同名的项目和加入的项目
        @author:彭亮
        '''
        self.全局搜索工作区.项目搜索()


    @add_to_report
    def test_04_项目成员搜索(self):
        '''
        用例编号：
        用例描述：
                1、输入项目名称，可以搜索到该项目下的所有成员
                2、项目成员搜索支持项目名称模糊匹配
                3、项目成员搜索支持项目成员名称、项目名称、项目成员角色名称作为搜索条件
                4、项目成员搜索列表显示成员用户名、项目名称、权限名称、权限说明、加入日期列
        @author:彭亮
        '''
        self.全局搜索工作区.项目成员搜索()
