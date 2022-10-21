import time

from HNtest.testcasesec.testcasesec import TestCaseSec
from HNtest.BeautifulReport.BeautifulReport import add_to_report
import HNtest.Secselenium.secdriver as secdriver
from 自动化测试.冒烟测试.冒烟业务实现 import *
from 自动化测试.基础操作.登录页面 import *
import openpyxl as op
import random

class Test_登录页冒烟(TestCaseSec):
    @classmethod
    def setUp(cls):
        cls.driver=secdriver.Secdriver()
        cls.driver.driver.maximize_window()
        cls.登录页冒烟实现=登录页冒烟实现(Secdriver=cls.driver)

    @classmethod
    def tearDown(cls):
        cls.driver.quite()

    @add_to_report
    def test_00_数据准备(self):
        self.登录页冒烟实现.数据准备()

    @add_to_report
    def test_01_短信快捷登录(self):
        '''
        用例编号：dly_041
        用例描述：
                1、勾选用户协议，手机号合法，验证码合法，点击开始使用
        @author:彭亮
        '''
        self.登录页冒烟实现.短信快捷登录()

    @add_to_report
    def test_02_账号密码登录(self):
        '''
        用例编号：dly_042、dly_028
        用例描述：
                1、点击账号密码登录，当前页面跳转至账号密码登录页面
                2、勾选用户协议账号存在且密码正确，点击登录
        @author:彭亮
        '''
        self.登录页冒烟实现.账号密码登录()

    @add_to_report
    def test_03_忘记密码(self):
        '''
        用例编号：dly_027、dly_012
        用例描述：
                1、使用重置后的密码登录，查看是否能正常登录
                2、点击短信快捷登录，当前页面跳转至短信快捷登录页面
        @author:彭亮
        '''
        self.登录页冒烟实现.忘记密码()


class Test_用户信息冒烟(TestCaseSec):
    @classmethod
    def setUp(cls):
        cls.driver=secdriver.Secdriver()
        cls.driver.driver.maximize_window()
        cls.用户信息=用户信息冒烟实现(Secdriver=cls.driver)
        cls.登录页=登录页面(Secdriver=cls.driver)
        # cls.登录页.短信快捷登录(手机号='18942178870')
        cls.登录页.账号密码登录(账号='18942178870', 密码='user@8870')

    @classmethod
    def tearDown(cls):
        cls.driver.quite()

    @add_to_report
    def test_00_数据准备(self):
        self.用户信息.数据准备()

    @add_to_report
    def test_01_用户基本信息维护(self):
        '''
        用例编号：yhxx_001~yhxx_013
        用例描述：
                1、点击更换头像，选择头像图片，点击确定
                2、点击下拉列表，点击可以选择对应的国家
                3、输入对应信息后点击保存，系统提示保存成功
        @author:彭亮
        '''
        self.用户信息.用户基本信息维护()

    @add_to_report
    def test_02_账号信息维护(self):
        '''
        用例编号：yhxx_032
        用例描述：
                1、点击修改密码按钮，弹出修改密码对话框
                2、修改密码后，使用手机号、邮箱、用户名登录系统

        @author:彭亮
        '''
        self.用户信息.账号信息维护()


