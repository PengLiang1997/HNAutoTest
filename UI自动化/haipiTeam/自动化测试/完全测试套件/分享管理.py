from HNtest.testcasesec.testcasesec import TestCaseSec
import HNtest.Secselenium.secdriver as secdriver
from HNtest.BeautifulReport.BeautifulReport import add_to_report
from 自动化测试.完全业务实现.分享管理业务实现 import *
from 自动化测试.基础操作.登录页面 import *

class Test_分享管理工作区(TestCaseSec):
    @classmethod
    def setUp(cls):
        cls.driver=secdriver.Secdriver()
        cls.driver.driver.maximize_window()
        cls.分享管理工作区=分享管理工作区(Secdriver=cls.driver)
        cls.登录页=登录页面(Secdriver=cls.driver)
        # cls.登录页.短信快捷登录(手机号='18942178870')
        cls.登录页.账号密码登录(账号='18942178870', 密码='user@8870')

    @classmethod
    def tearDown(cls):
        cls.driver.quite()

    @add_to_report
    def test_00_数据准备(self):
        '''
        用例编号：
        用例描述：
                1、
        @author:彭亮
        '''
        self.分享管理工作区.数据准备()

    @add_to_report
    def test_01_分享列表显示(self):
        '''
        用例编号：
        用例描述：
                1、在文件目录列表中创建分享后，在分享列表中可以查看到该分享
                2、分享记录列表中有分享内容、类型、过期时间、是否生效、分享创建人、访问记录、访问次数统计、操作列
        @author:彭亮
        '''
        self.分享管理工作区.分享列表显示()

    @add_to_report
    def test_02_查看分享内容(self):
        '''
        用例编号：
        用例描述：
                1、点击分享记录名称，可以进入到分享页，查看到分享文件
                2、过期的分享记录分享名称是置灰的
        @author:彭亮
        '''
        self.分享管理工作区.查看分享内容()

    @add_to_report
    def test_03_编辑分享状态(self):
        '''
        用例编号：
        用例描述：
                1、编辑生效按钮为失效，可以编辑成功
                2、生效按钮为失效后，访问该分享链接，提示分享失效
                3、编辑生效按钮为失效，分享内容置灰
                4、编辑生效按钮为生效，分享内容没有置灰
                5、编辑生效按钮为生效，点击分享内容，可以访问该分享页面
        @author:彭亮
        '''
        self.分享管理工作区.编辑分享状态()

    @add_to_report
    def test_04_编辑过期时间(self):
        '''
        用例编号：
        用例描述：
                1、点击操作列编辑过期时间按钮，过期时间处于编辑状态
                2、点击过期时间栏，弹出过期时间编辑窗口
                3、过期时间不可以选择过去的时间
                4、编辑过期时间，点击确定，过期时间生效，然后查看到达该时间后，分享链接是否过期
                5、编辑过期时间，点击取消编辑按钮，不保存编辑结果
        @author:彭亮
        '''
        self.分享管理工作区.编辑过期时间()

    @add_to_report
    def test_05_查看访问记录(self):
        '''
        用例编号：
        用例描述：
                1、对分享资源进行访问，浏览，下载操作，查看对应的统计数量是否正确
                2、弹出分享访问记录，弹出我的访问记录弹窗
                3、记录列表显示查看人对分享资源的操作记录，有访问人ip地址、ip地理位置、操作类型、操作人、记录时间
                4、可以根据操作过滤显示访问记录，过滤条件默认全部
                5、过滤条件有全部、查看、下载、浏览
                6、选择不同的过滤条件，查看过滤结果是否正确
        @author:彭亮
        '''
        self.分享管理工作区.查看访问记录()

    @add_to_report
    def test_06_取消分享(self):
        '''
        用例编号：
        用例描述：
                1、点击取消分享按钮，分享列表中该条记录被清除，访问分享链接，显示链接失效
                2、勾选多条分享记录，点击取消分享，分享列表中该条记录被清除，访问分享链接，显示链接失效
        @author:彭亮
        '''
        self.分享管理工作区.取消分享()

    @add_to_report
    def test_07_访问列表显示(self):
        '''
        用例编号：
        用例描述：
                1、访问列表显示的是当前用户访问的分享链接的记录
                2、访问记录列表有分享内容、类型、分享创建人、创建时间、最后一次访问时间、操作列
        @author:彭亮
        '''
        self.分享管理工作区.访问列表显示()

    @add_to_report
    def test_08_点击查看访问(self):
        '''
        用例编号：
        用例描述：
                1、点击分享内容，可以查看到分享内容
                2、查看分享内容后，点击查看列表中最后一次访问时间是否正确
                3、访问分享链接后，查看列表中填充的信息是否正确
        @author:彭亮
        '''
        self.分享管理工作区.点击查看访问()

    @add_to_report
    def test_09_删除访问记录(self):
        '''
        用例编号：
        用例描述：
                1、点击删除按钮，访问记录从列表中移除
                2、勾选多个访问记录，点击删除，勾选的访问记录从访问列表中移除
        @author:彭亮
        '''
        self.分享管理工作区.删除访问记录()