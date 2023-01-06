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


class 成员权限管理工作区(page):
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

    def 数据准备(self):
        #项目动态数据准备
        self.项目管理页面.删除所有项目()
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.创建空白项目(项目名称="项目权限")
        self.项目管理页面.邀请项目成员(项目名称='项目权限', 当前用户手机号='18942178870', 成员手机号='18942178871',角色='PROJECT MANAGER')
        self.项目管理页面.点击进入项目(项目名称="项目权限")
        self.wait(项目对象库.目录节点.format("项目权限"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="项目权限")
        self.项目页面.创建文件目录(目录名称="一级目录2", 目录父节点名称="项目权限")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        self.项目管理页面.删除项目模板(模板名称="权限设置模板")
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.存为模板(项目名称="项目权限",模板名称="权限设置模板",保留团队成员=True,保留层级=2)

    def PROJECT_MANAGER角色权限验证(self):
        self.项目管理页面.删除项目(项目名称='项目权限设置')
        self.项目管理页面.根据模板创建项目(模板名称="权限设置模板",项目名称='项目权限设置')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        self.项目页面.上传单个文件(目录路径=['项目权限设置', '一级目录'], 文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'])
        self.项目页面.上传单个文件(目录路径=['项目权限设置', '一级目录', '二级目录'], 文件路径=['TestData', 'FrontData', '项目页', '素材2.jpg'])

        self.项目管理页面.进入点击项目设置(项目名称='项目权限设置',项目成员tab页=True)
        self.项目设置页面.切换用户角色(成员名称='18942178871',角色名称='PROJECT MANAGER')
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871',密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        #目录查询
        if not self.wait(项目对象库.目录节点.format("项目权限设置"),3):
            raise AssertionError("PROJECT_MANAGER角色没有查看到项目目录")
        #目录新增
        self.click(项目对象库.目录节点.format("项目权限设置"))
        self.click(项目对象库.新建目录)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新建文件目录"), 3)
        self.send_keys(公共元素对象库.输入框.format("文件目录名称"), "目录新增")
        self.click(对话框对象库.对话框按钮.format("新建文件目录", "提交"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("PROJECT_MANAGER角色没有配置创建项目目录的权限")
        #目录删除
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="目录新增")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("删除"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("PROJECT_MANAGER角色没有配置删除项目目录的权限")
        #目录检入检出
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='检入检出素材.txt')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("检出"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("PROJECT_MANAGER角色没有配置检出文件的权限")
        time.sleep(3)
        self.公共操作.修改文件内容(文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'], 内容=str(int(time.time())))
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("检入"))
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'])
        self.wait(项目对象库.待上传文件.format('检入检出素材.txt'), 5)
        self.click(项目对象库.上传文件按钮)
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("PROJECT_MANAGER角色没有配置检入文件的权限")
        #目录打包
        self.click(项目对象库.目录节点.format("项目权限设置"))
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="一级目录")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("打包"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("PROJECT_MANAGER角色没有配置目录打包的权限")
        #目录下载
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='检入检出素材.txt')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("下载"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("PROJECT_MANAGER角色没有配置下载文件的权限")
        #目录上传
        self.click(项目对象库.上传)
        self.wait(对话框对象库.弹框标题.format("上传文件"), 3)
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=['TestData', 'FrontData', '项目页', '素材2.jpg'])
        self.wait(项目对象库.待上传文件.format('素材2.jpg'), 5)
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=['TestData', 'FrontData', '项目页', '素材3.jpg'])
        self.wait(项目对象库.待上传文件.format('素材3.jpg'), 5)
        self.click(项目对象库.上传文件按钮)
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("PROJECT_MANAGER角色没有配置上传文件的权限")
        #文件附加
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='素材2.jpg')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("附加文件"))
        self.wait(对话框对象库.弹框标题.format("附加文件"), 3)
        self.click(项目对象库.附加文件.列表单选按钮.format("素材3.jpg"))
        self.click(项目对象库.附加文件.附加按钮)
        self.default_content()
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("PROJECT_MANAGER角色没有配置附加文件的权限")
        #改变生命周期状态
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='素材2.jpg')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("改变状态"))
        self.click(项目对象库.行操作选项.format("Review"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("PROJECT_MANAGER角色没有配置改变文件生命周期状态的权限")
        #删除文件
        self.click(项目对象库.列表复选框.format("素材2.jpg"))
        self.click(项目对象库.列表复选框.format("素材3.jpg"))
        self.click(项目对象库.工具栏按钮.format('删除'))
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("PROJECT_MANAGER角色没有配置删除文件的权限")

    def PROJECT_ASSISTANT角色权限验证(self):
        self.项目管理页面.进入点击项目设置(项目名称='项目权限',项目成员tab页=True)
        self.项目设置页面.切换用户角色(成员名称='18942178871',角色名称='PROJECT ASSISTANT')
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871',密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限')
        #目录查询
        if self.wait(项目对象库.目录节点.format("项目权限"),3):
            raise AssertionError("PROJECT_ASSISTANT角色查看到了项目目录")

    def DOCUMENT_MANAGER角色权限验证(self):
        self.项目管理页面.删除项目(项目名称='项目权限设置')
        self.项目管理页面.根据模板创建项目(模板名称="权限设置模板", 项目名称='项目权限设置')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        self.项目页面.上传单个文件(目录路径=['项目权限设置', '一级目录'], 文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'])
        self.项目页面.上传单个文件(目录路径=['项目权限设置', '一级目录', '二级目录'], 文件路径=['TestData', 'FrontData', '项目页', '素材2.jpg'])

        self.项目管理页面.进入点击项目设置(项目名称='项目权限设置', 项目成员tab页=True)
        self.项目设置页面.切换用户角色(成员名称='18942178871', 角色名称='DOCUMENT MANAGER')
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        # 目录查询
        if not self.wait(项目对象库.目录节点.format("项目权限设置"), 3):
            raise AssertionError("DOCUMENT_MANAGERz角色没有查看到项目目录")
        # 目录新增
        self.click(项目对象库.目录节点.format("项目权限设置"))
        self.click(项目对象库.新建目录)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新建文件目录"), 3)
        self.send_keys(公共元素对象库.输入框.format("文件目录名称"), "目录新增")
        self.click(对话框对象库.对话框按钮.format("新建文件目录", "提交"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_MANAGER角色没有配置创建项目目录的权限")
        # 目录删除
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="目录新增")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("删除"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_MANAGER角色没有配置删除项目目录的权限")
        # 目录检入检出
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='检入检出素材.txt')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("检出"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_MANAGER角色没有配置检出文件的权限")
        time.sleep(3)
        self.公共操作.修改文件内容(文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'], 内容=str(int(time.time())))
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("检入"))
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'])
        self.wait(项目对象库.待上传文件.format('检入检出素材.txt'), 5)
        self.click(项目对象库.上传文件按钮)
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_MANAGER角色没有配置检入文件的权限")
        # 目录打包
        self.click(项目对象库.目录节点.format("项目权限设置"))
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="一级目录")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("打包"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_MANAGER角色没有配置目录打包的权限")
        # 目录下载
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='检入检出素材.txt')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("下载"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_MANAGER角色没有配置下载文件的权限")
        # 目录上传
        self.click(项目对象库.上传)
        self.wait(对话框对象库.弹框标题.format("上传文件"), 3)
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=['TestData', 'FrontData', '项目页', '素材2.jpg'])
        self.wait(项目对象库.待上传文件.format('素材2.jpg'), 5)
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=['TestData', 'FrontData', '项目页', '素材3.jpg'])
        self.wait(项目对象库.待上传文件.format('素材3.jpg'), 5)
        self.click(项目对象库.上传文件按钮)
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_MANAGER角色没有配置上传文件的权限")
        # 文件附加
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='素材2.jpg')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("附加文件"))
        self.wait(对话框对象库.弹框标题.format("附加文件"), 3)
        self.click(项目对象库.附加文件.列表单选按钮.format("素材3.jpg"))
        self.click(项目对象库.附加文件.附加按钮)
        self.default_content()
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_MANAGER角色没有配置附加文件的权限")
        # 改变生命周期状态
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='素材2.jpg')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("改变状态"))
        self.click(项目对象库.行操作选项.format("Review"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_MANAGER角色没有配置改变文件生命周期状态的权限")
        # 删除文件
        self.click(项目对象库.列表复选框.format("素材2.jpg"))
        self.click(项目对象库.列表复选框.format("素材3.jpg"))
        self.click(项目对象库.工具栏按钮.format('删除'))
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_MANAGER角色没有配置删除文件的权限")

    def DOCUMENT_EDITOR角色权限验证(self):
        self.项目管理页面.删除项目(项目名称='项目权限设置')
        self.项目管理页面.根据模板创建项目(模板名称="权限设置模板", 项目名称='项目权限设置')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        self.项目页面.上传单个文件(目录路径=['项目权限设置', '一级目录'], 文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'])
        self.项目页面.上传单个文件(目录路径=['项目权限设置', '一级目录', '二级目录'], 文件路径=['TestData', 'FrontData', '项目页', '素材2.jpg'])

        self.项目管理页面.进入点击项目设置(项目名称='项目权限设置', 项目成员tab页=True)
        self.项目设置页面.切换用户角色(成员名称='18942178871', 角色名称='DOCUMENT EDITOR')
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        # 目录查询
        if not self.wait(项目对象库.目录节点.format("项目权限设置"), 3):
            raise AssertionError("DOCUMENT_EDITOR角色没有查看到项目目录")
        # 目录新增
        self.click(项目对象库.目录节点.format("项目权限设置"))
        self.click(项目对象库.新建目录)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新建文件目录"), 3)
        self.send_keys(公共元素对象库.输入框.format("文件目录名称"), "目录新增")
        self.click(对话框对象库.对话框按钮.format("新建文件目录", "提交"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_EDITOR角色没有配置创建项目目录的权限")
        # 目录删除
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="目录新增")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("删除"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_EDITOR角色不可以有删除项目目录的权限")
        # 目录检入检出
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='检入检出素材.txt')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("检出"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_EDITOR角色没有配置检出文件的权限")
        time.sleep(3)
        self.公共操作.修改文件内容(文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'], 内容=str(int(time.time())))
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("检入"))
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'])
        self.wait(项目对象库.待上传文件.format('检入检出素材.txt'), 5)
        self.click(项目对象库.上传文件按钮)
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_EDITOR角色没有配置检入文件的权限")
        # 目录打包
        self.click(项目对象库.目录节点.format("项目权限设置"))
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="一级目录")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("打包"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_EDITOR角色没有配置目录打包的权限")
        # 目录下载
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='检入检出素材.txt')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("下载"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_EDITOR角色没有配置下载文件的权限")
        # 目录上传
        self.click(项目对象库.上传)
        self.wait(对话框对象库.弹框标题.format("上传文件"), 3)
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=['TestData', 'FrontData', '项目页', '素材2.jpg'])
        self.wait(项目对象库.待上传文件.format('素材2.jpg'), 5)
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=['TestData', 'FrontData', '项目页', '素材3.jpg'])
        self.wait(项目对象库.待上传文件.format('素材3.jpg'), 5)
        self.click(项目对象库.上传文件按钮)
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_EDITOR角色没有配置上传文件的权限")
        # 文件附加
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='素材2.jpg')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("附加文件"))
        self.wait(对话框对象库.弹框标题.format("附加文件"), 3)
        self.click(项目对象库.附加文件.列表单选按钮.format("素材3.jpg"))
        self.click(项目对象库.附加文件.附加按钮)
        self.default_content()
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_EDITOR角色没有配置附加文件的权限")
        if self.wait(对话框对象库.弹框标题.format("附加文件"),3):
            self.click(对话框对象库.关闭弹框.format("附加文件"))
        # 改变生命周期状态
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='素材2.jpg')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("改变状态"))
        self.click(项目对象库.行操作选项.format("Review"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_EDITOR角色没有配置改变文件生命周期状态的权限")
        # 删除文件
        self.click(项目对象库.列表复选框.format("素材2.jpg"))
        self.click(项目对象库.列表复选框.format("素材3.jpg"))
        self.click(项目对象库.工具栏按钮.format('删除'))
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_EDITOR角色不可以配置删除文件的权限")

    def DOCUMENT_CONSUMER角色权限验证(self):
        self.项目管理页面.删除项目(项目名称='项目权限设置')
        self.项目管理页面.根据模板创建项目(模板名称="权限设置模板", 项目名称='项目权限设置')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        检入素材 = ['TestData', 'FrontData', '项目页', '检入检出素材.txt']
        self.项目页面.上传单个文件(目录路径=['项目权限设置', '一级目录'], 文件路径=检入素材)
        self.项目页面.上传单个文件(目录路径=['项目权限设置', '一级目录', '二级目录'], 文件路径=素材2)
        self.项目页面.批量上传文件(目录路径=['项目权限设置', '一级目录2'], 文件路径列表=[检入素材, 素材2, 素材3])


        self.项目管理页面.进入点击项目设置(项目名称='项目权限设置', 项目成员tab页=True)
        self.项目设置页面.切换用户角色(成员名称='18942178871', 角色名称='DOCUMENT CONSUMER')
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        # 目录查询
        if not self.wait(项目对象库.目录节点.format("项目权限设置"), 3):
            raise AssertionError("DOCUMENT_CONSUMER角色没有查看到项目目录")
        # 目录新增
        self.click(项目对象库.目录节点.format("项目权限设置"))
        self.click(项目对象库.新建目录)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新建文件目录"), 3)
        self.send_keys(公共元素对象库.输入框.format("文件目录名称"), "目录新增")
        self.click(对话框对象库.对话框按钮.format("新建文件目录", "提交"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_CONSUMER角色配置了创建项目目录的权限")
        # 目录删除
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="一级目录2")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("删除"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_CONSUMER角色配置了删除项目目录的权限")
        # 目录打包
        self.click(项目对象库.目录节点.format("项目权限设置"))
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="一级目录2")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("打包"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_CONSUMER角色没有配置目录打包的权限")
        # 目录下载
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录2'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='检入检出素材.txt')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("下载"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_CONSUMER角色没有配置下载文件的权限")
        # 目录上传
        self.click(项目对象库.上传)
        self.wait(对话框对象库.弹框标题.format("上传文件"), 3)
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=['TestData', 'FrontData', '项目页', '素材2.jpg'])
        self.wait(项目对象库.待上传文件.format('素材2.jpg'), 5)
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=['TestData', 'FrontData', '项目页', '素材3.jpg'])
        self.wait(项目对象库.待上传文件.format('素材3.jpg'), 5)
        self.click(项目对象库.上传文件按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_CONSUMER角色配置了上传文件的权限")
        # 文件附加
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='素材2.jpg')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("附加文件"))
        self.wait(对话框对象库.弹框标题.format("附加文件"), 3)
        self.click(项目对象库.附加文件.列表单选按钮.format("素材3.jpg"))
        self.click(项目对象库.附加文件.附加按钮)
        self.default_content()
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_CONSUMER角色配置了附加文件的权限")
        self.click(对话框对象库.关闭弹框.format("附加文件"))
        # 改变生命周期状态
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='素材2.jpg')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("改变状态"))
        self.click(项目对象库.行操作选项.format("Review"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_CONSUMER角色配置了改变文件生命周期状态的权限")
        # 删除文件
        self.click(项目对象库.列表复选框.format("素材2.jpg"))
        self.click(项目对象库.列表复选框.format("素材3.jpg"))
        self.click(项目对象库.工具栏按钮.format('删除'))
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_CONSUMER角色配置了删除文件的权限")

    def DOCUMENT_VIEWER角色权限验证(self):
        self.项目管理页面.删除项目(项目名称='项目权限设置')
        self.项目管理页面.根据模板创建项目(模板名称="权限设置模板", 项目名称='项目权限设置')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        self.项目页面.创建文件目录(目录名称="一级目录3", 目录父节点名称="项目权限设置")
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        检入素材 = ['TestData', 'FrontData', '项目页', '检入检出素材.txt']
        self.项目页面.上传单个文件(目录路径=['项目权限设置', '一级目录'], 文件路径=检入素材)
        self.项目页面.上传单个文件(目录路径=['项目权限设置', '一级目录', '二级目录'], 文件路径=素材2)
        self.项目页面.批量上传文件(目录路径=['项目权限设置', '一级目录3'], 文件路径列表=[检入素材, 素材2, 素材3])
        self.项目页面.检出资源(资源名称='检入检出素材.txt', 目录路径=['项目权限设置', '一级目录3'])

        self.项目管理页面.进入点击项目设置(项目名称='项目权限设置', 项目成员tab页=True)
        self.项目设置页面.切换用户角色(成员名称='18942178871', 角色名称='DOCUMENT VIEWER')
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        # 目录查询
        if not self.wait(项目对象库.目录节点.format("项目权限设置"), 3):
            raise AssertionError("DOCUMENT_VIEWER角色没有查看到项目目录")
        # 目录新增
        self.click(项目对象库.目录节点.format("项目权限设置"))
        self.click(项目对象库.新建目录)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新建文件目录"), 3)
        self.send_keys(公共元素对象库.输入框.format("文件目录名称"), "目录新增")
        self.click(对话框对象库.对话框按钮.format("新建文件目录", "提交"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_VIEWER角色配置了创建项目目录的权限")
        # 目录删除
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="一级目录3")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("删除"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_VIEWER角色配置了删除项目目录的权限")
        # 目录检入检出
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='检入检出素材.txt')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("检出"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_VIEWER角色配置了检出文件的权限")
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录3'])
        self.公共操作.修改文件内容(文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'], 内容=str(int(time.time())))
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("检入"))
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'])
        self.wait(项目对象库.待上传文件.format('检入检出素材.txt'), 5)
        self.click(项目对象库.上传文件按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_VIEWER角色没有配置检入文件的权限")
        # 目录打包
        self.click(项目对象库.目录节点.format("项目权限设置"))
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="一级目录3")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("打包"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_VIEWER角色配置了目录打包的权限")
        # 目录下载
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录3'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='检入检出素材.txt')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("下载"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_VIEWER角色配置了下载文件的权限")
        # 目录上传
        self.click(项目对象库.上传)
        self.wait(对话框对象库.弹框标题.format("上传文件"), 3)
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=['TestData', 'FrontData', '项目页', '素材2.jpg'])
        self.wait(项目对象库.待上传文件.format('素材2.jpg'), 5)
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=['TestData', 'FrontData', '项目页', '素材3.jpg'])
        self.wait(项目对象库.待上传文件.format('素材3.jpg'), 5)
        self.click(项目对象库.上传文件按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_VIEWER角色配置了上传文件的权限")
        # 文件附加
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='素材2.jpg')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("附加文件"))
        self.wait(对话框对象库.弹框标题.format("附加文件"), 3)
        self.click(项目对象库.附加文件.列表单选按钮.format("素材3.jpg"))
        self.click(项目对象库.附加文件.附加按钮)
        self.default_content()
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_VIEWER角色配置了附加文件的权限")
        self.click(对话框对象库.关闭弹框.format("附加文件"))
        # 改变生命周期状态
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='素材2.jpg')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("改变状态"))
        self.click(项目对象库.行操作选项.format("Review"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_CONSUMER角色配置了改变文件生命周期状态的权限")
        # 删除文件
        self.click(项目对象库.列表复选框.format("素材2.jpg"))
        self.click(项目对象库.列表复选框.format("素材3.jpg"))
        self.click(项目对象库.工具栏按钮.format('删除'))
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("DOCUMENT_VIEWER角色配置了删除文件的权限")

    def GUEST角色权限验证(self):
        self.项目管理页面.删除项目(项目名称='项目权限设置')
        self.项目管理页面.根据模板创建项目(模板名称="权限设置模板", 项目名称='项目权限设置')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        self.项目页面.创建文件目录(目录名称="一级目录3", 目录父节点名称="项目权限设置")
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        检入素材 = ['TestData', 'FrontData', '项目页', '检入检出素材.txt']
        self.项目页面.上传单个文件(目录路径=['项目权限设置', '一级目录'], 文件路径=检入素材)
        self.项目页面.上传单个文件(目录路径=['项目权限设置', '一级目录', '二级目录'], 文件路径=素材2)
        self.项目页面.批量上传文件(目录路径=['项目权限设置', '一级目录3'], 文件路径列表=[检入素材, 素材2, 素材3])
        self.项目页面.检出资源(资源名称='检入检出素材.txt', 目录路径=['项目权限设置', '一级目录3'])

        self.项目管理页面.进入点击项目设置(项目名称='项目权限设置', 项目成员tab页=True)
        self.项目设置页面.切换用户角色(成员名称='18942178871', 角色名称='GUEST')
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        # 目录查询
        if not self.wait(项目对象库.目录节点.format("项目权限设置"), 3):
            raise AssertionError("GUEST角色没有查看到项目目录")
        # 目录新增
        self.click(项目对象库.目录节点.format("项目权限设置"))
        self.click(项目对象库.新建目录)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新建文件目录"), 3)
        self.send_keys(公共元素对象库.输入框.format("文件目录名称"), "目录新增")
        self.click(对话框对象库.对话框按钮.format("新建文件目录", "提交"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("GUEST角色配置了创建项目目录的权限")
        # 目录删除
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="一级目录3")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("删除"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("GUEST角色配置了删除项目目录的权限")
        # # 目录检入检出
        # self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录'])
        # 序号 = self.公共操作.获取文件在列表中的行号(文件名称='检入检出素材.txt')
        # self.click(项目对象库.悬浮列行操作.format(序号))
        # self.click(项目对象库.行操作选项.format("检出"))
        # if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
        #     raise AssertionError("GUEST角色配置了检出文件的权限")
        # self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录3'])
        # self.公共操作.修改文件内容(文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'], 内容=str(int(time.time())))
        # self.click(项目对象库.悬浮列行操作.format(序号))
        # self.click(项目对象库.行操作选项.format("检入"))
        # self.click(项目对象库.点击上传按钮)
        # self.公共操作.win上传文件(文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'])
        # self.wait(项目对象库.待上传文件.format('检入检出素材.txt'), 5)
        # self.click(项目对象库.上传文件按钮)
        # if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
        #     raise AssertionError("GUEST角色没有配置检入文件的权限")
        # 目录打包
        self.click(项目对象库.目录节点.format("项目权限设置"))
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="一级目录3")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("打包"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("GUEST角色配置了目录打包的权限")
        # 目录下载
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录3'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='检入检出素材.txt')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("下载"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("GUEST角色配置了下载文件的权限")
        # 目录上传
        self.click(项目对象库.上传)
        self.wait(对话框对象库.弹框标题.format("上传文件"), 3)
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=['TestData', 'FrontData', '项目页', '素材2.jpg'])
        self.wait(项目对象库.待上传文件.format('素材2.jpg'), 5)
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=['TestData', 'FrontData', '项目页', '素材3.jpg'])
        self.wait(项目对象库.待上传文件.format('素材3.jpg'), 5)
        self.click(项目对象库.上传文件按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("GUEST角色配置了上传文件的权限")
        # 文件附加
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='素材2.jpg')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("附加文件"))
        self.wait(对话框对象库.弹框标题.format("附加文件"), 3)
        self.click(项目对象库.附加文件.列表单选按钮.format("素材3.jpg"))
        self.click(项目对象库.附加文件.附加按钮)
        self.default_content()
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("GUEST角色配置了附加文件的权限")
        self.click(对话框对象库.关闭弹框.format("附加文件"))
        # 改变生命周期状态
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='素材2.jpg')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("改变状态"))
        self.click(项目对象库.行操作选项.format("Review"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("GUEST角色配置了改变文件生命周期状态的权限")
        # 删除文件
        self.click(项目对象库.列表复选框.format("素材2.jpg"))
        self.click(项目对象库.列表复选框.format("素材3.jpg"))
        self.click(项目对象库.工具栏按钮.format('删除'))
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("GUEST角色配置了删除文件的权限")

    def 撤回用户目录查询权限(self):
        self.项目管理页面.删除项目(项目名称='项目权限设置')
        self.项目管理页面.根据模板创建项目(模板名称="权限设置模板", 项目名称='项目权限设置')

        self.项目管理页面.进入点击项目设置(项目名称='项目权限设置', 项目成员tab页=True)
        self.项目设置页面.切换用户角色(成员名称='18942178871', 角色名称='PROJECT MANAGER')
        self.项目设置页面.撤回用户授权(成员名称='18942178871',目录列表=['项目权限设置', '一级目录'],权限列表=['目录查询'])
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        self.click(项目对象库.目录节点.format("项目权限设置"))
        if self.wait(项目对象库.列表文件名称.format("一级目录"),3):
            raise AssertionError("撤回用户目录查询权限，登录用户后还是能看到该目录")

    def 授予用户目录查询权限(self):
        self.项目管理页面.删除项目(项目名称='角色权限验证')
        self.项目管理页面.根据模板创建项目(模板名称="权限设置模板", 项目名称='项目权限设置')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        检入素材 = ['TestData', 'FrontData', '项目页', '检入检出素材.txt']
        self.项目页面.上传单个文件(目录路径=['项目权限设置', '一级目录'], 文件路径=检入素材)
        self.项目页面.上传单个文件(目录路径=['项目权限设置', '一级目录', '二级目录'], 文件路径=素材2)

        self.项目管理页面.进入点击项目设置(项目名称='项目权限设置', 项目成员tab页=True)
        self.项目设置页面.撤回用户授权(成员名称='18942178871', 目录列表=['项目权限设置', '一级目录'], 权限列表=['目录查询'])
        self.项目设置页面.用户授权(成员名称='18942178871', 目录列表=['项目权限设置', '一级目录'], 权限列表=['目录查询'])
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        self.click(项目对象库.目录节点.format("项目权限设置"))
        if not self.wait(项目对象库.列表文件名称.format("一级目录"), 3):
            raise AssertionError("授予用户目录查询权限，登录用户后不能看到该目录")
        self.click(项目对象库.列表文件名称.format("一级目录"))
        if not self.wait(项目对象库.列表文件名称.format("一级目录"), 3):
            raise AssertionError("授予用户目录查询权限，登录用户后不能查看到该目录下的子目录")
        if not self.wait(项目对象库.列表文件名称.format("检入检出素材.txt"), 3):
            raise AssertionError("授予用户目录查询权限，登录用户后不能查看到该目录下的文件")
        self.click(项目对象库.列表文件名称.format("二级目录"))
        if not self.wait(项目对象库.列表文件名称.format("素材2.jpg"), 3):
            raise AssertionError("授予用户目录查询权限，登录用户后不能查看到该目录子目录下的文件")

    def 用户目录新增权限(self):
        self.项目管理页面.删除项目(项目名称='项目权限设置')
        self.项目管理页面.根据模板创建项目(模板名称="权限设置模板", 项目名称='项目权限设置')
        self.项目管理页面.进入点击项目设置(项目名称='项目权限设置', 项目成员tab页=True)
        self.项目设置页面.撤回用户授权(成员名称='18942178871', 目录列表=['项目权限设置', '一级目录'], 权限列表=['目录新增'])
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        #不对用户授予目录新增权限，使用用户登录后不能在该目录及其子目录在新增文件目录
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置','一级目录'])
        self.click(项目对象库.新建目录)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新建文件目录"), 3)
        self.send_keys(公共元素对象库.输入框.format("文件目录名称"), "目录新增")
        self.click(对话框对象库.对话框按钮.format("新建文件目录", "提交"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("撤回用户的新增目录的权限，用户还能新增目录")
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录', '二级目录'])
        self.click(项目对象库.新建目录)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新建文件目录"), 3)
        self.send_keys(公共元素对象库.输入框.format("文件目录名称"), "目录新增")
        self.click(对话框对象库.对话框按钮.format("新建文件目录", "提交"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("撤回用户的新增目录的权限，用户在该目录的子目录下还能新增目录")
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178870', 密码='user@8870')
        self.项目管理页面.进入点击项目设置(项目名称='项目权限设置', 项目成员tab页=True)
        self.项目设置页面.用户授权(成员名称='18942178871', 目录列表=['项目权限设置', '一级目录'], 权限列表=['目录新增'])
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        # 不对用户授予目录新增权限，使用用户登录后不能在该目录及其子目录在新增文件目录
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录'])
        self.click(项目对象库.新建目录)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新建文件目录"), 3)
        self.send_keys(公共元素对象库.输入框.format("文件目录名称"), "目录新增")
        self.click(对话框对象库.对话框按钮.format("新建文件目录", "提交"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("授予用户的新增目录的权限，登录该用户后不能新增目录")
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录', '二级目录'])
        self.click(项目对象库.新建目录)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新建文件目录"), 3)
        self.send_keys(公共元素对象库.输入框.format("文件目录名称"), "目录新增")
        self.click(对话框对象库.对话框按钮.format("新建文件目录", "提交"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("授予用户的新增目录的权限，登录该用户后在该目录的子目录下不能新增目录")

    def 用户目录删除权限(self):
        self.项目管理页面.删除项目(项目名称='项目权限设置')
        self.项目管理页面.根据模板创建项目(模板名称="权限设置模板", 项目名称='项目权限设置')
        self.项目管理页面.点击进入项目(项目名称="项目权限设置")
        self.wait(项目对象库.目录节点.format("项目权限设置"), 3)
        self.driver.refrsh()
        self.项目页面.删除资源(资源名称='目录新增权限')
        self.项目页面.创建文件目录(目录名称="目录删除权限", 目录父节点名称="项目权限设置")
        self.项目页面.创建文件目录(目录名称="删除权限", 目录父节点名称="目录删除权限")
        self.项目页面.上传单个文件(目录路径=['项目权限设置', '目录删除权限','删除权限'], 文件路径=['TestData', 'FrontData', '项目页', '素材2.jpg'])
        self.项目管理页面.进入点击项目设置(项目名称='项目权限设置', 项目成员tab页=True)
        self.项目设置页面.撤回用户授权(成员名称='18942178871', 目录列表=['项目权限设置', '目录删除权限'], 权限列表=['目录删除'])
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        # 不对用户授予目录删除权限，使用用户登录后不能删除该目录及其子目录以及目录下的资源
        self.click(项目对象库.目录节点.format('项目权限设置'))
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="目录删除权限")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("删除"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户收目录的删除权限，登录用户后该目录还是可以被删除")
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '目录删除权限'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="删除权限")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("删除"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户收目录的删除权限，登录用户后该目录的子目录还是可以被删除")
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '目录删除权限','删除权限'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="素材2.jpg")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("删除"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户收目录的删除权限，登录用户后该目录的子目录下的文件还是可以被删除")
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178870', 密码='user@8870')
        self.项目管理页面.进入点击项目设置(项目名称='项目权限设置', 项目成员tab页=True)
        self.项目设置页面.用户授权(成员名称='18942178871', 目录列表=['项目权限设置', '目录删除权限'], 权限列表=['目录删除'])
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        # 对用户授予目录删除权限，使用用户登录后可以删除该目录及其子目录和目录下的任意资源
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '目录删除权限', '删除权限'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="素材2.jpg")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("删除"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户授予目录的删除权限，登录用户后该目录的子目录下的文件不可以被删除")
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '目录删除权限'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="删除权限")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("删除"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户授予目录的删除权限，登录用户后该目录的子目录不可以被删除")
        self.click(项目对象库.目录节点.format('项目权限设置'))
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="目录删除权限")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("删除"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户授予目录的删除权限，登录用户后该目录不可以被删除")

    def 收回用户目录检入检出权限(self):
        self.项目管理页面.删除项目(项目名称='项目权限设置')
        self.项目管理页面.根据模板创建项目(模板名称="权限设置模板", 项目名称='项目权限设置')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        self.项目页面.创建文件目录(目录名称="一级目录3", 目录父节点名称="项目权限设置")
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        检入素材 = ['TestData', 'FrontData', '项目页', '检入检出素材.txt']
        self.项目页面.上传单个文件(目录路径=['项目权限设置', '一级目录'], 文件路径=检入素材)
        self.项目页面.批量上传文件(目录路径=['项目权限设置', '一级目录', '二级目录'], 文件路径列表=[素材2, 素材3])
        self.项目页面.批量上传文件(目录路径=['项目权限设置', '一级目录3'], 文件路径列表=[检入素材, 素材2, 素材3])
        self.项目管理页面.进入点击项目设置(项目名称='项目权限设置', 项目成员tab页=True)
        self.项目设置页面.撤回用户授权(成员名称='18942178871', 目录列表=['项目权限设置', '一级目录'], 权限列表=['目录检入检出'])
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        #对用户收回目录检出检出权限，登录该用户后，该目录不能进行检出操作
        self.click(项目对象库.目录节点.format('项目权限设置'))
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="一级目录")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("检出"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户收目录的检入检出权限，登录用户后该目录还是可以被检出")
        #当用户没有目录检入检出权限时，该用户不能对该目录进行批量检出操作
        self.click(项目对象库.列表复选框.format("一级目录"))
        self.click(项目对象库.列表复选框.format("一级目录3"))
        self.click(项目对象库.工具栏按钮.format('检出'))
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户收目录的检入检出权限，登录用户后该目录还是可以被批量检出")
        #对用户收回目录检出检出权限，登录该用户后，该目录及其子目录下的任意文件不能进行检入检出操作
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="二级目录")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("检出"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户收目录的检入检出权限，登录用户后该目录的子目录还是可以被检出")
        #当用户没有目录检入检出权限时，该用户不能对该目录下的任意资源进行批量检出操作
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录', '二级目录'])
        self.click(项目对象库.列表复选框.format("素材2.jpg"))
        self.click(项目对象库.列表复选框.format("素材3.jpg"))
        self.click(项目对象库.工具栏按钮.format('检出'))
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户收目录的检入检出权限，登录用户后该目录下子目录的资源还是可以被批量检出")

    def 授予用户目录检入检出权限(self):
        self.项目管理页面.删除项目(项目名称='项目权限设置')
        self.项目管理页面.根据模板创建项目(模板名称="权限设置模板", 项目名称='项目权限设置')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        self.项目页面.创建文件目录(目录名称="一级目录3", 目录父节点名称="项目权限设置")
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        检入素材 = ['TestData', 'FrontData', '项目页', '检入检出素材.txt']
        self.项目页面.上传单个文件(目录路径=['项目权限设置', '一级目录'], 文件路径=检入素材)
        self.项目页面.批量上传文件(目录路径=['项目权限设置', '一级目录', '二级目录'], 文件路径列表=[ 素材2, 素材3])
        self.项目页面.批量上传文件(目录路径=['项目权限设置', '一级目录3'], 文件路径列表=[检入素材, 素材2, 素材3])
        self.项目管理页面.进入点击项目设置(项目名称='项目权限设置', 项目成员tab页=True)
        self.项目设置页面.撤回用户授权(成员名称='18942178871', 目录列表=['项目权限设置', '一级目录'], 权限列表=['目录检入检出'])
        self.项目设置页面.用户授权(成员名称='18942178871', 目录列表=['项目权限设置', '一级目录'], 权限列表=['目录检入检出'])
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        #对用户授予目录检出检出权限，该目录及其子目录可以进行检出操作，该目录及其子目录下的任意文件可以进行检入检出操作
        self.click(项目对象库.目录节点.format('项目权限设置'))
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="一级目录")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("检出"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户授予目录的检入检出权限，登录用户后该目录还是不能被检出")
        #当用户授予目录检入检出权限时，该用户可以对该目录进行批量检出操作
        self.click(项目对象库.列表复选框.format("一级目录"))
        self.click(项目对象库.列表复选框.format("一级目录3"))
        self.click(项目对象库.工具栏按钮.format('检出'))
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户收目录的检入检出权限，登录用户后该目录还是可以被批量检出")
        #对用户授予目录检出检出权限，登录该用户后，该目录及其子目录下的任意文件可以进行检入检出操作
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="二级目录")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("检出"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户授予目录的检入检出权限，登录用户后该目录的子目录还是不能被检出")
        #检入
        self.公共操作.修改文件内容(文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'], 内容=str(int(time.time())))
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="检入检出素材.txt")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("检入"))
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'])
        self.wait(项目对象库.待上传文件.format('检入检出素材.txt'), 5)
        self.click(项目对象库.上传文件按钮)
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户授予目录的检入检出权限，登录用户后该目录下的文件不能被检入")

        #当用户授予目录检入检出权限时，该用户可以对该目录下的任意资源进行批量检出操作
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录', '二级目录'])
        self.click(项目对象库.列表复选框.format("素材2.jpg"))
        self.click(项目对象库.列表复选框.format("素材3.jpg"))
        self.click(项目对象库.工具栏按钮.format('检出'))
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户收授予目录的检入检出权限，登录用户后该目录下子目录的资源还是不能被批量检出")

    def 收回用户目录打包权限(self):
        self.项目管理页面.删除项目(项目名称='项目权限设置')
        self.项目管理页面.根据模板创建项目(模板名称="权限设置模板", 项目名称='项目权限设置')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        self.项目页面.创建文件目录(目录名称="一级目录3", 目录父节点名称="项目权限设置")
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        检入素材 = ['TestData', 'FrontData', '项目页', '检入检出素材.txt']
        self.项目页面.上传单个文件(目录路径=['项目权限设置', '一级目录'], 文件路径=检入素材)
        self.项目页面.批量上传文件(目录路径=['项目权限设置', '一级目录', '二级目录'], 文件路径列表=[素材2,素材3])
        self.项目页面.批量上传文件(目录路径=['项目权限设置', '一级目录3'], 文件路径列表=[检入素材, 素材2, 素材3])
        self.项目管理页面.进入点击项目设置(项目名称='项目权限设置', 项目成员tab页=True)
        self.项目设置页面.撤回用户授权(成员名称='18942178871', 目录列表=['项目权限设置', '一级目录'], 权限列表=['目录打包'])
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        # 当收回用户的目录打包权限时，登录该用户后，不能对该目录进行打包操作
        self.click(项目对象库.目录节点.format('项目权限设置'))
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="一级目录")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("打包"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户收目录的打包权限，登录用户后该目录还是可以打包")
        # 当收回用户的目录打包权限时，登录该用户后，不能对该目录进行批量打包操作
        self.click(项目对象库.列表复选框.format("一级目录"))
        self.click(项目对象库.列表复选框.format("一级目录3"))
        self.click(项目对象库.工具栏按钮.format('打包'))
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户收回目录的打包权限，登录用户后该目录还是可以被批量打包")
        # 当收回用户的目录打包权限时，登录该用户后，不能对该目录下的任意资源进行批量打包操作
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="二级目录")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("打包"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户收回目录的打包权限，登录用户后该目录的子目录还是可以被打包")
        #
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录', '二级目录'])
        self.click(项目对象库.列表复选框.format("素材2.jpg"))
        self.click(项目对象库.列表复选框.format("素材3.jpg"))
        self.click(项目对象库.工具栏按钮.format('打包'))
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户收回目录的打包权限，登录用户后该目录下子目录的资源还是可以被批量打包")

    def 授予用户目录打包权限(self):
        self.项目管理页面.删除项目(项目名称='项目权限设置')
        self.项目管理页面.根据模板创建项目(模板名称="权限设置模板", 项目名称='项目权限设置')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        self.项目页面.创建文件目录(目录名称="一级目录3", 目录父节点名称="项目权限设置")
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        检入素材 = ['TestData', 'FrontData', '项目页', '检入检出素材.txt']
        self.项目页面.上传单个文件(目录路径=['项目权限设置', '一级目录'], 文件路径=检入素材)
        self.项目页面.批量上传文件(目录路径=['项目权限设置', '一级目录', '二级目录'], 文件路径列表=[素材2,素材3])
        self.项目页面.批量上传文件(目录路径=['项目权限设置', '一级目录3'], 文件路径列表=[检入素材, 素材2, 素材3])
        self.项目管理页面.进入点击项目设置(项目名称='项目权限设置', 项目成员tab页=True)
        self.项目设置页面.撤回用户授权(成员名称='18942178871', 目录列表=['项目权限设置', '一级目录'], 权限列表=['目录打包'])
        self.项目设置页面.用户授权(成员名称='18942178871', 目录列表=['项目权限设置', '一级目录'], 权限列表=['目录打包'])
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        # 当授予用户目录打包权限，登录该用户后，可以对该目录进行打包操作
        self.click(项目对象库.目录节点.format('项目权限设置'))
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="一级目录")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("打包"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户授予目录的打包权限，登录用户后该目录还是不能打包")
        # 当授予用户目录打包权限，登录该用户后，可以对该目录进行批量打包操作
        self.click(项目对象库.列表复选框.format("一级目录"))
        self.click(项目对象库.列表复选框.format("一级目录3"))
        self.click(项目对象库.工具栏按钮.format('打包'))
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户授予目录的打包权限，登录用户后该目录还是不能被批量打包")
        # 当授予用户目录打包权限，登录该用户后，可以对该目录下的任意资源进行打包操作
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="二级目录")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("打包"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户授予目录的打包权限，登录用户后该目录的子目录还是不能被打包")
        #当授予用户目录打包权限，登录该用户后，可以对该目录下的任意资源进行批量打包操作
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录', '二级目录'])
        self.click(项目对象库.列表复选框.format("素材2.jpg"))
        self.click(项目对象库.列表复选框.format("素材3.jpg"))
        self.click(项目对象库.工具栏按钮.format('打包'))
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户授予目录的打包权限，登录用户后该目录下子目录的资源还是不能被批量打包")

    def 收回用户目录下载权限(self):
        self.项目管理页面.删除项目(项目名称='项目权限设置')
        self.项目管理页面.根据模板创建项目(模板名称="权限设置模板", 项目名称='项目权限设置')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        检入素材 = ['TestData', 'FrontData', '项目页', '检入检出素材.txt']
        self.项目页面.上传单个文件(目录路径=['项目权限设置', '一级目录'], 文件路径=检入素材)
        self.项目页面.上传单个文件(目录路径=['项目权限设置', '一级目录', '二级目录'], 文件路径=素材2)
        self.项目管理页面.进入点击项目设置(项目名称='项目权限设置', 项目成员tab页=True)
        self.项目设置页面.撤回用户授权(成员名称='18942178871', 目录列表=['项目权限设置', '一级目录'], 权限列表=['目录下载'])
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        # 当收回用户的目录下载权限时，登录该用户后，不能对该目录下的任意文件进行下载操作
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="检入检出素材.txt")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("下载"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户撤销目录的下载权限，登录用户后该目录下的文件还是可以被下载")
        # 当收回用户的目录下载权限时，登录该用户后，不能对该目录下的任意文件的历史版本文件进行下载操作
        self.click(项目对象库.文件信息.版本更多操作.format("1"))
        self.click(项目对象库.文件信息.版本更多操作选项.format("下载"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户撤销目录的下载权限，登录用户后该目录下的文件的历史版本文件还是可以被下载")
        # 当收回用户的目录下载权限时，登录该用户后，不能对该目录下子目录的任意文件进行下载操作
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录', '二级目录'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="素材2.jpg")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("下载"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户撤销目录的下载权限，登录用户后该目录子目录下的文件还是可以被下载")
        #当收回用户的目录下载权限时，登录该用户后，不能对该目录下子目录的任意文件的历史版本文件进行下载操作
        self.click(项目对象库.文件信息.版本更多操作.format("1"))
        self.click(项目对象库.文件信息.版本更多操作选项.format("下载"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户撤销目录的下载权限，登录用户后该目录子目录下的文件的历史版本文件还是可以被下载")

    def 授予用户目录下载权限(self):
        self.项目管理页面.删除项目(项目名称='项目权限设置')
        self.项目管理页面.根据模板创建项目(模板名称="权限设置模板", 项目名称='项目权限设置')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        检入素材 = ['TestData', 'FrontData', '项目页', '检入检出素材.txt']
        self.项目页面.上传单个文件(目录路径=['项目权限设置', '一级目录'], 文件路径=检入素材)
        self.项目页面.上传单个文件(目录路径=['项目权限设置', '一级目录', '二级目录'], 文件路径=素材2)
        self.项目管理页面.进入点击项目设置(项目名称='项目权限设置', 项目成员tab页=True)
        self.项目设置页面.撤回用户授权(成员名称='18942178871', 目录列表=['项目权限设置', '一级目录'], 权限列表=['目录下载'])
        self.项目设置页面.用户授权(成员名称='18942178871', 目录列表=['项目权限设置', '一级目录'], 权限列表=['目录下载'])
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        # 当授予用户的目录下载权限时，登录该用户后，对该目录下的任意文件进行下载操作
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="检入检出素材.txt")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("下载"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户授予目录的下载权限，登录用户后该目录下的文件还是不能被下载")
        # 当授予用户的目录下载权限时，登录该用户后，对该目录下的任意文件的历史版本文件进行下载操作
        self.click(项目对象库.文件信息.版本更多操作.format("1"))
        self.click(项目对象库.文件信息.版本更多操作选项.format("下载"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户授予目录的下载权限，登录用户后该目录下的文件的历史版本文件还是不能被下载")
        # 当授予用户的目录下载权限时，登录该用户后，不能对该目录下子目录的任意文件进行下载操作
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录', '二级目录'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="素材2.jpg")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("下载"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户授予目录的下载权限，登录用户后该目录子目录下的文件还是不能被下载")
        # 当授予用户的目录下载权限时，登录该用户后，不能对该目录下子目录的任意文件的历史版本文件进行下载操作
        self.click(项目对象库.文件信息.版本更多操作.format("1"))
        self.click(项目对象库.文件信息.版本更多操作选项.format("下载"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户授予目录的下载权限，登录用户后该目录子目录下的文件的历史版本文件还是不能被下载")

    def 用户目录上传权限(self):
        self.项目管理页面.删除项目(项目名称='项目权限设置')
        self.项目管理页面.根据模板创建项目(模板名称="权限设置模板", 项目名称='项目权限设置')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        检入素材 = ['TestData', 'FrontData', '项目页', '检入检出素材.txt']
        self.项目管理页面.进入点击项目设置(项目名称='项目权限设置', 项目成员tab页=True)
        self.项目设置页面.撤回用户授权(成员名称='18942178871', 目录列表=['项目权限设置', '一级目录'], 权限列表=['目录上传'])
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        #当收回用户的目录下上传权限时，登录该用户后，不能在该目录及其子目录下进行上传操作
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录'])
        self.click(项目对象库.上传)
        self.wait(对话框对象库.弹框标题.format("上传文件"), 3)
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=素材2)
        self.wait(项目对象库.待上传文件.format('素材2.jpg'), 5)
        self.click(项目对象库.上传文件按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户撤回目录的上传权限，登录用户后该目录下还是可以上传文件")
        self.click(对话框对象库.关闭弹框.format("上传文件"))
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录','二级目录'])
        self.click(项目对象库.上传)
        self.wait(对话框对象库.弹框标题.format("上传文件"), 3)
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=素材2)
        self.wait(项目对象库.待上传文件.format('素材2.jpg'), 5)
        self.click(项目对象库.上传文件按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户撤回目录的上传权限，登录用户后该目录的子目录下还是可以上传文件")
        self.click(对话框对象库.关闭弹框.format("上传文件"))
        #当授予用户目录上传权限，登录该用户后，可以在该目录及其子目录下进行上传操作
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178870', 密码='user@8870')
        self.项目管理页面.进入点击项目设置(项目名称='项目权限设置', 项目成员tab页=True)
        self.项目设置页面.用户授权(成员名称='18942178871', 目录列表=['项目权限设置', '一级目录'], 权限列表=['目录上传'])
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录'])
        self.click(项目对象库.上传)
        self.wait(对话框对象库.弹框标题.format("上传文件"), 3)
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=检入素材)
        self.wait(项目对象库.待上传文件.format('检入检出素材.txt'), 5)
        self.click(项目对象库.上传文件按钮)
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户授予目录的上传权限，登录用户后该目录下不可以上传文件")
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录', '二级目录'])
        self.click(项目对象库.上传)
        self.wait(对话框对象库.弹框标题.format("上传文件"), 3)
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=检入素材)
        self.wait(项目对象库.待上传文件.format('检入检出素材.txt'), 5)
        self.click(项目对象库.上传文件按钮)
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户撤回目录的上传权限，登录用户后该目录的子目录下还是不可以上传文件")

    def 用户文件附加权限(self):
        self.项目管理页面.删除项目(项目名称='项目权限设置')
        self.项目管理页面.根据模板创建项目(模板名称="权限设置模板", 项目名称='项目权限设置')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        检入素材 = ['TestData', 'FrontData', '项目页', '检入检出素材.txt']
        self.项目页面.批量上传文件(目录路径=['项目权限设置', '一级目录'], 文件路径列表=[检入素材, 素材2, 素材3])
        self.项目管理页面.进入点击项目设置(项目名称='项目权限设置', 项目成员tab页=True)
        self.项目设置页面.撤回用户授权(成员名称='18942178871', 目录列表=['项目权限设置', '一级目录'], 权限列表=['文件附加'])
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        #当收回用户的文件附加权限时，登录该用户后，不能在该目录及其子目录下文件进行文件附加操作
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录'])

        序号 = self.公共操作.获取文件在列表中的行号(文件名称="素材2.jpg")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("附加文件"))
        self.wait(对话框对象库.弹框标题.format("附加文件"), 3)

        self.项目页面.展开附加文件弹窗资源树(['项目权限设置', '一级目录'])
        self.click(项目对象库.附加文件.列表单选按钮.format("素材3.jpg"))
        self.click(项目对象库.附加文件.附加按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户撤回目录的附加文件权限，登录用户后该目录下还是可以附加文件")
        self.click(对话框对象库.关闭弹框.format("附加文件"))
        #当授予用户文件附加权限，登录该用户后，可以在该目录及其子目录下文件进行文件附加操作
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178870', 密码='user@8870')
        self.项目管理页面.进入点击项目设置(项目名称='项目权限设置', 项目成员tab页=True)
        self.项目设置页面.用户授权(成员名称='18942178871', 目录列表=['项目权限设置', '一级目录'], 权限列表=['文件附加'])
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="素材2.jpg")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("撤销检出"))
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("附加文件"))
        self.wait(对话框对象库.弹框标题.format("附加文件"), 3)

        self.项目页面.展开附加文件弹窗资源树(['项目权限设置', '一级目录'])
        self.click(项目对象库.附加文件.列表单选按钮.format("素材3.jpg"))
        self.click(项目对象库.附加文件.附加按钮)
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户授予目录的附加文件权限，登录用户后该目录下不可以附加文件")


class 目录权限管理工作区(page):
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

    def 数据准备(self):
        #项目动态数据准备
        self.项目管理页面.删除所有项目()
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.创建空白项目(项目名称="项目权限")
        self.项目管理页面.邀请项目成员(项目名称='项目权限', 当前用户手机号='18942178870', 成员手机号='18942178871',角色='PROJECT MANAGER')
        self.项目管理页面.点击进入项目(项目名称="项目权限")
        self.wait(项目对象库.目录节点.format("项目权限"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="项目权限")
        self.项目页面.创建文件目录(目录名称="一级目录2", 目录父节点名称="项目权限")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        self.项目管理页面.删除项目模板(模板名称="权限设置模板")
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.存为模板(项目名称="项目权限",模板名称="权限设置模板",保留团队成员=True,保留层级=2)

    def 撤回用户目录查询权限(self):
        self.项目管理页面.删除项目(项目名称='项目权限设置')
        self.项目管理页面.根据模板创建项目(模板名称="权限设置模板", 项目名称='项目权限设置')
        self.项目管理页面.点击进入项目(项目名称="项目权限设置")
        self.项目页面.进入目录设置(目录名称='一级目录')
        self.click(项目对象库.目录设置.目录设置tab页.format("权限设置"))
        self.项目页面.撤回用户权限(用户名称='18942178871',权限列表=['目录查询'])

        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        self.click(项目对象库.目录节点.format("项目权限设置"))
        if self.wait(项目对象库.列表文件名称.format("一级目录"), 3):
            raise AssertionError("撤回用户目录查询权限，登录用户后还是能看到该目录")

    def 授予用户目录查询权限(self):
        self.项目管理页面.删除项目(项目名称='项目权限设置')
        self.项目管理页面.根据模板创建项目(模板名称="权限设置模板", 项目名称='项目权限设置')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        检入素材 = ['TestData', 'FrontData', '项目页', '检入检出素材.txt']
        self.项目页面.上传单个文件(目录路径=['项目权限设置', '一级目录'], 文件路径=检入素材)
        self.项目页面.上传单个文件(目录路径=['项目权限设置', '一级目录', '二级目录'], 文件路径=素材2)
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="项目权限设置")
        self.项目页面.进入目录设置(目录名称='一级目录')
        self.click(项目对象库.目录设置.目录设置tab页.format("权限设置"))
        self.项目页面.撤回用户权限(用户名称='18942178871', 权限列表=['目录查询'])
        self.项目页面.进入目录设置(目录名称='一级目录')
        self.click(项目对象库.目录设置.目录设置tab页.format("权限设置"))
        self.项目页面.设置用户权限(用户名称='18942178871', 权限列表=['目录查询'])
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        self.click(项目对象库.目录节点.format("项目权限设置"))
        if not self.wait(项目对象库.列表文件名称.format("一级目录"), 3):
            raise AssertionError("授予用户目录查询权限，登录用户后不能看到该目录")
        self.click(项目对象库.列表文件名称.format("一级目录"))
        if not self.wait(项目对象库.列表文件名称.format("检入检出素材.txt"), 3):
            raise AssertionError("授予用户目录查询权限，登录用户后不能查看到该目录下的文件")
        self.click(项目对象库.列表文件名称.format("二级目录"))
        if not self.wait(项目对象库.列表文件名称.format("素材2.jpg"), 3):
            raise AssertionError("授予用户目录查询权限，登录用户后不能查看到该目录子目录下的文件")

    def 用户目录新增权限(self):
        self.项目管理页面.删除项目(项目名称='项目权限设置')
        self.项目管理页面.根据模板创建项目(模板名称="权限设置模板", 项目名称='项目权限设置')
        self.项目管理页面.点击进入项目(项目名称="项目权限设置")
        self.项目页面.进入目录设置(目录名称='一级目录')
        self.click(项目对象库.目录设置.目录设置tab页.format("权限设置"))
        self.项目页面.撤回用户权限(用户名称='18942178871', 权限列表=['目录新增'])
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        # 不对用户授予目录新增权限，使用用户登录后不能在该目录及其子目录在新增文件目录
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录'])
        self.click(项目对象库.新建目录)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新建文件目录"), 3)
        self.send_keys(公共元素对象库.输入框.format("文件目录名称"), "目录新增")
        self.click(对话框对象库.对话框按钮.format("新建文件目录", "提交"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("撤回用户的新增目录的权限，用户还能新增目录")
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录', '二级目录'])
        self.click(项目对象库.新建目录)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新建文件目录"), 3)
        self.send_keys(公共元素对象库.输入框.format("文件目录名称"), "目录新增")
        self.click(对话框对象库.对话框按钮.format("新建文件目录", "提交"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("撤回用户的新增目录的权限，用户在该目录的子目录下还能新增目录")
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178870', 密码='user@8870')
        self.项目管理页面.点击进入项目(项目名称="项目权限设置")
        self.项目页面.进入目录设置(目录名称='一级目录')
        self.click(项目对象库.目录设置.目录设置tab页.format("权限设置"))
        self.项目页面.设置用户权限(用户名称='18942178871', 权限列表=['目录新增'])
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        # 不对用户授予目录新增权限，使用用户登录后不能在该目录及其子目录在新增文件目录
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录'])
        self.click(项目对象库.新建目录)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新建文件目录"), 3)
        self.send_keys(公共元素对象库.输入框.format("文件目录名称"), "目录新增")
        self.click(对话框对象库.对话框按钮.format("新建文件目录", "提交"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("授予用户的新增目录的权限，登录该用户后不能新增目录")
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录', '二级目录'])
        self.click(项目对象库.新建目录)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新建文件目录"), 3)
        self.send_keys(公共元素对象库.输入框.format("文件目录名称"), "目录新增")
        self.click(对话框对象库.对话框按钮.format("新建文件目录", "提交"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("授予用户的新增目录的权限，登录该用户后在该目录的子目录下不能新增目录")

    def 用户目录删除权限(self):
        self.项目管理页面.删除项目(项目名称='项目权限设置')
        self.项目管理页面.根据模板创建项目(模板名称="权限设置模板", 项目名称='项目权限设置')
        self.项目管理页面.点击进入项目(项目名称="项目权限设置")
        self.wait(项目对象库.目录节点.format("项目权限设置"), 3)
        self.driver.refrsh()
        self.项目页面.删除资源(资源名称='目录新增权限')
        self.项目页面.创建文件目录(目录名称="目录删除权限", 目录父节点名称="项目权限设置")
        self.项目页面.创建文件目录(目录名称="删除权限", 目录父节点名称="目录删除权限")
        self.项目页面.上传单个文件(目录路径=['项目权限设置', '目录删除权限', '删除权限'], 文件路径=['TestData', 'FrontData', '项目页', '素材2.jpg'])
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="项目权限设置")
        self.项目页面.进入目录设置(目录名称='目录删除权限')
        self.click(项目对象库.目录设置.目录设置tab页.format("权限设置"))
        self.项目页面.撤回用户权限(用户名称='18942178871', 权限列表=['目录删除'])
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        # 不对用户授予目录删除权限，使用用户登录后不能删除该目录及其子目录以及目录下的资源
        self.click(项目对象库.目录节点.format('项目权限设置'))
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="目录删除权限")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("删除"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户收目录的删除权限，登录用户后该目录还是可以被删除")
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '目录删除权限'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="删除权限")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("删除"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户收目录的删除权限，登录用户后该目录的子目录还是可以被删除")
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '目录删除权限', '删除权限'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="素材2.jpg")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("删除"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户收目录的删除权限，登录用户后该目录的子目录下的文件还是可以被删除")
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178870', 密码='user@8870')
        self.项目管理页面.点击进入项目(项目名称="项目权限设置")
        self.项目页面.进入目录设置(目录名称='目录删除权限')
        self.click(项目对象库.目录设置.目录设置tab页.format("权限设置"))
        self.项目页面.设置用户权限(用户名称='18942178871', 权限列表=['目录删除'])
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        # 对用户授予目录删除权限，使用用户登录后可以删除该目录及其子目录和目录下的任意资源
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '目录删除权限', '删除权限'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="素材2.jpg")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("删除"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户授予目录的删除权限，登录用户后该目录的子目录下的文件不可以被删除")
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '目录删除权限'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="删除权限")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("删除"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户授予目录的删除权限，登录用户后该目录的子目录不可以被删除")
        self.click(项目对象库.目录节点.format('项目权限设置'))
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="目录删除权限")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("删除"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户授予目录的删除权限，登录用户后该目录不可以被删除")

    def 收回用户目录检入检出权限(self):
        self.项目管理页面.删除项目(项目名称='项目权限设置')
        self.项目管理页面.根据模板创建项目(模板名称="权限设置模板", 项目名称='项目权限设置')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        self.项目页面.创建文件目录(目录名称="一级目录3", 目录父节点名称="项目权限设置")
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        检入素材 = ['TestData', 'FrontData', '项目页', '检入检出素材.txt']
        self.项目页面.上传单个文件(目录路径=['项目权限设置', '一级目录'], 文件路径=检入素材)
        self.项目页面.批量上传文件(目录路径=['项目权限设置', '一级目录', '二级目录'], 文件路径列表=[素材2,素材3])
        self.项目页面.批量上传文件(目录路径=['项目权限设置', '一级目录3'], 文件路径列表=[检入素材, 素材2, 素材3])
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="项目权限设置")
        self.项目页面.进入目录设置(目录名称='一级目录')
        self.click(项目对象库.目录设置.目录设置tab页.format("权限设置"))
        self.项目页面.撤回用户权限(用户名称='18942178871', 权限列表=['目录检入检出'])

        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        # 对用户收回目录检出检出权限，登录该用户后，该目录不能进行检出操作
        self.click(项目对象库.目录节点.format('项目权限设置'))
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="一级目录")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("检出"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户收目录的检入检出权限，登录用户后该目录还是可以被检出")
        # 当用户没有目录检入检出权限时，该用户不能对该目录进行批量检出操作
        self.click(项目对象库.列表复选框.format("一级目录"))
        self.click(项目对象库.列表复选框.format("一级目录3"))
        self.click(项目对象库.工具栏按钮.format('检出'))
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户收目录的检入检出权限，登录用户后该目录还是可以被批量检出")
        # 对用户收回目录检出检出权限，登录该用户后，该目录及其子目录下的任意文件不能进行检入检出操作
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="二级目录")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("检出"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户收目录的检入检出权限，登录用户后该目录的子目录还是可以被检出")
        # 当用户没有目录检入检出权限时，该用户不能对该目录下的任意资源进行批量检出操作
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录', '二级目录'])
        self.click(项目对象库.列表复选框.format("素材2.jpg"))
        self.click(项目对象库.列表复选框.format("素材3.jpg"))
        self.click(项目对象库.工具栏按钮.format('检出'))
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户收目录的检入检出权限，登录用户后该目录下子目录的资源还是可以被批量检出")

    def 授予用户目录检入检出权限(self):
        self.项目管理页面.删除项目(项目名称='项目权限设置')
        self.项目管理页面.根据模板创建项目(模板名称="权限设置模板", 项目名称='项目权限设置')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        self.项目页面.创建文件目录(目录名称="一级目录3", 目录父节点名称="项目权限设置")
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        检入素材 = ['TestData', 'FrontData', '项目页', '检入检出素材.txt']
        self.项目页面.上传单个文件(目录路径=['项目权限设置', '一级目录'], 文件路径=检入素材)
        self.项目页面.批量上传文件(目录路径=['项目权限设置', '一级目录', '二级目录'], 文件路径列表=[素材2,素材3])
        self.项目页面.批量上传文件(目录路径=['项目权限设置', '一级目录3'], 文件路径列表=[检入素材, 素材2, 素材3])
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="项目权限设置")
        self.项目页面.进入目录设置(目录名称='一级目录')
        self.click(项目对象库.目录设置.目录设置tab页.format("权限设置"))
        self.项目页面.撤回用户权限(用户名称='18942178871', 权限列表=['目录检入检出'])
        self.项目页面.进入目录设置(目录名称='一级目录')
        self.click(项目对象库.目录设置.目录设置tab页.format("权限设置"))
        self.项目页面.设置用户权限(用户名称='18942178871', 权限列表=['目录检入检出'])
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        # 对用户授予目录检出检出权限，该目录及其子目录可以进行检出操作，该目录及其子目录下的任意文件可以进行检入检出操作
        self.click(项目对象库.目录节点.format('项目权限设置'))
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="一级目录")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("检出"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户授予目录的检入检出权限，登录用户后该目录还是不能被检出")
        # 当用户授予目录检入检出权限时，该用户可以对该目录进行批量检出操作
        self.click(项目对象库.列表复选框.format("一级目录"))
        self.click(项目对象库.列表复选框.format("一级目录3"))
        self.click(项目对象库.工具栏按钮.format('检出'))
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户收目录的检入检出权限，登录用户后该目录还是可以被批量检出")
        # 对用户授予目录检出检出权限，登录该用户后，该目录及其子目录下的任意文件可以进行检入检出操作
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="二级目录")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("检出"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户授予目录的检入检出权限，登录用户后该目录的子目录还是不能被检出")
        # 检入
        self.公共操作.修改文件内容(文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'], 内容=str(int(time.time())))
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="检入检出素材.txt")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("检入"))
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'])
        self.wait(项目对象库.待上传文件.format('检入检出素材.txt'), 5)
        self.click(项目对象库.上传文件按钮)
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户授予目录的检入检出权限，登录用户后该目录下的文件不能被检入")

        # 当用户授予目录检入检出权限时，该用户可以对该目录下的任意资源进行批量检出操作
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录', '二级目录'])
        self.click(项目对象库.列表复选框.format("素材2.jpg"))
        self.click(项目对象库.列表复选框.format("素材3.jpg"))
        self.click(项目对象库.工具栏按钮.format('检出'))
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户收授予目录的检入检出权限，登录用户后该目录下子目录的资源还是不能被批量检出")

    def 收回用户目录打包权限(self):
        self.项目管理页面.删除项目(项目名称='项目权限设置')
        self.项目管理页面.根据模板创建项目(模板名称="权限设置模板", 项目名称='项目权限设置')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        self.项目页面.创建文件目录(目录名称="一级目录3", 目录父节点名称="项目权限设置")
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        检入素材 = ['TestData', 'FrontData', '项目页', '检入检出素材.txt']
        self.项目页面.上传单个文件(目录路径=['项目权限设置', '一级目录'], 文件路径=检入素材)
        self.项目页面.批量上传文件(目录路径=['项目权限设置', '一级目录', '二级目录'], 文件路径列表=[素材2,素材3])
        self.项目页面.批量上传文件(目录路径=['项目权限设置', '一级目录3'], 文件路径列表=[检入素材, 素材2, 素材3])
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="项目权限设置")
        self.项目页面.进入目录设置(目录名称='一级目录')
        self.click(项目对象库.目录设置.目录设置tab页.format("权限设置"))
        self.项目页面.撤回用户权限(用户名称='18942178871', 权限列表=['目录打包'])
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        # 当收回用户的目录打包权限时，登录该用户后，不能对该目录进行打包操作
        self.click(项目对象库.目录节点.format('项目权限设置'))
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="一级目录")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("打包"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户收目录的打包权限，登录用户后该目录还是可以打包")
        # 当收回用户的目录打包权限时，登录该用户后，不能对该目录进行批量打包操作
        self.click(项目对象库.列表复选框.format("一级目录"))
        self.click(项目对象库.列表复选框.format("一级目录3"))
        self.click(项目对象库.工具栏按钮.format('打包'))
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户收回目录的打包权限，登录用户后该目录还是可以被批量打包")
        # 当收回用户的目录打包权限时，登录该用户后，不能对该目录下的任意资源进行批量打包操作
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="二级目录")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("打包"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户收回目录的打包权限，登录用户后该目录的子目录还是可以被打包")
        #
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录', '二级目录'])
        self.click(项目对象库.列表复选框.format("素材2.jpg"))
        self.click(项目对象库.列表复选框.format("素材3.jpg"))
        self.click(项目对象库.工具栏按钮.format('打包'))
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户收回目录的打包权限，登录用户后该目录下子目录的资源还是可以被批量打包")

    def 授予用户目录打包权限(self):
        self.项目管理页面.删除项目(项目名称='项目权限设置')
        self.项目管理页面.根据模板创建项目(模板名称="权限设置模板", 项目名称='项目权限设置')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        self.项目页面.创建文件目录(目录名称="一级目录3", 目录父节点名称="项目权限设置")
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        检入素材 = ['TestData', 'FrontData', '项目页', '检入检出素材.txt']
        self.项目页面.上传单个文件(目录路径=['项目权限设置', '一级目录'], 文件路径=检入素材)
        self.项目页面.批量上传文件(目录路径=['项目权限设置', '一级目录', '二级目录'], 文件路径列表=[素材2,素材3])
        self.项目页面.批量上传文件(目录路径=['项目权限设置', '一级目录3'], 文件路径列表=[检入素材, 素材2, 素材3])
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="项目权限设置")
        self.项目页面.进入目录设置(目录名称='一级目录')
        self.click(项目对象库.目录设置.目录设置tab页.format("权限设置"))
        self.项目页面.撤回用户权限(用户名称='18942178871', 权限列表=['目录打包'])
        self.项目页面.进入目录设置(目录名称='一级目录')
        self.click(项目对象库.目录设置.目录设置tab页.format("权限设置"))
        self.项目页面.设置用户权限(用户名称='18942178871', 权限列表=['目录打包'])
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        # 当授予用户目录打包权限，登录该用户后，可以对该目录进行打包操作
        self.click(项目对象库.目录节点.format('项目权限设置'))
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="一级目录")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("打包"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户授予目录的打包权限，登录用户后该目录还是不能打包")
        # 当授予用户目录打包权限，登录该用户后，可以对该目录进行批量打包操作
        self.click(项目对象库.列表复选框.format("一级目录"))
        self.click(项目对象库.列表复选框.format("一级目录3"))
        self.click(项目对象库.工具栏按钮.format('打包'))
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户授予目录的打包权限，登录用户后该目录还是不能被批量打包")
        # 当授予用户目录打包权限，登录该用户后，可以对该目录下的任意资源进行打包操作
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="二级目录")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("打包"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户授予目录的打包权限，登录用户后该目录的子目录还是不能被打包")
        # 当授予用户目录打包权限，登录该用户后，可以对该目录下的任意资源进行批量打包操作
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录', '二级目录'])
        self.click(项目对象库.列表复选框.format("素材2.jpg"))
        self.click(项目对象库.列表复选框.format("素材3.jpg"))
        self.click(项目对象库.工具栏按钮.format('打包'))
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户授予目录的打包权限，登录用户后该目录下子目录的资源还是不能被批量打包")

    def 收回用户目录下载权限(self):
        self.项目管理页面.删除项目(项目名称='项目权限设置')
        self.项目管理页面.根据模板创建项目(模板名称="权限设置模板", 项目名称='项目权限设置')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        检入素材 = ['TestData', 'FrontData', '项目页', '检入检出素材.txt']
        self.项目页面.上传单个文件(目录路径=['项目权限设置', '一级目录'], 文件路径=检入素材)
        self.项目页面.上传单个文件(目录路径=['项目权限设置', '一级目录', '二级目录'], 文件路径=素材2)
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="项目权限设置")
        self.项目页面.进入目录设置(目录名称='一级目录')
        self.click(项目对象库.目录设置.目录设置tab页.format("权限设置"))
        self.项目页面.撤回用户权限(用户名称='18942178871', 权限列表=['目录下载'])

        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        # 当收回用户的目录下载权限时，登录该用户后，不能对该目录下的任意文件进行下载操作
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="检入检出素材.txt")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("下载"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户撤销目录的下载权限，登录用户后该目录下的文件还是可以被下载")
        # 当收回用户的目录下载权限时，登录该用户后，不能对该目录下的任意文件的历史版本文件进行下载操作
        self.click(项目对象库.文件信息.版本更多操作.format("1"))
        self.click(项目对象库.文件信息.版本更多操作选项.format("下载"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户撤销目录的下载权限，登录用户后该目录下的文件的历史版本文件还是可以被下载")
        # 当收回用户的目录下载权限时，登录该用户后，不能对该目录下子目录的任意文件进行下载操作
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录', '二级目录'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="素材2.jpg")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("下载"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户撤销目录的下载权限，登录用户后该目录子目录下的文件还是可以被下载")
        # 当收回用户的目录下载权限时，登录该用户后，不能对该目录下子目录的任意文件的历史版本文件进行下载操作
        self.click(项目对象库.文件信息.版本更多操作.format("1"))
        self.click(项目对象库.文件信息.版本更多操作选项.format("下载"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户撤销目录的下载权限，登录用户后该目录子目录下的文件的历史版本文件还是可以被下载")

    def 授予用户目录下载权限(self):
        self.项目管理页面.删除项目(项目名称='项目权限设置')
        self.项目管理页面.根据模板创建项目(模板名称="权限设置模板", 项目名称='项目权限设置')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        检入素材 = ['TestData', 'FrontData', '项目页', '检入检出素材.txt']
        self.项目页面.上传单个文件(目录路径=['项目权限设置', '一级目录'], 文件路径=检入素材)
        self.项目页面.上传单个文件(目录路径=['项目权限设置', '一级目录', '二级目录'], 文件路径=素材2)
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="项目权限设置")
        self.项目页面.进入目录设置(目录名称='一级目录')
        self.click(项目对象库.目录设置.目录设置tab页.format("权限设置"))
        self.项目页面.撤回用户权限(用户名称='18942178871', 权限列表=['目录下载'])
        self.项目页面.进入目录设置(目录名称='一级目录')
        self.click(项目对象库.目录设置.目录设置tab页.format("权限设置"))
        self.项目页面.设置用户权限(用户名称='18942178871', 权限列表=['目录下载'])
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        # 当授予用户的目录下载权限时，登录该用户后，对该目录下的任意文件进行下载操作
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="检入检出素材.txt")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("下载"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户授予目录的下载权限，登录用户后该目录下的文件还是不能被下载")
        # 当授予用户的目录下载权限时，登录该用户后，对该目录下的任意文件的历史版本文件进行下载操作
        self.click(项目对象库.文件信息.版本更多操作.format("1"))
        self.click(项目对象库.文件信息.版本更多操作选项.format("下载"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户授予目录的下载权限，登录用户后该目录下的文件的历史版本文件还是不能被下载")
        # 当授予用户的目录下载权限时，登录该用户后，不能对该目录下子目录的任意文件进行下载操作
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录', '二级目录'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="素材2.jpg")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("下载"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户授予目录的下载权限，登录用户后该目录子目录下的文件还是不能被下载")
        # 当授予用户的目录下载权限时，登录该用户后，不能对该目录下子目录的任意文件的历史版本文件进行下载操作
        self.click(项目对象库.文件信息.版本更多操作.format("1"))
        self.click(项目对象库.文件信息.版本更多操作选项.format("下载"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户授予目录的下载权限，登录用户后该目录子目录下的文件的历史版本文件还是不能被下载")

    def 用户目录上传权限(self):
        self.项目管理页面.删除项目(项目名称='项目权限设置')
        self.项目管理页面.根据模板创建项目(模板名称="权限设置模板", 项目名称='项目权限设置')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        检入素材 = ['TestData', 'FrontData', '项目页', '检入检出素材.txt']
        self.项目页面.进入目录设置(目录名称='一级目录')
        self.click(项目对象库.目录设置.目录设置tab页.format("权限设置"))
        self.项目页面.撤回用户权限(用户名称='18942178871', 权限列表=['目录上传'])
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        # 当收回用户的目录下上传权限时，登录该用户后，不能在该目录及其子目录下进行上传操作
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录'])
        self.click(项目对象库.上传)
        self.wait(对话框对象库.弹框标题.format("上传文件"), 3)
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=素材2)
        self.wait(项目对象库.待上传文件.format('素材2.jpg'), 5)
        self.click(项目对象库.上传文件按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户撤回目录的上传权限，登录用户后该目录下还是可以上传文件")
        self.click(对话框对象库.关闭弹框.format("上传文件"))
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录', '二级目录'])
        self.click(项目对象库.上传)
        self.wait(对话框对象库.弹框标题.format("上传文件"), 3)
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=素材2)
        self.wait(项目对象库.待上传文件.format('素材2.jpg'), 5)
        self.click(项目对象库.上传文件按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户撤回目录的上传权限，登录用户后该目录的子目录下还是可以上传文件")
        self.click(对话框对象库.关闭弹框.format("上传文件"))
        # 当授予用户目录上传权限，登录该用户后，可以在该目录及其子目录下进行上传操作
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178870', 密码='user@8870')
        self.项目管理页面.点击进入项目(项目名称="项目权限设置")
        self.项目页面.进入目录设置(目录名称='一级目录')
        self.click(项目对象库.目录设置.目录设置tab页.format("权限设置"))
        self.项目页面.设置用户权限(用户名称='18942178871', 权限列表=['目录上传'])
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录'])
        self.click(项目对象库.上传)
        self.wait(对话框对象库.弹框标题.format("上传文件"), 3)
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=检入素材)
        self.wait(项目对象库.待上传文件.format('检入检出素材.txt'), 5)
        self.click(项目对象库.上传文件按钮)
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户授予目录的上传权限，登录用户后该目录下不可以上传文件")
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录', '二级目录'])
        self.click(项目对象库.上传)
        self.wait(对话框对象库.弹框标题.format("上传文件"), 3)
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=检入素材)
        self.wait(项目对象库.待上传文件.format('检入检出素材.txt'), 5)
        self.click(项目对象库.上传文件按钮)
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户撤回目录的上传权限，登录用户后该目录的子目录下还是不可以上传文件")

    def 用户文件附加权限(self):
        self.项目管理页面.删除项目(项目名称='项目权限设置')
        self.项目管理页面.根据模板创建项目(模板名称="权限设置模板", 项目名称='项目权限设置')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        检入素材 = ['TestData', 'FrontData', '项目页', '检入检出素材.txt']
        self.项目页面.批量上传文件(目录路径=['项目权限设置', '一级目录'], 文件路径列表=[检入素材, 素材2, 素材3])
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="项目权限设置")
        self.项目页面.进入目录设置(目录名称='一级目录')
        self.click(项目对象库.目录设置.目录设置tab页.format("权限设置"))
        self.项目页面.撤回用户权限(用户名称='18942178871', 权限列表=['文件附加'])
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        # 当收回用户的文件附加权限时，登录该用户后，不能在该目录及其子目录下文件进行文件附加操作
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录'])

        序号 = self.公共操作.获取文件在列表中的行号(文件名称="素材2.jpg")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("附加文件"))
        self.wait(对话框对象库.弹框标题.format("附加文件"), 3)

        self.项目页面.展开附加文件弹窗资源树(['项目权限设置', '一级目录'])
        self.click(项目对象库.附加文件.列表单选按钮.format("素材3.jpg"))
        self.click(项目对象库.附加文件.附加按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户撤回目录的附加文件权限，登录用户后该目录下还是可以附加文件")
        self.click(对话框对象库.关闭弹框.format("附加文件"))
        # 当授予用户文件附加权限，登录该用户后，可以在该目录及其子目录下文件进行文件附加操作
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178870', 密码='user@8870')
        self.项目管理页面.点击进入项目(项目名称="项目权限设置")
        self.项目页面.进入目录设置(目录名称='一级目录')
        self.click(项目对象库.目录设置.目录设置tab页.format("权限设置"))
        self.项目页面.设置用户权限(用户名称='18942178871', 权限列表=['文件附加'])
        self.登录页面.退出登录()
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.项目管理页面.点击进入项目(项目名称='项目权限设置')
        self.公共操作.项目下按路径展开目录(目录路径=['项目权限设置', '一级目录'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称="素材2.jpg")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("撤销检出"))
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("附加文件"))
        self.wait(对话框对象库.弹框标题.format("附加文件"), 3)

        self.项目页面.展开附加文件弹窗资源树(['项目权限设置', '一级目录'])
        self.click(项目对象库.附加文件.列表单选按钮.format("素材3.jpg"))
        self.click(项目对象库.附加文件.附加按钮)
        if self.wait(公共元素对象库.系统提示信息弹框.format("没有相关权限"), 3):
            raise AssertionError("对用户授予目录的附加文件权限，登录用户后该目录下不可以附加文件")