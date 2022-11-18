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
from ..元素对象库.收藏页 import *
from ..基础操作.设置页面 import *
from HNtest.testcasesec.testcasesec import page

class 其他操作(page):
    def __init__(self,Secdriver = None):
        page.__init__(self,secdriver=Secdriver)
        self.滑块验证=滑块验证(Secdriver=Secdriver)
        self.公共操作 = 公共操作(Secdriver=Secdriver)
        self.登录页面 = 登录页面(Secdriver=Secdriver)
        self.项目页面 = 项目页面(Secdriver=Secdriver)
        self.用户信息页面 = 用户信息页面(Secdriver=Secdriver)
        self.项目管理页面 = 项目管理页面(Secdriver=Secdriver)
        self.进入到操作位置 = 进入到操作位置(Secdriver=Secdriver)
        self.生命周期管理页面 = 生命周期管理页面(Secdriver=Secdriver)
        self.版次管理页面 = 版次管理页面(Secdriver=Secdriver)
        self.项目设置页面=项目管理页面.项目设置页面(Secdriver=Secdriver)

    def 创建目录再删除(self):
        self.项目管理页面.删除所有项目()
        self.项目管理页面.创建空白项目(项目名称="创建目录再删除")
        self.项目管理页面.点击进入项目(项目名称="创建目录再删除")
        self.wait(项目对象库.目录节点.format("创建目录再删除"), 3)
        self.driver.refrsh()
        for i in range(20):
            self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="创建目录再删除")
            素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
            素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
            self.click(项目对象库.目录节点.format("一级目录"))
            self.项目页面.上传单个文件(目录路径=['创建目录再删除', '一级目录'], 文件路径=素材3)
            self.项目页面.上传单个文件(目录路径=['创建目录再删除', '一级目录'], 文件路径=素材2)
            self.项目页面.附加文件(文件名称='素材2.jpg', 附加文件路径列表=[['创建目录再删除', '一级目录', '素材3.jpg']])
            self.项目页面.删除资源(目录路径=['创建目录再删除'], 资源名称='一级目录')
