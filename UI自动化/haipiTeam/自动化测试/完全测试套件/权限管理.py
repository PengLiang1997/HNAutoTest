from HNtest.testcasesec.testcasesec import TestCaseSec
import HNtest.Secselenium.secdriver as secdriver
from HNtest.BeautifulReport.BeautifulReport import add_to_report
from 自动化测试.完全业务实现.权限业务实现 import *
from 自动化测试.基础操作.登录页面 import *


class Test_项目管理工作区(TestCaseSec):
    @classmethod
    def setUp(cls):
        cls.driver=secdriver.Secdriver()
        cls.driver.driver.maximize_window()
        cls.成员权限管理工作区=成员权限管理工作区(Secdriver=cls.driver)
        cls.登录页=登录页面(Secdriver=cls.driver)
        # cls.登录页.短信快捷登录(手机号='18942178870')
        cls.登录页.账号密码登录(账号='18942178870', 密码='user@8870')

    @classmethod
    def tearDown(cls):
        cls.driver.quite()

    @add_to_report
    def test_00_数据准备(self):
        self.成员权限管理工作区.数据准备()

    @add_to_report
    def test_01_PROJECT_MANAGER角色权限验证(self):
        '''
        用例编号：
        用例描述：
                1、PROJECT MANAGER角色用户拥有目录查询、目录新增、目录删除、目录修改、目录检入检出、目录打包、目录下载、上传、文件附加、版本回退的权限
        @author:彭亮
        '''
        self.成员权限管理工作区.PROJECT_MANAGER角色权限验证()

    @add_to_report
    def test_02_PROJECT_ASSISTANT角色权限验证(self):
        '''
        用例编号：
        用例描述：
                1、PROJECT ASSISTANT不具有任何文件或文件目录的权限
        @author:彭亮
        '''
        self.成员权限管理工作区.PROJECT_ASSISTANT角色权限验证()

    @add_to_report
    def test_03_DOCUMENT_MANAGER角色权限验证(self):
        '''
        用例编号：
        用例描述：
                1、DOCUMENT MANAGER角色用户拥有目录查询、目录新增、目录删除、目录修改、目录检入检出、目录打包、目录下载、上传、文件附加、版本回退的权限
        @author:彭亮
        '''
        self.成员权限管理工作区.DOCUMENT_MANAGER角色权限验证()

    @add_to_report
    def test_04_DOCUMENT_EDITOR角色权限验证(self):
        '''
        用例编号：
        用例描述：
                1、DOCUMENT EDITOR角色用户拥有目录查询、目录新增、目录删除、目录修改、目录检入检出、目录打包、目录下载、上传、文件附加、版本回退的权限
        @author:彭亮
        '''
        self.成员权限管理工作区.DOCUMENT_EDITOR角色权限验证()

    @add_to_report
    def test_05_DOCUMENT_CONSUMER角色权限验证(self):
        '''
        用例编号：
        用例描述：
                1、DOCUMENT CONSUMER角色用户拥有目录查询、目录打包和目录下载权限
        @author:彭亮
        '''
        self.成员权限管理工作区.DOCUMENT_CONSUMER角色权限验证()

    @add_to_report
    def test_06_DOCUMENT_VIEWER角色权限验证(self):
        '''
        用例编号：
        用例描述：
                1、DOCUMENT VIEWER拥有项目的查询权限
        @author:彭亮
        '''
        self.成员权限管理工作区.DOCUMENT_VIEWER角色权限验证()

    @add_to_report
    def test_07_GUEST角色权限验证(self):
        '''
        用例编号：
        用例描述：
                1、GUEST拥有项目的查询权限
        @author:彭亮
        '''
        self.成员权限管理工作区.GUEST角色权限验证()

    @add_to_report
    def test_08_撤回用户目录查询权限(self):
        '''
        用例编号：
        用例描述：
                1、对用户授予目录查看权限，使用用户登录后查看到该文件目录及其子目录下的全部资源
        @author:彭亮
        '''
        self.成员权限管理工作区.撤回用户目录查询权限()

    @add_to_report
    def test_09_授予用户目录查询权限(self):
        '''
        用例编号：
        用例描述：
                1、对用户授予目录查看权限，使用用户登录后查看到该文件目录及其子目录下的全部资源
        @author:彭亮
        '''
        self.成员权限管理工作区.授予用户目录查询权限()

    @add_to_report
    def test_10_用户目录新增权限(self):
        '''
        用例编号：
        用例描述：
                1、不对用户授予目录新增权限，使用用户登录后不能在该目录及其子目录在新增文件目录
                2、对用户授予目录新增权限，使用用户登录后可以在该目录及其子目录下新增目录
        @author:彭亮
        '''
        self.成员权限管理工作区.用户目录新增权限()

    @add_to_report
    def test_11_用户目录删除权限(self):
        '''
        用例编号：
        用例描述：
                1、不对用户授予目录删除权限，使用用户登录后不能删除该目录及其子目录以及目录下的资源
                2、对用户授予目录删除权限，使用用户登录后可以删除该目录及其子目录和目录下的任意资源
        @author:彭亮
        '''
        self.成员权限管理工作区.用户目录删除权限()

    @add_to_report
    def test_12_收回用户目录检入检出权限(self):
        '''
        用例编号：
        用例描述：
                1、对用户收回目录检出检出权限，登录该用户后，该目录及其子目录不能进行检出操作，该目录及其子目录下的任意文件不能进行检入检出操作
                2、当用户没有目录检入检出权限时，该用户不能对该目录进行批量检出操作
                3、当用户没有目录检入检出权限时，该用户不能对该目录下的任意资源进行批量检出操作
        @author:彭亮
        '''
        self.成员权限管理工作区.收回用户目录检入检出权限()

    @add_to_report
    def test_13_授予用户目录检入检出权限(self):
        '''
        用例编号：
        用例描述：
                1、对用户授予目录检出检出权限，该目录及其子目录可以进行检出操作，该目录及其子目录下的任意文件可以进行检入检出操作
        @author:彭亮
        '''
        self.成员权限管理工作区.授予用户目录检入检出权限()

    @add_to_report
    def test_14_收回用户目录打包权限(self):
        '''
        用例编号：
        用例描述：
                1、当收回用户的目录打包权限时，登录该用户后，不能对该目录进行打包操作
                2、当收回用户的目录打包权限时，登录该用户后，不能对该目录进行批量打包操作
                3、当收回用户的目录打包权限时，登录该用户后，不能对该目录下的任意资源进行批量打包操作

        @author:彭亮
        '''
        self.成员权限管理工作区.收回用户目录打包权限()

    @add_to_report
    def test_15_授予用户目录打包权限(self):
        '''
        用例编号：
        用例描述：
                1、当授予用户目录打包权限，登录该用户后，可以对该目录进行打包操作
                2、当授予用户目录打包权限，登录该用户后，可以对该目录进行批量打包操作
                3、当授予用户目录打包权限，登录该用户后，可以对该目录下的任意资源进行打包操作
                4、当授予用户目录打包权限，登录该用户后，可以对该目录下的任意资源进行批量打包操作

        @author:彭亮
        '''
        self.成员权限管理工作区.授予用户目录打包权限()

    @add_to_report
    def test_16_收回用户目录下载权限(self):
        '''
        用例编号：
        用例描述：
                1、当收回用户的目录下载权限时，登录该用户后，不能对该目录下的任意文件进行下载操作
                2、当收回用户的目录下载权限时，登录该用户后，不能对该目录下的任意文件的历史版本文件进行下载操作
                3、当收回用户的目录下载权限时，登录该用户后，不能对该目录下子目录的任意文件进行下载操作
                4、当收回用户的目录下载权限时，登录该用户后，不能对该目录下子目录的任意文件的历史版本文件进行下载操作
        @author:彭亮
        '''
        self.成员权限管理工作区.收回用户目录下载权限()

    @add_to_report
    def test_17_授予用户目录下载权限(self):
        '''
        用例编号：
        用例描述：
                1、当授予用户的目录下载权限时，登录该用户后，对该目录下的任意文件进行下载操作
                2、当授予用户的目录下载权限时，登录该用户后，对该目录下的任意文件的历史版本文件进行下载操作
                3、当授予用户的目录下载权限时，登录该用户后，对该目录下子目录的任意文件进行下载操作
                4、当授予用户的目录下载权限时，登录该用户后，对该目录下子目录的任意文件的历史版本文件进行下载操作
        @author:彭亮
        '''
        self.成员权限管理工作区.授予用户目录下载权限()

    @add_to_report
    def test_18_用户目录上传权限(self):
        '''
        用例编号：
        用例描述：
                1、当收回用户的目录下上传权限时，登录该用户后，不能在该目录及其子目录下进行上传操作
                2、当授予用户目录上传权限，登录该用户后，可以在该目录及其子目录下进行上传操作
        @author:彭亮
        '''
        self.成员权限管理工作区.用户目录上传权限()

    @add_to_report
    def test_19_用户文件附加权限(self):
        '''
        用例编号：
        用例描述：
                1、当收回用户的文件附加权限时，登录该用户后，不能在该目录及其子目录下文件进行文件附加操作
                2、当授予用户文件附加权限，登录该用户后，可以在该目录及其子目录下文件进行文件附加操作
        @author:彭亮
        '''
        self.成员权限管理工作区.用户文件附加权限()

    @add_to_report
    def test_20_用户改变文件状态权限(self):
        '''
        用例编号：
        用例描述：
                1、当收回用户改变生命周期状态权限时，登录该用户后，不能在该目录及其子目录下文件进行改变生命周期状态操作
                2、当授予用户改变生命周期状态权限，登录该用户后，可以在该目录及其子目录下文件进行改变生命周期状态操作
        '''
        self.成员权限管理工作区.用户改变文件状态权限()


