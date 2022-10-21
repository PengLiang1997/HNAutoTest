import os.path
import random
import time

from ..基础操作.用户信息页面 import *
from ..基础操作.登录页面 import *
from ..基础操作.滑块验证 import *
from ..基础操作.项目页面 import *
from ..元素对象库.公共元素 import *
from ..元素对象库.收藏页 import *
from HNtest.testcasesec.testcasesec import page

class 收藏页面(page):
    def __init__(self,Secdriver = None):
        page.__init__(self,secdriver=Secdriver)
        self.滑块验证=滑块验证(Secdriver=Secdriver)
        self.公共操作 = 公共操作(Secdriver=Secdriver)
        self.登录页面 = 登录页面(Secdriver=Secdriver)
        self.项目页面 = 项目页面(Secdriver=Secdriver)
        self.用户信息页面 = 用户信息页面(Secdriver=Secdriver)
        self.项目管理页面 = 项目管理页面(Secdriver=Secdriver)
        self.进入到操作位置 = 进入到操作位置(Secdriver=Secdriver)

    def 数据准备(self):
        #注册账号2:18942178871 pw:user0000
        self.用户信息页面.进入账号信息页面()
        self.用户信息页面.维护用户账号信息(用户名='user8870', 用户密码='user8870')
        self.用户信息页面.进入基本信息页面()
        self.用户信息页面.维护用户基本信息(用户昵称="18942178870")

    def 收藏过滤显示(self):
        #项目动态数据准备
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="收藏资源")
        self.项目管理页面.创建空白项目(项目名称="收藏资源")

        self.click(项目管理对象库.更多操作按钮.format("收藏资源"))
        self.click(项目管理对象库.更多操作选项.format("项目设置"))
        self.click(项目设置页面.收藏按钮)
        self.wait("收藏成功",3)
        self.click(项目设置页面.查看项目目录)
        self.driver.refrsh()
        # 创建文件目录
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="收藏资源")
        self.项目页面.收藏资源(目录路径=['收藏资源'],资源名称='一级目录')
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        # 上传文件
        素材2=['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3=['TestData', 'FrontData', '项目页', '素材3.jpg']
        self.click(项目对象库.目录节点.format("收藏资源"))
        self.项目页面.批量上传文件(目录路径=['收藏资源', '一级目录'], 文件路径列表=[素材2,素材3])
        self.项目页面.收藏资源(目录路径=['收藏资源', '一级目录'], 资源名称='素材2.jpg')
        #点击过滤条件列表，点击所有收藏，收藏列表显示部收藏的资源
        self.进入到操作位置.进入收藏页()
        if not self.wait(收藏对象库.资源类型.format("收藏资源","项目"),3) or \
            not self.wait(收藏对象库.资源类型.format("一级目录","目录"),3) or \
            not self.wait(收藏对象库.资源类型.format("素材2.jpg","文件"),3):
            raise AssertionError("在收藏页面未发现收藏的资源")
        #点击过滤条件列表，点击收藏的项目，收藏列表显示收藏的项目资源
        self.click(收藏对象库.收藏条件列表框)
        self.click(收藏对象库.收藏条件列表选项.format("收藏的项目"))
        if not self.wait(收藏对象库.资源类型.format("收藏资源", "项目"), 3):
            raise AssertionError("设置过滤条件后，未过滤显示出项目")
        if self.wait(收藏对象库.资源类型.format("一级目录","目录"),3) or \
            self.wait(收藏对象库.资源类型.format("素材2.jpg", "文件"), 3):
            raise AssertionError("设置过滤条件后，其他显示数据未被过滤掉")
        #点击过滤条件列表，点击收藏的目录，收藏列表显示收藏的文件目录
        self.click(收藏对象库.收藏条件列表框)
        self.click(收藏对象库.收藏条件列表选项.format("收藏的目录"))
        if not self.wait(收藏对象库.资源类型.format("一级目录", "目录"), 3):
            raise AssertionError("设置过滤条件后，未过滤显示出项目")
        if self.wait(收藏对象库.资源类型.format("收藏资源", "项目"), 3) or \
                self.wait(收藏对象库.资源类型.format("素材2.jpg", "文件"), 3):
            raise AssertionError("设置过滤条件后，其他显示数据未被过滤掉")
        #点击过滤条件列表，点击收藏的文件，收藏列表显示收藏的文件
        self.click(收藏对象库.收藏条件列表框)
        self.click(收藏对象库.收藏条件列表选项.format("收藏的文件"))
        if not self.wait(收藏对象库.资源类型.format("素材2.jpg", "文件"), 3):
            raise AssertionError("设置过滤条件后，未过滤显示出项目")
        if self.wait(收藏对象库.资源类型.format("收藏资源", "项目"), 3) or \
                self.wait(收藏对象库.资源类型.format("一级目录", "目录"), 3):
            raise AssertionError("设置过滤条件后，其他显示数据未被过滤掉")

    def 资源行操作(self):
        #项目动态数据准备
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="收藏资源")
        self.项目管理页面.创建空白项目(项目名称="收藏资源")

        self.click(项目管理对象库.更多操作按钮.format("收藏资源"))
        self.click(项目管理对象库.更多操作选项.format("项目设置"))
        self.click(项目设置页面.收藏按钮)
        self.wait("收藏成功",3)
        self.click(项目设置页面.查看项目目录)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="收藏资源")
        self.项目页面.收藏资源(目录路径=['收藏资源'],资源名称='一级目录')
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        # 上传文件
        素材2=['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3=['TestData', 'FrontData', '项目页', '素材3.jpg']
        self.click(项目对象库.目录节点.format("收藏资源"))
        self.项目页面.批量上传文件(目录路径=['收藏资源', '一级目录'], 文件路径列表=[素材2,素材3])
        self.项目页面.收藏资源(目录路径=['收藏资源', '一级目录'], 资源名称='素材2.jpg')
        self.进入到操作位置.进入收藏页()
        #点击资源行操作中的查看按钮，可以查看到收藏的资源
        self.click(收藏对象库.查看收藏按钮.format("收藏资源"))
        if not self.wait(项目对象库.目录节点.format("收藏资源"),3):
            raise AssertionError("点击查看收藏的项目，页面未跳转到项目下")
        self.进入到操作位置.进入收藏页()
        self.click(收藏对象库.查看收藏按钮.format("一级目录"))
        if not self.wait(项目对象库.目录节点.format("一级目录"), 3):
            raise AssertionError("点击查看收藏的目录，页面未跳转到目录页面")
        self.进入到操作位置.进入收藏页()
        self.click(收藏对象库.查看收藏按钮.format("素材2.jpg"))
        if not self.wait(项目对象库.列表文件名称.format("素材2.jpg"), 3):
            raise AssertionError("点击查看收藏的文件，页面未跳转到文件查看页面")
        self.进入到操作位置.进入收藏页()
        #点击收藏的项目的行操作中的取消收藏按钮，提示取消收藏成功
        self.click(收藏对象库.取消收藏按钮.format("收藏资源"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("取消收藏成功"),3):
            raise AssertionError("进行取消收藏项目操作后，未查看到系统提示取消收藏成功")
        if self.wait(收藏对象库.收藏资源名称.format("收藏资源"),3):
            raise AssertionError("取消收藏成功后，收藏列表中仍然能查看到取消收藏的项目")
        #点击收藏的目录的行操作中的取消收藏按钮，提示取消收藏成功
        self.click(收藏对象库.取消收藏按钮.format("一级目录"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("取消收藏成功"), 3):
            raise AssertionError("进行取消收藏目录操作后，未查看到系统提示取消收藏成功")
        if self.wait(收藏对象库.收藏资源名称.format("一级目录"), 3):
            raise AssertionError("取消收藏成功后，收藏列表中仍然能查看到取消收藏的目录")
        #点击收藏的文件的行操作中的取消收藏按钮，提示取消收藏成功
        self.click(收藏对象库.取消收藏按钮.format("素材2.jpg"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("取消收藏成功"), 3):
            raise AssertionError("进行取消收藏文件操作后，未查看到系统提示取消收藏成功")
        if self.wait(收藏对象库.收藏资源名称.format("素材2.jpg"), 3):
            raise AssertionError("取消收藏成功后，收藏列表中仍然能查看到取消收藏的文件")