class Test_项目页冒烟(TestCaseSec):
    @classmethod
    def setUp(cls):
        cls.driver=secdriver.Secdriver()
        cls.driver.driver.maximize_window()
        cls.项目页冒烟实现=项目页冒烟实现(Secdriver=cls.driver)
        cls.登录页 = 登录页面(Secdriver=cls.driver)
        # cls.登录页.短信快捷登录(手机号='18942178870')
        cls.登录页.账号密码登录(账号='18942178870', 密码='user@8870')

    @classmethod
    def tearDown(cls):
        cls.driver.quite()

    @add_to_report
    def test_00_数据准备(self):
        self.项目页冒烟实现.数据准备()

    @add_to_report
    def test_01_创建空白项目(self):
        '''
        用例编号：xm_010
        用例描述：
                1、输入有效的项目名称，点击提交按钮,项目成功创建并跳转到项目设置页面
        @author:彭亮
        '''
        self.项目页冒烟实现.创建空白项目()

    @add_to_report
    def test_02_邀请项目成员(self):
        '''
        用例编号：xm_015~xm_019
        用例描述：
                1、点击项目详情按钮，悬浮显示项目名称、创建人、创建日期、团队人数、文件数量、项目状态、备注等信息
                2、点击项目成员按钮，悬浮显示项目成员用户名列表
                3、点击项目成员按钮，在悬浮页点击添加成员按钮，弹出项目协作弹窗
                4、配置项目标题、角色、有效期和链接，点击复制链接
                5、打开链接，可以查看到配置的信息，点击加入，项目成员可以看到加入的项目
        @author:彭亮
        '''
        self.项目页冒烟实现.邀请项目成员()

    @add_to_report
    def test_03_移除项目成员(self):
        '''
        用例编号：xm_020
        用例描述：
                1、点击项目成员按钮，点击移除成员操作，成员能被移除
        @author:彭亮
        '''
        self.项目页冒烟实现.移除项目成员()

    @add_to_report
    def test_04_删除项目(self):
        '''
        用例编号：xm_025
        用例描述：
                1、点击项目操作按钮，点击删除项目，弹出删除确认对话框，点击确认删除,项目被删除
        @author:彭亮
        '''
        self.项目页冒烟实现.删除项目()

    @add_to_report
    def test_05_查看项目动态(self):
        '''
        用例编号：xm_026
        用例描述：
                1、对项目进行创建，成员管理等操作后，点击项目动态，可以查看到相关操作记录
        @author:彭亮
        '''
        self.项目页冒烟实现.查看项目动态()

    @add_to_report
    def test_06_存为模板(self):
        '''
        用例编号：xm_026
        用例描述：
                1、勾选保留团队成员，保存模板，查看保存的模板的项目成员tab页
                2、勾选保留项目文件，保存模板，查看保存的模板的项目结构tab页
                3、使用模板创建项目，查看模板下的文件和成员是否存在
                4、删除模板，模板是否正常删除
        @author:彭亮
        '''
        self.项目页冒烟实现.存为模板()

    @add_to_report
    def test_07_项目设置操作(self):
        '''
        用例编号：xm_027
        用例描述：
                1、点击项目操作按钮，点击项目设置，页面跳转到项目设置页面，执行设置操作后可以被保存
        @author:彭亮
        '''
        self.项目页冒烟实现.项目设置操作()

    @add_to_report
    def test_08_切换生命周期(self):
        '''
        用例编号：xm_027
        用例描述：
                1、空白项目点击切换生命周期可以直接切换
                2.进行生命周期节点变更操作后，点击确定按钮，查看项目生命周期是否别变更
        @author:彭亮
        '''
        self.项目页冒烟实现.切换生命周期()

    @add_to_report
    def test_09_切换版次(self):
        '''
        用例编号：xm_027
        用例描述：
                1、空白项目点击切换版次时，可以直接切换
                2.修改版次预览弹窗列表显示当前与使用版次和变更后对应版次的信息
                3、修改版次预览弹窗中点击确定，查看版次是否变更
        @author:彭亮
        '''
        self.项目页冒烟实现.切换版次()

    @add_to_report
    def test_10_切换属性(self):
        '''
        用例编号：xm_027
        用例描述：
                1、点击属性下拉列表，点击目标属性模板就可以完成切换
        @author:彭亮
        '''
        self.项目页冒烟实现.切换属性()

    @add_to_report
    def test_11_生命周期控制(self):
        '''
        用例编号：xm_027
        用例描述：
                1、进入生命周期tab页，显示当前生命周期的节点信息
                2、成员列表默认存在项目创建人、点击节点名称，点击添加人员按钮，进入选择人员弹窗
                3、选择人员弹窗内列表显示当前项目的所有项目成员，已经被添加的成员置灰
                4、勾选列表中的成员，点击确定，可以在节点的成员列表中查看到新添加的成员
                5、点击成员的移除按钮，人员被移除，项目创建人不可以被移除
        @author:彭亮
        '''
        self.项目页冒烟实现.生命周期控制()

    @add_to_report
    def test_12_生命周期节点人员提交设置(self):
        '''
        用例编号：xm_027
        用例描述：
                1、所有人提交后进入下一节点按钮关闭时，该节点下成员只要有一个成员完成提交，生命周期就可以进入下个节点
                2、所有人提交后进入下一节点按钮开启时，该节点下一个成员提交后，该文件生命周期状态为中间态
                3、所有人提交后进入下一节点按钮开启时，该节点下所有成员都提交后才能进入下个节点
        @author:彭亮
        '''
        self.项目页冒烟实现.生命周期节点人员提交设置()



    @add_to_report
    def test_13_创建文件目录(self):
        '''
        用例编号：xm_027、xm_029、xm_033
        用例描述：
                1、点击新建，弹出新建文件目录对话框，输入合法文件目录名称,点击提交，可以正常创建文件目录
                2、点击项目名称，进入项目页面，资源树默认全部展开
                3、点击展开和收缩各级资源节点，资源节点可以被正常展开和收缩
        @author:彭亮
        '''
        self.项目页冒烟实现.创建文件目录()

    @add_to_report
    def test_14_上传单个文件(self):
        '''
        用例编号：xm_031、xm_038、xm_035、xm_045
        用例描述：
                2、点击资源树任意节点，右侧列表显示该节点下的所有资源和子分组
                3、点击上传按钮，选择单个文件，点击上传
                4、选择上传文件后，弹窗内会出现被选中的待上传文件
                6、点击上传按钮，弹窗上传文件对话框
        @author:彭亮
        '''
        self.项目页冒烟实现.上传单个文件()

    @add_to_report
    def test_15_批量上传文件(self):
        '''
        用例编号：xm_039、xm_042
        用例描述：
                1、点击上传按钮，批量选择文件，点击上传
                2、选择多个待上传文件，在弹窗中清除部分待上传文件，文件被清除
        @author:彭亮
        '''
        self.项目页冒烟实现.批量上传文件()

    @add_to_report
    def test_16_列表显示管理(self):
        '''
        用例编号：xm_030、xm_044
        用例描述：
                1、点击资源树任意节点，右侧列表展示该节点下资源的文件名称、状态、版本、创建人、最后检入人、最后检入时间等信息
                2、点击列表设置按钮，可以自定义列表展示内容
        @author:彭亮
        '''
        self.项目页冒烟实现.列表显示管理()

    @add_to_report
    def test_17_批量操作工具栏显示(self):
        '''
        用例编号：
        用例描述：
                1、在右侧文件列表中勾选多个资源时，批量操作工具栏出现，工具栏中包括浏览、检入、检出、撤销检出、收藏、下载、批量删除按钮
        @author:彭亮
        '''
        self.项目页冒烟实现.批量操作工具栏显示()

    @add_to_report
    def test_18_收藏文件或文件目录(self):
        '''
        用例编号：
        用例描述：
                1、点击资源行操作的收藏按钮，可以对文件或文件目录收藏成功
                2、点击资源行操作的收藏按钮，可以对文件或文件目录取消收藏成功
        @author:彭亮
        '''
        self.项目页冒烟实现.收藏文件或文件目录()

    @add_to_report
    def test_19_文件检出和撤销检出(self):
        '''
        用例编号：
        用例描述：
                1、进行检出操作后，文件列表中文件会被标记为检出状态
                2、文件被检出后可以通过撤销检出修改文件检出状态
                3、文件成功检出后，文件状态会发生变化
                4、成功撤销检出后文件状态也会发生变化
        @author:彭亮
        '''
        self.项目页冒烟实现.文件检出和撤销检出()

    @add_to_report
    def test_20_文件检入(self):
        '''
        用例编号：
        用例描述：
                1、检出文件后，下载文件后，修改文件再检入文件，文件可以被正常检入
                2、成功检入文件后，文件状态会发生变化
        @author:彭亮
        '''
        self.项目页冒烟实现.文件检入()

    @add_to_report
    def test_21_文件或目录删除(self):
        '''
        用例编号：
        用例描述：
                1、点击删除，文件或目录可以被删除成功
        @author:彭亮
        '''
        self.项目页冒烟实现.文件或目录删除()

    @add_to_report
    def test_22_批量上传文件并下载校验(self):
        '''
        用例编号：
        用例描述：
                1、批量上传文件查看上传文件的数量是否正常
                2、下载文件，查看下载的文件大小是否正常
        @author:彭亮
        '''
        # for i in range(5):
        #     self.项目页冒烟实现.批量上传文件并下载校验()
        #     self.项目页冒烟实现.批量上传文件并下载校验2()
        # self.项目页冒烟实现.批量上传文件并下载校验()
        # self.项目页冒烟实现.批量上传文件并下载校验2()
        pass

    @add_to_report
    def test_23_附加文件(self):
        '''
        用例编号：
        用例描述：
                1、点击文件行操作中的添加附件操作，弹出附件文件弹窗
                2、左侧资源树默认全部展开，点击目录，右侧列表显示该目录下全部文件
                3、勾选单个文件点击附加，系统提示附加成功，在文件的引用tab页可以查看到该文件被引用文件名称
                4、勾选多个文件点击附加，系统提示附加成功，在文件的引用tab页可以查看到该文件被引用文件名称
        @author:彭亮
        '''
        self.项目页冒烟实现.附加文件()

    @add_to_report
    def test_24_文件打包(self):
        '''
        用例编号：
        用例描述：
                1、文件行操作，点击打包，自动下载打包后的压缩包，压缩包名为被打包的文件名，压缩包内容为被打包的文件
                2、目录行操作，点击打包，自动下载打包后的压缩包，压缩包名为被打包的目录的名称，压缩包内容为被打包的目录及目录下的全部资源
        @author:彭亮
        '''
        self.项目页冒烟实现.文件打包()

    @add_to_report
    def test_25_文件下载(self):
        '''
        用例编号：
        用例描述：
                1、点击下载，文件可以被正常下载
        @author:彭亮
        '''
        self.项目页冒烟实现.文件下载()

    @add_to_report
    def test_26_批量检出(self):
        '''
        用例编号：
        用例描述：
                1、批量选择文件，点击检出，可以检出成功
                2、批量选择目录和文件，点击检出，可以检出成功
        @author:彭亮
        '''
        self.项目页冒烟实现.批量检出()

    @add_to_report
    def test_27_批量撤销检出(self):
        '''
        用例编号：
        用例描述：
                1、批量选择已检出的文件，点击撤销检出，可以撤销检出成功
                2、批量选择文件和目录，点击撤销检出，可以撤销成功
        @author:彭亮
        '''
        self.项目页冒烟实现.批量撤销检出()

    @add_to_report
    def test_28_批量删除(self):
        '''
        用例编号：
        用例描述：
                1、勾选多个文件，点击删除，弹出删除确认对话框
                2、勾选多个文件，点击删除，可以删除
                3、勾选多个文件和目录，点击删除，可以删除成功
        @author:彭亮
        '''
        self.项目页冒烟实现.批量删除()

    @add_to_report
    def test_29_批量收藏(self):
        '''
        用例编号：
        用例描述：
                1、勾选多个文件，点击收藏，可以收藏成功
                2、勾选多个文件，点击收藏，可以收藏成功
                3、勾选文件和目录，点击收藏，可以收藏成功
        @author:彭亮
        '''
        self.项目页冒烟实现.批量收藏()

    @add_to_report
    def test_30_面包屑(self):
        '''
        用例编号：
        用例描述：
                1、在不同的文件目录下，面包屑会显示对应的路径
                2、点击面包屑上的节点，会跳转到对应的页面
        @author:彭亮
        '''
        self.项目页冒烟实现.面包屑()

    @add_to_report
    def test_31_面包屑(self):
        '''
        用例编号：
        用例描述：
                1、在不同的文件目录下，面包屑会显示对应的路径
                2、点击面包屑上的节点，会跳转到对应的页面
        @author:彭亮
        '''
        self.项目页冒烟实现.面包屑()