class Test_文件目录设置工作区(TestCaseSec):
    @classmethod
    def setUp(cls):
        cls.driver=secdriver.Secdriver()
        cls.driver.driver.maximize_window()
        cls.目录权限管理工作区=目录权限管理工作区(Secdriver=cls.driver)
        cls.登录页=登录页面(Secdriver=cls.driver)
        # cls.登录页.短信快捷登录(手机号='18942178870')
        cls.登录页.账号密码登录(账号='18942178870', 密码='user@8870')

    @classmethod
    def tearDown(cls):
        cls.driver.quite()

    @add_to_report
    def test_00_数据准备(self):
        self.目录权限管理工作区.数据准备()

    @add_to_report
    def test_01_撤回用户目录查询权限(self):
        '''
        用例编号：
        用例描述：
                1、对用户授予目录查看权限，使用用户登录后查看到该文件目录及其子目录下的全部资源
        @author:彭亮
        '''
        self.目录权限管理工作区.撤回用户目录查询权限()

    @add_to_report
    def test_02_授予用户目录查询权限(self):
        '''
        用例编号：
        用例描述：
                1、对用户授予目录查看权限，使用用户登录后查看到该文件目录及其子目录下的全部资源
        @author:彭亮
        '''
        self.目录权限管理工作区.授予用户目录查询权限()

    @add_to_report
    def test_03_用户目录新增权限(self):
        '''
        用例编号：
        用例描述：
                1、不对用户授予目录新增权限，使用用户登录后不能在该目录及其子目录在新增文件目录
                2、对用户授予目录新增权限，使用用户登录后可以在该目录及其子目录下新增目录
        @author:彭亮
        '''
        self.目录权限管理工作区.用户目录新增权限()

    @add_to_report
    def test_04_用户目录删除权限(self):
        '''
        用例编号：
        用例描述：
                1、不对用户授予目录删除权限，使用用户登录后不能删除该目录及其子目录以及目录下的资源
                2、对用户授予目录删除权限，使用用户登录后可以删除该目录及其子目录和目录下的任意资源
        @author:彭亮
        '''
        self.目录权限管理工作区.用户目录删除权限()

    @add_to_report
    def test_05_收回用户目录检入检出权限(self):
        '''
        用例编号：
        用例描述：
                1、对用户收回目录检出检出权限，登录该用户后，该目录及其子目录不能进行检出操作，该目录及其子目录下的任意文件不能进行检入检出操作
                2、当用户没有目录检入检出权限时，该用户不能对该目录进行批量检出操作
                3、当用户没有目录检入检出权限时，该用户不能对该目录下的任意资源进行批量检出操作
        @author:彭亮
        '''
        self.目录权限管理工作区.收回用户目录检入检出权限()

    @add_to_report
    def test_06_授予用户目录检入检出权限(self):
        '''
        用例编号：
        用例描述：
                1、对用户授予目录检出检出权限，该目录及其子目录可以进行检出操作，该目录及其子目录下的任意文件可以进行检入检出操作
        @author:彭亮
        '''
        self.目录权限管理工作区.授予用户目录检入检出权限()

    @add_to_report
    def test_07_收回用户目录打包权限(self):
        '''
        用例编号：
        用例描述：
                1、当收回用户的目录打包权限时，登录该用户后，不能对该目录进行打包操作
                2、当收回用户的目录打包权限时，登录该用户后，不能对该目录进行批量打包操作
                3、当收回用户的目录打包权限时，登录该用户后，不能对该目录下的任意资源进行批量打包操作

        @author:彭亮
        '''
        self.目录权限管理工作区.收回用户目录打包权限()

    @add_to_report
    def test_08_授予用户目录打包权限(self):
        '''
        用例编号：
        用例描述：
                1、当授予用户目录打包权限，登录该用户后，可以对该目录进行打包操作
                2、当授予用户目录打包权限，登录该用户后，可以对该目录进行批量打包操作
                3、当授予用户目录打包权限，登录该用户后，可以对该目录下的任意资源进行打包操作
                4、当授予用户目录打包权限，登录该用户后，可以对该目录下的任意资源进行批量打包操作

        @author:彭亮
        '''
        self.目录权限管理工作区.授予用户目录打包权限()

    @add_to_report
    def test_09_收回用户目录下载权限(self):
        '''
        用例编号：
        用例描述：
                1、当收回用户的目录下载权限时，登录该用户后，不能对该目录下的任意文件进行下载操作
                2、当收回用户的目录下载权限时，登录该用户后，不能对该目录下的任意文件的历史版本文件进行下载操作
                3、当收回用户的目录下载权限时，登录该用户后，不能对该目录下子目录的任意文件进行下载操作
                4、当收回用户的目录下载权限时，登录该用户后，不能对该目录下子目录的任意文件的历史版本文件进行下载操作
        @author:彭亮
        '''
        self.目录权限管理工作区.收回用户目录下载权限()

    @add_to_report
    def test_10_授予用户目录下载权限(self):
        '''
        用例编号：
        用例描述：
                1、当授予用户的目录下载权限时，登录该用户后，对该目录下的任意文件进行下载操作
                2、当授予用户的目录下载权限时，登录该用户后，对该目录下的任意文件的历史版本文件进行下载操作
                3、当授予用户的目录下载权限时，登录该用户后，对该目录下子目录的任意文件进行下载操作
                4、当授予用户的目录下载权限时，登录该用户后，对该目录下子目录的任意文件的历史版本文件进行下载操作
        @author:彭亮
        '''
        self.目录权限管理工作区.授予用户目录下载权限()

    @add_to_report
    def test_11_用户目录上传权限(self):
        '''
        用例编号：
        用例描述：
                1、当收回用户的目录下上传权限时，登录该用户后，不能在该目录及其子目录下进行上传操作
                2、当授予用户目录上传权限，登录该用户后，可以在该目录及其子目录下进行上传操作
        @author:彭亮
        '''
        self.目录权限管理工作区.用户目录上传权限()

    @add_to_report
    def test_12_用户文件附加权限(self):
        '''
        用例编号：
        用例描述：
                1、当收回用户的文件附加权限时，登录该用户后，不能在该目录及其子目录下文件进行文件附加操作
                2、当授予用户文件附加权限，登录该用户后，可以在该目录及其子目录下文件进行文件附加操作
        @author:彭亮
        '''
        self.目录权限管理工作区.用户文件附加权限()