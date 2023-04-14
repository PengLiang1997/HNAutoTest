import os.path
import os
import random
import time
from HNtest.Log.Logger import Logger

from ..基础操作.用户信息页面 import *
from ..基础操作.登录页面 import *
from ..基础操作.滑块验证 import *
from ..基础操作.项目页面 import *
from ..元素对象库.公共元素 import *
from ..元素对象库.全局搜索 import *
from ..基础操作.全局搜索页面 import *
from HNtest.testcasesec.testcasesec import page


class 全局搜索工作区(page):
    def __init__(self,Secdriver = None):
        page.__init__(self,secdriver=Secdriver)
        self.滑块验证=滑块验证(Secdriver=Secdriver)
        self.公共操作 = 公共操作(Secdriver=Secdriver)
        self.登录页面 = 登录页面(Secdriver=Secdriver)
        self.进入到操作位置 = 进入到操作位置(Secdriver=Secdriver)
        self.项目页面 = 项目页面(Secdriver=Secdriver)
        self.项目管理页面 = 项目管理页面(Secdriver=Secdriver)
        self.全局搜索页面 = 全局搜索页面(Secdriver=Secdriver)


    def 数据准备(self):
        同素材2 = ['TestData', 'FrontData', '项目页', '同素材2.jpg']
        素材1 = ['TestData', 'FrontData', '项目页', '素材1.png']
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        素材4 = ['TestData', 'FrontData', '项目页', '素材4.png']
        素材5 = ['TestData', 'FrontData', '项目页', '素材5.png']
        素材6 = ['TestData', 'FrontData', '项目页', '素材6.png']
        素材7 = ['TestData', 'FrontData', '项目页', '素材7.jpg']
        检入检出素材 = ['TestData', 'FrontData', '项目页', '检入检出素材.txt']
        项目属性模板表 = ['TestData', 'FrontData', '项目页', '项目属性模板表.xlsx']
        #项目动态数据准备
        self.项目管理页面.删除所有项目()
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.创建空白项目(项目名称="全局搜索1",生命周期名称='系统默认生命周期')
        self.项目管理页面.创建空白项目(项目名称="全局搜索2",生命周期名称='系统默认生命周期')
        self.项目管理页面.创建空白项目(项目名称="全局搜索3", 生命周期名称='系统默认生命周期')
        self.项目管理页面.点击进入项目(项目名称="全局搜索1")
        self.wait(项目对象库.目录节点.format("全局搜索1"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="全局搜索1")
        self.项目页面.创建文件目录(目录名称="一级目录21", 目录父节点名称="一级目录")
        self.项目页面.创建文件目录(目录名称="一级目录2", 目录父节点名称="全局搜索1")
        self.项目页面.批量上传文件(目录路径=['全局搜索1', '一级目录'], 文件路径列表=[素材1,素材2,素材3])
        self.项目页面.批量上传文件(目录路径=['全局搜索1', '一级目录2'], 文件路径列表=[同素材2,检入检出素材,素材1,素材2,素材3,素材4,素材5,项目属性模板表])
        self.项目页面.改变文件状态(文件名='素材2.jpg',状态名称='Release')
        self.项目页面.改变文件状态(文件名='素材2.jpg', 状态名称='Design')
        self.项目页面.改变文件状态(文件名='素材3.jpg', 状态名称='Release')
        self.项目页面.检出资源(资源名称='素材4.png')
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.邀请项目成员(项目名称='全局搜索1', 当前用户手机号='18942178870', 成员手机号='18942178871',角色='PROJECT MANAGER',是否返回项目创建账户=False)
        self.项目页面.创建文件目录(目录名称="一级目录3", 目录父节点名称="全局搜索1")
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="一级目录3")
        self.项目页面.批量上传文件(目录路径=['全局搜索1', '一级目录'], 文件路径列表=[素材6])
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称='全局搜索3')
        self.项目管理页面.创建空白项目(项目名称="全局搜索3", 生命周期名称='系统默认生命周期')
        self.项目管理页面.点击进入项目(项目名称="全局搜索3")
        self.wait(项目对象库.目录节点.format("全局搜索3"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="全局搜索3")
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.邀请项目成员(项目名称='全局搜索3', 当前用户手机号='18942178871', 成员手机号='18942178870', 角色='PROJECT MANAGER',
                           是否返回项目创建账户=False)
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="全局搜索2")
        self.wait(项目对象库.目录节点.format("全局搜索2"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="全局搜索2")
        self.项目页面.批量上传文件(目录路径=['全局搜索2', '一级目录'], 文件路径列表=[素材1])

    def 文件搜索(self):
        self.进入到操作位置.进入搜索页()
        #文件搜索结果列表显示文件名称、文件类型、文件大小、目录路径、版本、版次、生命周期状态列
        结果列 = []
        lelements = self.driver.getelements('//div[@class="el-table__header-wrapper"]//tr/th/div')
        for element in lelements:
            结果列.append(element.text)
        if 结果列 != ['文件名称', '文件类型','文件大小','目录路径','版本','版次','生命周期状态']:
            raise AssertionError("文件搜索结果列表显示文件名称、文件类型、文件大小、目录路径、版本、版次、生命周期状态列")
        #搜索框不输入任何条件，点击搜索，不出现搜索结果
        self.click(全局搜索对象库.搜索框)
        if not self.wait(全局搜索对象库.暂无数据提示,3):
            raise AssertionError("在搜索框未输入任何条件，点击搜索，可以搜索处文件")
        #输入文件名称，点击搜索，可以搜索到指定文件
        self.全局搜索页面.搜索文件(搜索条件="素材4.png")
        if not self.wait(全局搜索对象库.文件路径.format("素材4.png","全局搜索1/一级目录2"),3):
            raise AssertionError("输入文件名称，点击搜索，没有搜索到指定文件")
        #如果多个项目或目录存在相同的文件，输入文件名搜索后，会展示全部符合搜索条件的文件
        self.全局搜索页面.搜索文件(搜索条件="素材1.png")
        if not self.wait(全局搜索对象库.文件路径.format("素材1.png","全局搜索1/一级目录"),3) or\
            not self.wait(全局搜索对象库.文件路径.format("素材1.png","全局搜索1/一级目录2"),3) or\
            not self.wait(全局搜索对象库.文件路径.format("素材1.png","全局搜索2/一级目录"),3):
            raise AssertionError("多个项目或目录存在相同的文件，输入文件名搜索后，没有搜索到全部符合条件的文件")
        #搜索框输入文件名称、格式、版次、生命周期节点，检入检出状态、自定义属性等条件，搜索结果列表展示所有符合搜索条件的文件
        self.全局搜索页面.搜索文件(搜索条件="XLSX")
        if not self.wait(全局搜索对象库.列表文件名称.format("项目属性模板表.xlsx"),3):
            raise AssertionError("使用文件格式作为搜索条件，未搜索到该格式的文件")
        self.全局搜索页面.搜索文件(搜索条件="B")
        if not self.wait(全局搜索对象库.列表文件名称.format("素材2.jpg"), 3):
            raise AssertionError("使用版次作为搜索条件，未搜索到该版次的文件")
        self.全局搜索页面.搜索文件(搜索条件="Release")
        if not self.wait(全局搜索对象库.列表文件名称.format("素材3.jpg"), 3):
            raise AssertionError("使用生命周期节点作为搜索条件，未搜索到该版次的文件")
        self.全局搜索页面.搜索文件(搜索条件="检出")
        if not self.wait(全局搜索对象库.列表文件名称.format("素材4.png"), 3):
            raise AssertionError("使用检入检出状态作为搜索条件，未搜索到该版次的文件")
        self.全局搜索页面.搜索文件(搜索条件="18942178871")
        if not self.wait(全局搜索对象库.列表文件名称.format("素材6.png"), 3):
            raise AssertionError("使用作者作为搜索条件，未搜索到该作者上传的文件")
        #文件搜索支持组合条件搜索
        self.全局搜索页面.搜索文件(搜索条件="素材2.jpg B")
        if not self.wait(全局搜索对象库.文件版次.format("素材2.jpg","B"), 3):
            raise AssertionError("使用组合条件进行搜索，未搜索到指定条件的文件")
        #点击搜索结构列表中的文件名称，页面自动跳转到对应文件的项目目录下
        self.click(全局搜索对象库.列表文件名称.format("素材2.jpg"))
        面包屑 = []
        elements = self.driver.getelements('//span[@class="el-breadcrumb__item"]//span[@class="el-link--inner"]')
        for element in elements:
            面包屑.append(element.text)
        if 面包屑 != ['全局搜索1', '一级目录2']:
            raise AssertionError("击搜索结构列表中的文件名称，页面没有自动跳转到对应文件的项目目录下")

    def 目录搜索(self):
        self.进入到操作位置.进入搜索页()
        self.click(全局搜索对象库.目录tab页)
        # 目录搜索结果列表显示文件目录名称、创建人、目录路径列
        结果列 = []
        lelements = self.driver.getelements('//div[@class="el-table__header-wrapper"]//tr/th/div')
        for element in lelements:
            结果列.append(element.text)
        if 结果列 != ['文件目录名称', '创建人', '目录路径']:
            raise AssertionError("目录搜索结果列表显示文件目录名称、创建人、目录路径列")
        # 输入目录名称，点击搜索,搜索结果列表显示对应的文件目录
        self.全局搜索页面.搜索文件(搜索条件="一级目录21")
        if not self.wait(全局搜索对象库.目录创建人.format("一级目录21", "18942178870"), 3):
            raise AssertionError("输入文件目录名称，未搜索到指定的文件目录")
        # 目录搜索支持目录名称模糊匹配
        self.全局搜索页面.搜索文件(搜索条件="一级目录")
        if not self.wait(全局搜索对象库.目录创建人.format("一级目录21", "18942178870"), 3)or \
                not self.wait(全局搜索对象库.目录创建人.format("一级目录2", "18942178870"),3):
            raise AssertionError("模糊搜索文件目录，未搜索到指定的文件目录")
        # 目录搜索支持目录创建人为搜索条件
        self.全局搜索页面.搜索文件(搜索条件="18942178871")
        if not self.wait(全局搜索对象库.目录创建人.format("一级目录3", "18942178871"), 3):
            raise AssertionError("根据创建人搜索文件目录，未搜索到指定的文件目录")
        #目录搜索支持目录名和创建人条件组合搜索
        self.全局搜索页面.搜索文件(搜索条件="一级目录 18942178871")
        if not self.wait(全局搜索对象库.目录创建人.format("一级目录", "18942178871"), 3):
            raise AssertionError("使用创建人和目录名称组合搜索，未搜索到指定的文件目录")
        #点击搜索结果列表中的文件目录名称，页面跳转到对应的项目文件目录中
        self.click(全局搜索对象库.目录名称.format("一级目录"))
        面包屑 = []
        elements = self.driver.getelements('//span[@class="el-breadcrumb__item"]//span[@class="el-link--inner"]')
        for element in elements:
            面包屑.append(element.text)
        if 面包屑 != ['全局搜索1','一级目录3','一级目录']:
            raise AssertionError("击搜索结构列表中的目录名称，页面没有自动跳转到对应文件的项目目录下")
        #如果多个项目或目录存在相同的文件目录，输入文件目录名搜索后，会展示全部符合搜索条件的文件目录
        self.进入到操作位置.进入搜索页()
        self.click(全局搜索对象库.目录tab页)
        self.全局搜索页面.搜索文件(搜索条件="一级目录")
        if not self.wait(全局搜索对象库.目录路径.format("一级目录", "全局搜索1/一级目录"), 3) or \
                not self.wait(全局搜索对象库.目录路径.format("一级目录", "全局搜索1/一级目录3/一级目录"), 3):
            raise AssertionError("搜索相同名称的文件目录，未搜索到指定的文件目录")

    def 项目搜索(self):
        self.进入到操作位置.进入搜索页()
        self.click(全局搜索对象库.项目tab页)
        # 项目搜索结果列表显示项目名称、项目描述、创建人、项目大小、团队名称
        结果列 = []
        lelements = self.driver.getelements('//div[@class="el-table__header-wrapper"]//tr/th/div')
        for element in lelements:
            结果列.append(element.text)
        if 结果列 != ['项目名称', '项目描述', '创建人','项目大小','团队名称']:
            raise AssertionError("项目搜索结果列表显示项目名称、项目描述、创建人、项目大小、团队名称")
        # 在搜索框中输入项目名，点击搜索，可以搜索到对应的项目
        self.全局搜索页面.搜索文件(搜索条件="全局搜索1")
        if not self.wait(全局搜索对象库.项目名称.format("全局搜索1"), 3):
            raise AssertionError("输入文件项目名称，未搜索到指定的项目")
        # 项目搜索支持项目名称模糊匹配
        self.全局搜索页面.搜索文件(搜索条件="全局搜索")
        if not self.wait(全局搜索对象库.项目创建人.format("全局搜索1", "18942178870"), 3) or \
                not self.wait(全局搜索对象库.项目创建人.format("全局搜索2", "18942178870"), 3) or \
                not self.wait(全局搜索对象库.项目创建人.format("全局搜索3", "18942178871"), 3):
            raise AssertionError("模糊搜索项目，未搜索到全部符合条件的项目")
        # # 项目搜索创建人作为搜索条件进行搜索
        # self.全局搜索页面.搜索文件(搜索条件="18942178871")
        # if not self.wait(全局搜索对象库.目录创建人.format("全局搜索3", "18942178871"), 3):
        #     raise AssertionError("根据创建人搜索项目，未搜索到指定的项目")
        # # 项目搜索支持项目名称和创建人组合搜索
        # self.全局搜索页面.搜索文件(搜索条件="全局搜索 18942178871")
        # if not self.wait(全局搜索对象库.目录创建人.format("全局搜索3", "18942178871"), 3):
        #     raise AssertionError("使用创建人和项目名称组合搜索，未搜索到指定的项目")
        # 点击搜索结果列表中的项目名称，页面跳转到对应的项目页面
        self.click(全局搜索对象库.目录名称.format("全局搜索3"))
        面包屑 = []
        elements = self.driver.getelements('//span[@class="el-breadcrumb__item"]//span[@class="el-link--inner"]')
        for element in elements:
            面包屑.append(element.text)
        if 面包屑 != ['全局搜索3']:
            raise AssertionError("击搜索结果列表中的项目名称，页面没有自动跳转到对应的项目下")
        # 如果同时存在同名的项目和加入的项目
        self.进入到操作位置.进入搜索页()
        self.click(全局搜索对象库.项目tab页)
        self.全局搜索页面.搜索文件(搜索条件="全局搜索3")
        if not self.wait(全局搜索对象库.项目创建人.format("全局搜索3", "18942178870"), 3) or \
                not self.wait(全局搜索对象库.项目创建人.format("全局搜索3", "18942178871"), 3):
                raise AssertionError("存在同名的项目和加入的项目，未能搜索到全部的同名项目")

    def 项目成员搜索(self):
        self.进入到操作位置.进入搜索页()
        self.click(全局搜索对象库.项目成员tab页)
        # 项目成员搜索列表显示成员用户名、项目名称、权限名称、权限说明、加入日期列
        结果列 = []
        lelements = self.driver.getelements('//div[@class="el-table__header-wrapper"]//tr/th/div')
        for element in lelements:
            结果列.append(element.text)
        if 结果列 != ['成员用户名', '项目名称', '权限名称', '权限说明', '加入日期']:
            raise AssertionError("项目成员搜索列表显示成员用户名、项目名称、权限名称、权限说明、加入日期列")
        # 输入项目名称，可以搜索到该项目下的所有成员
        self.全局搜索页面.搜索文件(搜索条件="全局搜索1")
        if not self.wait(全局搜索对象库.成员项目名称.format("18942178870","全局搜索1"), 3) or\
                not self.wait(全局搜索对象库.成员项目名称.format("18942178871","全局搜索1"), 3):
            raise AssertionError("输入项目名称，没有搜索到该项目下的所有成员")
        #项目成员搜索支持项目名称模糊匹配
        self.全局搜索页面.搜索文件(搜索条件="全局搜索")
        成员目录=[["18942178870","全局搜索1"],["18942178871","全局搜索1"],["18942178870","全局搜索3"],["18942178871","全局搜索3"],["18942178870","全局搜索2"]]
        for 成员 in 成员目录:
            if not self.wait(全局搜索对象库.成员项目名称.format(成员[0],成员[1]), 3):
                raise AssertionError("输入项目名称没有模糊搜索到所有符合条件的成员")
        # 项目成员搜索支持项目成员名称、项目名称、项目成员角色名称作为搜索条件
        self.全局搜索页面.搜索文件(搜索条件="18942178871")
        if not self.wait(全局搜索对象库.成员项目名称.format("18942178871", "全局搜索1"), 3) or \
                not self.wait(全局搜索对象库.成员项目名称.format("18942178871", "全局搜索3"), 3):
            raise AssertionError("使用成员用户名进行搜索，未搜索到符合条件的成员")






