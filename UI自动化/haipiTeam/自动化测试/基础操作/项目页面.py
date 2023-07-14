import time

import pyautogui
from HNtest import Pltest
from HNtest.testcasesec.testcasesec import page
from HNtest.Secselenium.secdriver import Secdriver
from ..元素对象库.公共元素 import *
from ..基础操作.公共操作 import *
from ..基础操作.登录页面 import *
from ..基础操作.进入到操作位置 import *
from ..元素对象库.项目 import *


class 项目管理页面(page):
    def __init__(self,Secdriver=None):
        page.__init__(self,secdriver=Secdriver)
        self.进入到操作位置 = 进入到操作位置(Secdriver=Secdriver)
        self.公共操作 = 公共操作(Secdriver=Secdriver)
        self.登录页面 = 登录页面(Secdriver=Secdriver)

    def 展开并点击最后一项目录(self, 结构目录):
        for i in 结构目录[0:-1]:
            if self.wait(项目设置页面.节点展开按钮.format(i), 3):
                self.click(项目设置页面.节点展开按钮.format(i))
        self.click(项目设置页面.节点名称.format(结构目录[-1]))

    def 显示设置(self,value):
        self.click(项目管理对象库.显示设置按钮)
        self.click(项目管理对象库.显示设置选项.format(value))

    def 创建空白项目(self,项目名称,生命周期名称=None,版次名称=None,属性名称=None):
        self.click(项目管理对象库.创建新项目)
        self.wait(创建项目页面.页面名称, 3)
        self.click(创建项目页面.创建空白项目)
        self.wait(对话框对象库.弹框标题.format("项目名称"), 3)
        self.clear(公共元素对象库.输入框.format("项目名称"))
        self.send_keys(公共元素对象库.输入框.format("项目名称"),项目名称)
        self.click(创建项目页面.提交按钮)
        self.default_content()
        self.wait(项目设置页面.项目成员tab页, 30)

        self.click(项目设置页面.项目生命周期模板设置)
        self.click(项目设置页面.新增生命周期)
        self.wait(对话框对象库.对话框标题.format("新增项目生命周期模板"), 3)
        self.click('//div[@class="el-dialog__body"]//div[text()="生命周期名称"]/ancestor::tr/th[1]//span')
        self.click(对话框对象库.对话框按钮.format("新增项目生命周期模板","保存"))
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 3)
        if 生命周期名称:
            self.click(公共元素对象库.列表框.format("生命周期"))
            self.公共操作.滚动选择列表框选项(选项名称=生命周期名称)
        if 版次名称:
            self.click(公共元素对象库.列表框.format("版次"))
            self.公共操作.滚动选择列表框选项(选项名称=版次名称)
        if 属性名称:
            self.click(公共元素对象库.列表框.format("属性"))
            self.公共操作.滚动选择列表框选项(选项名称=属性名称)
        self.进入到操作位置.进入项目管理页()

    def 根据模板创建项目(self,模板名称,项目名称):
        self.click(项目管理对象库.创建新项目)
        self.wait(创建项目页面.页面名称, 3)
        self.click(创建项目页面.使用.format(模板名称))
        self.wait(对话框对象库.弹框标题.format("项目名称"), 3)
        self.clear(公共元素对象库.输入框.format("项目名称"))
        self.send_keys(公共元素对象库.输入框.format("项目名称"), 项目名称)
        self.click(创建项目页面.提交按钮)
        self.default_content()
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"),300)

    def 查看项目详情(self,项目名称):
        self.click(项目管理对象库.项目详情按钮.format(项目名称))

    def 查看项目成员(self,项目名称):
        self.click(项目管理对象库.项目成员按钮.format(项目名称))

    def 邀请项目成员(self,项目名称,当前用户手机号,成员手机号,标题=None,角色=None,有效期=None,链接=None,是否返回项目创建账户=True):
        self.click(项目管理对象库.项目成员按钮.format(项目名称))
        self.click(项目管理对象库.添加项目成员)
        self.wait(对话框对象库.弹框标题.format("项目协作"), 3)
        if 标题:
            self.clear(公共元素对象库.输入框.format("标题"))
            self.send_keys(公共元素对象库.输入框.format("标题"),标题)
        if 角色:
            self.click(公共元素对象库.列表框.format("角色"))
            self.公共操作.滚动选择列表框选项(选项名称=角色)
        if 有效期:
            self.click(公共元素对象库.单选按钮.format(有效期))
        if 链接:
            self.send_keys(公共元素对象库.输入框.format("链接"),链接)
        self.click(对话框对象库.弹框按钮.format("项目协作", "复制链接"))
        self.click(对话框对象库.关闭弹框.format("项目协作"))
        链接 = self.公共操作.获取剪切板内容()

        链接1=Pltest.testurl
        链接2=链接[16:]
        if 链接[7:16]=="localhost":
            链接=链接1[:20]+链接2
        self.登录页面.退出登录()
        #新开标签页
        self.driver.driver.execute_script("window.open('');")
        self.driver.close()
        self.switch_to_new_window()
        self.driver.get(链接)
        if self.wait(对话框对象库.对话框按钮.format("确认注销","重新登录"),3):
            self.click(对话框对象库.对话框按钮.format("确认注销","重新登录"))
        # self.登录页面.短信快捷登录(手机号=成员手机号)
        self.登录页面.账号密码登录(账号=成员手机号, 密码='user@'+成员手机号[7:])
        time.sleep(3)
        self.click(对话框对象库.对话框按钮2.format(f"邀请你参加“{项目名称}”", "加入"))
        if 角色=="PROJECT ASSISTANT" or 角色==None:
            self.driver.driver.execute_script("window.open('');")
            self.driver.close()
            self.switch_to_new_window()
            if 链接1[8:16]=="hapyteam":
                self.driver.get('https://hapyteam.com/project')
            else:
                self.driver.get(链接1[:20]+'project')
        else:
            self.wait(项目对象库.目录节点.format(项目名称), 3)
        if 是否返回项目创建账户:
            self.登录页面.退出登录()
            # self.登录页面.短信快捷登录(手机号=当前用户手机号)
            self.driver.refrsh()
            if self.wait(对话框对象库.对话框按钮.format("确认注销", "重新登录"), 3):
                self.click(对话框对象库.对话框按钮.format("确认注销", "重新登录"))
            self.登录页面.账号密码登录(账号=当前用户手机号, 密码='user@' + 当前用户手机号[7:])
            self.进入到操作位置.进入项目管理页()

    def 移除项目成员(self,项目名称,移除成员名称):
        self.click(项目管理对象库.项目成员按钮.format(项目名称))
        if self.wait(项目管理对象库.移除项目成员.format(移除成员名称), 3):
            self.click(项目管理对象库.移除项目成员.format(移除成员名称))
            self.wait(公共元素对象库.系统提示信息弹框.format("操作成功"), 3)

    def 设置项目标签(self,项目名称,标签序号):
        self.click(项目管理对象库.更多操作按钮.format(项目名称))
        self.click(项目管理对象库.更多操作选项.format("标签"))
        self.wait(项目管理对象库.标签.format(标签序号),3)
        self.click(项目管理对象库.标签.format(标签序号))

    def 设置项目节点(self,项目名称,状态):
        self.click(项目管理对象库.更多操作按钮.format(项目名称))
        self.click(项目管理对象库.展开操作选项.format("项目节点"))
        self.wait(项目管理对象库.更多操作选项2.format(状态),3)
        self.click(项目管理对象库.更多操作选项2.format(状态))

    def 删除项目(self,项目名称):
        if self.wait(项目管理对象库.项目卡片.format(项目名称),3):
            self.click(项目管理对象库.更多操作按钮.format(项目名称))
            if self.wait(项目管理对象库.更多操作选项.format("删除项目"),3):
                self.click(项目管理对象库.更多操作选项.format("删除项目"))
                self.default_content()
                self.wait(对话框对象库.对话框标题.format("提示"),3)
                self.click(对话框对象库.对话框按钮.format("提示","确定"))
                self.wait(公共元素对象库.系统提示信息弹框.format("删除"),3)
            elif self.wait(项目管理对象库.更多操作选项.format("退出项目")) :
                self.click(项目管理对象库.更多操作选项.format("退出项目"))
                self.wait(公共元素对象库.系统提示信息弹框.format("成功"),3)

    def 删除所有项目(self):
        names=[]
        if self.wait('//div[@class="project_box"]//span[@class="project_name"]',3):
            elems=self.driver.getelements('//div[@class="project_box"]//span[@class="project_name"]')
            for elem in elems:
                names.append(elem.text)
            if len(names)!=0:
                for name in names:
                    self.删除项目(项目名称=name)

    def 查看项目动态(self,项目名称):
        self.click(项目管理对象库.更多操作按钮.format(项目名称))
        self.click(项目管理对象库.更多操作选项.format("项目动态"))
        self.wait(项目管理对象库.项目动态页.项目动态页标题, 3)

    def 存为模板(self,项目名称,模板名称,保留团队成员=None,保留项目文件=None,文件路径列表=None,目录文件列表=None,保留层级=None):
        i=0
        self.click(项目管理对象库.更多操作按钮.format(项目名称))
        self.click(项目管理对象库.更多操作选项.format("存为模板"))
        self.wait(对话框对象库.弹框标题.format("存为模板"),3)
        self.send_keys(公共元素对象库.输入框.format("模板名称"),模板名称)
        if 保留团队成员:
            self.click(公共元素对象库.单选按钮.format("保留团队成员"))
        if 保留项目文件:
            self.click(公共元素对象库.单选按钮.format("保留项目文件"))
        if 文件路径列表:
            for 文件路径 in 文件路径列表:
                for path in 文件路径:
                    if self.wait(项目对象库.节点展开按钮2.format(path), 1):
                        self.click(项目对象库.节点展开按钮2.format(path))
                self.click(项目对象库.目录节点2.format(文件路径[-1]))
                time.sleep(2)
                目录文件=目录文件列表[i]
                for 文件 in 目录文件:
                    self.click(项目管理对象库.目录文件复选框.format(文件))
                i+=1
        if 保留层级:
            self.clear(项目管理对象库.保留层级)
            self.send_keys(项目管理对象库.保留层级, 保留层级)
        self.click(对话框对象库.对话框按钮.format("存为模板","确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"),3)

    def 项目设置(self,项目名称,修改项目名称=None,项目权限=None,项目简介=None):
        self.click(项目管理对象库.更多操作按钮.format(项目名称))
        self.click(项目管理对象库.更多操作选项.format("项目设置"))
        if 修改项目名称:
            self.clear(公共元素对象库.输入框.format("项目名称"))
            self.send_keys(公共元素对象库.输入框.format("项目名称"),修改项目名称)
        if 项目权限:
            self.click(公共元素对象库.列表框.format("项目权限"))
            self.click(公共元素对象库.列表框选项.format(项目权限))
        if 项目简介:
            self.clear(公共元素对象库.文本框.format("项目简介"))
            self.send_keys(公共元素对象库.文本框.format("项目简介"),项目简介)
        self.进入到操作位置.进入项目管理页()
        self.wait(公共元素对象库.系统提示信息弹框.format("修改成功"),3)

    def 点击进入项目(self,项目名称):
        self.进入到操作位置.进入项目管理页()
        self.wait(项目管理对象库.项目卡片.format(项目名称), 3)
        time.sleep(3)
        self.click(项目管理对象库.项目卡片.format(项目名称))

    def 删除项目模板(self,模板名称):
        self.进入到操作位置.进入项目管理页()
        self.click(项目管理对象库.创建新项目)
        if self.wait(创建项目页面.模板卡片.format(模板名称),3):
            self.click(创建项目页面.删除.format(模板名称))
            self.wait(对话框对象库.对话框标题.format("提示"))
            self.click(对话框对象库.对话框按钮.format("提示","确定"))
            self.wait(公共元素对象库.系统提示信息弹框.format("删除成功"),3)
        self.进入到操作位置.进入项目管理页()

    def 点击进入标签管理(self,项目名称):
        self.进入到操作位置.进入项目管理页()
        self.click(项目管理对象库.更多操作按钮.format(项目名称))
        self.click(项目管理对象库.更多操作选项.format("标签管理"))

    def 进入点击项目设置(self,项目名称,项目成员tab页=None,项目生命周期模板设置=None):
        self.进入到操作位置.进入项目管理页()
        self.click(项目管理对象库.更多操作按钮.format(项目名称))
        self.click(项目管理对象库.更多操作选项.format("项目设置"))
        if 项目成员tab页:
            self.click(项目设置页面.项目成员tab页)
        if 项目生命周期模板设置:
            self.click(项目设置页面.项目生命周期模板设置)

    class 项目设置页面(page):

        def __init__(self, Secdriver=None):
            page.__init__(self, secdriver=Secdriver)
            self.进入到操作位置 = 进入到操作位置(Secdriver=Secdriver)
            self.公共操作 = 公共操作(Secdriver=Secdriver)
            self.登录页面 = 登录页面(Secdriver=Secdriver)

        def 展开并点击最后一项目录(self,结构目录):
            for i in 结构目录[0:-1]:
                if self.wait(项目设置页面.节点展开按钮.format(i), 3):
                    self.click(项目设置页面.节点展开按钮.format(i))
            self.click(项目设置页面.节点名称.format(结构目录[-1]))

        def 项目设置(self, 项目名称, 修改项目名称=None, 项目权限=None, 项目简介=None):
            self.click(项目管理对象库.更多操作按钮.format(项目名称))
            self.click(项目管理对象库.更多操作选项.format("项目设置"))
            if 修改项目名称:
                self.clear(公共元素对象库.输入框.format("项目名称"))
                self.send_keys(公共元素对象库.输入框.format("项目名称"), 修改项目名称)
            if 项目权限:
                self.click(公共元素对象库.列表框.format("项目权限"))
                self.click(公共元素对象库.列表框选项.format(项目权限))
            if 项目简介:
                self.clear(公共元素对象库.文本框.format("项目简介"))
                self.send_keys(公共元素对象库.文本框.format("项目简介"), 项目简介)
            self.进入到操作位置.进入项目管理页()
            self.wait(公共元素对象库.系统提示信息弹框.format("修改成功"), 3)

        def 用户授权(self,成员名称,目录列表,权限列表):
            self.click(项目设置页面.权限编辑按钮.format(成员名称))
            self.wait(对话框对象库.弹框标题.format("编辑权限"),3)
            self.展开并点击最后一项目录(结构目录=目录列表)
            for qx in 权限列表:
                if self.wait(项目设置页面.未选_权限复选框.format(qx),3):
                    self.click(项目设置页面.未选_权限复选框.format(qx))
            self.click(对话框对象库.弹框按钮.format("编辑权限","保存"))
            self.click(对话框对象库.关闭弹框.format("编辑权限"))

        def 撤回用户授权(self,成员名称,目录列表,权限列表):
            self.click(项目设置页面.权限编辑按钮.format(成员名称))
            self.wait(对话框对象库.弹框标题.format("编辑权限"), 3)
            self.展开并点击最后一项目录(结构目录=目录列表)
            for qx in 权限列表:
                if self.wait(项目设置页面.已选_权限复选框.format(qx), 3):
                    self.click(项目设置页面.已选_权限复选框.format(qx))
            self.click(对话框对象库.弹框按钮.format("编辑权限", "保存"))
            self.click(对话框对象库.关闭弹框.format("编辑权限"))

        def 切换用户角色(self,成员名称,角色名称):
            self.click(项目设置页面.角色编辑按钮.format(成员名称))
            self.wait(对话框对象库.弹框标题.format("编辑角色"), 3)
            self.click(公共元素对象库.列表框.format("选择角色"))
            self.click(公共元素对象库.列表框选项.format(角色名称))
            self.click(对话框对象库.弹框按钮.format("编辑角色", "提交"))
            self.wait(公共元素对象库.系统提示信息弹框.format("成功"),3)
            if self.wait(对话框对象库.弹框标题.format("编辑角色"),3):
                self.click(对话框对象库.关闭弹框.format("编辑角色"))


        def 批量删除生命周期(self,生命周期列表):
            self.click(项目设置页面.项目生命周期模板设置)
            for 生命周期 in 生命周期列表:
                self.click(项目设置页面.生命周期复选框.format(生命周期))
            self.click(项目设置页面.删除生命周期)
            self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 3)

    class 标签管理页面(page):

        def __init__(self, Secdriver=None):
            page.__init__(self, secdriver=Secdriver)
            self.进入到操作位置 = 进入到操作位置(Secdriver=Secdriver)
            self.公共操作 = 公共操作(Secdriver=Secdriver)

        def 新增标签(self,标签名称):
            self.click(标签管理对象库.新增标签按钮)
            self.wait(对话框对象库.弹框标题.format("新增标签"), 3)
            self.send_keys(公共元素对象库.输入框.format("标签名"), 标签名称)
            self.click(对话框对象库.弹框按钮.format("新增标签", "确定"))
            self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 3)

        def 删除单个标签(self,标签名称):
            self.click(标签管理对象库.删除单个标签.format("删除标签1"))
            self.wait(对话框对象库.对话框标题.format("提示"), 3)
            self.click(对话框对象库.对话框按钮.format("提示", "确定"))
            self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 3)