class Test_设置页冒烟(TestCaseSec):
    @classmethod
    def setUp(cls):
        cls.driver=secdriver.Secdriver()
        cls.driver.driver.maximize_window()
        cls.设置页冒烟实现=设置页冒烟实现(Secdriver=cls.driver)
        cls.登录页=登录页面(Secdriver=cls.driver)
        # cls.登录页.短信快捷登录(手机号='18942178870')
        cls.登录页面.账号密码登录(账号='18942178870', 密码='user@8870')

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
        self.设置页冒烟实现.数据准备()

    @add_to_report
    def test_01_新增生命周期(self):
        '''
        用例编号：
        用例描述：
                1、点击新增生命周期节点，生命周期节点列表中新增一行空白生命周期节点
                2、点击生命周期节点行的编辑按钮，生命周期行进入编辑状态
                3、点击生命周期节点行，点击删除按钮，生命周期行被删除
                4、点击生命周期节点行，点击上移按钮，节点行上移一行，点击下移按钮，节点行下移一行
        @author:彭亮
        '''
        self.设置页冒烟实现.创建生命周期()

    @add_to_report
    def test_02_升版设置(self):
        '''
        用例编号：
        用例描述：
                1、点击生命周期节点，右侧节点流程显示当前节点与上级节点的流程和当前节点与下级节点的流程
                2、不选择跨节点，右侧节点流程中不出现跨节点流程，选择跨节点，右侧节点流程出现跨节点流程
                3、设置升版流程，项目生命周期经过此流程时，项目进行升版
        @author:彭亮
        '''
        self.设置页冒烟实现.升版设置()

    @add_to_report
    def test_03_编辑生命周期(self):
        '''
        用例编号：
        用例描述：
                1、选择生命周期后，点击编辑，进入编辑生命周期界面
                2、点击新增生命周期节点，生命周期节点列表中新增一行空白生命周期节点
                3、点击生命周期节点行的编辑按钮，生命周期行进入编辑状态
                4、点击生命周期节点行，点击删除按钮，生命周期行被删除
                5、点击生命周期节点行，点击上移按钮，节点行上移一行，点击下移按钮，节点行下移一行
        @author:彭亮
        '''
        self.设置页冒烟实现.编辑生命周期()

    @add_to_report
    def test_04_编辑生命周期升版流程(self):
        '''
        用例编号：
        用例描述：
                1、不选择跨节点，右侧节点流程中不出现跨节点流程，选择跨节点，右侧节点流程出现跨节点流程
                2、设置升版流程，项目生命周期经过此流程时，项目进行升版
        @author:彭亮
        '''
        self.设置页冒烟实现.编辑生命周期升版流程()

    @add_to_report
    def test_05_编辑生命周期(self):
        '''
        用例编号：
        用例描述：
                1、择生命周期后，点击复制，进入复制生命周期界面
                2、点击生命周期节点行的编辑按钮，生命周期行进入编辑状态
                3、点击生命周期节点行，点击删除按钮，生命周期行被删除
        @author:彭亮
        '''
        self.设置页冒烟实现.编辑生命周期()

    @add_to_report
    def test_06_复制生命周期升版流程(self):
        '''
        用例编号：
        用例描述：
                1、不选择跨节点，右侧节点流程中不出现跨节点流程，选择跨节点，右侧节点流程出现跨节点流程
                2、设置升版流程，项目生命周期经过此流程时，项目进行升版
        @author:彭亮
        '''
        self.设置页冒烟实现.复制生命周期升版流程()

    @add_to_report
    def test_07_删除生命周期(self):
        '''
        用例编号：
        用例描述：
                1、勾选单个生命周期，点击删除，弹出删除提示对话框
                2、点击确定删除提示对话框，查看生命周期是否被删除
                3、系统上面周期不可以被删除
        @author:彭亮
        '''
        self.设置页冒烟实现.删除生命周期()

    @add_to_report
    def test_08_批量删除生命周期(self):
        '''
        用例编号：
        用例描述：
                1、勾选多个生命周期，点击删除，弹出删除提示对话框
                2、当勾选的生命周期中含有系统生命周期时，删除按钮不可用
                3、点击确定删除提示对话框，查看生命周期是否被删除
        @author:彭亮
        '''
        self.设置页冒烟实现.批量删除生命周期()

    @add_to_report
    def test_09_设置默认生命周期(self):
        '''
        用例编号：
        用例描述：
                1、点击生命周期列表中的生命周期，生命周期节点列表显示改生命周期下的生命周期节点
                2、点击对应的生命周期节点，节点流程列表显示该节点对应的节点流程
                3、勾选生命周期列表，生命周期行的是否默认单选按钮，设置对应的生命周期为默认生命周期
        @author:彭亮
        '''
        self.设置页冒烟实现.设置默认生命周期()

    @add_to_report
    def test_10_新增版次(self):
        '''
        用例编号：
        用例描述：
                1、添加、编辑、移动、删除版次节点
        @author:彭亮
        '''
        self.设置页冒烟实现.新增版次()

    @add_to_report
    def test_11_编辑版次(self):
        '''
        用例编号：
        用例描述：
                1、选择版次后，点击编辑，进入编辑版次界面
                2、添加、编辑、移动、删除版次节点
        @author:彭亮
        '''
        self.设置页冒烟实现.编辑版次()

    @add_to_report
    def test_12_删除版次(self):
        '''
        用例编号：
        用例描述：
                1、勾选单个版次，点击删除，弹出删除提示对话框
                2、系统版次不可以被删除
        @author:彭亮
        '''
        self.设置页冒烟实现.删除版次()

    @add_to_report
    def test_13_批量删除版次(self):
        '''
        用例编号：
        用例描述：
                1、勾选多个版次，点击删除，弹出删除提示对话框
                2、点击确定按钮，勾选的版次模板被删除
        @author:彭亮
        '''
        self.设置页冒烟实现.批量删除版次()

    @add_to_report
    def test_14_设置默认版次(self):
        '''
        用例编号：
        用例描述：
                1、点击版次列表中的版次，版次明细列表显示该版次下的版次节点
                2、勾选版次列表，版次行的是否默认单选按钮，设置对应的版次为默认版次
        @author:彭亮
        '''
        self.设置页冒烟实现.设置默认版次()

    @add_to_report
    def test_15_属性系统管理(self):
        '''
        用例编号：
        用例描述：
                1、点击属性列表属性新增按钮，属性列表新增一行属性系统，属性系统处于编辑状态
                2、点击属性系统，点击编辑按钮，被选中的属性系统处于编辑状态
                3、删除系统、系统属性模板不能被删除
        @author:彭亮
        '''
        self.设置页冒烟实现.属性系统管理()

    @add_to_report
    def test_16_添加属性(self):
        '''
        用例编号：
        用例描述：
                1、点击下载模板，属性模板可以正常下载
                2、正确填写模板，使用导入属性，可以正常导入
                3、属性列表中，点击删除属性行操作，出现属性删除提示框、属性删除提示框点击确定，属性被删除
                4、点击添加属性，属性列表新增一行属性、编辑属性
                5、批量删除属性
        @author:彭亮
        '''
        self.设置页冒烟实现.添加属性()