class 项目页面(page):
    def __init__(self, Secdriver=None):
        page.__init__(self, secdriver=Secdriver)
        self.进入到操作位置 = 进入到操作位置(Secdriver=Secdriver)
        self.公共操作 = 公共操作(Secdriver=Secdriver)
        self.登录页面 = 登录页面(Secdriver=Secdriver)

    def 刷新列表(self):
        self.click(项目对象库.刷新列表)
        time.sleep(3)

    def 创建文件目录(self,目录名称,目录父节点名称):
        self.click(项目对象库.目录节点.format(目录父节点名称))
        self.click(项目对象库.新建目录)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新建文件目录"),3)
        self.clear(公共元素对象库.输入框.format("文件目录名称"))
        self.send_keys(公共元素对象库.输入框.format("文件目录名称"),目录名称)
        self.click(对话框对象库.对话框按钮.format("新建文件目录","提交"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"),3)

    def 按路径展开目录(self,目录路径):
        '''
        :param 目录路径: 路径列表 ['根节点名称','','']
        '''
        for path in 目录路径:
            if self.wait(项目对象库.节点展开按钮.format(path),1):
                self.click(项目对象库.节点展开按钮.format(path))
        self.click(项目对象库.目录节点.format(目录路径[-1]))
        time.sleep(2)

    def 收起目录(self,目录名称):
        if self.wait(项目对象库.节点收起按钮.format(目录名称),3):
            self.click(项目对象库.节点收起按钮.format(目录名称))

    def 上传单个文件(self,目录路径,文件路径):
        '''
        :param 目录路径: 路径列表 ['根节点名称','','']
        :param 文件路径: ['TestData','BaseData',moudel,file]
        '''
        self.按路径展开目录(目录路径=目录路径)
        self.click(项目对象库.上传)
        self.wait(对话框对象库.弹框标题.format("上传文件"), 3)
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=文件路径)
        self.wait(项目对象库.待上传文件.format(文件路径[-1]), 5)
        self.click(项目对象库.上传文件按钮)
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 300)

    def 批量上传文件(self,目录路径,文件路径列表):
        '''
        :param 目录路径: 路径列表 ['根节点名称','','']
        :param 文件路径列表: [['TestData','BaseData',moudel,file1],['TestData','BaseData',moudel,file2]]
        '''
        self.按路径展开目录(目录路径=目录路径)
        self.click(项目对象库.上传)
        self.wait(对话框对象库.弹框标题.format("上传文件"), 3)
        for 文件路径 in 文件路径列表:
            self.click(项目对象库.点击上传按钮)
            self.公共操作.win上传文件(文件路径=文件路径)
            self.wait(项目对象库.待上传文件.format(文件路径[-1]), 5)
        self.click(项目对象库.上传文件按钮)
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 300)
        time.sleep(10)

    def 收藏资源(self,目录路径,资源名称):
        self.按路径展开目录(目录路径=目录路径)
        序号 = self.公共操作.获取文件在列表中的行号(文件名称=资源名称)
        self.click(项目对象库.悬浮列收藏.format(序号))
        self.wait(公共元素对象库.系统提示信息弹框.format("收藏成功"))

    def 检出资源(self, 资源名称, 目录路径=None):
        if 目录路径:
            self.按路径展开目录(目录路径=目录路径)
        time.sleep(1)
        序号 = self.公共操作.获取文件在列表中的行号(文件名称=资源名称)
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("检出"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "打包预览文件"))
            if self.wait(对话框对象库.对话框标题.format("提示"), 3):
                self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        self.wait(项目对象库.检出按钮.format(资源名称), 3)

    def 文件撤销检出(self, 资源名称, 目录路径=None):
        if 目录路径:
            self.按路径展开目录(目录路径=目录路径)
        time.sleep(1)
        序号 = self.公共操作.获取文件在列表中的行号(文件名称=资源名称)
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("撤销检出"))
        self.wait(项目对象库.检出按钮.format(资源名称), 3)

    def 文件检入(self,目录路径,文件名,文件路径):
        self.按路径展开目录(目录路径=目录路径)
        time.sleep(1)
        序号 = self.公共操作.获取文件在列表中的行号(文件名称=文件名)
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("检入"))
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=文件路径)
        self.wait(项目对象库.待上传文件.format(文件名), 5)
        self.click(项目对象库.上传文件按钮)
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 300)

    def 改变文件状态(self,文件名,状态名称,目录路径=None):
        if 目录路径:
            self.按路径展开目录(目录路径=目录路径)
            time.sleep(1)
        序号 = self.公共操作.获取文件在列表中的行号(文件名称=文件名)
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("改变状态"))
        self.click(项目对象库.行操作选项.format(状态名称))
        self.wait(公共元素对象库.系统提示信息弹框.format("操作成功"))


    def 附加文件(self,文件名称,附加文件路径列表,目录路径=None):
        if 目录路径:
            self.按路径展开目录(目录路径=目录路径)
            time.sleep(1)
        序号 = self.公共操作.获取文件在列表中的行号(文件名称=文件名称)
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("附加文件"))
        self.wait(对话框对象库.弹框标题.format("附加文件"),3)
        for 附加文件路径 in 附加文件路径列表:
            附加文件=附加文件路径[-1]
            文件路径=附加文件路径.remove(附加文件路径[-1])
            if 文件路径:
                self.展开附加文件弹窗资源树(资源路径=文件路径)
            self.click(项目对象库.附加文件.列表单选按钮.format(附加文件))
        self.click(项目对象库.附加文件.附加按钮)
        self.default_content()
        self.wait(公共元素对象库.系统提示信息弹框.format("操作成功"), 3)

    def 展开附加文件弹窗资源树(self,资源路径):
        for code in 资源路径:
            if self.wait(项目对象库.附加文件.节点展开按钮.format(code),1):
                self.click(项目对象库.附加文件.节点展开按钮.format(code))

    def 删除资源(self,资源名称,目录路径=None):
        if 目录路径:
            self.按路径展开目录(目录路径=目录路径)
        if self.wait(项目对象库.列表行操作.format(资源名称)):
            序号 = self.公共操作.获取文件在列表中的行号(文件名称=资源名称)
            self.click(项目对象库.悬浮列行操作.format(序号))
            self.click(项目对象库.行操作选项.format("删除"))
            if self.wait(对话框对象库.对话框标题.format("提示"),3):
                self.click(对话框对象库.对话框按钮.format("提示","确定"))
            self.wait(公共元素对象库.系统提示信息弹框.format("操作成功"), 3)

    def 资源打包(self,目录路径,资源名称):
        self.按路径展开目录(目录路径=目录路径)
        序号 = self.公共操作.获取文件在列表中的行号(文件名称=资源名称)
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("打包"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "是"))
        filepath=self.公共操作.检查文件是否下载完成()
        return filepath

    def 下载文件(self,目录路径,资源名称):
        self.按路径展开目录(目录路径=目录路径)
        序号 = self.公共操作.获取文件在列表中的行号(文件名称=资源名称)
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("下载"))
        filepath = self.公共操作.检查文件是否下载完成()
        return filepath

    def 分享文件(self,目录路径,资源名称,有效期=None,下载=False):
        self.按路径展开目录(目录路径=目录路径)
        序号 = self.公共操作.获取文件在列表中的行号(文件名称=资源名称)
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("分享"))
        if 有效期:
            self.click(公共元素对象库.单选按钮.format(有效期))
        if 下载==True:
            self.click(公共元素对象库.单选按钮.format("下载"))
        self.click(对话框对象库.弹框按钮.format('分享文件', '生成链接'))
        self.click(对话框对象库.弹框按钮.format('分享文件', '复制链接'))
        self.click(对话框对象库.关闭弹框.format("分享文件"))

    def 批量分享文件(self,目录路径,资源列表,有效期=None,下载=False):
        self.按路径展开目录(目录路径=目录路径)
        for 资源 in 资源列表:
            self.click(项目对象库.列表复选框.format(资源))
        self.click(项目对象库.工具栏按钮.format('分享'))
        self.click(项目对象库.行操作选项.format("分享"))
        if 有效期:
            self.click(公共元素对象库.单选按钮.format(有效期))
        if 下载 == True:
            self.click(公共元素对象库.单选按钮.format("下载"))
        self.click(对话框对象库.弹框按钮.format('分享文件', '生成链接'))
        self.click(对话框对象库.弹框按钮.format('分享文件', '复制链接'))
        self.click(对话框对象库.关闭弹框.format("分享文件"))

    def 批量检出资源(self,目录路径,资源列表):
        self.按路径展开目录(目录路径=目录路径)
        for 资源 in 资源列表:
            self.click(项目对象库.列表复选框.format(资源))
        self.click(项目对象库.工具栏按钮.format('检出'))
        self.wait(公共元素对象库.系统提示信息弹框.format("检出成功"), 3)

    def 批量撤销检出(self,目录路径,资源列表):
        self.按路径展开目录(目录路径=目录路径)
        for 资源 in 资源列表:
            self.click(项目对象库.列表复选框.format(资源))
        self.click(项目对象库.工具栏按钮.format('撤销检出'))
        self.wait(公共元素对象库.系统提示信息弹框.format("撤销检出成功"), 3)

    def 批量删除资源(self,目录路径,资源列表):
        self.按路径展开目录(目录路径=目录路径)
        for 资源 in 资源列表:
            self.click(项目对象库.列表复选框.format(资源))
        self.click(项目对象库.工具栏按钮.format('删除'))
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("删除成功!"), 3)

    def 批量打包资源(self,目录路径,资源列表):
        self.按路径展开目录(目录路径=目录路径)
        for 资源 in 资源列表:
            self.click(项目对象库.列表复选框.format(资源))
        self.click(项目对象库.工具栏按钮.format('打包'))
        filepath = self.公共操作.检查文件是否下载完成()
        return filepath

    def 搜索文件(self,关键词):
        self.clear(项目对象库.搜索框)
        self.send_keys(项目对象库.搜索框,关键词)
        self.click(项目对象库.搜索按钮)
        time.sleep(3)

    def 归档单个文件(self,文件名称):
        序号 = self.公共操作.获取文件在列表中的行号(文件名称=文件名称)
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("文件归档"))
        self.wait(公共元素对象库.系统提示信息弹框.format("操作成功"), 3)

    def 批量归档(self,资源列表):
        for 资源 in 资源列表:
            self.click(项目对象库.列表复选框.format(资源))
        self.click(项目对象库.工具栏按钮.format('文件归档'))
        self.wait(公共元素对象库.系统提示信息弹框.format("操作成功"), 3)

    def 单个添加标签(self,文件名称,标签名):
        序号 = self.公共操作.获取文件在列表中的行号(文件名称=文件名称)
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("添加标签"))
        self.wait(对话框对象库.弹框标题.format("添加标签"),3)
        self.click(公共元素对象库.列表框.format("标签名"))
        self.send_keys(公共元素对象库.输入框.format("标签名"),标签名)
        self.click(公共元素对象库.列表框选项.format(标签名))
        self.click(对话框对象库.对话框按钮.format("添加标签","确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"),3)

    def 添加标签文件(self,标签名称,标签文件路径列表):
        self.click(标签管理对象库.标签名.format(标签名称))
        self.click(标签管理对象库.新增文件按钮)
        self.wait(对话框对象库.弹框标题.format("选择文件"), 3)
        for 标签文件路径 in 标签文件路径列表:
            附加文件 = 标签文件路径[-1]
            文件路径 = 标签文件路径.remove(标签文件路径[-1])
            if 文件路径:
                for code in 文件路径:
                    if self.wait(标签管理对象库.新增标签文件.节点展开按钮.format(code), 1):
                        self.click(标签管理对象库.新增标签文件.节点展开按钮.format(code))
            self.click(标签管理对象库.新增标签文件.列表单选按钮.format(附加文件))
        self.click(标签管理对象库.新增标签文件.保存按钮)
        self.default_content()
        self.wait(公共元素对象库.系统提示信息弹框.format("操作成功"), 3)






    def 进入目录设置(self, 目录名称):
        序号 = self.公共操作.获取文件在列表中的行号(文件名称=目录名称)
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("设置"))
        self.wait(对话框对象库.弹框标题.format("设置"), 3)

    def 目录设置生命周期(self, 目录名称,生命周期名称):
        序号 = self.公共操作.获取文件在列表中的行号(文件名称=目录名称)
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("设置"))
        self.wait(对话框对象库.弹框标题.format("设置"), 3)
        self.click(项目对象库.目录设置.生命周期列表框)
        self.click(公共元素对象库.列表框选项.format(生命周期名称))
        self.click(对话框对象库.关闭弹框.format("设置"))

    def 添加节点人员(self, 节点名称, 成员名称=None, 所有人提交后可进入下一节点=True):
        self.click(项目对象库.目录设置.节点下成员.format(节点名称))
        if 成员名称:
            self.click(项目对象库.目录设置.添加人员按钮)
            self.wait(对话框对象库.弹框标题.format("选择人员"), 3)
            self.click(项目对象库.目录设置.未选_成员复选框.format(成员名称))
            self.click(对话框对象库.弹框按钮.format("选择人员", "确定"))
        if 所有人提交后可进入下一节点 == True:
            if self.wait(项目对象库.目录设置.未选_所有人提交后可进入下一节点按钮, 3):
                self.click(项目对象库.目录设置.未选_所有人提交后可进入下一节点按钮)
        if 所有人提交后可进入下一节点 == False:
            if self.wait(项目对象库.目录设置.已选_所有人提交后可进入下一节点按钮, 3):
                self.click(项目对象库.目录设置.已选_所有人提交后可进入下一节点按钮)

    def 移除节点人员(self, 节点名称, 成员名称):
        self.click(项目对象库.目录设置.节点下成员.format(节点名称))
        self.click(项目对象库.目录设置.移除成员按钮.format(成员名称))

    def 新增会签(self,专业,人员):
        self.click(项目对象库.目录设置.新增会签)
        self.wait(对话框对象库.弹框标题.format("新增"), 3)
        self.click(公共元素对象库.列表框.format("专业:"))
        self.click(公共元素对象库.列表框选项.format(专业))
        self.click(公共元素对象库.列表框.format("人员:"))
        self.click(公共元素对象库.列表框选项.format(人员))
        self.click(对话框对象库.弹框按钮.format("新增", "确定"))

    def 设置用户权限(self,用户名称,权限列表):
        权限=['全选','目录查询','目录新增','目录删除','目录修改','目录检入检出','目录打包','目录下载','目录上传','文件附加','版本回退','文件改变生命周期状态']
        for i in 权限列表:
            序号 = 权限.index(i)+2
            if self.wait(项目对象库.目录设置.未授权复选框.format(用户名称,序号),3):
                self.click(项目对象库.目录设置.未授权复选框.format(用户名称,序号))
        self.click(对话框对象库.弹框按钮.format("设置","保存"))
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"),300)

    def 撤回用户权限(self,用户名称,权限列表):
        权限=['全选','目录查询','目录新增','目录删除','目录修改','目录检入检出','目录打包','目录下载','目录上传','文件附加','版本回退','文件改变生命周期状态']
        for i in 权限列表:
            序号 = 权限.index(i)+2
            if self.wait(项目对象库.目录设置.已授权复选框.format(用户名称,序号),3):
                self.click(项目对象库.目录设置.已授权复选框.format(用户名称,序号))
        self.click(对话框对象库.弹框按钮.format("设置", "保存"))
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 300)