class Test_压测数据准备(TestCaseSec):
    @classmethod
    def setUp(cls):
        cls.driver=secdriver.Secdriver()
        cls.driver.driver.maximize_window()
        cls.登录页=登录页面(Secdriver=cls.driver)


    @classmethod
    def tearDown(cls):
        cls.driver.quite()

    def test_00_数据准备(self):
        ids=[]
        for i in range(1000):
            num = random.randint(11111,99999)
            nummber = '189421' + str(num)
            # nummber = '18942178870'
            self.登录页.短信快捷登录(手机号=nummber)
            # self.登录页.账号密码登录(账号='18942178870', 密码='user@8870')
            time.sleep(1)
            self.driver.refrsh()
            self.driver.driver.execute_script("window.open('');")
            self.driver.switch_to_new_window()
            time.sleep(1)
            # self.driver.get(url='https://hapyteam.com/api/account/userInfo')
            self.driver.get(url='http://192.168.1.99:8555/account/userInfo')
            message = self.driver.getelement("//pre").text
            strid = str(message)
            index1=strid.find('"id":')
            index2=strid.find(',"userName":')
            id = strid[index1+5:index2]
            ids.append(id)
            self.driver.close()
            self.driver.switch_to_window_byTitle(title="HAPYTEAM")
            self.登录页.退出登录()

        bg = op.load_workbook(r"D:\121.xlsx")
        sheet = bg["Sheet1"]
        for i in range(1, len(ids) + 1):
            sheet.cell(i, 1, ids[i - 1])
        bg.save("D:\\121.xlsx")




