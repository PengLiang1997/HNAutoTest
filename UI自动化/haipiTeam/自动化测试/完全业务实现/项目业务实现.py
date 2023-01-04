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

class 项目管理工作区(page):
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
        self.进入到操作位置.进入生命周期工作区()
        self.生命周期管理页面.删除所有生命周期()
        self.进入到操作位置.进入版次工作区()
        self.版次管理页面.删除所有版次()
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.创建空白项目(项目名称="查看项目动态")
        self.项目管理页面.邀请项目成员(项目名称='查看项目动态', 当前用户手机号='18942178870', 成员手机号='18942178871')
        self.项目管理页面.邀请项目成员(项目名称='查看项目动态', 当前用户手机号='18942178870', 成员手机号='17789371421',角色='PROJECT MANAGER')
        self.项目管理页面.移除项目成员(项目名称="查看项目动态", 移除成员名称="18942178871")
        self.项目管理页面.点击进入项目(项目名称="查看项目动态")
        self.wait(项目对象库.目录节点.format("查看项目动态"), 3)
        self.driver.refrsh()
        # 创建文件目录
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="查看项目动态")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        # 上传文件
        素材2=['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3=['TestData', 'FrontData', '项目页', '素材3.jpg']
        self.click(项目对象库.目录节点.format("一级目录"))
        self.项目页面.批量上传文件(目录路径=['查看项目动态', '一级目录'], 文件路径列表=[素材2,素材3])
        time.sleep(3)
        self.项目页面.刷新列表()
        self.项目页面.删除资源(目录路径=['查看项目动态', '一级目录'],资源名称='素材3.jpg')
        self.项目页面.上传单个文件(目录路径=['文件检入', '一级目录'], 文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'])
        self.项目页面.检出资源(目录路径=['文件检入', '一级目录'], 资源名称='检入检出素材.txt')
        self.项目页面.文件撤销检出(目录路径=['文件检入', '一级目录'], 资源名称='检入检出素材.txt')
        self.项目页面.检出资源(目录路径=['文件检入', '一级目录'], 资源名称='检入检出素材.txt')
        self.公共操作.修改文件内容(文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'], 内容=str(int(time.time())))
        self.项目页面.文件检入(目录路径=['文件检入', '一级目录'],文件名='检入检出素材.txt',文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'])
        #
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.创建空白项目(项目名称="模板保存文件")
        self.项目管理页面.点击进入项目(项目名称="模板保存文件")
        for i in range(5):
            文件列表=[]
            for j in range(10):
                num1=i*10
                num2=num1+j
                list=['TestData', 'FrontData', '存为模板', f'{i*10+j}.jpg']
                文件列表.append(['TestData', 'FrontData', '存为模板', f'{i*10+j}.jpg'])
            print(文件列表)
            self.项目页面.批量上传文件(目录路径=['模板保存文件'], 文件路径列表=文件列表)
        self.项目页面.上传单个文件(目录路径=['模板保存文件'], 文件路径=['TestData', 'FrontData', '存为模板', '50.jpg'])

    def 准备项目模板(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目模板(模板名称='根据模板创建项目')
        self.项目管理页面.存为模板(项目名称='查看项目动态',模板名称='根据模板创建项目',文件路径列表=[['查看项目动态', '一级目录']],目录文件列表=[['素材2.jpg','检入检出素材.txt']])

    def 准备项目设置数据(self):
        self.进入到操作位置.进入项目管理页()
        self.进入到操作位置.进入生命周期工作区()
        self.生命周期管理页面.删除生命周期('生命周期')
        self.生命周期管理页面.删除生命周期('切换生命周期')
        self.生命周期管理页面.进入新增生命周期弹框(生命周期名称='生命周期')
        self.生命周期管理页面.添加生命周期节点(节点名称='11')
        self.生命周期管理页面.添加生命周期节点(节点名称='22')
        self.生命周期管理页面.添加生命周期节点(节点名称='33')
        self.生命周期管理页面.设置升版流程(节点名称='11',开始节点='11',结束节点='22')
        self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        self.生命周期管理页面.进入新增生命周期弹框(生命周期名称='切换生命周期')
        self.生命周期管理页面.添加生命周期节点(节点名称='aa')
        self.生命周期管理页面.添加生命周期节点(节点名称='bb')
        self.生命周期管理页面.设置升版流程(节点名称='aa', 开始节点='aa', 结束节点='bb')
        self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        self.进入到操作位置.进入版次工作区()
        self.版次管理页面.删除版次("版次")
        self.版次管理页面.删除版次("切换版次")
        self.版次管理页面.进入新增版次弹框(版次名称="版次")
        self.版次管理页面.添加版次节点(节点名称="A")
        self.版次管理页面.添加版次节点(节点名称="B")
        self.版次管理页面.添加版次节点(节点名称="C")
        self.版次管理页面.添加版次节点(节点名称="D")
        self.click(对话框对象库.弹框按钮.format("新增", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        self.版次管理页面.进入新增版次弹框(版次名称="切换版次")
        self.版次管理页面.添加版次节点(节点名称="E")
        self.版次管理页面.添加版次节点(节点名称="F")
        self.版次管理页面.添加版次节点(节点名称="G")
        self.版次管理页面.添加版次节点(节点名称="H")
        self.click(对话框对象库.弹框按钮.format("新增", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)

    def 权限编辑数据准备(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="权限编辑")
        self.项目管理页面.创建空白项目(项目名称="权限编辑",生命周期名称='生命周期')
        self.项目管理页面.邀请项目成员(项目名称='权限编辑', 当前用户手机号='18942178870', 成员手机号='18942178871', 角色='PROJECT MANAGER')
        self.项目管理页面.点击进入项目(项目名称="权限编辑")
        self.wait(项目对象库.目录节点.format("权限编辑"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="权限编辑")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        self.项目页面.创建文件目录(目录名称="三级目录", 目录父节点名称="二级目录")
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        self.click(项目对象库.目录节点.format("一级目录"))
        self.项目页面.批量上传文件(目录路径=['权限编辑', '一级目录','二级目录'], 文件路径列表=[素材2, 素材3])

    ##################以下为业务实现方法#####################

    def 项目显示方式(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="项目显示1")
        self.项目管理页面.创建空白项目(项目名称="项目显示1")
        #项目显示方式选择为卡片，所有项目以卡片形式，在项目管理管理页面平铺展示
        self.default_content()
        self.项目管理页面.显示设置(value="卡片")
        if not self.wait(项目管理对象库.项目卡片.format("项目显示1"), 3):
            raise AssertionError("项目显示方式设置为卡片，在项目管理页面为查看到项目卡片")
        #项目显示方式选择为列表，所有项目在项目管理页面列表展示
        self.项目管理页面.显示设置(value="列表")
        self.default_content()
        if not self.wait(项目管理对象库.列表项目名称.format("项目显示1"),3):
            raise AssertionError("列表显示项目时，未查看到项目：项目显示1")
        # 列表显示项目名称、创建人、创建日期、团队、文件数量、状态、备注等信息
        creater=self.driver.getelement(项目管理对象库.列表内容.format("项目显示1","3")).text
        创建人=creater.replace(' ','')
        if 创建人!="18942178870":
            raise AssertionError(f"列表显示项目时，项目的创建人信息显示有误，基准为：18942178870，页面为：{创建人}")
        createdata = self.driver.getelement(项目管理对象库.列表内容.format("项目显示1", "4")).text
        创建日期 = createdata.replace(' ', '')
        Y= time.strftime('%Y')
        m = time.strftime('%m')
        d = time.strftime('%d')
        now=Y+'-'+m+'-'+d
        if 创建日期[0:10] !=now:
            raise AssertionError(f"列表显示项目时，项目的创建时间显示有误，基准为：{now}，页面为：{创建日期}")
        filenum = self.driver.getelement(项目管理对象库.列表内容.format("项目显示1", "6")).text
        文件数量 = filenum.replace(' ', '')
        if 文件数量 != "0":
            raise AssertionError(f"列表显示项目时，项目的文件数量显示有误，基准为：0，页面为：{文件数量}")
        station = self.driver.getelement(项目管理对象库.列表内容.format("项目显示1", "7")).text
        状态 = station.replace(' ', '')
        if 状态 != "进行中":
            raise AssertionError(f"列表显示项目时，项目的状态信息显示有误，基准为：工作中，页面为：{状态}")

    def 项目过滤显示(self):
        pass

    def 创建空白项目(self):
        self.进入到操作位置.进入项目管理页()
        if not self.wait(项目管理对象库.项目卡片.format("创建空白项目"), 3):
            self.项目管理页面.创建空白项目(项目名称="创建空白项目")
        self.项目管理页面.删除项目(项目名称="创建空白项目1")
        self.click(项目管理对象库.创建新项目)
        #点击创建新项目卡片，跳转到创建项目页面
        if not self.wait(创建项目页面.页面名称,3):
            raise AssertionError("点击新建项目，未跳转到新建项目页面")
        self.click(创建项目页面.创建空白项目)
        self.wait(对话框对象库.弹框标题.format("项目名称"),3)
        #对项目名称进行空值校验、超长校验、重名校验
        self.clear(公共元素对象库.输入框.format("项目名称"))
        self.click(创建项目页面.提交按钮)
        if not self.wait(公共元素对象库.输入框错误信息提示.format("请输入项目名称"),3):
            raise AssertionError("创建项目时项目名称为空时，没有项目名称为空的提示")
        self.clear(公共元素对象库.输入框.format("项目名称"))
        self.send_keys(公共元素对象库.输入框.format("项目名称"), "创建空白项目")
        self.click(创建项目页面.提交按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format('项目名已存在'), 3):
            raise AssertionError("创建项目时项目名称重名时，系统未给出提示信息")
        self.clear(公共元素对象库.输入框.format("项目名称"))
        self.send_keys(公共元素对象库.输入框.format("项目名称"),"创建空白项目1")
        self.click(创建项目页面.提交按钮)
        self.default_content()
        if not self.wait(项目设置页面.项目成员tab页,3):
            raise AssertionError("创建项目后没有自动跳转到项目设置页面")
        self.进入到操作位置.进入项目管理页()
        if not self.wait(项目管理对象库.项目卡片.format("创建空白项目1"),3):
            raise AssertionError("项目创建成功后，在项目管理页面未查看到新创建的项目的卡片")

    def 根据模板创建项目(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="模板创建项目")
        #点击使用模板按钮，弹出项目名称弹窗
        self.click(项目管理对象库.创建新项目)
        self.click(创建项目页面.使用.format("根据模板创建项目"))
        self.wait(对话框对象库.弹框标题.format("项目名称"), 3)
        # 对项目名称进行空值校验、超长校验、重名校验
        self.clear(公共元素对象库.输入框.format("项目名称"))
        self.click(创建项目页面.提交按钮)
        if not self.wait(公共元素对象库.输入框错误信息提示.format("请输入项目名称"), 3):
            raise AssertionError("创建项目时项目名称为空时，没有项目名称为空的提示")
        # self.send_keys(公共元素对象库.输入框.format("项目名称"),
        #                "01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567891")
        # self.click(创建项目页面.提交按钮)
        # if not self.wait(公共元素对象库.系统提示信息弹框.format('操作失败'), 3):
        #     raise AssertionError("创建项目时项目名称超长，系统未给出提示信息")
        self.clear(公共元素对象库.输入框.format("项目名称"))
        self.send_keys(公共元素对象库.输入框.format("项目名称"), "查看项目动态")
        self.click(创建项目页面.提交按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format('项目名已存在'), 3):
            raise AssertionError("创建项目时项目名称重名时，系统未给出提示信息")
        #输入名称，点击关闭弹窗，查看项目是否被创建
        self.clear(公共元素对象库.输入框.format("项目名称"))
        self.send_keys(公共元素对象库.输入框.format("项目名称"), "根据模板创建项目")
        self.click(对话框对象库.关闭弹框.format("项目名称"))
        self.进入到操作位置.进入项目管理页()
        if self.wait(项目管理对象库.项目卡片.format("根据模板创建项目"), 3):
            raise AssertionError("使用模板创建项目时，点击关闭创建弹窗，项目仍然被创建")
        #输入有效名称，点击确定，系统提示创建成功
        self.click(项目管理对象库.创建新项目)
        self.click(创建项目页面.使用.format("根据模板创建项目"))
        self.wait(对话框对象库.弹框标题.format("项目名称"), 3)
        self.send_keys(公共元素对象库.输入框.format("项目名称"), "根据模板创建项目")
        self.click(创建项目页面.提交按钮)
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"))
        self.default_content()
        self.进入到操作位置.进入项目管理页()
        if not self.wait(项目管理对象库.项目卡片.format("根据模板创建项目"), 3):
            raise AssertionError("项目创建成功后，在项目管理页面未查看到新创建的项目的卡片")

    def 存为模板(self):
        self.项目管理页面.删除项目模板(模板名称='保存模板1')
        self.项目管理页面.删除项目模板(模板名称='保存模板2')
        self.进入到操作位置.进入项目管理页()
        self.click(项目管理对象库.更多操作按钮.format("查看项目动态"))
        self.click(项目管理对象库.更多操作选项.format("存为模板"))
        self.wait(对话框对象库.弹框标题.format("存为模板"), 3)
        #对模板名称进行空值、重名、超长校验
        #空值
        self.click(对话框对象库.对话框按钮.format("存为模板", "确定"))
        if not self.wait(公共元素对象库.输入框错误信息提示.format("请输项目模板名称"), 3):
            raise AssertionError("保存项目模板时，项目模板名称为空时没有提示信息")
        #重名
        self.send_keys(公共元素对象库.输入框.format("模板名称"),'根据模板创建项目')
        self.click(对话框对象库.对话框按钮.format("存为模板", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("存在同名项目模板！"),3):
            raise AssertionError("保存模板时存在同名模板，点击保存，没有出现存在同名模板提示信息")
        self.clear(公共元素对象库.输入框.format("模板名称"))
        self.send_keys(公共元素对象库.输入框.format("模板名称"), "保存模板1")
        self.clear(项目管理对象库.保留层级)
        self.send_keys(项目管理对象库.保留层级,"2")
        self.click(对话框对象库.对话框按钮.format("存为模板", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 3)
        self.click(项目管理对象库.创建新项目)
        if not self.wait(创建项目页面.模板卡片.format("保存模板1"),3):
            raise AssertionError("点击保存模板，模板未被成功保存")
        self.click(创建项目页面.预览.format("保存模板1"))
        self.wait(对话框对象库.弹框标题.format("模板预览"),3)
        #不勾选保留项目文件，保存模板，查看保存的模板的项目结构tab页
        if not self.wait(创建项目页面.节点展开按钮.format("保存模板1"),3):
            raise AssertionError("保存的项目模板的项目结构未保存")
        self.click(创建项目页面.节点展开按钮.format("保存模板1"))
        if not self.wait(创建项目页面.节点展开按钮.format("一级目录"),3):
            raise AssertionError("保存的项目模板的项目结构未保存")
        self.click(创建项目页面.节点展开按钮.format("一级目录"))
        if not self.wait(创建项目页面.节点名称.format("二级目录"),3):
            raise AssertionError("保存的项目模板的项目结构未保存")
        #不勾选保留团队成员，保存模板，查看保存的模板的项目成员tab页
        self.click(创建项目页面.模板tab页.format("团队成员"))
        if not self.wait('//span[text()="暂无数据"]',3):
            raise AssertionError("保存模板时未选择保存团队成员，但团队成员实际被保存")
        self.click(对话框对象库.关闭弹框.format("模板预览"))
        self.进入到操作位置.进入项目管理页()
        self.click(项目管理对象库.更多操作按钮.format("查看项目动态"))
        self.click(项目管理对象库.更多操作选项.format("存为模板"))
        self.wait(对话框对象库.弹框标题.format("存为模板"), 3)
        self.send_keys(公共元素对象库.输入框.format("模板名称"), "保存模板2")
        self.click(公共元素对象库.单选按钮.format("保留团队成员"))
        self.click(公共元素对象库.单选按钮.format("保留项目文件"))
        self.click(对话框对象库.对话框按钮.format("存为模板", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 3)
        self.click(项目管理对象库.创建新项目)
        if not self.wait(创建项目页面.模板卡片.format("保存模板2"), 3):
            raise AssertionError("点击保存模板，模板未被成功保存")
        self.click(创建项目页面.预览.format("保存模板2"))
        self.wait(对话框对象库.弹框标题.format("模板预览"), 3)
        #勾选保留项目文件，保存模板，查看保存的模板的项目结构tab页
        if not self.wait(创建项目页面.节点展开按钮.format("保存模板2"), 3):
            raise AssertionError("保存的项目模板的项目结构未保存")
        self.click(创建项目页面.节点展开按钮.format("保存模板2"))
        if not self.wait(创建项目页面.节点展开按钮.format("一级目录"), 3):
            raise AssertionError("保存的项目模板的项目结构未保存")
        self.click(创建项目页面.节点展开按钮.format("一级目录"))
        if not self.wait(创建项目页面.节点名称.format("二级目录"), 3):
            raise AssertionError("保存的项目模板的项目结构未保存")
        #勾选保留团队成员，保存模板，查看保存的模板的项目成员tab页
        self.click(创建项目页面.模板tab页.format("团队成员"))
        if not self.wait(创建项目页面.模板团队成员.format("18942178870","PROJECT MANAGER"),3) or not \
               self.wait(创建项目页面.模板团队成员.format("17789371421","PROJECT MANAGER"),3):
            raise AssertionError("保存模板时勾选保存项目成员，预览模板时项目成员没有被保存")

    def 项目模板管理(self):
        self.项目管理页面.删除项目模板(模板名称='保存模板3')
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.存为模板(项目名称='查看项目动态',模板名称='保存模板3')
        self.click(项目管理对象库.创建新项目)
        #点击删除模板按钮，弹出删除确认对话框
        self.click(创建项目页面.删除.format("保存模板3"))
        if not self.wait(对话框对象库.对话框标题.format("提示"),3):
            raise AssertionError("点击删除项目模板，未出现删除提示信息")
        #点击关闭删除确认对话框，查看项目模板是否被删除
        self.click(对话框对象库.关闭对话框.format("提示"))
        if not self.wait(创建项目页面.模板卡片.format("保存模板3"), 3):
            raise AssertionError("删除项目模板时，点击关闭删除提示对话框后，项目模板仍然被删除")
        #删除确认对话框点击取消按钮，查看项目模板是否别删除
        self.click(创建项目页面.删除.format("保存模板3"))
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示","取消"))
        if not self.wait(创建项目页面.模板卡片.format("保存模板3"), 3):
            raise AssertionError("删除项目模板时，点击取消删除提示对话框后，项目模板仍然被删除")
        #删除确认对话框点击确定按钮，查看项目模板是否被删除
        self.click(创建项目页面.删除.format("保存模板3"))
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if self.wait(创建项目页面.模板卡片.format("保存模板3"), 3):
            raise AssertionError("删除项目模板时，点击确定删除后，项目模板未被删除")

    def 查看项目信息(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="项目信息")
        self.项目管理页面.创建空白项目(项目名称="项目信息")
        self.项目管理页面.查看项目详情(项目名称="项目信息")
        self.default_content()
        if not self.wait(项目管理对象库.项目详情信息.format("项目名称", "项目信息"), 3):
            raise AssertionError("项目详情中项目名称未被显示或显示错误")
        if not self.wait(项目管理对象库.项目详情信息.format("创建人", "18942178870"), 3):
            raise AssertionError("项目详情中创建人未被显示或显示错误")
        Y = time.strftime('%Y')
        m = time.strftime('%m')
        d = time.strftime('%d')
        now = Y + '-' + m + '-' + d
        if not self.wait(项目管理对象库.项目详情信息.format("创建日期", now), 3):
            raise AssertionError("项目详情中创建时间未被显示或者显示有误")
        if not self.wait(项目管理对象库.项目详情信息.format("团队人数", "1"), 3):
            raise AssertionError("项目详情中团队人数未被显示或者显示有误")
        if not self.wait(项目管理对象库.项目详情信息.format("文件数量", "0"), 3):
            raise AssertionError("项目详情中文件数量未被显示或者显示有误")
        if not self.wait(项目管理对象库.项目详情信息.format("项目状态", "进行中"), 3):
            raise AssertionError("项目详情中项目状态未被显示或者显示有误")
        if not self.wait(项目管理对象库.项目详情信息.format("备注", ""), 3):
            raise AssertionError("项目详情中项目备注未被显示或者显示有误")

    def 邀请项目成员(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="邀请成员项目")
        self.项目管理页面.创建空白项目(项目名称="邀请成员项目")
        #点击项目成员按钮，悬浮显示项目成员用户名列表，默认显示项目创建者
        self.click(项目管理对象库.项目成员按钮.format("邀请成员项目"))
        self.default_content()
        if not self.wait(项目管理对象库.移除项目成员.format("18942178870"), 3):
            raise AssertionError("点击查看项目成员，未查看到默认的项目创建者")
        # 点击项目成员按钮，在悬浮页点击添加成员按钮，弹出项目协作弹窗
        self.click(项目管理对象库.添加项目成员)
        if not self.wait(对话框对象库.弹框标题.format("项目协作"), 3):
            raise AssertionError("点击添加项目成员，项目协作弹框未出现")
        #角色有ENTERPRISE MANAGER、PROJECT MANAGER、PROJECT ASSISTANT、DOCUMENT MANAGER、DOCUMENT EDITOR、DOCUMENT CONSUMER、DOCUMENT VIEWER、GUEST、INDIVIDUAL ADMINISTRATOR
        基准数据=["ENTERPRISE MANAGER","PROJECT MANAGER","PROJECT ASSISTANT","DOCUMENT MANAGER","DOCUMENT EDITOR","DOCUMENT CONSUMER","DOCUMENT VIEWER","GUEST","INDIVIDUAL ADMINISTRATOR"]
        self.click(公共元素对象库.列表框.format("角色"))
        elements=self.driver.getelements('//ul/li[contains(@class,"dropdown__item")]/span')
        for element in elements:
            if element.text not in 基准数据 or len(基准数据)!=9:
                raise AssertionError(f"{element.text}不在角色列表中，或者页面角色列表长度为{len(elements)},基准长度为9")
        self.公共操作.滚动选择列表框选项(选项名称='DOCUMENT CONSUMER')
        self.click(对话框对象库.弹框按钮.format("项目协作", "复制链接"))
        self.click(对话框对象库.关闭弹框.format("项目协作"))
        链接 = self.公共操作.获取剪切板内容()
        self.登录页面.退出登录()
        # self.登录页面.短信快捷登录(手机号='18942178871')
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        # 新开标签页
        self.driver.driver.execute_script("window.open('');")
        self.switch_to_new_window()
        self.driver.driver.get(链接)
        time.sleep(3)
        # 打开链接，可以查看到配置的信息，点击加入，项目成员可以看到加入的项目
        self.click(对话框对象库.对话框按钮2.format("邀请你参加“邀请成员项目”", "加入"))
        if not self.wait(项目对象库.目录节点.format("邀请成员项目"), 3):
            raise AssertionError("成员加入项目后，没有跳转到项目内容页面")
        self.进入到操作位置.进入项目管理页()
        # 点击项目成员按钮，悬浮显示项目成员用户名列表
        self.click(项目管理对象库.项目成员按钮.format("邀请成员项目"))
        if not self.wait(项目管理对象库.项目成员名称.format("18942178871"),3):
            raise AssertionError("点击项目成员按钮，未查看到当前项目多有的项目成员")

    def 移除项目成员(self):
        pass

    def 项目标签和节点管理(self):
        pass

    def 删除项目(self):
        self.进入到操作位置.进入项目管理页()
        # 创建项目
        if not self.wait(项目管理对象库.项目卡片.format("删除项目1"), 3):
            self.项目管理页面.创建空白项目(项目名称="删除项目1")
        self.click(项目管理对象库.更多操作按钮.format("删除项目1"))
        self.click(项目管理对象库.更多操作选项.format("删除项目"))
        self.default_content()
        if not self.wait(对话框对象库.对话框标题.format("提示"), 3):
            raise AssertionError("点击删除项目，未查看到删除确认的对话框")
        #点击项目操作按钮，点击删除项目，弹出删除确认对话框，点击取消删除
        self.click(对话框对象库.对话框按钮.format("提示", "取消"))
        self.wait(公共元素对象库.系统提示信息弹框.format("已取消删除"), 3)
        if not self.wait(项目管理对象库.项目卡片.format("删除项目1"), 3):
            raise AssertionError("删除项目点击取消后项目管理页面未查看到被删除项目卡片")
        #点击项目操作按钮，点击删除项目，弹出删除确认对话框，点击关闭对话框
        self.click(项目管理对象库.更多操作按钮.format("删除项目1"))
        self.click(项目管理对象库.更多操作选项.format("删除项目"))
        self.default_content()
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.关闭对话框.format("提示"))
        self.wait(公共元素对象库.系统提示信息弹框.format("已取消删除"), 3)
        if not self.wait(项目管理对象库.项目卡片.format("删除项目1"), 3):
            raise AssertionError("删除项目点击关闭删除提示后项目管理页面未查看到被删除项目卡片")
        #点击项目操作按钮，点击删除项目，弹出删除确认对话框，点击确认删除
        self.click(项目管理对象库.更多操作按钮.format("删除项目1"))
        self.click(项目管理对象库.更多操作选项.format("删除项目"))
        self.default_content()
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("删除"), 3)
        if self.wait(项目管理对象库.项目卡片.format("删除项目1"), 3):
            raise AssertionError("删除项目成功后项目管理页面仍然能查看到被删除项目卡片")

    def 查看项目动态(self):
        self.进入到操作位置.进入项目管理页()
        self.click(项目管理对象库.更多操作按钮.format("查看项目动态"))
        #点击项目动态，可以进入项目动态页面
        self.click(项目管理对象库.更多操作选项.format("项目动态"))
        if not self.wait(项目管理对象库.项目动态页.项目动态页标题, 3):
            raise AssertionError("点击项目动态未跳转到项目动态页面")
        #点击右上方项目成员列表框，列表框显示当前项目所有项目成员
        self.click(公共元素对象库.列表框.format("项目动态"))
        if not self.wait(公共元素对象库.列表框选项.format("18942178870"),3) or \
            not self.wait(公共元素对象库.列表框选项.format("17789371421"),3):
            raise AssertionError("点击右上方项目成员列表框，列表框未查看到当前项目所有项目成员")
        #点击右上方项目成员列表框选择不同的项目成员，可以过滤显示相应成员的操作记录
        self.click(公共元素对象库.列表框选项.format("17789371421"))
        if not self.wait(项目管理对象库.项目动态页.操作1.format("18942178870  邀请了 17789371421 加入了"), 5):
            raise AssertionError("项目动态过滤显示时，勾选项目成员，项目动态未过滤出有关该成员的动态")
        elements=self.driver.getelements(项目管理对象库.项目动态页.操作1.format("18942178870"))
        if len(elements)!=1:
            raise AssertionError("项目动态过滤显示时，过滤结果数量出错")
        #对项目进行新建项目、邀请成员、移除成员、创建目录、添加文件、删除文件、检入检出撤销检出文件操作后，可以在项目动态产看到相应的操作记录
        self.click(公共元素对象库.列表框.format("项目动态"))
        if not self.wait(项目管理对象库.项目动态页.操作1.format("18942178870 创建了 项目"),3):
            raise AssertionError("创建项目操作未被记录在项目动态中")
        if not self.wait(项目管理对象库.项目动态页.操作1.format("18942178870 移除了 查看项目动态 团队成员 18942178871"),3):
            raise AssertionError("移除成员操作未被记录在项目动态中")
        if not self.wait(项目管理对象库.项目动态页.操作1.format("18942178870 创建了 目录"), 3):
            raise AssertionError("创建文件目录操作未被记录在项目动态中")
        if not self.wait(项目管理对象库.项目动态页.操作1.format("18942178870 创建了 项目文件"), 3):
            raise AssertionError("上传文件操作未被记录在项目动态中")
        if not self.wait(项目管理对象库.项目动态页.操作1.format("18942178870 删除了 项目文件"), 3):
            raise AssertionError("删除文件操作未被记录在项目动态中")
        if not self.wait(项目管理对象库.项目动态页.操作1.format("18942178870 检出 项目文件"), 3):
            raise AssertionError("检出文件操作未被记录在项目动态中")
        if not self.wait(项目管理对象库.项目动态页.操作1.format("18942178870 撤销检出 项目文件"), 3):
            raise AssertionError("撤销检出文件操作未被记录在项目动态中")
        if not self.wait(项目管理对象库.项目动态页.操作1.format("18942178870 检入 项目文件"), 3):
            raise AssertionError("检入文件操作未被记录在项目动态中")

    def 检查根据模板创建的项目的项目设置(self):
        #项目团队成员将项目保存为项目模板，当该成员没有模板对应的项目生命周期模板、版次模板、属性模板时，使用该项目模板创建项目后，项目的生命周期、版次、属性自动填充未系统默认的选项
        pass

    def 保存项目模板(self):
        self.项目管理页面.删除项目模板(模板名称='保存项目模板')
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="查看模板信息是否保存")
        self.click(项目管理对象库.更多操作按钮.format("查看项目动态"))
        self.click(项目管理对象库.更多操作选项.format("存为模板"))
        self.wait(对话框对象库.弹框标题.format("存为模板"), 3)
        #设置模板的数据后，关闭存为模板弹窗，查看模板是否被保存
        self.send_keys(公共元素对象库.输入框.format("模板名称"), "保存项目模板")
        self.click(对话框对象库.关闭弹框.format("存为模板"))
        self.click(项目管理对象库.创建新项目)
        if self.wait(创建项目页面.模板卡片.format("保存项目模板"), 3):
            raise AssertionError("点击关闭保存模板弹框，模板却被成功保存")
        self.进入到操作位置.进入项目管理页()
        #设置模板的数据后，点击取消按钮，查看模板是否被保存
        self.click(项目管理对象库.更多操作按钮.format("查看项目动态"))
        self.click(项目管理对象库.更多操作选项.format("存为模板"))
        self.wait(对话框对象库.弹框标题.format("存为模板"), 3)
        self.send_keys(公共元素对象库.输入框.format("模板名称"), "保存项目模板")
        self.click(对话框对象库.弹框按钮.format("存为模板","取消"))
        self.click(项目管理对象库.创建新项目)
        if self.wait(创建项目页面.模板卡片.format("保存项目模板"), 3):
            raise AssertionError("点击取消保存模板弹框，模板却被成功保存")
        #设置模板的数据后，点击确定按钮，查看模板是否被保存
        self.进入到操作位置.进入项目管理页()
        self.click(项目管理对象库.更多操作按钮.format("查看项目动态"))
        self.click(项目管理对象库.更多操作选项.format("存为模板"))
        self.wait(对话框对象库.弹框标题.format("存为模板"), 3)
        self.send_keys(公共元素对象库.输入框.format("模板名称"), "保存项目模板")
        self.click(公共元素对象库.单选按钮.format("保留团队成员"))
        self.click(公共元素对象库.单选按钮.format("保留项目文件"))
        self.click(对话框对象库.弹框按钮.format("存为模板", "确定"))
        self.click(项目管理对象库.创建新项目)
        if not self.wait(创建项目页面.模板卡片.format("保存项目模板"), 3):
            raise AssertionError("点击保存模板，模板未被成功保存")
        #使用保留了项目文件的模板创建项目，查看项目结构下的文件是否存在
        self.click(创建项目页面.使用.format("保存项目模板"))
        self.wait(对话框对象库.弹框标题.format("项目名称"))
        self.send_keys(公共元素对象库.输入框.format("项目名称"),"查看模板信息是否保存")
        self.click(创建项目页面.提交按钮)
        self.项目管理页面.点击进入项目(项目名称="查看模板信息是否保存")
        self.项目页面.按路径展开目录(目录路径=['查看模板信息是否保存','一级目录'])
        资源列表=['二级目录','素材2.jpg','检入检出素材.txt']
        for i in 资源列表:
            if not self.wait(项目对象库.列表文件名称.format(i),3):
                raise AssertionError(f"使用保存项目文件的项目模板创建项目后，源项目中{i}文件不存在")
        #使用保留了项目成员的模板创建项目，查看项目成员列表中成员是否存在
        self.进入到操作位置.进入项目管理页()
        self.click(项目管理对象库.项目成员按钮.format("查看模板信息是否保存"))
        if not self.wait(项目管理对象库.移除项目成员.format("18942178870"), 3) or not\
            self.wait(项目管理对象库.移除项目成员.format("17789371421"), 3):
            raise AssertionError("使用保存项目文件的项目模板创建项目后，源项目中的项目成员在新项目中不存在")

    def 进入项目设置(self):
        pass

    def 项目设置页操作(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="收藏项目")
        self.项目管理页面.创建空白项目(项目名称="收藏项目")
        self.click(项目管理对象库.更多操作按钮.format("收藏项目"))
        self.click(项目管理对象库.更多操作选项.format("项目设置"))
        #点击资源行操作的收藏按钮，可以对文件或文件目录收藏成功
        self.click(项目设置页面.收藏按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("成功"),3):
            raise AssertionError("点击收藏按钮，系统未提示收藏成功")
        self.进入到操作位置.进入收藏页()
        if not self.wait(收藏对象库.收藏资源名称.format("收藏项目"),3):
            raise AssertionError("点击收藏按钮，项目收藏页未出现收藏成功的项目")
        #点击资源行操作的收藏按钮，可以对文件或文件目录取消收藏成功
        self.进入到操作位置.进入项目管理页()
        self.click(项目管理对象库.更多操作按钮.format("收藏项目"))
        self.click(项目管理对象库.更多操作选项.format("项目设置"))
        self.click(项目设置页面.收藏按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 3):
            raise AssertionError("点击取消收藏按钮，系统未提示取消收藏成功")
        self.进入到操作位置.进入收藏页()
        if self.wait(收藏对象库.收藏资源名称.format("收藏项目"), 3):
            raise AssertionError("进行取消收藏按钮，项目收藏页仍然出现收藏成功的项目")
        #点击目录按钮，可以进入项目
        self.进入到操作位置.进入项目管理页()
        self.click(项目管理对象库.更多操作按钮.format("收藏项目"))
        self.click(项目管理对象库.更多操作选项.format("项目设置"))
        self.click(项目设置页面.查看项目目录)
        if not self.wait(项目对象库.目录节点.format("收藏项目"),3):
            raise AssertionError("在项目设置按钮后，页面未跳转到项目目录页面")
        #点击删除按钮，弹出删除对话框
        self.进入到操作位置.进入项目管理页()
        self.click(项目管理对象库.更多操作按钮.format("收藏项目"))
        self.click(项目管理对象库.更多操作选项.format("项目设置"))
        self.click(项目设置页面.删除项目)
        if not self.wait(对话框对象库.对话框标题.format("提示"),3):
            raise AssertionError("在项目设置页面点击删除按钮，未出现删除提示对话框")
        #点击确定，删除当前项目，提示删除成功，页面跳转到创建项目页面
        self.click(对话框对象库.对话框按钮.format("提示","确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("成功"),3):
            raise AssertionError("在项目设置页面进行删除操作后，系统未提示删除成功")
        if not self.wait(创建项目页面.页面名称, 3):
            raise AssertionError("删除项目成功后，未跳转到新建项目页面")

    def 项目切换生命周期(self):
        self.进入到操作位置.进入设置页()
        self.进入到操作位置.进入生命周期工作区()
        生命周期lists=[]
        elements=self.driver.getelements("//table//tr/td[2]//span[1]")
        for element in elements:
            生命周期lists.append(element.text)
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="切换生命周期")
        self.项目管理页面.创建空白项目(项目名称="切换生命周期",生命周期名称='切换生命周期')
        self.项目管理页面.点击进入项目(项目名称="切换生命周期")
        self.项目页面.上传单个文件(目录路径=['切换生命周期'], 文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'])
        self.进入到操作位置.进入项目管理页()
        #点击生命周期下拉列表，列表显示所有的生命周期模板，选择对应的生命周期设置
        self.click(项目管理对象库.更多操作按钮.format("切换生命周期"))
        self.click(项目管理对象库.更多操作选项.format("项目设置"))
        self.click(公共元素对象库.列表框.format("生命周期"))
        列表框list=self.driver.getelements('//ul/li[contains(@class,"dropdown__item")]/span')
        for 列表框 in 列表框list:
            if 列表框.text not in 生命周期lists or len(生命周期lists)!=len(列表框list):
                raise AssertionError(f"{列表框.text}不在生命周期列表中")
        #空白项目点击切换生命周期可以直接切换
        self.公共操作.滚动选择列表框选项(选项名称='生命周期')
        self.click(公共元素对象库.列表框.format("生命周期"))
        if not self.wait('//ul/li[contains(@class,"el-select-dropdown__item selected")]/span[text()="生命周期"]', 3):
            raise AssertionError("空白项目点击切换生命周期没有直接切换")
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="切换生命周期")
        #切换生命周期后，在根目录上传文件，查看生命周期是否被切换
        self.项目页面.上传单个文件(目录路径=['切换生命周期'], 文件路径=['TestData', 'FrontData', '项目页', '素材2.jpg'])
        elestat1 = self.driver.getelement(项目对象库.生命周期状态.format('素材2.jpg')).text
        if elestat1 != "11":
            raise AssertionError("切换生命周期后，在根目录上传文件，生命周期没有被切换")
        #对切换生命周期前的根目录文件进行改变状态操作，查看文件是否还在使用切换前的生命周期
        self.项目页面.改变文件状态(文件名='检入检出素材.txt',状态名称='bb')
        elestat2 = self.driver.getelement(项目对象库.生命周期状态.format('检入检出素材.txt')).text
        if elestat2!="bb":
            raise AssertionError("对切换生命周期前的根目录文件进行改变状态操作，文件没有使用切换前的生命周期")

    def 项目切换版次(self):
        self.进入到操作位置.进入设置页()
        self.进入到操作位置.进入版次工作区()
        版次lists = []
        elements = self.driver.getelements("//table//tr/td[2]//span[1]")
        for element in elements:
            版次lists.append(element.text)
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="切换版次")
        self.项目管理页面.创建空白项目(项目名称="切换版次", 版次名称='切换版次')
        #点击版次下拉列表，列表显示所有的版次模板，选择对应的版次
        self.click(项目管理对象库.更多操作按钮.format("切换版次"))
        self.click(项目管理对象库.更多操作选项.format("项目设置"))
        self.click(公共元素对象库.列表框.format("版次"))
        列表框list = self.driver.getelements('//ul/li[contains(@class,"dropdown__item")]/span')
        for 列表框 in 列表框list:
            if 列表框.text not in 版次lists or len(版次lists) != len(列表框list):
                raise AssertionError(f"{列表框.text}不在版次列表中")
        # 空白项目点击切换版次时，可以直接切换
        self.公共操作.滚动选择列表框选项(选项名称='版次')
        self.click(公共元素对象库.列表框.format("版次"))
        if not self.wait('//ul/li[contains(@class,"el-select-dropdown__item selected")]/span[text()="版次"]', 3):
            raise AssertionError("空白项目点击切换生命周期没有直接切换")
        #点击版次列表框切换版次，弹窗修改版次预览弹窗
        self.click(项目设置页面.查看项目目录)
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="切换版次")
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        self.click(项目对象库.目录节点.format("一级目录"))
        self.项目页面.批量上传文件(目录路径=['切换版次', '一级目录'], 文件路径列表=[素材2, 素材3])
        self.进入到操作位置.进入项目管理页()
        self.click(项目管理对象库.更多操作按钮.format("切换版次"))
        self.click(项目管理对象库.更多操作选项.format("项目设置"))
        self.click(公共元素对象库.列表框.format("版次"))
        self.公共操作.滚动选择列表框选项(选项名称='切换版次')
        if not self.wait(对话框对象库.弹框标题.format("修改版次预览"), 3):
            raise AssertionError("如果项目中已经存在文件，点击切换版次时没有弹出修改版次预览弹窗")
        #修改版次预览弹窗列表显示当前与使用版次和变更后对应版次的信息
        if not self.wait('//div[text()="A"]/ancestor::tr/td[last()]/div[text()="E"]',3):
            raise AssertionError("修改版次弹框显示版次变更选项不正确")
        #修改版次预览弹窗中点击关闭修改版次预览，查看版次时候变更
        self.click(对话框对象库.关闭弹框.format("修改版次预览"))
        self.click(公共元素对象库.列表框.format("版次"))
        if self.wait('//ul/li[contains(@class,"el-select-dropdown__item selected")]/span[text()="版次"]', 3):
            raise AssertionError("修改版次预览弹窗中点击关闭修改版次预览，版次发生变更")
        #修改版次预览弹窗中点击取消，查看版次是否变更
        self.公共操作.滚动选择列表框选项(选项名称='切换版次')
        self.wait(对话框对象库.弹框标题.format("修改版次预览"), 3)
        self.click(对话框对象库.弹框按钮.format("修改版次预览","取消"))
        self.click(公共元素对象库.列表框.format("版次"))
        if not self.wait('//ul/li[contains(@class,"el-select-dropdown__item selected")]/span[text()="版次"]', 3):
            raise AssertionError("修改版次预览弹窗中点击取消，版次发生变更")
        #修改版次预览弹窗中点击确定，查看版次是否变更
        self.公共操作.滚动选择列表框选项(选项名称='切换版次')
        self.wait(对话框对象库.弹框标题.format("修改版次预览"), 3)
        self.click(对话框对象库.弹框按钮.format("修改版次预览", "确定"))
        self.click(公共元素对象库.列表框.format("版次"))
        if not self.wait('//ul/li[contains(@class,"el-select-dropdown__item selected")]/span[text()="切换版次"]', 3):
            raise AssertionError("修改版次预览弹窗中点击确定，版次未发生变更")

    def 权限编辑(self):
        self.权限编辑数据准备()
        self.进入到操作位置.进入项目管理页()
        self.click(项目管理对象库.更多操作按钮.format("权限编辑"))
        self.click(项目管理对象库.更多操作选项.format("项目设置"))
        #点击成员tab页，显示当前项目下的所有项目成员
        if not self.wait(项目设置页面.项目成员名称.format('18942178870','PROJECT MANAGER'),3) or not\
            self.wait(项目设置页面.项目成员名称.format('18942178871','PROJECT MANAGER'),3):
            raise AssertionError("项目设置中，项目成员tab页下项目成员信息显示不正确")
        #点击成员列表中的权限编辑按钮，出现权限编辑弹框
        self.click(项目设置页面.权限编辑按钮.format('18942178871'))
        if not self.wait(对话框对象库.弹框标题.format("编辑权限"),3):
            raise AssertionError("点击权限编辑按钮，未弹出权限编辑弹框")
        #权限编辑弹窗下，左侧显示当前项目的项目文件目录结构
        基准数据=['权限编辑', '一级目录','二级目录','三级目录']
        j=0
        for i in 基准数据[:-1]:
            if self.wait(项目设置页面.节点展开按钮.format(i),3):
                self.click(项目设置页面.节点展开按钮.format(i))
            if not self.wait(项目设置页面.子节点.format(基准数据[j],基准数据[j+1]),3):
                raise AssertionError(f"在权限编辑弹框，未查看到文件目录{基准数据[j]}和它的子目录{基准数据[j+1]}")
            j+=1
        self.click(对话框对象库.关闭弹框.format("编辑权限"))
        #编辑权限时，只对上级目录进行权限操作时，下级目录自动继承上级目录的权限操作结果
        self.项目设置页面.撤回用户授权(成员名称='18942178871',目录列表=['权限编辑', '一级目录'],权限列表=['目录新增','目录删除'])
        self.click(项目设置页面.权限编辑按钮.format('18942178871'))
        self.项目设置页面.展开并点击最后一项目录(结构目录=['权限编辑', '一级目录','二级目录'])
        if not self.wait(项目设置页面.禁用_权限复选框.format("目录新增"),3) or \
            not self.wait(项目设置页面.禁用_权限复选框.format("目录删除"),3):
            raise AssertionError("对父级节点授权后，子级节点未继承父级节点的授权结果")
        #编辑下级目录权限时，上级目录权限不收影响
        self.click(对话框对象库.关闭弹框.format("编辑权限"))
        self.项目设置页面.撤回用户授权(成员名称='18942178871', 目录列表=['权限编辑', '一级目录','二级目录'], 权限列表=['目录打包', '目录下载'])
        self.click(项目设置页面.权限编辑按钮.format('18942178871'))
        self.项目设置页面.展开并点击最后一项目录(结构目录=['权限编辑', '一级目录'])
        if not self.wait(项目设置页面.已选_权限复选框.format("目录打包"),3) or \
            not self.wait(项目设置页面.已选_权限复选框.format("目录下载"),3):
            raise AssertionError("对子级节点授权后，父级节点的权限被改变")
        #设置权限后，点击关闭权限编辑弹窗，权限没有被保存
        self.click(项目设置页面.已选_权限复选框.format("目录修改"))
        self.click(对话框对象库.关闭弹框.format("编辑权限"))
        self.click(项目设置页面.权限编辑按钮.format('18942178871'))
        self.项目设置页面.展开并点击最后一项目录(结构目录=['权限编辑', '一级目录'])
        if not self.wait(项目设置页面.已选_权限复选框.format("目录修改"),3):
            raise AssertionError("对节点授权后，点击关闭授权弹框，授权结果被保存")

    def 验证所有人提交后可进入下一节点(self):
        self.权限编辑数据准备()
        self.项目管理页面.进入点击项目设置(项目名称='权限编辑',生命周期控制tab页=True)
        self.项目设置页面.添加节点人员(节点名称='11',成员名称='18942178871',所有人提交后可进入下一节点=False)
        #所有人提交后进入下一节点按钮关闭时，该节点下成员只要有一个成员完成提交，生命周期就可以进入下个节点
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="权限编辑")
        self.项目页面.改变文件状态(目录路径=['权限编辑', '一级目录','二级目录'],文件名='素材2.jpg',状态名称='22')
        生命周期状态1=self.driver.getelement(项目对象库.生命周期状态.format('素材2.jpg')).text
        if 生命周期状态1!='22':
            raise AssertionError("所有人提交后进入下一节点按钮关闭时，该节点下成员下有一个成员完成提交，生命周期未进入下个节点")
        #所有人提交后进入下一节点按钮开启时，该节点下一个成员提交后，该文件生命周期状态为中间态
        self.项目管理页面.进入点击项目设置(项目名称='权限编辑', 生命周期控制tab页=True)
        self.项目设置页面.添加节点人员(节点名称='11',所有人提交后可进入下一节点=True)
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="权限编辑")
        self.项目页面.改变文件状态(目录路径=['权限编辑', '一级目录', '二级目录'], 文件名='素材3.jpg', 状态名称='22')
        lines=''
        elems=self.driver.getelements(项目对象库.生命周期状态.format('素材3.jpg'))
        # for elem in elems:
        #     lines=lines+elem.text
        # if lines!='11 -> 22':
        if len(elems)!=2:
            raise AssertionError("开启所有人提交后可进入下一节点后，改变生命周期状态后，生命周期中间态未出现")
        #所有人提交后进入下一节点按钮开启时，该节点下一个成员提交后，其他成员未提交的情况下改变生命周期状态
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]',文件名称='素材3.jpg')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("改变状态"))
        self.click(项目对象库.行操作选项.format('22'))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("生命周期状态已提交过,不可重复提交"),3):
            raise AssertionError("开启所有人提交后可进入下一节点后，用户重复操作，未出现提示信息")
        #所有人提交后进入下一节点按钮开启时，该节点下一个成员提交后。所有人提交后进入下一节点按钮不可被关闭
        self.项目管理页面.进入点击项目设置(项目名称='权限编辑', 生命周期控制tab页=True)
        self.click(项目设置页面.节点下成员.format("11"))
        self.click(项目设置页面.已选_所有人提交后可进入下一节点按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("当前项目中存在文件正处于当前流程节点，不允许操作"),3):
            raise AssertionError("所有人提交后进入下一节点按钮开启时，该节点下一个成员提交后。所有人提交后进入下一节点按钮可以被关闭")
        #所有人提交后进入下一节点按钮开启时，该节点下一个成员提交后，切换生命周期，系统给出对应的提示信息
        self.click(公共元素对象库.列表框.format("生命周期"))
        self.公共操作.滚动选择列表框选项(选项名称='切换生命周期')
        self.wait(对话框对象库.弹框标题.format("修改生命周期预览"), 3)
        self.click(项目设置页面.变更节点列表框.format("11"))
        self.click(公共元素对象库.列表框选项.format("aa"))
        self.click(项目设置页面.变更节点列表框.format("22"))
        self.click(公共元素对象库.列表框选项.format("aa"))
        self.click(项目设置页面.变更节点列表框.format("33"))
        self.click(公共元素对象库.列表框选项.format("aa"))
        self.click(对话框对象库.弹框按钮.format("修改生命周期预览", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("当前项目存在正在进行的生命周期流程节点，不允许变更生命周期模板"),3):
            raise AssertionError("所有人提交后进入下一节点按钮开启时，该节点下一个成员提交后，切换生命周期，系统没有给出对应的提示信息")
        #所有人提交后进入下一节点按钮开启时，该节点下所有成员都提交后才能进入下个节点
        self.click(对话框对象库.关闭弹框.format("修改生命周期预览"))
        self.登录页面.退出登录()
        # self.登录页面.短信快捷登录(手机号='18942178871')
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="权限编辑")
        self.项目页面.改变文件状态(目录路径=['权限编辑', '一级目录', '二级目录'], 文件名='素材3.jpg', 状态名称='22')
        生命周期状态1 = self.driver.getelement(项目对象库.生命周期状态.format('素材3.jpg')).text
        if 生命周期状态1 != '22':
            raise AssertionError("所有人提交后进入下一节点按钮开启时，该节点下所有成员都提交后生命周期没有进入下个节点")

    def 清理项目版本(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="清理项目版本")
        self.项目管理页面.创建空白项目(项目名称="清理项目版本",生命周期名称='系统默认生命周期')
        self.项目管理页面.点击进入项目(项目名称="清理项目版本")
        素材1 = ['TestData', 'FrontData', '项目页', '素材1.png']
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        素材4 = ['TestData', 'FrontData', '项目页', '素材4.png']
        素材5 = ['TestData', 'FrontData', '项目页', '素材5.png']

        self.项目页面.批量上传文件(目录路径=['清理项目版本'], 文件路径列表=[素材1,素材2, 素材3,素材4,素材5])
        for filename in ['素材2.jpg','素材3.jpg','素材4.png','素材5.png']:
            self.项目页面.附加文件(目录路径=['清理项目版本'],文件名称="素材1.png",附加文件路径列表=[['清理项目版本',filename]])
        self.进入到操作位置.进入项目管理页()
        #点击项目更多操作，点击清理版本，弹出清理版本弹窗
        self.click(项目管理对象库.更多操作按钮.format("清理项目版本"))
        self.click(项目管理对象库.更多操作选项.format("清除项目版本"))
        self.default_content()
        if not self.wait(对话框对象库.弹框标题.format("清除项目版本"),3):
            raise AssertionError("点击项目的清理项目版本操作按钮，未查看到清理项目版本弹窗")
        #设置保留版本数，关闭弹窗，版本没有被清理
        self.click(对话框对象库.关闭弹框.format("清除项目版本"))
        self.项目管理页面.点击进入项目(项目名称="清理项目版本")
        self.click(项目对象库.列表文件名称.format("素材1.png"))
        if not self.wait(项目对象库.文件版本.format("4"),3):
            raise AssertionError("设置保留版本数为1，关闭清理项目版本弹窗，文件版本还是被清理")
        self.进入到操作位置.进入项目管理页()
        #设置保留版本数，点击提交，符合要求的版本被清理，设置保留版本数为1时，只保留最新版本
        self.click(项目管理对象库.更多操作按钮.format("清理项目版本"))
        self.click(项目管理对象库.更多操作选项.format("清除项目版本"))
        self.default_content()
        self.click(公共元素对象库.增加版本数)
        self.click(对话框对象库.弹框按钮.format("清除项目版本","提交"))
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"))
        self.项目管理页面.点击进入项目(项目名称="清理项目版本")
        self.click(项目对象库.列表文件名称.format("素材1.png"))
        if not self.wait(项目对象库.文件版本.format("4"), 3):
            raise AssertionError("设置保留版本数为2，但是倒数第二个版本被清理")
        if self.wait(项目对象库.文件版本.format("3"), 3):
            raise AssertionError("设置保留版本数为2，但是倒数第三个版本未被清理")

    def 项目归档(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="项目归档")
        self.项目管理页面.创建空白项目(项目名称="项目归档", 生命周期名称='系统默认生命周期')
        self.项目管理页面.点击进入项目(项目名称="项目归档")
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="项目归档")
        素材1 = ['TestData', 'FrontData', '项目页', '素材1.png']
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        self.项目页面.批量上传文件(目录路径=['项目归档', '一级目录'], 文件路径列表=[素材1, 素材2, 素材3])
        # 当项目下项目文件的生命周期状态不是生命周期模板的最后一个节点时，项目节点不能设置为已归档
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.设置项目节点(项目名称='项目归档',状态='已归档')
        if not self.wait(公共元素对象库.系统提示信息弹框.format('项目文件尚在处理中,不可归档'),3):
            raise AssertionError('项目文件的生命周期没有处于生命周期模板的最后一个节点，但是项目却可以设置为已归档')
        self.项目管理页面.点击进入项目(项目名称="项目归档")
        self.项目页面.按路径展开目录(目录路径=['项目归档', '一级目录'])
        self.项目页面.改变文件状态(文件名='素材1.png',状态名称='Release')
        self.项目页面.改变文件状态(文件名='素材2.jpg', 状态名称='Release')
        self.项目页面.改变文件状态(文件名='素材3.jpg', 状态名称='Release')
        #当项目下存在检出文件时，项目节点不能设置为已归档
        self.项目页面.检出资源(资源名称='素材1.png')
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.设置项目节点(项目名称='项目归档', 状态='已归档')
        if not self.wait(公共元素对象库.系统提示信息弹框.format('项目文件尚在处理中,不可归档'), 3):
            raise AssertionError('项目中存在文件处于检出状态，但是项目却可以设置为已归档')
        #点击项目操作按钮，点击项目节点，可以选择项目状态
        self.项目管理页面.点击进入项目(项目名称="项目归档")
        self.项目页面.按路径展开目录(目录路径=['项目归档', '一级目录'])
        self.项目页面.文件撤销检出(资源名称='素材1.png')
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.设置项目节点(项目名称='项目归档', 状态='已归档')
        if self.wait(公共元素对象库.系统提示信息弹框.format('项目文件尚在处理中,不可归档'), 3):
            raise AssertionError('项目进行归档操作失败')
        #项目归档后，项目详情中的项目状态为已归档
        self.项目管理页面.查看项目详情(项目名称='项目归档')
        if not self.wait('//div/span[text()="项目状态:"]/following-sibling::span[text()="已归档"]', 3):
            raise AssertionError("项目归档后，查看项目详情，没有查看到项目状态为已归档")

    def 存为模板2(self):
        self.项目管理页面.删除项目模板(模板名称='保存模板3')
        self.进入到操作位置.进入项目管理页()
        self.click(项目管理对象库.更多操作按钮.format("模板保存文件"))
        self.click(项目管理对象库.更多操作选项.format("存为模板"))
        self.wait(对话框对象库.弹框标题.format("存为模板"), 3)
        #在存为模板界面点击项目目录节点，右侧文件列表显示该文件目录下的所有文件
        self.项目管理页面.展开并点击最后一项目录(结构目录=['模板保存文件'])
        pass

    def 项目生命周期模板设置新增(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="配置生命周期")
        self.项目管理页面.创建空白项目(项目名称="配置生命周期", 生命周期名称='系统默认生命周期')
        self.click(项目管理对象库.更多操作按钮.format("配置生命周期"))
        self.click(项目管理对象库.更多操作选项.format("项目设置"))
        self.click(项目设置页面.项目生命周期模板设置)
        self.项目设置页面.批量删除生命周期(生命周期列表=['切换生命周期', '生命周期'])
        #点击新增按钮，弹出新增项目生命周期模板弹窗
        self.click(项目设置页面.新增生命周期)
        if not self.wait(对话框对象库.弹框标题.format("新增项目生命周期模板"),3):
            raise AssertionError("点击生命周期新增按钮，未查看到新增生命周期弹框")
        #弹窗中显示未进行新增的生命周期模板
        if not self.wait(项目设置页面.未配置生命周期名称.format("生命周期"),3):
            raise AssertionError("项目生命周期模板设置新增生命周期时，未查看到未新增的生命周期")
        #新增生命周期模板时，勾选生命周期模板，点击保存，提示操作成功后，可以在列表中查看到新增的生命周期
        self.click(项目设置页面.未配置生命周期复选框.format("生命周期"))
        self.click(对话框对象库.弹框按钮.format("新增项目生命周期模板","保存"))
        if not self.wait(项目设置页面.生命周期名称.format("生命周期"),3):
            raise AssertionError("保存生命周期成功后，未在生命周期列表查看到新增的生命周期")
        #新增生命周期模板时，勾选生命周期模板，点击取消，查看是否添加成功
        self.click(项目设置页面.新增生命周期)
        self.wait(对话框对象库.弹框标题.format("新增项目生命周期模板"), 3)
        self.click(项目设置页面.未配置生命周期复选框.format("切换生命周期"))
        self.click(对话框对象库.弹框按钮.format("新增项目生命周期模板", "取消"))
        if self.wait(项目设置页面.生命周期名称.format("切换生命周期"),3):
            raise AssertionError("新增生命周期取消后，在生命周期列表查看到取消新增的生命周期")
        #新增生命周期模板时，勾选生命周期模板，关闭窗口，查看是否添加成功
        self.click(项目设置页面.新增生命周期)
        self.wait(对话框对象库.弹框标题.format("新增项目生命周期模板"), 3)
        self.click(项目设置页面.未配置生命周期复选框.format("切换生命周期"))
        self.click(对话框对象库.关闭弹框.format("新增项目生命周期模板"))
        if self.wait(项目设置页面.生命周期名称.format("切换生命周期"), 3):
            raise AssertionError("新增生命周期取消后，在生命周期列表查看到取消新增的生命周期")

    def 项目生命周期模板设置删除(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="配置生命周期")
        self.项目管理页面.创建空白项目(项目名称="配置生命周期", 生命周期名称='系统默认生命周期')
        self.click(项目管理对象库.更多操作按钮.format("配置生命周期"))
        self.click(项目管理对象库.更多操作选项.format("项目设置"))
        self.click(项目设置页面.项目生命周期模板设置)
        #勾选生命周期，点击删除，等待提示信息，查看被删除的生命周期模板是够存在
        self.click(项目设置页面.生命周期复选框.format("切换生命周期"))
        self.click(项目设置页面.删除生命周期)
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"),3)
        if self.wait(项目设置页面.生命周期名称.format("切换生命周期"),3):
            raise AssertionError("删除生命周期后，被删除的生命周期仍然可以被查看到")
        #不勾选生命周期，点击删除，查看是否出现提示信息
        self.click(项目设置页面.删除生命周期)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("请选择需要删除的数据"),3):
            raise AssertionError("不选择任何生命周期，点击删除，未出现提示信息")
        #勾选被使用的生命周期，点击删除，查看是否出现提示信息
        self.click(项目设置页面.生命周期复选框.format("系统默认生命周期"))
        self.click(项目设置页面.删除生命周期)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("不能删除根目录使用的生命周期模板"), 3):
            raise AssertionError("删除已经被使用的生命周期，未出现提示信息")


class 项目工作区(page):

    def __init__(self,Secdriver = None):
        page.__init__(self,secdriver=Secdriver)
        self.进入到操作位置 = 进入到操作位置(Secdriver=Secdriver)
        self.滑块验证=滑块验证(Secdriver=Secdriver)
        self.登录页面 = 登录页面(Secdriver=Secdriver)
        self.用户信息页面 = 用户信息页面(Secdriver=Secdriver)
        self.项目管理页面 = 项目管理页面(Secdriver=Secdriver)
        self.公共操作 = 公共操作(Secdriver=Secdriver)
        self.项目页面 = 项目页面(Secdriver=Secdriver)
        self.生命周期管理页面 = 生命周期管理页面(Secdriver=Secdriver)
        self.logger = Logger(logger='logger').getlog()

    def 数据准备(self):
        # 注册账号1:18942178870 pw:user8870
        # self.用户信息页面.进入账号信息页面()
        # self.用户信息页面.维护用户账号信息(用户名='user8870')
        self.用户信息页面.进入基本信息页面()
        self.用户信息页面.维护用户基本信息(用户昵称="18942178870")
        #准备项目数据
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除所有项目()
        self.进入到操作位置.进入生命周期工作区()
        self.生命周期管理页面.删除所有生命周期()
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.创建空白项目(项目名称="资源树展示")
        self.项目管理页面.点击进入项目(项目名称="资源树展示")
        self.wait(项目对象库.目录节点.format("资源树展示"), 3)
        self.driver.refrsh()
        # 创建文件目录
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="资源树展示")
        self.项目页面.创建文件目录(目录名称="一级目录2", 目录父节点名称="资源树展示")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        self.项目页面.创建文件目录(目录名称="二级目录2", 目录父节点名称="一级目录2")
        # 上传文件
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        self.click(项目对象库.目录节点.format("一级目录"))
        self.项目页面.批量上传文件(目录路径=['资源树展示', '一级目录'], 文件路径列表=[素材2, 素材3])
        self.进入到操作位置.进入项目管理页()
        self.进入到操作位置.进入生命周期工作区()
        self.生命周期管理页面.删除生命周期('生命周期')
        self.生命周期管理页面.删除生命周期('切换生命周期')
        self.生命周期管理页面.进入新增生命周期弹框(生命周期名称='生命周期')
        self.生命周期管理页面.添加生命周期节点(节点名称='11')
        self.生命周期管理页面.添加生命周期节点(节点名称='22')
        self.生命周期管理页面.添加生命周期节点(节点名称='33')
        self.生命周期管理页面.设置升版流程(节点名称='11', 开始节点='11', 结束节点='22')
        self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 10)
        self.生命周期管理页面.进入新增生命周期弹框(生命周期名称='切换生命周期')
        self.生命周期管理页面.添加生命周期节点(节点名称='aa')
        self.生命周期管理页面.添加生命周期节点(节点名称='bb')
        self.生命周期管理页面.设置升版流程(节点名称='aa', 开始节点='aa', 结束节点='bb')
        self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)

    def 权限设置数据准备(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="权限设置")
        self.项目管理页面.创建空白项目(项目名称="权限设置",生命周期名称='生命周期')
        self.项目管理页面.邀请项目成员(项目名称='权限设置', 当前用户手机号='18942178870', 成员手机号='18942178871', 角色='PROJECT MANAGER')
        self.项目管理页面.点击进入项目(项目名称="权限设置")
        self.wait(项目对象库.目录节点.format("权限设置"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="权限设置")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        self.项目页面.创建文件目录(目录名称="三级目录", 目录父节点名称="二级目录")
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        self.click(项目对象库.目录节点.format("一级目录"))
        self.项目页面.批量上传文件(目录路径=['权限设置', '一级目录','二级目录'], 文件路径列表=[素材2, 素材3])

    def 对比两个列表的差异项(self,列表1,列表2):
        len1=len(列表1)
        len2=len(列表2)
        result=[]
        if len1>=len2:
            for i in 列表1:
                if not i in 列表2:
                    result.append(i)
        elif len1<len2:
            for i in 列表2:
                if not i in 列表1:
                    result.append(i)
        return result

    def 获取列表列名(self):
        titles = []
        mxpath = '//div[contains(@class,"-header-wrapper")]//table[@class="vxe-table--header"]//tr/th//span'
        elements = self.driver.getelements(mxpath)
        for element in elements:
            if element.text != "":
                titles.append(element.text)
        return titles

    def 收藏页清理所有收藏(self):
        while(True):
            if self.wait('//tr/td//i[contains(@class,"icon-shoucang shoucang-yellow")]',3):
                self.click('//tr/td//i[contains(@class,"icon-shoucang shoucang-yellow")]')
            else:
                break

######################以下为业务实现方法############################

    def 资源树展示(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="资源树展示")
        self.wait(项目对象库.目录节点.format("资源树展示"), 3)
        self.driver.refrsh()
        # 点击项目名称，进入项目页面，资源树默认全部展开
        if self.wait(项目对象库.节点展开按钮.format("资源树展示"), 3):
            raise AssertionError("点击项目名称，进入项目页面，资源树默认全部展开")
        # 点击展开和收缩各级资源节点，资源节点可以被正常展开和收缩
        self.click(项目对象库.节点展开按钮.format("一级目录2"))
        if not self.wait(项目对象库.目录节点.format("二级目录2"), 3):
            raise AssertionError("节点展开按钮，目录未被正常展开")
        self.click(项目对象库.节点收起按钮.format("一级目录2"))
        if self.wait(项目对象库.子节点.format("一级目录2", "二级目录2"), 3):
            raise AssertionError("点击目录收起按钮，目录未被正常收起")

    def 资源树节点搜索(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="资源树展示")
        self.wait(项目对象库.目录节点.format("资源树展示"), 3)
        self.driver.refrsh()
        #搜索框不输入值，点击搜索，显示全部资源节点
        self.clear(项目对象库.搜索框)
        self.click(项目对象库.搜索按钮)
        if not self.wait(项目对象库.子节点.format("一级目录","二级目录"),3):
            raise AssertionError("资源树搜索框空值搜索，未显示全部节点")
        #搜索框输入指定的目录名称，只显示指定的目录的资源树
        self.clear(项目对象库.搜索框)
        self.send_keys(项目对象库.搜索框,"二级目录2")
        self.click(项目对象库.搜索按钮)
        if not self.wait(项目对象库.子节点.format("一级目录2", "二级目录2"), 3):
            raise AssertionError("资源树搜索框搜索指定节点，资源树未显示指定的节点")
        #搜索框输入模糊名称，显示匹配到的所有的目录的资源树
        self.clear(项目对象库.搜索框)
        self.send_keys(项目对象库.搜索框, "二级目录")
        self.click(项目对象库.搜索按钮)
        if not self.wait(项目对象库.子节点.format("一级目录2", "二级目录2"), 3) or\
                not self.wait(项目对象库.子节点.format("一级目录", "二级目录"), 3):
            raise AssertionError("资源树搜索框模糊搜索节点，资源树未显示匹配到的节点")
        #搜索框输入不存在的目录名称，不显示任何目录的资源树
        self.clear(项目对象库.搜索框)
        self.send_keys(项目对象库.搜索框, "不存在")
        self.click(项目对象库.搜索按钮)
        if self.wait('//div[@role="treeitem"]//span',3):
            raise AssertionError("资源树搜索框搜索不存在的节点，资源树显示了节点")

    def 文件列表显示(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="资源树展示")
        self.wait(项目对象库.目录节点.format("资源树展示"), 3)
        self.driver.refrsh()
        self.click(项目对象库.目录节点.format("一级目录"))
        # #点击资源树任意节点，右侧列表展示该节点下资源的文件名称、状态、版本、创建人、最后检入人、最后检入时间等信息
        # titles = []
        # mxpath = '//div[contains(@class,"el-table--border")]//table[@class="el-table__header"]//tr/th'
        # elements = self.driver.getelements(mxpath)
        # for element in elements:
        #     if element.text != "":
        #         titles.append(element.text)
        # 基准数据 = ['文件名称','作者', '创建时间', '版本', '版次']
        # if titles != 基准数据:
        #     raise AssertionError(f"列表默认显示列错误,基准数据为：{基准数据}，页面数据为：{titles}")
        #点击资源树任意节点，右侧列表显示该节点下的所有资源和子分组
        if not self.wait(项目对象库.列表文件名称.format("二级目录"), 3) or not \
                self.wait(项目对象库.列表文件名称.format("素材2.jpg"), 3)or not \
                self.wait(项目对象库.列表文件名称.format("素材3.jpg"), 3):
            raise AssertionError("点击资源树任意节点，右侧列表未发现该节点下的子分组和文件资源")

    def 列表显示管理(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="列表显示管理")
        self.项目管理页面.创建空白项目(项目名称="列表显示管理")
        self.项目管理页面.点击进入项目(项目名称="列表显示管理")
        self.wait(项目对象库.目录节点.format("列表显示管理"), 30)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="列表显示管理")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        self.click(项目对象库.目录节点.format("一级目录"))
        列名1=self.获取列表列名()
        #点击列表展示管理按钮，弹出列表展示管理弹窗
        self.click(项目对象库.列显示管理)
        if not self.wait(项目对象库.列显示弹窗名称,3):
            raise AssertionError("点击列表显示管理按钮，未弹出设置显示内容的弹窗")
        #勾选对应选项，文件列表可以实时预览
        self.click(项目对象库.列显示单选钮.format("检出人"))
        self.click(项目对象库.列显示管理)
        列名2 = self.获取列表列名()
        差异1=self.对比两个列表的差异项(列表1=列名1,列表2=列名2)
        if len(差异1)!=1 and 差异1[0]!="检出人":
            raise AssertionError("设置显示内容弹窗设置后，资源列表的列未发生变化")
        #勾选对应选项，不点击保存，退出项目后再进入项目，查看是否有变化
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="列表显示管理")
        self.wait(项目对象库.目录节点.format("列表显示管理"), 3)
        self.driver.refrsh()
        self.click(项目对象库.目录节点.format("一级目录"))
        列名3 = self.获取列表列名()
        if 列名1!=列名3 or 列名2==列名3:
            raise AssertionError("设置显示内容弹窗设置后未点击保存，退出重新进入项目后发现设置的显示内容已经被保存")
        #选择对应的选项，点击保存，退出项目后再点击进入项目查看列表是否变化
        self.click(项目对象库.列显示管理)
        self.wait(项目对象库.列显示弹窗名称, 3)
        self.click(项目对象库.列显示单选钮.format("检出人"))
        self.click(项目对象库.保存设置按钮)
        self.wait(公共元素对象库.系统提示信息弹框.format("操作成功"),3)
        列名4 = self.获取列表列名()
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="列表显示管理")
        self.wait(项目对象库.目录节点.format("列表显示管理"), 3)
        self.driver.refrsh()
        self.click(项目对象库.目录节点.format("一级目录"))
        列名5 = self.获取列表列名()
        if 列名4!=列名5:
            raise AssertionError("列表设置显示内容设置失败")

    def 创建文件目录(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="创建文件目录")
        self.项目管理页面.创建空白项目(项目名称="创建文件目录")
        self.项目管理页面.点击进入项目(项目名称="创建文件目录")
        self.wait(项目对象库.目录节点.format("创建文件目录"), 3)
        self.driver.refrsh()
        #项目默认勾选根节点
        if not self.wait('//div[@role="treeitem" and contains(@class,"is-current")]//span[contains(@title,"创建文件目录")]',3):
            raise AssertionError("进入项目后未默认选择根节点")
        #点击指定节点，点击新建，弹出新建文件目录对话框，输入合法文件目录名称点击提交，可以正常在该节点下创建文件目录
        self.click(项目对象库.目录节点.format("创建文件目录"))
        self.click(项目对象库.新建目录)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新建文件目录"), 3)
        self.clear(公共元素对象库.输入框.format("文件目录名称"))
        self.send_keys(公共元素对象库.输入框.format("文件目录名称"), "一级目录")
        self.click(对话框对象库.对话框按钮.format("新建文件目录", "提交"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        if not self.wait(项目对象库.子节点.format("创建文件目录","一级目录"),3):
            raise AssertionError("创建文件目录后未查看到创建的目录")
        #点击新建，弹出新建文件目录对话框，输入目录名称，点击关闭对话框，查看目录是否被创建
        self.click(项目对象库.目录节点.format("创建文件目录"))
        self.click(项目对象库.新建目录)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新建文件目录"), 3)
        self.clear(公共元素对象库.输入框.format("文件目录名称"))
        self.send_keys(公共元素对象库.输入框.format("文件目录名称"), "一级目录2")
        self.click(对话框对象库.关闭弹框.format("新建文件目录"))
        if self.wait(项目对象库.子节点.format("创建文件目录", "一级目录2"), 3):
            raise AssertionError("弹出新建文件目录对话框，输入目录名称，点击关闭对话框，但目录被创建")
        #点击新建，弹出新建文件目录对话框，对文件目录名称进行空值、超长、重名校验
        self.click(项目对象库.目录节点.format("创建文件目录"))
        self.click(项目对象库.新建目录)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新建文件目录"), 3)
        self.clear(公共元素对象库.输入框.format("文件目录名称"))
        self.send_keys(公共元素对象库.输入框.format("文件目录名称"), "")
        self.click(对话框对象库.对话框按钮.format("新建文件目录", "提交"))
        if not self.wait(公共元素对象库.输入框错误信息提示.format("请输入目录名称"),3):
            raise AssertionError("创建文件目录时不输入目录名称，点击提交，未出现提示信息")
        # self.clear(公共元素对象库.输入框.format("文件目录名称"))
        # leng='sadgfklasdkjlfgasldjkgfasldjgksadgfklasdkjlfgasldjkgfasldjgksadgfklasdkjlfgasldjkgfasldjgksadgfklasdkjlfgasldjkgfasldjgksadgfklasdkjlfgasldjkgfasldjgk'
        # self.send_keys(公共元素对象库.输入框.format("文件目录名称"),leng)
        # self.click(对话框对象库.对话框按钮.format("新建文件目录", "提交"))
        # if not self.wait(公共元素对象库.系统提示信息弹框.format("操作失败"),3):
        #     raise AssertionError("当文件目录名称超长时，系统未给出提示")
        # self.click(项目对象库.新建目录)
        # self.default_content()
        # self.wait(对话框对象库.弹框标题.format("新建文件目录"), 3)
        # self.clear(公共元素对象库.输入框.format("文件目录名称"))
        self.send_keys(公共元素对象库.输入框.format("文件目录名称"), "一级目录")
        self.click(对话框对象库.对话框按钮.format("新建文件目录", "提交"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("目录名称已存在"), 3):
            raise AssertionError("当文件目录名称重名时，系统未给出提示")

    def 上传单个文件(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="上传文件")
        self.项目管理页面.创建空白项目(项目名称="上传文件")
        self.项目管理页面.点击进入项目(项目名称="上传文件")
        self.wait(项目对象库.目录节点.format("上传文件"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="上传文件")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        self.click(项目对象库.目录节点.format("一级目录"))
        #点击上传按钮，弹窗上传文件对话框
        self.click(项目对象库.上传)
        if not self.wait(对话框对象库.弹框标题.format("上传文件"), 3):
            raise AssertionError("点击上传按钮，未弹出上传文件的弹窗")
        #不选择任何文件，点击上传文件，提示未选择文件
        self.click(项目对象库.上传文件按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("请上传文件"),3):
            raise AssertionError("未选择上传文件，点击上传，系统未作出提示")
        #选择文件，关闭上传弹窗，查看文件是否上传
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=['TestData','FrontData','项目页','素材1.png'])
        self.wait(项目对象库.待上传文件.format("素材1.png"), 5)
        self.click(对话框对象库.关闭弹框.format("上传文件"))
        self.wait(对话框对象库.对话框标题.format("警告"),3)
        self.click(对话框对象库.对话框按钮.format("警告","确定"))
        if self.wait(项目对象库.列表文件名称.format("素材1.png"), 3):
            raise AssertionError("上传文件时，选择待上传文件后关闭上传文件弹窗，文件被上传")
        #点击上传按钮，选择单个文件，点击上传
        self.click(项目对象库.上传)
        self.wait(对话框对象库.弹框标题.format("上传文件"), 3)
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=['TestData', 'FrontData', '项目页', '素材1.png'])
        self.wait(项目对象库.待上传文件.format("素材1.png"), 5)
        self.click(项目对象库.上传文件按钮)
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 300)
        if not self.wait(项目对象库.列表文件名称.format("素材1.png"), 3):
            raise AssertionError("上传文件时，上传文件成功后点击查看文件列表，未查看到被上传的文件")

    def 上传文件管理(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="上传文件")
        self.项目管理页面.创建空白项目(项目名称="上传文件")
        self.项目管理页面.点击进入项目(项目名称="上传文件")
        self.wait(项目对象库.目录节点.format("上传文件"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="上传文件")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        self.click(项目对象库.目录节点.format("一级目录"))
        #选择多个待上传文件，在弹窗中清除部分待上传文件，文件被清除
        self.click(项目对象库.上传)
        self.wait(对话框对象库.弹框标题.format("上传文件"), 3)
        素材1 = ['TestData', 'FrontData', '项目页', '素材1.png']
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        素材4 = ['TestData', 'FrontData', '项目页', '素材4.png']
        素材5 = ['TestData', 'FrontData', '项目页', '素材5.png']
        for 文件路径 in [素材1,素材2,素材3,素材4,素材5]:
            self.click(项目对象库.点击上传按钮)
            self.公共操作.win上传文件(文件路径=文件路径)
            self.wait(项目对象库.待上传文件.format(文件路径[-1]), 5)
        self.move_to_by_pyautogui(项目对象库.待上传文件.format("素材5.png"),y_offset=-3)
        self.click(项目对象库.移除待上传文件.format("素材5.png"))
        self.move_to_by_pyautogui(项目对象库.待上传文件.format("素材4.png"))
        self.click(项目对象库.移除待上传文件.format("素材4.png"))
        if self.wait(项目对象库.列表文件名称.format("素材4.png"), 3) or\
            self.wait(项目对象库.列表文件名称.format("素材5.png"), 3):
            raise AssertionError("移除待上传文件：素材5.png和素材4.png后，仍然在待上传文件列表中能查看到：素材5.png和素材4.png")
        #选择多个待上传文件，在弹窗中清除部分待上传文件，点击上传，查看被清除文件是否被上传
        self.click(项目对象库.上传文件按钮)
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 300)
        if self.wait(项目对象库.列表文件名称.format("素材4.png"),3) or\
                self.wait(项目对象库.列表文件名称.format("素材5.png"),3):
            raise AssertionError("批量上传资源时，被移除的待上传文件页被上传")
        #上传完成后，可以在列表中查看到上传文件的名称
        if not self.wait(项目对象库.列表文件名称.format("素材2.jpg"), 3) or not \
                self.wait(项目对象库.列表文件名称.format("素材3.jpg"), 3) or not \
                self.wait(项目对象库.列表文件名称.format("素材1.png"), 3):
            raise AssertionError("批量上传资源后，在目标目录下未查看到批量上传的资源")

    def 查看文件属性(self):
        pass

    def 预览操作(self):
        pass

    def 检入文件(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="文件检入")
        self.项目管理页面.创建空白项目(项目名称="文件检入")
        self.项目管理页面.点击进入项目(项目名称="文件检入")
        self.wait(项目对象库.目录节点.format("文件检入"), 3)
        self.driver.refrsh()
        # 创建文件目录
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="文件检入")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        self.项目页面.上传单个文件(目录路径=['文件检入', '一级目录'], 文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'])
        #文件未检出，进行检入操作时，提示未检出，不能进行检入
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]', 文件名称='检入检出素材.txt')
        self.click(项目对象库.悬浮列行操作.format(序号))
        if not self.wait(项目对象库.置灰_行操作选项.format("检入"),3):
            raise AssertionError("文件未检出，检入文件按钮可用")
        #检入检出时的相同的未修改的文件，提示文件相同不能检入
        self.项目页面.检出资源(目录路径=['文件检入', '一级目录'], 资源名称='检入检出素材.txt')
        time.sleep(2)
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]', 文件名称='检入检出素材.txt')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("检入"))
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'])
        self.wait(项目对象库.待上传文件.format("检入检出素材.txt"), 5)
        self.click(项目对象库.上传文件按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("检入文件与检出文件相同"), 5):
            raise AssertionError("检入检出时的相同的未修改的文件，系统未出现提示信息")
        #检入和检出时文件名不同的文件，提示文件不同不能检入
        time.sleep(3)
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=['TestData', 'FrontData', '项目页', '头像2.txt'])
        self.wait(项目对象库.待上传文件.format("头像2.txt"), 5)
        self.click(项目对象库.上传文件按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("文件名不一致不可检入"), 5):
            raise AssertionError("检入和检出时文件名不同的文件，未出现提示文件不同不能检入的信息")
        #检出文件后，下载文件后，修改文件再检入文件，文件可以被正常检入
        self.公共操作.修改文件内容(文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'], 内容=str(int(time.time())))
        time.sleep(3)
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'])
        self.wait(项目对象库.待上传文件.format("检入检出素材.txt"), 5)
        self.click(项目对象库.上传文件按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 300):
            raise AssertionError("检出文件后，下载文件后，修改文件再检入文件，文件未被正常检入")
        #检入文件后，文件检出状态自动关闭，文件列表中检出状态被取消
        if self.wait(项目对象库.检出按钮.format("检入检出素材.txt"), 3):
            raise AssertionError("对已检出的文件进行检入操作后，列表仍然有文件检出标志")
        #检出文件后，检入空文件，文件不能被检入
        self.项目页面.检出资源(目录路径=['文件检入', '一级目录'], 资源名称='检入检出素材.txt')
        time.sleep(2)
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]',
                                   文件名称='检入检出素材.txt')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("检入"))
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=['TestData', 'FrontData', '文件上传下载', '检入检出素材.txt'])
        self.wait(项目对象库.待上传文件.format("检入检出素材.txt"), 5)
        self.click(项目对象库.上传文件按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("不能上传空文件"), 5):
            raise AssertionError("检入空文件，系统未出现提示信息")

    def 检出文件(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="检出文件")
        self.项目管理页面.创建空白项目(项目名称="检出文件")
        self.项目管理页面.邀请项目成员(项目名称='检出文件',当前用户手机号='18942178870',成员手机号='18942178871',角色='PROJECT MANAGER')
        self.项目管理页面.点击进入项目(项目名称="检出文件")
        self.wait(项目对象库.目录节点.format("检出文件"), 3)
        self.driver.refrsh()
        # 创建文件目录
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="检出文件")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        self.项目页面.上传单个文件(目录路径=['检出文件', '一级目录'], 文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'])
        #进行检出操作后，文件列表中文件会被标记为检出状态
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]', 文件名称='检入检出素材.txt')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("检出"))
        if not self.wait(项目对象库.检出按钮.format('检入检出素材.txt'), 3):
            raise AssertionError("进行检出操作后，文件列表中文件未被标记为检出状态")
        #文件检出后，检出操作按钮不可见
        time.sleep(2)
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]', 文件名称='检入检出素材.txt')
        self.click(项目对象库.悬浮列行操作.format(序号))
        if self.wait(项目对象库.行操作选项.format("检出"), 3):
            raise AssertionError("进行检出操作后，文件的检出操作按钮仍然可见")
        #文件被检出后，不能进行删除操作
        if not self.wait(项目对象库.置灰_行操作选项.format("删除")):
            raise AssertionError("文件被检出后，该文件不能进行删除操作")
        #除检出人以外的其他项目成员不能对文件进行删除和撤销检出操作
        self.登录页面.退出登录()
        # self.登录页面.短信快捷登录(手机号='18942178871')
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="检出文件")
        self.click(项目对象库.目录节点.format("一级目录"))
        序号=self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]', 文件名称='检入检出素材.txt')
        self.click(项目对象库.悬浮列行操作.format(序号))
        if not self.wait(项目对象库.置灰_行操作选项.format("删除"),3):
            raise AssertionError("被检出的文件可以进行删除操作")
        self.click(项目对象库.行操作选项.format("撤销检出"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("不能撤销检出他人检出的文件"),3):
            raise AssertionError("文件被检出后，项目其他成员进行撤销检出操作时未出现提示信息")
        if not self.wait(项目对象库.检出按钮.format('检入检出素材.txt'), 3):
            raise AssertionError("文件被检出后，项目其他成员进行撤销检出操作时，撤销检出成功")

    def 检出文件目录(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="检出文件目录")
        self.项目管理页面.创建空白项目(项目名称="检出文件目录")
        self.项目管理页面.邀请项目成员(项目名称='检出文件目录', 当前用户手机号='18942178870', 成员手机号='18942178871',角色='PROJECT MANAGER')
        self.项目管理页面.点击进入项目(项目名称="检出文件目录")
        self.wait(项目对象库.目录节点.format("检出文件目录"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="检出文件目录")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        素材1=['TestData', 'FrontData', '项目页', '检入检出素材.txt']
        素材2=['TestData', 'FrontData', '项目页', '头像2.txt']
        self.项目页面.批量上传文件(目录路径=['检出文件目录', '一级目录'], 文件路径列表=[素材1,素材2])
        #文件目录下没有文件，点击检出，系统提示没有要检出的文件
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]', 文件名称='二级目录')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("检出"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("没有可以检出的项目文件"),3):
            raise AssertionError("对空文件目录进行检出操作时，系统没有提示信息")
        if self.wait(对话框对象库.对话框标题.format("提示"),3):
            self.click(对话框对象库.对话框按钮.format("提示","确定"))
        #文件目录下没有已检出的文件，点击检出，可以正常检出
        self.click(项目对象库.目录节点.format("检出文件目录"))
        time.sleep(1)
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]', 文件名称='一级目录')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("检出"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 3):
            raise AssertionError("文件目录下没有已检出的文件，点击检出，没有检出成功的提示信息")
        #对文件目录检出操作后，不能进行删除操作
        self.click(项目对象库.目录节点.format("检出文件目录"))
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]', 文件名称='一级目录')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("删除"))
        self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("文件夹下存在被锁定的文件"), 3):
            raise AssertionError("对文件目录检出操作后，对文件目录进行删除操作，系统未给出不能删除的提示")
        #对文件目录进行检出操作后，再次进行检出操作，系统提示已被检出
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]', 文件名称='一级目录')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("检出"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("存在已被检出的文件，不能执行该操作"), 3):
            raise AssertionError("对文件目录进行检出操作后，再次进行检出操作，系统未给出不能检出的提示信息")
        self.click(项目对象库.目录节点.format("一级目录"))
        time.sleep(1)
        if not self.wait(项目对象库.检出按钮.format('检入检出素材.txt'), 3) or not\
                self.wait(项目对象库.检出按钮.format('头像2.txt'), 3):
            raise AssertionError("文件目录检出成功后，文件目录下的文件没有被检出")
        #文件目录下含有已检出的文件，点击检出，不能检出成功
        self.项目页面.文件撤销检出(目录路径=['检出文件目录', '一级目录'], 资源名称='检入检出素材.txt')
        self.click(项目对象库.目录节点.format("检出文件目录"))
        time.sleep(1)
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]', 文件名称='一级目录')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("检出"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("存在已被检出的文件，不能执行该操作"), 3):
            raise AssertionError("文件目录下含有已检出的文件，点击检出，系统未出现不能检出的提示信息")
        self.click(项目对象库.目录节点.format("一级目录"))
        time.sleep(1)
        if self.wait(项目对象库.检出按钮.format('检入检出素材.txt'), 3) or not\
                self.wait(项目对象库.检出按钮.format('头像2.txt'), 3):
            raise AssertionError("文件目录检出失败后，文件目录下的文件的检出状态发生变化")
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]', 文件名称='检入检出素材.txt')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("检出"))
        if self.wait(对话框对象库.对话框标题.format("提示"),3):
            self.click(对话框对象库.对话框按钮.format("提示","确定"))
        #对文件目录检出操作后，检出人以外的其他项目成员不能对文件目录进行删除和撤销检出操作
        self.登录页面.退出登录()
        if self.wait(对话框对象库.对话框按钮.format("确认注销","重新登录"),3):
            self.click(对话框对象库.对话框按钮.format("确认注销","重新登录"))
        # self.登录页面.短信快捷登录(手机号='18942178871')
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="检出文件目录")
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]', 文件名称='一级目录')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("删除"))
        self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("文件夹下存在被锁定的文件"), 3):
            raise AssertionError("文件目录被检出后，项目其他成员进行删除操作未出现不能删除的提示")
        if not self.wait(项目对象库.列表文件名称.format("一级目录"), 3):
            raise AssertionError("文件目录被检出后，项目其他成员进行删除操作时文件目录被删除")
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]', 文件名称='一级目录')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("撤销检出"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("不能撤销检出他人检出的文件"), 3):
            raise AssertionError("文件目录被检出后，项目其他成员进行撤销检出操作时未出现提示信息")
        self.click(项目对象库.目录节点.format("一级目录"))
        time.sleep(1)
        if not self.wait(项目对象库.检出按钮.format('头像2.txt'), 3):
            raise AssertionError("文件目录被检出后，项目其他成员进行撤销检出操作时，撤销检出成功")

    def 撤销检出(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="撤销检出1")
        self.项目管理页面.创建空白项目(项目名称="撤销检出1")
        self.项目管理页面.点击进入项目(项目名称="撤销检出1")
        self.wait(项目对象库.目录节点.format("撤销检出1"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="撤销检出1")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        素材1 = ['TestData', 'FrontData', '项目页', '检入检出素材.txt']
        素材2 = ['TestData', 'FrontData', '项目页', '头像2.txt']
        self.项目页面.批量上传文件(目录路径=['检出文件目录', '一级目录'], 文件路径列表=[素材1, 素材2])
        #文件被检出后可以通过撤销检出修改文件检出状态
        self.项目页面.检出资源(目录路径=['撤销检出1', '一级目录'], 资源名称='检入检出素材.txt')
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]', 文件名称='检入检出素材.txt')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("撤销检出"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 3):
            raise AssertionError("对已检出的文件进行撤销检出操作时，系统未给出撤销成功的提示")
        if self.wait(项目对象库.检出按钮.format('检入检出素材.txt'), 3):
            raise AssertionError("对已检出的文件进行撤销检出操作后，文件仍然处于检出状态")
        #文件未被检出时，进行检出操作，提示文件未被检出
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]', 文件名称='检入检出素材.txt')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("撤销检出"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("存在文件未被检出，不能执行该操作"), 3):
            raise AssertionError("对未检出的文件进行撤销检出操作时，系统未给出不能进行撤销操作的提示")
        #文件目录下没有文件，点击撤销检出，可以撤销成功
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]', 文件名称='二级目录')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("撤销检出"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("未选择文件"), 3):
            raise AssertionError("文件目录下没有文件，点击撤销检出，未出现撤销成功提示")
        #文件目录下没有未检出的文件，点击撤销检出，可以撤销成功
        self.项目页面.检出资源(目录路径=['撤销检出1', '一级目录'], 资源名称='检入检出素材.txt')
        self.项目页面.检出资源(目录路径=['撤销检出1', '一级目录'], 资源名称='头像2.txt')
        self.click(项目对象库.目录节点.format("撤销检出1"))
        time.sleep(1)
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]', 文件名称='一级目录')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("撤销检出"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 3):
            raise AssertionError("文件目录下没有未检出的文件，点击撤销检出，未出现撤销成功提示")
        self.click(项目对象库.目录节点.format("一级目录"))
        time.sleep(1)
        if self.wait(项目对象库.检出按钮.format('检入检出素材.txt'), 3) or\
                self.wait(项目对象库.检出按钮.format('头像2.txt'), 3):
            raise AssertionError("对文件目录进行撤销检出后，文件目录下的文件仍然处于检出状态")
        #文件目录下含有未检出的文件，点击撤销检出，不能撤销成功
        self.项目页面.检出资源(目录路径=['撤销检出1', '一级目录'], 资源名称='头像2.txt')
        self.click(项目对象库.目录节点.format("撤销检出1"))
        time.sleep(2)
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]', 文件名称='一级目录')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("撤销检出"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("存在文件未被检出，不能执行该操作"), 3):
            raise AssertionError("文件目录下含有未检出的文件，点击撤销检出，未出现不能执行撤销检出的提示")
        self.click(项目对象库.目录节点.format("一级目录"))
        time.sleep(1)
        if self.wait(项目对象库.检出按钮.format('检入检出素材.txt'), 3) or not \
                self.wait(项目对象库.检出按钮.format('头像2.txt'), 3):
            raise AssertionError("对文件目录下含有未检出的文件的文件目录撤销检出，文件目录下的文件的状态发生变化")

    def 改变文件状态(self):
        pass

    def 添加附加文件(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="附加文件")
        self.项目管理页面.创建空白项目(项目名称="附加文件")
        self.项目管理页面.点击进入项目(项目名称="附加文件")
        self.wait(项目对象库.目录节点.format("附加文件"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="附加文件")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        素材1 = ['TestData', 'FrontData', '项目页', '素材1.png']
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        素材4 = ['TestData', 'FrontData', '项目页', '素材4.png']
        素材5 = ['TestData', 'FrontData', '项目页', '素材5.png']
        素材6 = ['TestData', 'FrontData', '项目页', '素材6.png']
        self.项目页面.批量上传文件(目录路径=['附加文件', '一级目录'], 文件路径列表=[素材1,素材2,素材3,素材4,素材5,素材6])
        #点击文件行操作中的添加附件操作，弹出附件文件弹窗
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]', 文件名称='素材1.png')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("附加文件"))
        if not self.wait(对话框对象库.弹框标题.format("附加文件"),3):
            raise AssertionError("点击文件的附加文件操作，未查看到附加文件弹窗")
        #左侧资源树默认全部展开，点击目录，右侧列表显示该目录下全部文件
        self.click(项目对象库.附加文件.树资源节点.format("一级目录"))
        for 文件 in ['素材2','素材3','素材4','素材5','素材6']:
            if not self.wait(项目对象库.附加文件.列表单选按钮.format(文件),3):
                raise AssertionError(f"附加文件弹窗显示文件目录下的文件时{文件}未被显示")
        #不勾选任何文件点击附加，系统提示附加文件不能为空
        self.click(项目对象库.附加文件.附加按钮)
        self.default_content()
        if not self.wait(公共元素对象库.系统提示信息弹框.format("请选择附加文件"),3):
            raise AssertionError("附加文件操作时不选择文件，点击附加，系统未给出附加文件为空的提示")
        #勾选单个文件点击附加，系统提示附加成功，在文件的引用tab页可以查看到该文件被引用文件名称
        self.click(项目对象库.附加文件.列表单选按钮.format("素材2"))
        self.click(项目对象库.附加文件.附加按钮)
        self.default_content()
        if not self.wait(公共元素对象库.系统提示信息弹框.format("操作成功"), 3):
            raise AssertionError("附加文件操作时选择文件点击附加后，系统未给出附加成功的提示")
        self.click(项目对象库.列表文件名称.format('素材1.png'))
        self.click(项目对象库.文件信息.引用tab页)
        if not self.wait(项目对象库.文件信息.引用文件名称.format("素材2.jpg"),3):
            raise AssertionError("对文件设置附加文件后，在文件信息中查看不到该文件的引用文件信息")
        self.click(项目对象库.列表文件名称.format('素材2.jpg'))
        self.click(项目对象库.文件信息.被引用tab页)
        if not self.wait(项目对象库.文件信息.被引用文件名称.format("素材1.png"),3):
            raise AssertionError("对文件设置附加文件后，在被引用文件信息中查看不到该文件的被引用信息")
        #勾选多个文件点击附加，系统提示附加成功，在文件的引用tab页可以查看到该文件被引用文件名称
        序号=self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]', 文件名称='素材1.png')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("附加文件"))
        self.wait(对话框对象库.弹框标题.format("附加文件"), 3)
        self.click(项目对象库.附加文件.树资源节点.format("一级目录"))
        self.click(项目对象库.附加文件.列表单选按钮.format("素材3"))
        self.click(项目对象库.附加文件.列表单选按钮.format("素材4"))
        self.click(项目对象库.附加文件.列表单选按钮.format("素材5"))
        self.click(项目对象库.附加文件.附加按钮)
        self.default_content()
        self.wait(公共元素对象库.系统提示信息弹框.format("操作成功"), 3)
        for 文件名 in ['素材3.jpg','素材4.png','素材5.png']:
            self.click(项目对象库.列表文件名称.format('素材1.png'))
            self.click(项目对象库.文件信息.引用tab页)
            if not self.wait(项目对象库.文件信息.引用文件名称.format(文件名), 3):
                raise AssertionError(f"对文件设置附加文件后，在文件信息中查看不到该文件的引用{文件名}的信息")
            self.click(项目对象库.列表文件名称.format(文件名))
            self.click(项目对象库.文件信息.被引用tab页)
            if not self.wait(项目对象库.文件信息.被引用文件名称.format("素材1.png"), 3):
                raise AssertionError(f"对文件设置附加文件后，在被引用文件{文件名}的信息中查看不到该文件的被引用信息")
        #勾选单个或多个文件，点击取消，在文件的引用tab页查看是否被引用
        序号=self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]', 文件名称='素材1.png')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("附加文件"))
        self.wait(对话框对象库.弹框标题.format("附加文件"), 3)
        self.click(项目对象库.附加文件.树资源节点.format("一级目录"))
        self.click(项目对象库.附加文件.列表单选按钮.format("素材6"))
        self.click(项目对象库.附加文件.取消按钮)
        self.default_content()
        self.click(项目对象库.列表文件名称.format('素材1.png'))
        self.click(项目对象库.文件信息.引用tab页)
        if self.wait(项目对象库.文件信息.引用文件名称.format("素材6.png"), 3):
            raise AssertionError("文件设置附加文件勾选单个文件点击取消，在文件信息中查看到了该文件的引用文件信息")
        self.click(项目对象库.列表文件名称.format('素材6.png'))
        self.click(项目对象库.文件信息.被引用tab页)
        if self.wait(项目对象库.文件信息.被引用文件名称.format("素材1.png"), 3):
            raise AssertionError("文件设置附加文件勾选单个文件点击取消，在被引用文件信息中查看到该文件的被引用信息")
        #勾选单个或多个文件，关闭引用文件弹窗，在文件的引用tab页查看是否被引用
        序号=self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]', 文件名称='素材1.png')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("附加文件"))
        self.wait(对话框对象库.弹框标题.format("附加文件"), 3)
        self.click(项目对象库.附加文件.树资源节点.format("一级目录"))
        self.click(项目对象库.附加文件.列表单选按钮.format("素材6"))
        self.click(对话框对象库.关闭弹框.format("附加文件"))
        self.default_content()
        self.click(项目对象库.列表文件名称.format('素材1.png'))
        self.click(项目对象库.文件信息.引用tab页)
        if self.wait(项目对象库.文件信息.引用文件名称.format("素材6.png"), 3):
            raise AssertionError("文件设置附加文件勾选单个文件点击取消，在文件信息中查看到了该文件的引用文件信息")
        self.click(项目对象库.列表文件名称.format('素材6.png'))
        self.click(项目对象库.文件信息.被引用tab页)
        if self.wait(项目对象库.文件信息.被引用文件名称.format("素材1.png"), 3):
            raise AssertionError("文件设置附加文件勾选单个文件点击取消，在被引用文件信息中查看到该文件的被引用信息")

    def 删除文件或目录(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="删除文件或目录")
        self.项目管理页面.创建空白项目(项目名称="删除文件或目录")
        self.项目管理页面.点击进入项目(项目名称="删除文件或目录")
        self.wait(项目对象库.目录节点.format("删除文件或目录"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="删除文件或目录")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        素材1 = ['TestData', 'FrontData', '项目页', '素材1.png']
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        self.项目页面.批量上传文件(目录路径=['删除文件或目录', '一级目录'], 文件路径列表=[素材1, 素材2])
        #点击删除，文件可以被删除成功
        序号=self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]', 文件名称='素材1.png')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("删除"))
        self.click(对话框对象库.对话框按钮.format("提示","确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("删除成功"),3):
            raise AssertionError("对文件执行删除操作后，未查看到删除成功提示信息")
        self.项目页面.刷新列表()
        self.click(项目对象库.目录节点.format("一级目录"))
        if self.wait(项目对象库.列表文件名称.format('素材1.png'),3):
            raise AssertionError("删除文件成功后，在文件列表中仍然能查看到被删除的文件")
        #文件目录为空，点击删除，目录可以被删除成功
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]', 文件名称='二级目录')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("删除"))
        self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("删除成功"), 3):
            raise AssertionError("对空文件目录执行删除操作后，未查看到删除成功提示信息")
        if self.wait(项目对象库.列表文件名称.format('二级目录'), 3):
            raise AssertionError("删除空文件目录成功后，在文件列表中仍然能查看到被删除的文件目录")
        #文件目录不含有已检出的文件，点击删除，可以删除成功
        self.click(项目对象库.目录节点.format("删除文件或目录"))
        time.sleep(1)
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]', 文件名称='一级目录')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("删除"))
        self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("删除成功"), 3):
            raise AssertionError("对文件目录执行删除操作后，未查看到删除成功提示信息")
        if self.wait(项目对象库.列表文件名称.format('一级目录'), 3):
            raise AssertionError("删除文件目录成功后，在文件列表中仍然能查看到被删除的文件目录")
        if self.wait(项目对象库.列表文件名称.format('素材2.jpg'),3):
            raise AssertionError("删除文件目录成功后，在文件列表中仍然能查看到被删除的文件目录下的文件")

    def 文件或目录打包(self):
        self.公共操作.清空浏览器下载目录()
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="文件或目录打包")
        self.项目管理页面.创建空白项目(项目名称="文件或目录打包")
        self.项目管理页面.点击进入项目(项目名称="文件或目录打包")
        self.wait(项目对象库.目录节点.format("文件或目录打包"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="文件或目录打包")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        素材1 = ['TestData', 'FrontData', '项目页', '素材1.png']
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        self.项目页面.批量上传文件(目录路径=['文件或目录打包', '一级目录'], 文件路径列表=[素材1, 素材2])
        #文件行操作，点击打包，自动下载打包后的压缩包，压缩包名为被打包的文件名，压缩包内容为被打包的文件
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]', 文件名称='素材1.png')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("打包"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "是"))
        downpath = self.公共操作.检查文件是否下载完成()
        filepath = downpath + '\素材1.png.zip'
        time.sleep(3)
        if not os.path.exists(filepath):
            raise AssertionError("在下载目录下未查看到打包的文件")
        namelist=self.公共操作.查看zip文件(zip文件路径=filepath)
        if not '素材1.png' in namelist:
            raise AssertionError("在打包的文件中未查看到被打包的文件")
        #目录行操作，点击打包，自动下载打包后的压缩包，压缩包名为被打包的目录的名称，压缩包内容未被打包的目录及目录下的全部资源
        self.公共操作.清空浏览器下载目录()
        self.click(项目对象库.目录节点.format("文件或目录打包"))
        time.sleep(1)
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]', 文件名称='一级目录')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("打包"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "是"))
        downpath = self.公共操作.检查文件是否下载完成()
        filepath = downpath + '\一级目录.zip'
        time.sleep(3)
        if not os.path.exists(filepath):
            raise AssertionError("在下载目录下未查看到打包的文件目录")
        self.公共操作.解压zip到指定目录(zip文件路径=filepath,目标路径=downpath)
        文件目录=os.listdir(downpath + '\一级目录')
        if not '素材1.png' in 文件目录 or not '素材2.jpg' in 文件目录:
            raise AssertionError("在打包的文件中未查看到被打包的文件")
        self.公共操作.清空浏览器下载目录()
        #文件被检出后也可以打包
        self.公共操作.清空浏览器下载目录()
        self.项目页面.检出资源(目录路径=['文件或目录打包', '一级目录'], 资源名称='素材1.png')
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]', 文件名称='素材1.png')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("打包"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "是"))
        downpath = self.公共操作.检查文件是否下载完成()
        filepath = downpath + '\素材1.png.zip'
        time.sleep(3)
        if not os.path.exists(filepath):
            raise AssertionError("在下载目录下未查看到打包的文件")
        namelist = self.公共操作.查看zip文件(zip文件路径=filepath)
        if not '素材1.png' in namelist:
            raise AssertionError("在打包的文件中未查看到被打包的状态为检出的文件")
        #目录下含有被检出的文件时，目录也可以被正常打包，压缩包内容为被打包的目录及目录下的全部资源
        self.公共操作.清空浏览器下载目录()
        self.click(项目对象库.目录节点.format("文件或目录打包"))
        time.sleep(1)
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]', 文件名称='一级目录')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("打包"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "是"))
        downpath = self.公共操作.检查文件是否下载完成()
        filepath = downpath + '\一级目录.zip'
        time.sleep(3)
        if not os.path.exists(filepath):
            raise AssertionError("在下载目录下未查看到打包的文件目录")
        self.公共操作.解压zip到指定目录(zip文件路径=filepath, 目标路径=downpath)
        文件目录 = os.listdir(downpath + '\一级目录')
        if not '素材1.png' in 文件目录 or not '素材2.jpg' in 文件目录:
            raise AssertionError("在打包的文件中未查看到被打包的状态为检出的文件")

    def 文件或目录分享(self):
        pass

    def 文件下载(self):
        self.公共操作.清空浏览器下载目录()
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="文件下载")
        self.项目管理页面.创建空白项目(项目名称="文件下载")
        self.项目管理页面.点击进入项目(项目名称="文件下载")
        self.wait(项目对象库.目录节点.format("文件下载"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="文件下载")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        素材1 = ['TestData', 'FrontData', '项目页', '素材1.png']
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        self.项目页面.批量上传文件(目录路径=['文件下载', '一级目录'], 文件路径列表=[素材1, 素材2])
        #点击下载，文件可以被正常下载
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]', 文件名称='素材1.png')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("下载"))
        downpath = self.公共操作.检查文件是否下载完成()
        filepath = downpath + '\素材1.png'
        time.sleep(3)
        if not os.path.exists(filepath):
            raise AssertionError("在下载目录下未查看到被下载的文件")
        self.公共操作.清空浏览器下载目录()
        #文件检出后也可以下载
        self.项目页面.检出资源(目录路径=['文件下载', '一级目录'], 资源名称='素材1.png')
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]', 文件名称='素材1.png')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("下载"))
        downpath = self.公共操作.检查文件是否下载完成()
        filepath = downpath + '\素材1.png'
        time.sleep(3)
        if not os.path.exists(filepath):
            raise AssertionError("在下载目录下未查看到被下载的状态为检出的文件")

    def 面包屑(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="查看面包屑")
        self.项目管理页面.创建空白项目(项目名称="查看面包屑")
        self.项目管理页面.点击进入项目(项目名称="查看面包屑")
        self.wait(项目对象库.目录节点.format("查看面包屑"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="查看面包屑")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        #在不同的文件目录下，面包屑会显示对应的路径
        面包屑=[]
        self.click(项目对象库.目录节点.format("二级目录"))
        elements=self.driver.getelements('//span[@class="el-breadcrumb__item"]//span[@class="el-link--inner"]')
        for element in elements:
            面包屑.append(element.text)
        if 面包屑!=['查看面包屑','一级目录','二级目录']:
            raise AssertionError("点击不同的目录，面包屑未显示对应的路径")
        #点击面包屑上的节点，会跳转到对应的页面
        self.click('//span[@class="el-breadcrumb__item"]//span[contains(text(),"查看面包屑")]')
        if not self.wait(项目对象库.列表文件名称.format('一级目录'), 3):
            raise AssertionError("点击面包屑上的节点，未跳转到对应的页面")

    def 工具栏检查(self):
        self.公共操作.清空浏览器下载目录()
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="工具栏检查")
        self.项目管理页面.创建空白项目(项目名称="工具栏检查")
        self.项目管理页面.点击进入项目(项目名称="工具栏检查")
        self.wait(项目对象库.目录节点.format("工具栏检查"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="工具栏检查")
        素材1 = ['TestData', 'FrontData', '项目页', '素材1.png']
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        self.项目页面.批量上传文件(目录路径=['工具栏检查', '一级目录'], 文件路径列表=[素材1, 素材2])
        #在右侧文件列表中勾选单个资源时，批量操作工具栏不会出现
        self.click(项目对象库.列表复选框.format('素材1.png'))
        if self.wait(项目对象库.工具栏按钮.format('检出'),3):
            raise AssertionError('勾选单个文件资源时，出现批量操作按钮')
        self.项目页面.刷新列表()
        #在右侧文件列表中勾选多个资源时，批量操作工具栏出现，工具栏中包括检出、撤销检出、收藏、下载、批量删除和打包按钮
        self.click(项目对象库.列表复选框.format('素材1.png'))
        self.click(项目对象库.列表复选框.format('素材2.jpg'))
        按钮列表=['检出','撤销检出','收藏','删除','打包']
        for 按钮 in 按钮列表:
            if not self.wait(项目对象库.工具栏按钮.format(按钮),3):
                raise AssertionError(f"工具栏{按钮}按钮未正常出现")

    def 批量检出(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="批量检出")
        self.项目管理页面.创建空白项目(项目名称="批量检出")
        self.项目管理页面.点击进入项目(项目名称="批量检出")
        self.wait(项目对象库.目录节点.format("批量检出"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="批量检出")
        self.项目页面.创建文件目录(目录名称="一级目录2", 目录父节点名称="批量检出")
        self.项目页面.创建文件目录(目录名称="一级目录3", 目录父节点名称="批量检出")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        素材1 = ['TestData', 'FrontData', '项目页', '素材1.png']
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        素材4 = ['TestData', 'FrontData', '项目页', '素材4.png']
        素材5 = ['TestData', 'FrontData', '项目页', '素材5.png']
        self.项目页面.批量上传文件(目录路径=['批量检出', '一级目录'], 文件路径列表=[素材1, 素材2,素材3,素材4,素材5])
        素材6 = ['TestData', 'FrontData', '项目页', '检入检出素材.txt']
        素材7 = ['TestData', 'FrontData', '项目页', '头像2.txt']
        self.项目页面.批量上传文件(目录路径=['批量检出', '一级目录2'], 文件路径列表=[素材6])
        self.项目页面.批量上传文件(目录路径=['批量检出', '一级目录3'], 文件路径列表=[素材7])
        self.项目页面.批量上传文件(目录路径=['批量检出', '一级目录','二级目录'], 文件路径列表=[素材6])
        #批量选择文件，点击检出，可以检出成功
        self.click(项目对象库.目录节点.format('一级目录'))
        self.click(项目对象库.列表复选框.format('素材1.png'))
        self.click(项目对象库.列表复选框.format('素材2.jpg'))
        self.click(项目对象库.工具栏按钮.format('检出'))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("成功"),3):
            raise AssertionError("对文件进行批量检出操作，未查看到系统提示信息")
        if not self.wait(项目对象库.检出按钮.format('素材1.png'), 3) or not\
                self.wait(项目对象库.检出按钮.format('素材2.jpg'), 3):
            raise AssertionError("进行批量检出操作后，文件列表中文件未被标记为检出状态")
        #批量选择文件，被选择文件中包含已检出的文件，点击检出，不能检出成功
        self.click(项目对象库.列表复选框.format('素材1.png'))
        self.click(项目对象库.列表复选框.format('素材3.jpg'))
        self.click(项目对象库.工具栏按钮.format('检出'))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("存在已被检出的文件，不能执行该操作"), 3):
            raise AssertionError("对文件进行批量检出操作，文件中含有已检出的文件，批量检出时未出现提示信息")
        if not self.wait(项目对象库.检出按钮.format('素材1.png'), 3) or \
                self.wait(项目对象库.检出按钮.format('素材3.jpg'), 3):
            raise AssertionError("批量检出文件失败，但是被检出文件的状态发生了变化")
        #批量选择目录和文件，点击检出，可以检出成功
        self.click(项目对象库.列表复选框.format('二级目录'))
        self.click(项目对象库.列表复选框.format('素材1.png'))
        self.click(项目对象库.工具栏按钮.format('检出'))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 3):
            raise AssertionError("对文件和文件目录进行批量检出操作，未查看到系统提示信息")
        if not self.wait(项目对象库.检出按钮.format('素材3.jpg'), 3) :
            raise AssertionError("进行文件和文件目录批量检出操作后，文件列表中文件未被标记为检出状态")
        self.click(项目对象库.目录节点.format('二级目录'))
        if not self.wait(项目对象库.检出按钮.format('检入检出素材.txt'), 3):
            raise AssertionError("进行文件和文件目录批量检出操作后，文件目录中文件未被标记为检出状态")
        #选择多个目录，目录下不含检出的文件，点击检出，目录下的文件可以检出成功
        self.click(项目对象库.目录节点.format('批量检出'))
        self.click(项目对象库.列表复选框.format('一级目录3'))
        self.click(项目对象库.列表复选框.format('一级目录2'))
        self.click(项目对象库.工具栏按钮.format('检出'))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 3):
            raise AssertionError("对文件和文件目录进行批量检出操作，未查看到系统提示信息")
        self.click(项目对象库.目录节点.format('一级目录2'))
        if not self.wait(项目对象库.检出按钮.format('检入检出素材.txt'), 3):
            raise AssertionError('对目录进行批量检出时，检出成功后在目录的下未查看到检出状态的文件')
        self.click(项目对象库.目录节点.format('一级目录3'))
        if not self.wait(项目对象库.检出按钮.format('头像2.txt'), 3):
            raise AssertionError('对目录进行批量检出时，检出成功后在目录的下未查看到检出状态的文件')
        self.项目页面.文件撤销检出(目录路径=['批量检出', '一级目录3'], 资源名称='头像2.txt')
        #选择多个目录，目录下含有检出的文件，点击检出，不能检出成功
        self.click(项目对象库.目录节点.format('批量检出'))
        self.click(项目对象库.列表复选框.format('一级目录3'))
        self.click(项目对象库.列表复选框.format('一级目录2'))
        self.click(项目对象库.工具栏按钮.format('检出'))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "是"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("存在已被检出的文件，不能执行该操作"), 3):
            raise AssertionError("对文件目录进行批量检出操作，目录下含有已检出的文件，未查看到系统提示信息")
        self.click(项目对象库.目录节点.format('一级目录2'))
        if not self.wait(项目对象库.检出按钮.format('检入检出素材.txt'), 3):
            raise AssertionError('对目录进行批量检出时，检出失败后，目录下已检出的文件的文件状态发现改变')
        self.click(项目对象库.目录节点.format('一级目录3'))
        if self.wait(项目对象库.检出按钮.format('头像2.txt'), 3):
            raise AssertionError('对目录进行批量检出时，检出失败后，目录下未检出的文件的检出状态发生改变')

    def 批量撤销检出(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="批量撤销检出")
        self.项目管理页面.创建空白项目(项目名称="批量撤销检出")
        self.项目管理页面.点击进入项目(项目名称="批量撤销检出")
        self.wait(项目对象库.目录节点.format("批量撤销检出"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="批量撤销检出")
        self.项目页面.创建文件目录(目录名称="一级目录2", 目录父节点名称="批量撤销检出")
        self.项目页面.创建文件目录(目录名称="一级目录3", 目录父节点名称="批量撤销检出")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        素材1 = ['TestData', 'FrontData', '项目页', '素材1.png']
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        素材4 = ['TestData', 'FrontData', '项目页', '素材4.png']
        素材5 = ['TestData', 'FrontData', '项目页', '素材5.png']
        self.项目页面.批量上传文件(目录路径=['批量撤销检出', '一级目录'], 文件路径列表=[素材1, 素材2, 素材3, 素材4, 素材5])
        self.项目页面.检出资源(目录路径=['批量撤销检出', '一级目录'], 资源名称='素材1.png')
        self.项目页面.检出资源(目录路径=['批量撤销检出', '一级目录'], 资源名称='素材2.jpg')
        self.项目页面.检出资源(目录路径=['批量撤销检出', '一级目录'], 资源名称='素材3.jpg')
        素材6 = ['TestData', 'FrontData', '项目页', '检入检出素材.txt']
        素材7 = ['TestData', 'FrontData', '项目页', '头像2.txt']
        self.项目页面.批量上传文件(目录路径=['批量撤销检出', '一级目录2'], 文件路径列表=[素材6])
        self.项目页面.批量上传文件(目录路径=['批量撤销检出', '一级目录3'], 文件路径列表=[素材7])
        self.项目页面.批量上传文件(目录路径=['批量撤销检出', '一级目录', '二级目录'], 文件路径列表=[素材6])
        self.项目页面.检出资源(目录路径=['批量撤销检出', '一级目录'], 资源名称='二级目录')
        self.项目页面.检出资源(目录路径=['批量撤销检出', '一级目录2'], 资源名称='检入检出素材.txt')
        self.项目页面.检出资源(目录路径=['批量撤销检出', '一级目录3'], 资源名称='头像2.txt')
        # 批量选择已检出的文件，点击撤销检出，可以撤销检出成功
        self.click(项目对象库.目录节点.format('一级目录'))
        self.click(项目对象库.列表复选框.format('素材1.png'))
        self.click(项目对象库.列表复选框.format('素材2.jpg'))
        self.click(项目对象库.工具栏按钮.format('撤销检出'))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 3):
            raise AssertionError("对文件进行批量撤销检出操作，未查看到系统提示信息")
        if self.wait(项目对象库.检出按钮.format('素材1.png'), 3) or\
                self.wait(项目对象库.检出按钮.format('素材2.jpg'), 3):
            raise AssertionError("进行批量撤销检出操作后，文件列表中文件仍被标记为检出状态")
        #选择多个文件，文件中包含未检出的文件，点击撤销检出，不能检出成功
        self.click(项目对象库.列表复选框.format('素材1.png'))
        self.click(项目对象库.列表复选框.format('素材3.jpg'))
        self.click(项目对象库.工具栏按钮.format('撤销检出'))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("存在文件未被检出，不能执行该操作"), 3):
            raise AssertionError("对文件进行批量撤销检出操作，文件中含有未检出的文件，未查看到系统提示信息")
        if self.wait(项目对象库.检出按钮.format('素材1.png'), 3) or not \
                self.wait(项目对象库.检出按钮.format('素材3.jpg'), 3):
            raise AssertionError("进行批量撤销检出操作失败后，文件列表中文件的检出状态发生变化")
        #批量选择文件和目录，点击撤销检出，可以撤销成功
        self.项目页面.刷新列表()
        self.click(项目对象库.列表复选框.format('素材3.jpg'))
        self.click(项目对象库.列表复选框.format('二级目录'))
        self.click(项目对象库.工具栏按钮.format('撤销检出'))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 3):
            raise AssertionError("对文件和目录进行批量撤销检出操作，未查看到系统提示信息")
        self.项目页面.刷新列表()
        if self.wait(项目对象库.检出按钮.format('素材3.jpg'), 3) :
            raise AssertionError("对文件和目录进行批量撤销检出操作后，文件列表中文件未被撤销检出")
        self.click(项目对象库.目录节点.format('二级目录'))
        if self.wait(项目对象库.检出按钮.format('检入检出素材.txt'), 3):
            raise AssertionError("对文件和目录进行批量撤销检出操作后，目录中的文件未被撤销检出")
        #批量选择目录，目录下含有未检出的文件，点击撤销检出，不能撤销检出成功
        self.click(项目对象库.目录节点.format('批量撤销检出'))
        self.click(项目对象库.列表复选框.format('一级目录3'))
        self.click(项目对象库.列表复选框.format('一级目录2'))
        self.click(项目对象库.工具栏按钮.format('撤销检出'))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 3):
            raise AssertionError("对文件和文件目录进行批量撤销检出操作，未查看到系统提示信息")
        self.click(项目对象库.目录节点.format('一级目录2'))
        if self.wait(项目对象库.检出按钮.format('检入检出素材.txt'), 3):
            raise AssertionError('对目录进行批量撤销检出时，检出成功后在目录的下仍能查看到检出状态的文件')
        self.click(项目对象库.目录节点.format('一级目录3'))
        if self.wait(项目对象库.检出按钮.format('头像2.txt'), 3):
            raise AssertionError('对目录进行批量撤销检出时，检出成功后在目录的下仍能查看到检出状态的文件')
        self.项目页面.检出资源(目录路径=['批量检出', '一级目录3'], 资源名称='头像2.txt')
        #选择多个目录，目录下不含有未检出的文件，点击撤销检出，可以撤销检出
        self.click(项目对象库.目录节点.format('批量撤销检出'))
        self.click(项目对象库.列表复选框.format('一级目录3'))
        self.click(项目对象库.列表复选框.format('一级目录2'))
        self.click(项目对象库.工具栏按钮.format('撤销检出'))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("存在文件未被检出，不能执行该操作"), 3):
            raise AssertionError("对文件目录进行批量撤销检出操作，目录下含有未检出的文件，未查看到系统提示信息")
        self.click(项目对象库.目录节点.format('一级目录2'))
        if self.wait(项目对象库.检出按钮.format('检入检出素材.txt'), 3):
            raise AssertionError('对目录进行批量撤销检出时，撤销检出失败后，目录下未检出的文件的文件状态发现改变')
        self.click(项目对象库.目录节点.format('一级目录3'))
        if not self.wait(项目对象库.检出按钮.format('头像2.txt'), 3):
            raise AssertionError('对目录进行批量撤销检出时，撤销检出失败后，目录下已检出的文件的检出状态发生改变')

    def 批量收藏(self):
        self.进入到操作位置.进入收藏页()
        self.收藏页清理所有收藏()
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="批量收藏资源")
        self.项目管理页面.创建空白项目(项目名称="批量收藏资源")
        self.项目管理页面.点击进入项目(项目名称="批量收藏资源")
        self.wait(项目对象库.目录节点.format("批量收藏资源"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="1", 目录父节点名称="批量收藏资源")
        self.项目页面.创建文件目录(目录名称="2", 目录父节点名称="批量收藏资源")
        self.项目页面.创建文件目录(目录名称="11", 目录父节点名称="1")
        self.项目页面.创建文件目录(目录名称="12", 目录父节点名称="1")
        self.项目页面.创建文件目录(目录名称="21", 目录父节点名称="2")
        self.项目页面.创建文件目录(目录名称="22", 目录父节点名称="2")
        self.项目页面.批量上传文件(目录路径=['收藏资源', '1'], 文件路径列表=[['TestData', 'FrontData', '项目页', '素材1.png'],
                                                        ['TestData', 'FrontData', '项目页', '素材2.jpg']])
        self.项目页面.批量上传文件(目录路径=['收藏资源', '2'], 文件路径列表=[['TestData', 'FrontData', '项目页', '素材3.jpg'],
                                                     ['TestData', 'FrontData', '项目页', '素材4.png']])
        #勾选多个文件，点击收藏，可以收藏成功
        self.click(项目对象库.目录节点.format('1'))
        self.click(项目对象库.列表复选框.format('素材1.png'))
        self.click(项目对象库.列表复选框.format('素材2.jpg'))
        self.click(项目对象库.工具栏按钮.format("收藏"))
        self.wait(公共元素对象库.系统提示信息弹框.format("收藏成功"),3)
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]',
                                   文件名称='素材1.png')
        序号2 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]',
                                   文件名称='素材2.jpg')
        if not self.wait(项目对象库.已选_悬浮列收藏.format(序号), 3) or not self.wait(项目对象库.已选_悬浮列收藏.format(序号), 3):
            raise AssertionError("点击收藏文件成功后，文件的收藏按钮未被点亮")
        self.进入到操作位置.进入收藏页()
        if not self.wait(收藏对象库.资源类型.format("素材1.png", "批量收藏资源"), 3) or not\
                self.wait(收藏对象库.资源类型.format("素材2.jpg", "批量收藏资源"), 3):
            raise AssertionError("点击文件批量收藏按钮，文件没有被收藏")
        #勾选多个目录，点击收藏，可以收藏成功
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="批量收藏资源")
        self.wait(项目对象库.目录节点.format("批量收藏资源"), 3)
        self.click(项目对象库.目录节点.format('1'))
        self.click(项目对象库.列表复选框.format('11'))
        self.click(项目对象库.列表复选框.format('12'))
        self.click(项目对象库.工具栏按钮.format("收藏"))
        self.wait(公共元素对象库.系统提示信息弹框.format("收藏成功"), 3)
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]',
                                   文件名称='11')
        序号2 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]',
                                    文件名称='12')
        if not self.wait(项目对象库.已选_悬浮列收藏.format(序号), 3) or not self.wait(项目对象库.已选_悬浮列收藏.format(序号), 3):
            raise AssertionError("点击收藏目录成功后，目录的收藏按钮未被点亮")
        self.进入到操作位置.进入收藏页()
        if not self.wait(收藏对象库.资源类型.format("11", "批量收藏资源"), 3) or not \
                self.wait(收藏对象库.资源类型.format("12", "批量收藏资源"), 3):
            raise AssertionError("点击目录批量收藏按钮，文件没有被收藏")
        #勾选文件和目录，点击收藏，可以收藏成功
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="批量收藏资源")
        self.wait(项目对象库.目录节点.format("批量收藏资源"), 3)
        self.click(项目对象库.目录节点.format('2'))
        self.click(项目对象库.列表复选框.format('21'))
        self.click(项目对象库.列表复选框.format('素材3.jpg'))
        self.click(项目对象库.工具栏按钮.format("收藏"))
        self.wait(公共元素对象库.系统提示信息弹框.format("收藏成功"), 3)
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]',
                                   文件名称='21')
        序号2 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]',
                                    文件名称='素材3.jpg')
        if not self.wait(项目对象库.已选_悬浮列收藏.format(序号), 3) or not self.wait(项目对象库.已选_悬浮列收藏.format(序号), 3):
            raise AssertionError("点击收藏目录和文件批量收藏成功后，目录和文件的收藏按钮未被点亮")
        self.进入到操作位置.进入收藏页()
        if not self.wait(收藏对象库.资源类型.format("21", "批量收藏资源"), 3) or not \
                self.wait(收藏对象库.资源类型.format("素材3.jpg", "批量收藏资源"), 3):
            raise AssertionError("点击文件和目录批量收藏按钮，文件没有被收藏")
        #勾选的文件或目录中存在以收藏的文件或目录，点击收藏，不能收藏成功
        # self.进入到操作位置.进入项目管理页()
        # self.项目管理页面.点击进入项目(项目名称="批量收藏资源")
        # self.wait(项目对象库.目录节点.format("批量收藏资源"), 3)
        # self.click(项目对象库.目录节点.format('2'))
        # self.click(项目对象库.列表复选框.format('21'))
        # self.click(项目对象库.列表复选框.format('22'))
        # self.click(项目对象库.列表复选框.format('素材3.jpg'))
        # self.click(项目对象库.列表复选框.format('素材4.png'))
        # self.click(项目对象库.工具栏按钮.format("收藏"))
        # if not self.wait(公共元素对象库.系统提示信息弹框.format("收藏记录已存在"), 3):
        #     raise AssertionError("批量收藏文件和目录时，勾选已经别收藏的文件或目录，点击收藏，系统未给出提示信息")
        # 序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]',
        #                            文件名称='22')
        # 序号2 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]',
        #                             文件名称='素材4.png')
        # if self.wait(项目对象库.已选_悬浮列收藏.format(序号), 3) or self.wait(项目对象库.已选_悬浮列收藏.format(序号), 3):
        #     raise AssertionError("点击收藏目录和文件批量收藏失败后，目录和文件的收藏按钮被点亮")
        # self.进入到操作位置.进入收藏页()
        # if self.wait(收藏对象库.资源类型.format("22", "批量收藏资源"), 3) or \
        #         self.wait(收藏对象库.资源类型.format("素材4.png", "批量收藏资源"), 3):
        #     raise AssertionError("点击文件和目录批量收藏失败，文件或目录被收藏")

    def 批量删除(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="批量删除")
        self.项目管理页面.创建空白项目(项目名称="批量删除")
        self.项目管理页面.点击进入项目(项目名称="批量删除")
        self.wait(项目对象库.目录节点.format("批量删除"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="批量删除")
        self.项目页面.创建文件目录(目录名称="一级目录2", 目录父节点名称="批量删除")
        self.项目页面.创建文件目录(目录名称="一级目录3", 目录父节点名称="批量删除")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        素材1 = ['TestData', 'FrontData', '项目页', '素材1.png']
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        素材4 = ['TestData', 'FrontData', '项目页', '素材4.png']
        素材5 = ['TestData', 'FrontData', '项目页', '素材5.png']
        self.项目页面.批量上传文件(目录路径=['批量删除', '一级目录'], 文件路径列表=[素材1, 素材2, 素材3, 素材4, 素材5])
        self.driver.refrsh()
        self.项目页面.检出资源(目录路径=['批量删除', '一级目录'], 资源名称='素材3.jpg')
        素材6 = ['TestData', 'FrontData', '项目页', '检入检出素材.txt']
        素材7 = ['TestData', 'FrontData', '项目页', '头像2.txt']
        self.项目页面.批量上传文件(目录路径=['批量删除', '一级目录2'], 文件路径列表=[素材6])
        self.项目页面.批量上传文件(目录路径=['批量删除', '一级目录3'], 文件路径列表=[素材7])
        self.项目页面.批量上传文件(目录路径=['批量删除', '一级目录', '二级目录'], 文件路径列表=[素材6])
        # self.项目页面.检出资源(目录路径=['批量删除', '一级目录3'], 资源名称='头像2.txt')
        #勾选多个文件，点击删除，弹出删除确认对话框
        self.click(项目对象库.目录节点.format('一级目录'))
        time.sleep(1)
        self.click(项目对象库.列表复选框.format('素材1.png'))
        self.click(项目对象库.列表复选框.format('素材2.jpg'))
        self.click(项目对象库.工具栏按钮.format('删除'))
        if not self.wait(对话框对象库.对话框标题.format("提示"),3):
            raise AssertionError("勾选多个文件时，点击批量删除按钮未出现删除确认对话框")
        #在删除确认对话框中点击取消，查看文件是否被删除
        self.click(对话框对象库.对话框按钮.format("提示","取消"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("已取消删除"),3):
            raise AssertionError("在删除确认对话框中点击取消，未查看到取消删除提示信息")
        if not self.wait(项目对象库.列表文件名称.format("素材1.png"),3) or not \
                self.wait(项目对象库.列表文件名称.format("素材2.jpg"), 3):
            raise AssertionError("在删除确认对话框中点击取消，列表中被选中的文件已经被删除")
        #在删除确认对话框中点击关闭删除确认对话框，查看文件是否被删除
        self.click(项目对象库.工具栏按钮.format('删除'))
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.关闭对话框.format("提示"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("已取消删除"), 3):
            raise AssertionError("在删除确认对话框中点击关闭对话框，未查看到取消删除提示信息")
        if not self.wait(项目对象库.列表文件名称.format("素材1.png"), 3) or not \
                self.wait(项目对象库.列表文件名称.format("素材2.jpg"), 3):
            raise AssertionError("在删除确认对话框中点击关闭对话框，列表中被选中的文件已经被删除")
        #勾选多个文件，点击删除，可以删除
        self.click(项目对象库.工具栏按钮.format('删除'))
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示","确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("删除成功!"), 3):
            raise AssertionError("在删除确认对话框中点击确定，未查看到删除提示信息")
        if self.wait(项目对象库.列表文件名称.format("素材1.png"), 3) or \
                self.wait(项目对象库.列表文件名称.format("素材2.jpg"), 3):
            raise AssertionError("在删除确认对话框中点击确定，列表中被选中的文件未被删除")
        #勾选多个文件，文件中含有检出的文件，点击删除，不能删除成功
        self.click(项目对象库.目录节点.format('一级目录'))
        time.sleep(1)
        self.click(项目对象库.列表复选框.format('素材4.png'))
        self.click(项目对象库.列表复选框.format('素材3.jpg'))
        self.click(项目对象库.工具栏按钮.format('删除'))
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("文件夹下存在被锁定的文件"), 3):
            raise AssertionError("勾选多个文件，文件中含有检出的文件，点击删除，未出现不能删除提示")
        self.click(项目对象库.目录节点.format('一级目录'))
        time.sleep(1)
        if not self.wait(项目对象库.列表文件名称.format("素材4.png"), 3) or not \
                self.wait(项目对象库.列表文件名称.format("素材3.jpg"), 3):
            raise AssertionError("勾选多个文件，文中含有检出的文件，点击删除，提示删除失败后列表中被选中的文件被删除")
        #勾选多个文件和目录，点击删除，可以删除成功
        self.driver.refrsh()
        self.click(项目对象库.目录节点.format('一级目录'))
        time.sleep(1)
        self.click(项目对象库.列表复选框.format('素材4.png'))
        self.click(项目对象库.列表复选框.format('二级目录'))
        self.click(项目对象库.工具栏按钮.format('删除'))
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("删除成功!"), 3):
            raise AssertionError("勾选多个文件和目录，点击删除，未查看到删除提示信息")
        self.click(项目对象库.目录节点.format('一级目录'))
        time.sleep(1)
        if self.wait(项目对象库.列表文件名称.format("素材4.png"), 3) or \
                self.wait(项目对象库.列表文件名称.format("二级目录"), 3):
            raise AssertionError("勾选多个文件和目录，点击删除，列表中被选中的文件或目录未被删除")
        #勾选多个目录，目录下含有检出的文件，点击删除，不能删除成功
        self.click(项目对象库.目录节点.format('批量删除'))
        time.sleep(1)
        self.click(项目对象库.列表复选框.format('一级目录'))
        self.click(项目对象库.列表复选框.format('一级目录2'))
        self.click(项目对象库.工具栏按钮.format('删除'))
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("文件夹下存在被锁定的文件"), 3):
            raise AssertionError("勾选多个目录，目录下含有检出的文件，点击删除，未出现不能删除提示")
        self.click(项目对象库.目录节点.format('一级目录'))
        time.sleep(1)
        if not self.wait(项目对象库.列表文件名称.format("素材5.png"), 3) or not \
                self.wait(项目对象库.列表文件名称.format("素材3.jpg"), 3):
            raise AssertionError("勾选多个目录，目录下含有检出的文件，点击删除,删除失败后，目录下的文件被删除")
        self.click(项目对象库.目录节点.format('一级目录2'))
        time.sleep(1)
        if not self.wait(项目对象库.列表文件名称.format("检入检出素材.txt"), 3):
            raise AssertionError("勾选多个目录，目录下含有检出的文件，点击删除，删除失败后，目录下的文件被删除")
        #勾选多个目录，目录下不含有检出文件，点击删除，可以删除成功
        self.click(项目对象库.目录节点.format('批量删除'))
        time.sleep(1)
        self.click(项目对象库.列表复选框.format('一级目录3'))
        self.click(项目对象库.列表复选框.format('一级目录2'))
        self.click(项目对象库.工具栏按钮.format('删除'))
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("删除成功!"), 3):
            raise AssertionError("勾选多个目录，点击删除，未查看到 删除提示信息")
        if self.wait(项目对象库.列表文件名称.format("一级目录3"), 3) or \
                self.wait(项目对象库.列表文件名称.format("一级目录2"), 3):
            raise AssertionError("勾选多个目录，点击删除，列表中被选中的目录未被删除")

    def 批量打包(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="批量打包")
        self.项目管理页面.创建空白项目(项目名称="批量打包")
        self.项目管理页面.点击进入项目(项目名称="批量打包")
        self.wait(项目对象库.目录节点.format("批量打包"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="批量打包")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        self.项目页面.创建文件目录(目录名称="二级目录2", 目录父节点名称="一级目录")
        素材1 = ['TestData', 'FrontData', '项目页', '素材1.png']
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        素材4 = ['TestData', 'FrontData', '项目页', '素材4.png']
        素材5 = ['TestData', 'FrontData', '项目页', '素材5.png']
        self.项目页面.批量上传文件(目录路径=['批量打包', '一级目录'], 文件路径列表=[素材1, 素材2, 素材3, 素材4, 素材5])
        self.driver.refrsh()
        self.项目页面.检出资源(目录路径=['批量打包', '一级目录'], 资源名称='素材3.jpg')
        素材6 = ['TestData', 'FrontData', '项目页', '检入检出素材.txt']
        self.项目页面.批量上传文件(目录路径=['批量打包', '一级目录', '二级目录'], 文件路径列表=[素材6])
        self.项目页面.检出资源(目录路径=['批量打包', '一级目录', '二级目录'], 资源名称='检入检出素材.txt')
        #勾选多个文件，点击打包，压缩包中含有被勾选文件
        self.公共操作.清空浏览器下载目录()
        self.click(项目对象库.目录节点.format('一级目录'))
        self.click(项目对象库.列表复选框.format('素材1.png'))
        self.click(项目对象库.列表复选框.format('素材2.jpg'))
        self.click(项目对象库.工具栏按钮.format('打包'))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "是"))
        while (True):
            if not self.wait(项目对象库.正在打包按钮,3):
                break
        time.sleep(3)
        downpath = self.公共操作.检查文件是否下载完成()
        filepath = downpath + '\批量打包.zip'
        time.sleep(4)
        namelist = self.公共操作.查看zip文件(zip文件路径=filepath)
        for name in ['素材1.png','素材2.jpg']:
            if not name in namelist or len(namelist)!=2:
                raise AssertionError("在打包的文件中未查看到被打包的文件")
        #勾选多个文件，文件中有被检出的文件，可以被正常打包
        self.公共操作.清空浏览器下载目录()
        self.click(项目对象库.列表复选框.format('素材1.png'))
        self.click(项目对象库.列表复选框.format('素材2.jpg'))
        self.click(项目对象库.列表复选框.format('素材3.jpg'))
        self.click(项目对象库.工具栏按钮.format('打包'))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "是"))
        while(True):
            if not self.wait(项目对象库.正在打包按钮,3):
                break
        time.sleep(3)
        downpath = self.公共操作.检查文件是否下载完成()
        filepath = downpath + '\批量打包.zip'
        time.sleep(4)
        namelist = self.公共操作.查看zip文件(zip文件路径=filepath)
        for name in ['素材1.png', '素材2.jpg','素材3.jpg']:
            if not name in namelist or len(namelist)!=3:
                raise AssertionError("在打包的文件中未查看到被打包的文件")
        #选文件和目录，点击打包，压缩包中含有被勾选的文件和目录，目录下的文件页被打包
        self.公共操作.清空浏览器下载目录()
        self.click(项目对象库.目录节点.format('批量打包'))
        self.click(项目对象库.目录节点.format('一级目录'))
        self.click(项目对象库.列表复选框.format('素材1.png'))
        self.click(项目对象库.列表复选框.format('二级目录2'))
        self.click(项目对象库.工具栏按钮.format('打包'))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "是"))
        downpath = self.公共操作.检查文件是否下载完成()
        filepath = downpath + '\批量打包.zip'
        time.sleep(30)
        namelist = self.公共操作.查看zip文件(zip文件路径=filepath)
        for name in ['素材1.png', '二级目录2']:
            if not name in namelist or len(namelist) != 2:
                raise AssertionError("在打包的文件中未查看到被打包的文件或目录")
        #勾选多个文件和目录，目录下含有被检出的文件，文件和目录可以被正常打包
        self.公共操作.清空浏览器下载目录()
        self.click(项目对象库.目录节点.format('批量打包'))
        self.click(项目对象库.目录节点.format('一级目录'))
        self.click(项目对象库.列表复选框.format('素材1.png'))
        self.click(项目对象库.列表复选框.format('二级目录'))
        self.click(项目对象库.工具栏按钮.format('打包'))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "是"))
        downpath = self.公共操作.检查文件是否下载完成()
        filepath = downpath + '\批量打包.zip'
        time.sleep(4)
        namelist = self.公共操作.查看zip文件(zip文件路径=filepath)
        for name in ['素材1.png', '二级目录/检入检出素材.txt']:
            if not name in namelist or len(namelist) != 2:
                raise AssertionError("在打包的文件中未查看到被打包的文件或目录")

    def 多层次文件目录大文件打包测试(self):
        # self.公共操作.清空浏览器下载目录()
        文件列表=['AdobeCameraRaw8.0All-x64.zip','AdobeCameraRawProfile8.0All.zip','AutoTest.rar','Chrome.rar','eclipse.zip','eclipse-jee-oxygen-R-win32-x86_64.rar','Edge.rar',
              'HNtest.rar','LIBS.rar','navicat150_premium_cs_x64.exe','UXPW.rar','红2-核战挣3.0.exe','红2-机甲争霸.exe','红2-解坊抬弯.exe','红2-局域网版.exe','红2-科技时代2.7.exe',
              '红2-科技时代3.3.exe','红2-狂兽人.exe','红2-尤哩得复仇.exe','红2-尤哩的复仇（局域网版）.exe','红2-原版无电影.exe','红2-中囯掘起.exe','开发工具打包.zip','AutoTest.rar','Chrome.rar']
        # sizelist=[126378153,495785787,128740604,235751374]
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="大文件打包")
        self.项目管理页面.创建空白项目(项目名称="大文件打包")
        self.项目管理页面.点击进入项目(项目名称="大文件打包")
        self.wait(项目对象库.目录节点.format("大文件打包"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="l0", 目录父节点名称="大文件打包")
        for i in range(50):
            self.项目页面.创建文件目录(目录名称=f"l{i+1}", 目录父节点名称=f"l{i}")
            if i%2==0:
                self.click(项目对象库.上传)
                self.wait(对话框对象库.弹框标题.format("上传文件"), 3)
                self.click(项目对象库.点击上传按钮)
                self.公共操作.win上传文件(文件路径=['TestData', 'FrontData', '大文件打包测试',文件列表[int(i/2)]])
                self.wait(项目对象库.待上传文件.format(文件列表[int(i/2)]), 300)
                self.click(项目对象库.上传文件按钮)
                self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 3000)
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="大文件打包")
        self.wait(项目对象库.目录节点.format("大文件打包"), 3)
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]', 文件名称='l0')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("打包"))
        time1=time.time()
        user = os.path.expanduser('~')
        downloadpath = user + '\Downloads'
        if os.path.exists(downloadpath):
            flage=True
            while(flage):
                lists = os.listdir(downloadpath)
                if lists:
                    for i in lists:
                        if 'crdownload' in i:
                            time2=time.time()
                            times = time2 - time1
                            self.logger.info(f"从点击打包按钮到开始下载打包文件所花费的时间为：{int(times)}s")
                            flage = False
                            break
                else:
                    continue
            time3 = time.time()
            flage2 = True
            while (flage2):
                lists = os.listdir(downloadpath)
                if lists:
                    for i in lists:
                        if 'crdownload' not in i:
                            time4 = time.time()
                            times2 = time4 - time3
                            self.logger.info(f"打包的文件下载的时间为：{int(times2)}s")
                            flage2 = False
                            break
                else:
                    continue
        打包文件内容=self.公共操作.解压zip到指定目录(zip文件路径=downloadpath+"\\l0.zip",目标路径=downloadpath)
        for i in range(50):
            if i==0:
                path=downloadpath+'\l0'
            else:
                path = downloadpath
                for j in range(i+1):
                    path=path+f'\l{j}'
            if not os.path.exists(path):
                raise AssertionError(f"打包的文件目录下的 {path} 目录不存在")
            if i%2==0:
                filelist = os.listdir(path)
                if f'l{i+1}' not in filelist or 文件列表[int(i/2)] not in filelist:
                    raise AssertionError(f"在 l{i} 文件目录下应该存在文件目录 l{i+1} 和文件 {文件列表[int(i/2)]} ,实际存在的文件为：{filelist} path是：{path}")
                # fsize = os.path.getsize(path+'\\'+文件列表[int(i/2)])

    def 批量上传文件(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="批量上传文件")
        self.项目管理页面.创建空白项目(项目名称="批量上传文件")
        self.项目管理页面.点击进入项目(项目名称="批量上传文件")
        self.wait(项目对象库.目录节点.format("批量上传文件"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="批量上传文件")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        self.click(项目对象库.目录节点.format("一级目录"))
        self.click(项目对象库.上传)
        self.wait(对话框对象库.弹框标题.format("上传文件"), 3)
        素材1 = ['TestData', 'FrontData', '项目页', '素材1.png']
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        检入检出素材 = ['TestData', 'FrontData', '项目页', '检入检出素材.txt']
        素材5 = ['TestData', 'FrontData', '项目页', '素材5.png']
        内容相同素材= ['TestData', 'FrontData', '项目页', '同素材2.jpg']
        名称相同素材=['TestData', 'FrontData', '文件上传下载', '素材3.jpg']

        # 多次选择同一个文件，点击上传
        for 文件路径 in [素材1, 素材1, 素材1]:
            self.click(项目对象库.点击上传按钮)
            self.公共操作.win上传文件(文件路径=文件路径)
            self.wait(项目对象库.待上传文件.format(文件路径[-1]), 5)
        self.click(项目对象库.上传文件按钮)
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 300)
        elems=self.driver.getelements(项目对象库.列表文件名称.format("素材1.png"))
        if len(elems)!=1:
            raise AssertionError("多次选择同一个文件，点击上传,文件列表中出现多个文件")
        #选择多个文件，文件内容相同，文件名不同，点击上传
        self.click(项目对象库.上传)
        self.wait(对话框对象库.弹框标题.format("上传文件"), 3)
        for 文件路径 in [素材2, 内容相同素材]:
            self.click(项目对象库.点击上传按钮)
            self.公共操作.win上传文件(文件路径=文件路径)
            self.wait(项目对象库.待上传文件.format(文件路径[-1]), 5)
        self.click(项目对象库.上传文件按钮)
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 300)
        if not self.wait(项目对象库.列表文件名称.format("素材2.jpg"), 3) or not \
                self.wait(项目对象库.列表文件名称.format("同素材2.jpg"), 3):
            raise AssertionError("选择多个文件，文件内容相同，文件名不同，点击上传，文件未被上传成功")
        #选择多个文件，文件名相同，文件内容不同，点击上传
        self.click(项目对象库.上传)
        self.wait(对话框对象库.弹框标题.format("上传文件"), 3)
        for 文件路径 in [素材3, 名称相同素材]:
            self.click(项目对象库.点击上传按钮)
            self.公共操作.win上传文件(文件路径=文件路径)
            self.wait(项目对象库.待上传文件.format(文件路径[-1]), 5)
        self.click(项目对象库.上传文件按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("存在相同文件，无法重复上传"),3):
            raise AssertionError("选择多个文件，文件名相同，文件内容不同，点击上传,没有出现提示信息")
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 300)
        elems2 = self.driver.getelements(项目对象库.列表文件名称.format("素材3.jpg"))
        if len(elems2) != 1:
            raise AssertionError("选择多个文件，文件内容相同，文件名不同，点击上传,文件列表中出现多个文件")
        #上传一个文件，修改该文件内容后再次点击上传
        self.click(项目对象库.上传)
        self.wait(对话框对象库.弹框标题.format("上传文件"), 3)
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=检入检出素材)
        self.wait(项目对象库.待上传文件.format(检入检出素材[-1]), 5)
        self.click(项目对象库.上传文件按钮)
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 300)
        self.公共操作.修改文件内容(文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'], 内容=str(int(time.time())))
        time.sleep(3)
        self.click(项目对象库.上传)
        self.wait(对话框对象库.弹框标题.format("上传文件"), 3)
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=检入检出素材)
        self.wait(项目对象库.待上传文件.format(检入检出素材[-1]), 5)
        self.click(项目对象库.上传文件按钮)
        if self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 5):
            raise AssertionError("上传一个文件，修改该文件内容后再次点击上传,文件被上传成功")

    def 收藏资源(self):
        self.进入到操作位置.进入收藏页()
        self.收藏页清理所有收藏()
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="收藏资源")
        self.项目管理页面.创建空白项目(项目名称="收藏资源")
        self.项目管理页面.点击进入项目(项目名称="收藏资源")
        self.wait(项目对象库.目录节点.format("收藏资源"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="收藏资源")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        self.项目页面.批量上传文件(目录路径=['收藏资源','一级目录'],文件路径列表=[['TestData', 'FrontData', '项目页', '素材1.png'],['TestData', 'FrontData', '项目页', '素材2.jpg']])
        #点击资源行操作的收藏按钮，可以对文件或文件目录收藏成功
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]',文件名称='素材1.png')
        self.click(项目对象库.未选_悬浮列收藏.format(序号))
        self.wait(公共元素对象库.系统提示信息弹框.format("收藏成功"))
        if not self.wait(项目对象库.已选_悬浮列收藏.format(序号),3):
            raise AssertionError("点击收藏文件成功后，文件的收藏按钮未被点亮")
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]',文件名称='二级目录')
        self.click(项目对象库.未选_悬浮列收藏.format(序号))
        self.wait(公共元素对象库.系统提示信息弹框.format("收藏成功"))
        if not self.wait(项目对象库.已选_悬浮列收藏.format(序号),3):
            raise AssertionError("点击收藏目录成功后，目录的收藏按钮未被点亮")
        self.进入到操作位置.进入收藏页()
        if not self.wait(收藏对象库.资源类型.format("素材1.png", "收藏资源"),3):
            raise AssertionError("点击文件行操作的收藏按钮，文件没有被收藏")
        if not self.wait(收藏对象库.资源类型.format("二级目录", "收藏资源"),3):
            raise AssertionError("点击目录行操作的收藏按钮，文件没有被收藏")
        #点击资源行操作的收藏按钮，可以对文件或文件目录取消收藏成功
        self.click(收藏对象库.查看收藏按钮.format("二级目录"))
        self.click(项目对象库.目录节点.format("一级目录"))
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]',文件名称='素材1.png')
        self.click(项目对象库.已选_悬浮列收藏.format(序号))
        self.wait(公共元素对象库.系统提示信息弹框.format("取消收藏成功"))
        if not self.wait(项目对象库.未选_悬浮列收藏.format(序号)):
            raise AssertionError("文件取消收藏操作成功后，收藏按钮仍是点亮状态")
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]',文件名称='二级目录')
        self.click(项目对象库.已选_悬浮列收藏.format(序号))
        self.wait(公共元素对象库.系统提示信息弹框.format("取消收藏成功"))
        if not self.wait(项目对象库.未选_悬浮列收藏.format(序号)):
            raise AssertionError("目录取消收藏操作成功后，收藏按钮仍是点亮状态")
        self.进入到操作位置.进入收藏页()
        if self.wait(收藏对象库.资源类型.format("素材1.png", "收藏资源"), 3):
            raise AssertionError("取消收藏文件后，文件仍然在收藏页")
        if self.wait(收藏对象库.资源类型.format("二级目录", "收藏资源"), 3):
            raise AssertionError("取消收藏目录后，目录仍然在收藏页")

    def 清理目录下文件版本(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="清理项目版本")
        self.项目管理页面.创建空白项目(项目名称="清理项目版本", 生命周期名称='系统默认生命周期')
        self.项目管理页面.点击进入项目(项目名称="清理项目版本")
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="清理项目版本")
        素材1 = ['TestData', 'FrontData', '项目页', '素材1.png']
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        素材4 = ['TestData', 'FrontData', '项目页', '素材4.png']
        素材5 = ['TestData', 'FrontData', '项目页', '素材5.png']

        self.项目页面.批量上传文件(目录路径=['清理项目版本','一级目录'], 文件路径列表=[素材1, 素材2, 素材3, 素材4, 素材5])
        for filename in ['素材2.jpg', '素材3.jpg', '素材4.png', '素材5.png']:
            self.项目页面.附加文件(目录路径=['清理项目版本','一级目录'], 文件名称="素材1.png", 附加文件路径列表=[['清理项目版本', filename]])
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="清理项目版本")
        self.项目页面.按路径展开目录(目录路径=['清理项目版本'])
        # 点击更多操作，点击清理版本，弹出清理版本弹窗
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]',
                                   文件名称='一级目录')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("清理版本"))
        self.default_content()
        if not self.wait(对话框对象库.弹框标题.format("清除项目版本"), 3):
            raise AssertionError("点击项目的清理项目版本操作按钮，未查看到清理项目版本弹窗")
        # 设置保留版本数，关闭弹窗，版本没有被清理
        self.click(对话框对象库.关闭弹框.format("清除项目版本"))
        self.项目页面.按路径展开目录(目录路径=['清理项目版本', '一级目录'])
        self.click(项目对象库.列表文件名称.format("素材1.png"))
        if not self.wait(项目对象库.文件版本.format("4"), 3):
            raise AssertionError("设置保留版本数为1，关闭清理项目版本弹窗，文件版本还是被清理")
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="清理项目版本")
        self.项目页面.按路径展开目录(目录路径=['清理项目版本'])
        # 设置保留版本数，点击提交，符合要求的版本被清理，设置保留版本数为1时，只保留最新版本
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]',
                                   文件名称='一级目录')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("清理版本"))
        self.default_content()
        self.click(公共元素对象库.增加版本数)
        self.click(对话框对象库.弹框按钮.format("清除项目版本", "提交"))
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"))
        self.项目页面.按路径展开目录(目录路径=['清理项目版本', '一级目录'])
        self.click(项目对象库.列表文件名称.format("素材1.png"))
        if not self.wait(项目对象库.文件版本.format("4"), 3):
            raise AssertionError("设置保留版本数为2，但是倒数第二个版本被清理")
        if self.wait(项目对象库.文件版本.format("3"), 3):
            raise AssertionError("设置保留版本数为2，但是倒数第三个版本未被清理")

    def 清理文件版本(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="清理项目版本")
        self.项目管理页面.创建空白项目(项目名称="清理项目版本", 生命周期名称='系统默认生命周期')
        self.项目管理页面.点击进入项目(项目名称="清理项目版本")
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="清理项目版本")
        素材1 = ['TestData', 'FrontData', '项目页', '素材1.png']
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        素材4 = ['TestData', 'FrontData', '项目页', '素材4.png']
        素材5 = ['TestData', 'FrontData', '项目页', '素材5.png']
        素材6 = ['TestData', 'FrontData', '项目页', '素材6.png']
        self.项目页面.批量上传文件(目录路径=['清理项目版本', '一级目录'], 文件路径列表=[素材1, 素材2, 素材3, 素材4, 素材5,素材6])
        #当文件只有一个版本时，点击清理版本，弹出暂无可清理版本
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]',
                                   文件名称='素材1.png')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("清理版本"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("暂无可清理的版本文件"),3):
            raise AssertionError("文件只有一个版本时，进行清理版本操作，未出现提示信息")
        for filename in ['素材2.jpg', '素材3.jpg']:
            self.项目页面.附加文件(目录路径=['清理项目版本', '一级目录'], 文件名称="素材1.png", 附加文件路径列表=[['清理项目版本', filename]])
        #点击文件行操作，点击清理版本，弹出清理版本弹窗
        # 当文件有大于一个版本时，点击清理，清理版本弹窗列出可清理的版本
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]',
                                   文件名称='素材1.png')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("清理版本"))
        if not self.wait(对话框对象库.弹框标题.format("清理版本"), 3):
            raise AssertionError("存在可清理版本时点击清理版本，未查看到清理版本弹窗")
        if not self.wait(项目对象库.可清理版本.format("1"),3) or not self.wait(项目对象库.可清理版本.format("2"),3):
            raise AssertionError("存在可清理版本时点击清理版本,在清理版本弹窗中未查看到全部可清理版本")
        #勾选可清理版本，点击关闭弹窗，勾选的版本未被清理
        self.click(项目对象库.可清理版本复选框.format("1"))
        self.click(对话框对象库.关闭弹框.format("清理版本"))
        self.click(项目对象库.列表文件名称.format("素材1.png"))
        if not self.wait(项目对象库.文件版本.format("1"), 3):
            raise AssertionError("在清理版本弹窗中勾选版本1后点击关闭清理版本弹窗，文件版本1还是被清理")
        #当有文件版本被其他文件引用时，此版本不能被清理
        self.项目页面.附加文件(目录路径=['清理项目版本', '一级目录'], 文件名称="素材5.png", 附加文件路径列表=[['清理项目版本', '素材1.png']])
        self.项目页面.附加文件(目录路径=['清理项目版本', '一级目录'], 文件名称="素材1.png", 附加文件路径列表=[['清理项目版本', '素材4.png']])
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]',
                                   文件名称='素材1.png')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("清理版本"))
        if self.wait(项目对象库.可清理版本.format("3"),3):
            raise AssertionError("文件版本3被其他文件引用后,在清理版本弹窗中仍然可以查看到版本3")
        #勾选可清理版本，点击取消，勾选的版本未被清理
        self.click(项目对象库.可清理版本复选框.format("1"))
        self.click(对话框对象库.弹框按钮.format("清理版本","取消"))
        self.click(项目对象库.列表文件名称.format("素材1.png"))
        if not self.wait(项目对象库.文件版本.format("1"), 3):
            raise AssertionError("在清理版本弹窗中勾选版本1后点击关闭清理版本弹窗，文件版本1还是被清理")
        #当有文件版本处于生命周期的升版流程节点时，此版本不能被清理
        self.项目页面.改变文件状态(文件名='素材1.png',状态名称='Release')
        self.项目页面.附加文件(目录路径=['清理项目版本', '一级目录'], 文件名称="素材1.png", 附加文件路径列表=[['清理项目版本', '素材5.png']])
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]',
                                   文件名称='素材1.png')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("清理版本"))
        if self.wait(项目对象库.可清理版本.format("4"), 3):
            raise AssertionError("文件版本4生命周期处于升版流程节点,在清理版本弹窗中仍然可以查看到版本4")
        #勾选可清理版本，点击提交，勾选的版本被清理
        self.click(项目对象库.可清理版本复选框.format("1"))
        self.click(对话框对象库.弹框按钮.format("清理版本", "提交"))
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"))
        self.click(项目对象库.列表文件名称.format("素材1.png"))
        if self.wait(项目对象库.文件版本.format("1"), 3):
            raise AssertionError("在清理版本弹窗中勾选版本1后点击提交，文件版本1没有被清理")

    def 文件搜索(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="文件搜索")
        self.项目管理页面.创建空白项目(项目名称="文件搜索", 生命周期名称='系统默认生命周期')
        self.项目管理页面.点击进入项目(项目名称="文件搜索")
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="文件搜索")
        self.项目页面.创建文件目录(目录名称="一级目录2", 目录父节点名称="文件搜索")
        素材1 = ['TestData', 'FrontData', '项目页', '素材1.png']
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        素材4 = ['TestData', 'FrontData', '项目页', '素材4.png']
        素材5 = ['TestData', 'FrontData', '项目页', '素材5.png']
        素材6 = ['TestData', 'FrontData', '项目页', '素材6.png']
        self.项目页面.批量上传文件(目录路径=['文件搜索', '一级目录'], 文件路径列表=[素材1, 素材2, 素材3, 素材4, 素材5, 素材6])
        self.项目页面.批量上传文件(目录路径=['文件搜索', '一级目录2'], 文件路径列表=[素材1, 素材2, 素材3, 素材4, 素材5])
        self.项目页面.按路径展开目录(目录路径=['文件搜索'])
        #文件搜索不支持空值搜索
        self.click(项目对象库.搜索按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("请输入搜索内容"),3):
            raise AssertionError("对文件进行空值搜索时，未出现不能空值搜索的提示信息")
        #文件搜索支持文件名称搜索和文件名称模糊搜索
        self.项目页面.搜索文件(关键词='素材6.png')
        if not self.wait(项目对象库.列表文件名称.format("素材6.png"),3):
            raise AssertionError("项目下进行单个文件搜索，未搜索到指定的文件")
        self.项目页面.搜索文件(关键词='素材')
        list=self.driver.getelements('//table//tr/td[2 or 3]//span[contains(text(),"素材")]')
        if len(list)!=11:
            raise AssertionError("模糊搜索文件，搜索结果数量不正确")
        #不同目录下存在同名文件，搜索时，同名文件也可以显示
        self.项目页面.搜索文件(关键词='素材1.png')
        list = self.driver.getelements('//table//tr/td[2 or 3]//span[contains(text(),"素材")]')
        if len(list) != 2:
            raise AssertionError("不同目录下存在同名文件，搜索时，同名文件没有显示出来")
        #文件搜索支持文件基本属性搜索，如版本、版次、生命周期节点，检入检出状态等
        self.项目页面.按路径展开目录(目录路径=['文件搜索', '一级目录'])
        self.项目页面.改变文件状态(文件名='素材1.png',状态名称='Release')
        self.项目页面.按路径展开目录(目录路径=['文件搜索'])
        self.项目页面.搜索文件(关键词='Release')
        list = self.driver.getelements('//table//tr/td[2 or 3]//span[contains(text(),"素材")]')
        if len(list) != 1:
            raise AssertionError("使用文件生命周期状态搜索文件，未搜索出符合条件的文件")
        self.项目页面.按路径展开目录(目录路径=['文件搜索', '一级目录'])
        self.项目页面.改变文件状态(文件名='素材1.png', 状态名称='Design')
        self.项目页面.按路径展开目录(目录路径=['文件搜索'])
        self.项目页面.搜索文件(关键词='B')
        list = self.driver.getelements('//table//tr/td[2 or 3]//span[contains(text(),"素材")]')
        if len(list) != 1:
            raise AssertionError("使用文件版次搜索文件，未搜索出符合条件的文件")
        self.项目页面.按路径展开目录(目录路径=['文件搜索', '一级目录'])
        self.项目页面.检出资源(资源名称='素材1.png')
        self.项目页面.按路径展开目录(目录路径=['文件搜索'])
        self.项目页面.搜索文件(关键词='检出')
        list = self.driver.getelements('//table//tr/td[2 or 3]//span[contains(text(),"素材")]')
        if len(list) != 1:
            raise AssertionError("使用文件检出状态搜索文件，未搜索出符合条件的文件")
        self.项目页面.搜索文件(关键词='PNG')
        list = self.driver.getelements('//table//tr/td[2 or 3]//span[contains(text(),"素材")]')
        if len(list) != 7:
            raise AssertionError("使用文件类型搜索文件，未搜索出符合条件的文件")
        #文件搜索支持多条件组合搜索
        self.driver.refrsh()
        self.项目页面.按路径展开目录(目录路径=['文件搜索'])
        self.项目页面.搜索文件(关键词='素材 B 检出')
        list = self.driver.getelements('//table//tr/td[2 or 3]//span[contains(text(),"素材")]')
        if len(list) != 1:
            raise AssertionError("使用文件属性组合搜索文件，未搜索出符合条件的文件")

    def 文件归档(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="文件归档")
        self.项目管理页面.创建空白项目(项目名称="文件归档", 生命周期名称='系统默认生命周期')
        self.项目管理页面.点击进入项目(项目名称="文件归档")
        素材1 = ['TestData', 'FrontData', '项目页', '素材1.png']
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        self.项目页面.批量上传文件(目录路径=['文件归档'], 文件路径列表=[素材1, 素材2])
        self.项目页面.检出资源(资源名称='素材2.jpg')
        #点击文件更多操作按钮，点击文件归档选项，归档成功后文件有归档标志
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='素材1.png')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("文件归档"))
        self.wait(公共元素对象库.系统提示信息弹框.format("操作成功"),3)
        if not self.wait(项目对象库.归档按钮.format('素材1.png'), 3):
            raise AssertionError("已归档的文件没有已归档的状态标志")
        #文件不能重复归档
        self.click(项目对象库.悬浮列行操作.format(序号))
        if not self.wait(项目对象库.置灰_行操作选项.format("文件归档"),3):
            raise AssertionError("已归档的文件操作选项中，文件归档按钮未置灰")
        #已归档的文件只能进行打包分享下载和撤销归档操作
        可操作选项=['打包','分享','下载','撤销归档']
        不可操作选项=['圈阅批注','检入','改变状态','附加文件','删除','清理版本','文件归档']
        for 可操作 in 可操作选项:
            if self.wait(项目对象库.置灰_行操作选项.format(可操作选项),3):
                raise AssertionError(f"在已归档文件中{可操作}操作不可用")
        for 不可操作 in 不可操作选项:
            if not self.wait(项目对象库.置灰_行操作选项.format(不可操作),3):
                raise AssertionError(f"在已归档文件中{不可操作}操作可用")
        # 状态为已检出的文件不能进行归档操作
        self.项目页面.刷新列表()
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='素材2.jpg')
        self.click(项目对象库.悬浮列行操作.format(序号))
        if not self.wait(项目对象库.置灰_行操作选项.format("文件归档"),3):
            raise AssertionError("已检出的文件不能进行归档操作")

    def 文件目录归档(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="文件目录归档")
        self.项目管理页面.创建空白项目(项目名称="文件目录归档", 生命周期名称='系统默认生命周期')
        self.项目管理页面.点击进入项目(项目名称="文件目录归档")
        self.项目页面.创建文件目录(目录名称="文件归档", 目录父节点名称="文件目录归档")
        self.项目页面.创建文件目录(目录名称="已检出文件", 目录父节点名称="文件目录归档")
        self.项目页面.创建文件目录(目录名称="空目录", 目录父节点名称="文件目录归档")
        素材1 = ['TestData', 'FrontData', '项目页', '素材1.png']
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        self.项目页面.批量上传文件(目录路径=['文件目录归档', '文件归档'], 文件路径列表=[素材1, 素材2, 素材3])
        self.项目页面.批量上传文件(目录路径=['文件目录归档', '已检出文件'], 文件路径列表=[素材1, 素材2, 素材3])
        self.项目页面.检出资源(资源名称='素材3.jpg')
        self.项目页面.按路径展开目录(目录路径=['文件目录归档'])
        #点击文件目录更多操作，点击文件归档按钮，文件目录下的所有文件都会归档
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='文件归档')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("文件归档"))
        self.wait(公共元素对象库.系统提示信息弹框.format("操作成功"), 3)
        self.项目页面.按路径展开目录(目录路径=['文件目录归档','文件归档'])
        for i in ['素材1.png','素材2.jpg','素材3.jpg']:
            if not self.wait(项目对象库.归档按钮.format(i), 3):
                raise AssertionError(f"已归档的文件{i}没有已归档的状态标志")
        #当文件目录为空时，进行文件归档操作，提示未选择文件
        self.项目页面.按路径展开目录(目录路径=['文件目录归档'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='空目录')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("文件归档"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("未选择文件"), 3):
            raise AssertionError("对空目录进行归档操作，未出现提示信息")
        #当文件目录下存在已检出文件时，进行文件归档操作，不能归档成功
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='已检出文件')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("文件归档"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("存在已被检出文件，不能执行该操作"), 3):
            raise AssertionError("对存在已检出文件的文件目录进行归档操作，未出现提示信息")
        #当文件目录下存在已归档文件时，进行文件归档操作，不能归档成功
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='文件归档')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("文件归档"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("存在已归档文件，不能执行该操作"), 3):
            raise AssertionError("对存在已归档文件的文件目录进行归档操作，未出现提示信息")
        #已归档的文件目录不能进行检出、撤销检出、删除、清理版本、文件归档等操作
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("检出"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("存在已归档文件，不能执行该操作"), 3):
            raise AssertionError("对存在已归档文件的文件目录进行检出操作，未出现提示信息")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("撤销检出"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("存在已归档文件，不能执行该操作"), 3):
            raise AssertionError("对存在已归档文件的文件目录进行撤销检出操作，未出现提示信息")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("删除"))
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("存在已归档文件，不能执行该操作"), 3):
            raise AssertionError("对存在已归档文件的文件目录进行删除操作，未出现提示信息")
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("清理版本"))
        self.click(对话框对象库.弹框按钮.format("清除项目版本", "提交"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("存在已归档文件，不能执行该操作"), 3):
            raise AssertionError("对存在已归档文件的文件目录进行清理版本操作，未出现提示信息")

    def 撤销归档(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="文件归档")
        self.项目管理页面.创建空白项目(项目名称="文件归档", 生命周期名称='系统默认生命周期')
        self.项目管理页面.点击进入项目(项目名称="文件归档")
        素材1 = ['TestData', 'FrontData', '项目页', '素材1.png']
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        self.项目页面.批量上传文件(目录路径=['文件归档'], 文件路径列表=[素材1, 素材2])
        self.项目页面.归档单个文件(文件名称='素材1.png')
        #点击已归档文件更多操作，点击撤销归档按钮，文件的已归档标志消失
        #只有已归档的文件才有撤销归档的操作
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='素材1.png')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("撤销归档"))
        self.wait(公共元素对象库.系统提示信息弹框.format("操作成功"), 3)
        if self.wait(项目对象库.归档按钮.format('素材1.png'), 3):
            raise AssertionError("已归档的文件撤销归档后已归档的状态标志未消失")
        #已归档的文件可以进行全部的文件操作
        self.click(项目对象库.悬浮列行操作.format(序号))
        操作列表=['圈阅批注','检出','撤销检出','改变状态','附加文件','删除','打包','分享','下载','清理版本','文件归档']
        for 操作 in 操作列表:
            if self.wait(项目对象库.置灰_行操作选项.format(操作),3):
                raise AssertionError(f"文件撤销归档后，文件的{操作}操作不可用")

    def 文件目录撤销归档(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="文件目录撤销归档")
        self.项目管理页面.创建空白项目(项目名称="文件目录撤销归档", 生命周期名称='系统默认生命周期')
        self.项目管理页面.点击进入项目(项目名称="文件目录撤销归档")
        self.项目页面.创建文件目录(目录名称="文件归档", 目录父节点名称="文件目录撤销归档")
        self.项目页面.创建文件目录(目录名称="已检出文件", 目录父节点名称="文件目录撤销归档")
        self.项目页面.创建文件目录(目录名称="空目录", 目录父节点名称="文件目录撤销归档")
        素材1 = ['TestData', 'FrontData', '项目页', '素材1.png']
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        self.项目页面.批量上传文件(目录路径=['文件目录撤销归档', '文件归档'], 文件路径列表=[素材1, 素材2, 素材3])
        self.项目页面.批量上传文件(目录路径=['文件目录撤销归档', '已检出文件'], 文件路径列表=[素材1, 素材2, 素材3])
        self.项目页面.归档单个文件(文件名称='素材1.png')
        self.项目页面.归档单个文件(文件名称='素材2.jpg')
        self.项目页面.检出资源(资源名称='素材3.jpg')
        self.项目页面.按路径展开目录(目录路径=['文件目录撤销归档'])
        self.项目页面.归档单个文件(文件名称='文件归档')
        #击文件目录更多操作按钮，点击撤销归档，文件目录下的全部文件都撤销归档
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='文件归档')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("撤销归档"))
        self.wait(公共元素对象库.系统提示信息弹框.format("操作成功"), 3)
        self.项目页面.按路径展开目录(目录路径=['文件目录归档', '文件归档'])
        for i in ['素材1.png', '素材2.jpg', '素材3.jpg']:
            if self.wait(项目对象库.归档按钮.format(i), 3):
                raise AssertionError(f"已归档的文件{i}撤销检出后的已归档的状态标志未消失")
        #当文件目录为空时，进行撤销归档操作，提示未选择文件
        self.项目页面.按路径展开目录(目录路径=['文件目录撤销归档'])
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='空目录')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("撤销归档"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("未选择文件"), 3):
            raise AssertionError("对空目录进行撤销归档操作，未出现提示信息")
        #当文件目录下存在已检出文件时，进行撤销归档操作，不能操作成功
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='已检出文件')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("撤销归档"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("存在未归档文件，不能执行该操作"), 3):
            raise AssertionError("对存在已检出文件的文件目录进行撤销归档操作，未出现提示信息")
        #当文件目录下存在未归档文件时，进行撤销归档操作，不能操作成功
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='文件归档')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("撤销归档"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("存在未归档文件，不能执行该操作"), 3):
            raise AssertionError("对存在未归档文件的文件目录进行撤销归档操作，未出现提示信息")

    def 批量归档(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="批量归档")
        self.项目管理页面.创建空白项目(项目名称="批量归档", 生命周期名称='系统默认生命周期')
        self.项目管理页面.点击进入项目(项目名称="批量归档")
        self.项目页面.创建文件目录(目录名称="文件归档", 目录父节点名称="批量归档")
        self.项目页面.创建文件目录(目录名称="文件归档2", 目录父节点名称="批量归档")
        self.项目页面.创建文件目录(目录名称="已检出文件", 目录父节点名称="批量归档")
        self.项目页面.创建文件目录(目录名称="空目录", 目录父节点名称="批量归档")
        self.项目页面.创建文件目录(目录名称="空目录2", 目录父节点名称="批量归档")
        素材1 = ['TestData', 'FrontData', '项目页', '素材1.png']
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        self.项目页面.批量上传文件(目录路径=['批量归档'], 文件路径列表=[素材1, 素材2,素材3])
        self.项目页面.批量上传文件(目录路径=['批量归档','文件归档'], 文件路径列表=[素材1, 素材2])
        self.项目页面.批量上传文件(目录路径=['批量归档', '文件归档2'], 文件路径列表=[素材1, 素材2])
        self.项目页面.批量上传文件(目录路径=['批量归档', '已检出文件'], 文件路径列表=[素材1, 素材2, 素材3])
        self.项目页面.检出资源(资源名称='素材3.jpg')
        self.项目页面.按路径展开目录(目录路径=['批量归档'])
        #选择多个未归档文件，点击工具栏文件归档按钮，操作成功后，所选文件全部为已归档状态
        self.click(项目对象库.列表复选框.format('素材1.png'))
        self.click(项目对象库.列表复选框.format('素材2.jpg'))
        self.click(项目对象库.工具栏按钮.format('文件归档'))
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"),3)
        if not self.wait(项目对象库.归档按钮.format('素材1.png'), 3) or \
            not self.wait(项目对象库.归档按钮.format('素材2.jpg'), 3):
            raise AssertionError("对文件进行批量归档后，未查看到文件的归档状态")
        #勾选多个文件和文件目录，点击归档按钮，操作成功后，所选文件为已归档状态，所选文件目录下的文件为已归档状态
        self.项目页面.刷新列表()
        self.click(项目对象库.文件目录复选框.format('文件归档'))
        self.click(项目对象库.列表复选框.format('素材3.jpg'))
        self.click(项目对象库.工具栏按钮.format('文件归档'))
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 3)
        if not self.wait(项目对象库.归档按钮.format('素材3.jpg'), 3):
            raise AssertionError("对文件和文件目录进行批量归档后，未查看到文件的归档状态")
        self.项目页面.按路径展开目录(目录路径=['批量归档','文件归档'])
        if not self.wait(项目对象库.归档按钮.format('素材1.png'), 3) or \
            not self.wait(项目对象库.归档按钮.format('素材2.jpg'), 3):
            raise AssertionError("对文件和文件目录进行批量归档后，未查看到文件的归档状态")
        #勾选多个文件目录，文件目录下存在已检出的文件，进行文件归档操作，不能归档成功
        self.项目页面.按路径展开目录(目录路径=['批量归档'])
        self.项目页面.刷新列表()
        self.click(项目对象库.文件目录复选框.format('文件归档2'))
        self.click(项目对象库.文件目录复选框.format('已检出文件'))
        self.click(项目对象库.工具栏按钮.format('文件归档'))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("存在已被检出文件，不能执行该操作"),3):
            raise AssertionError("文件目录下存在已检出文件时，对文件目录进行批量归档，未查看到提示信息")
        #勾选多个文件目录，文件目录下存在已归档的文件，进行文件归档操作，不能归档成功
        self.项目页面.按路径展开目录(目录路径=['批量归档'])
        self.项目页面.刷新列表()
        self.click(项目对象库.文件目录复选框.format('文件归档2'))
        self.click(项目对象库.文件目录复选框.format('文件归档'))
        self.click(项目对象库.工具栏按钮.format('文件归档'))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("存在已归档文件，不能执行该操作"), 3):
            raise AssertionError("文件目录下存在已归档文件时，对文件目录进行批量归档，未查看到提示信息")
        #勾选多个空文件目录，进行归档操作，提示未选择文件
        self.项目页面.按路径展开目录(目录路径=['批量归档'])
        self.项目页面.刷新列表()
        self.click(项目对象库.文件目录复选框.format('空目录'))
        self.click(项目对象库.文件目录复选框.format('空目录2'))
        self.click(项目对象库.工具栏按钮.format('文件归档'))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("未选择文件"), 3):
            raise AssertionError("文件目录为空时，进行批量归档，未查看到提示信息")

    def 批量撤销归档(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="批量撤销归档")
        self.项目管理页面.创建空白项目(项目名称="批量撤销归档", 生命周期名称='系统默认生命周期')
        self.项目管理页面.点击进入项目(项目名称="批量撤销归档")
        self.项目页面.创建文件目录(目录名称="批量撤销归档", 目录父节点名称="批量撤销归档")
        self.项目页面.创建文件目录(目录名称="批量撤销归档2", 目录父节点名称="批量撤销归档")
        self.项目页面.创建文件目录(目录名称="已检出文件", 目录父节点名称="批量撤销归档")
        self.项目页面.创建文件目录(目录名称="空目录", 目录父节点名称="批量撤销归档")
        self.项目页面.创建文件目录(目录名称="空目录2", 目录父节点名称="批量撤销归档")
        素材1 = ['TestData', 'FrontData', '项目页', '素材1.png']
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        self.项目页面.批量上传文件(目录路径=['批量撤销归档'], 文件路径列表=[素材1, 素材2,素材3])
        self.项目页面.批量归档(资源列表=['素材1.png','素材2.jpg','素材3.jpg'])
        self.项目页面.批量上传文件(目录路径=['批量撤销归档','批量撤销归档2'], 文件路径列表=[素材1, 素材2])
        self.项目页面.批量归档(资源列表=['素材1.png', '素材2.jpg'])
        self.项目页面.批量上传文件(目录路径=['批量撤销归档', '批量撤销归档'], 文件路径列表=[素材1, 素材2])
        self.项目页面.批量上传文件(目录路径=['批量撤销归档', '已检出文件'], 文件路径列表=[素材1, 素材2, 素材3])
        self.项目页面.检出资源(资源名称='素材3.jpg')
        self.项目页面.按路径展开目录(目录路径=['批量撤销归档'])
        #勾选多个已归档文件，点击撤销归档按钮，文件被撤销归档
        self.项目页面.刷新列表()
        self.click(项目对象库.列表复选框.format('素材1.png'))
        self.click(项目对象库.列表复选框.format('素材2.jpg'))
        self.click(项目对象库.工具栏按钮.format('撤销归档'))
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"),3)
        if self.wait(项目对象库.归档按钮.format('素材1.png'), 3) or \
            self.wait(项目对象库.归档按钮.format('素材2.jpg'), 3):
            raise AssertionError("对文件进行撤销归档后，仍然查看到文件的归档状态")
        #勾选多个已归档文件和文件目录，点击撤销归档，文件被撤销归档，文件目录下的所有文件被撤销归档
        self.项目页面.刷新列表()
        self.click(项目对象库.文件目录复选框.format('批量撤销归档2'))
        self.click(项目对象库.列表复选框.format('素材3.jpg'))
        self.click(项目对象库.工具栏按钮.format('撤销归档'))
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 3)
        if self.wait(项目对象库.归档按钮.format('素材3.jpg'), 3):
            raise AssertionError("对文件和文件目录进行批量撤销归档后，仍查看到文件的归档状态")
        self.项目页面.按路径展开目录(目录路径=['批量撤销归档','批量撤销归档2'])
        if self.wait(项目对象库.归档按钮.format('素材1.png'), 3) or \
            self.wait(项目对象库.归档按钮.format('素材2.jpg'), 3):
            raise AssertionError("对文件和文件目录进行批量撤销归档后，仍查看到文件的归档状态")
        #勾选多个文件文件目录，文件目录下存在已检出文件，进行撤销归档操作后，不能撤销归档成功
        self.项目页面.按路径展开目录(目录路径=['批量撤销归档'])
        self.项目页面.刷新列表()
        self.click(项目对象库.文件目录复选框.format('批量撤销归档2'))
        self.click(项目对象库.文件目录复选框.format('已检出文件'))
        self.click(项目对象库.工具栏按钮.format('撤销归档'))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("存在未归档文件，不能执行该操作"),3):
            raise AssertionError("文件目录下存在已检出文件时，对文件目录进行批量撤销归档，未查看到提示信息")
        #勾选多个文件目录，文件目录下存在未归档的文件，进行文件撤销归档操作，不能归档成功
        self.项目页面.按路径展开目录(目录路径=['批量撤销归档'])
        self.项目页面.刷新列表()
        self.click(项目对象库.文件目录复选框.format('批量撤销归档2'))
        self.click(项目对象库.文件目录复选框.format('批量撤销归档'))
        self.click(项目对象库.工具栏按钮.format('撤销归档'))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("存在未归档文件，不能执行该操作"), 3):
            raise AssertionError("文件目录下存在未归档文件时，对文件目录进行批量撤销归档，未查看到提示信息")
        #勾选多个空文件目录，进行归档操作，提示未选择文件
        self.项目页面.按路径展开目录(目录路径=['批量撤销归档'])
        self.项目页面.刷新列表()
        self.click(项目对象库.文件目录复选框.format('空目录'))
        self.click(项目对象库.文件目录复选框.format('空目录2'))
        self.click(项目对象库.工具栏按钮.format('撤销归档'))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("未选择文件"), 3):
            raise AssertionError("文件目录为空时，进行批量撤销归档，未查看到提示信息")

    def 目录设置生命周期模板(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="目录设置生命周期模板")
        self.项目管理页面.创建空白项目(项目名称="目录设置生命周期模板", 生命周期名称='系统默认生命周期')
        self.项目管理页面.进入点击项目设置(项目名称='目录设置生命周期模板',项目生命周期模板设置=True)
        已配置生命周期=[]
        elelists=self.driver.getelements(项目设置页面.已配置生命周期列表)
        for ele in elelists:
            已配置生命周期.append(ele.text)
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="目录设置生命周期模板")
        self.项目页面.创建文件目录(目录名称="目录1", 目录父节点名称="目录设置生命周期模板")
        self.项目页面.创建文件目录(目录名称="目录2", 目录父节点名称="目录1")
        self.click(项目对象库.目录节点.format("目录设置生命周期模板"))
        素材1 = ['TestData', 'FrontData', '项目页', '素材1.png']
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        #点击文件目录的更多操作，点击设置，弹出设置弹窗
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='目录1')
        self.click(项目对象库.悬浮列行操作.format(序号))
        if not self.wait(项目对象库.行操作选项.format("设置"),3):
            raise AssertionError("文件目录更多操作中没有文件目录设置选项")
        self.click(项目对象库.行操作选项.format("设置"))
        if not self.wait(对话框对象库.弹框标题.format("设置"),3):
            raise AssertionError("点击文件目录设置选项，未查看到文件目录设置弹框")
        #选择生命周期下拉框，显示项目设置中生命周期模板设置下配置的生命周期模板
        self.click(项目对象库.目录设置.生命周期列表框)
        生命周期列表=[]
        elemlists=self.driver.getelements(公共元素对象库.列表框选项列表)
        for elem in elemlists:
            生命周期列表.append(elem.text)
        if 已配置生命周期!=生命周期列表:
            raise AssertionError("生命周期列表框选项与已配置的生命周期不一致")
        #点击选择对应生命周期，下方显示该生命周期的节点
        self.click(公共元素对象库.列表框选项.format("生命周期"))
        for 节点 in ['11','22','33']:
            if not self.wait(项目对象库.目录设置.生命周期节点.format(节点),3):
                raise AssertionError(f"选择生命周期节点后，未查看到生命周期节点{节点}")
        #子目录不选择生命周期，则自动继承父目录的生命周期设置
        self.click(对话框对象库.关闭弹框.format("设置"))
        self.项目页面.按路径展开目录(目录路径=['目录设置生命周期模板','目录1','目录2'])
        self.项目页面.上传单个文件(目录路径=['批量撤销归档'], 文件路径=素材1)
        elestat1 = self.driver.getelement(项目对象库.生命周期状态.format('素材1.png')).text
        if elestat1 != "11":
            raise AssertionError("子目录不选择生命周期，没有自动继承父目录的生命周期设置")
        self.项目页面.按路径展开目录(目录路径=['目录设置生命周期模板', '目录1'])
        self.项目页面.目录设置生命周期(目录名称='目录2',生命周期名称='切换生命周期')
        self.项目页面.按路径展开目录(目录路径=['目录设置生命周期模板', '目录1', '目录2'])
        self.项目页面.上传单个文件(目录路径=['批量撤销归档'], 文件路径=素材2)
        elestat1 = self.driver.getelement(项目对象库.生命周期状态.format('素材2.jpg')).text
        if elestat1 != "aa":
            raise AssertionError("子目录选择生命周期后，新上传的文件并没有使用新的生命周期")

    def 目录切换生命周期模板(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="目录设切换生命周期模板")
        self.项目管理页面.创建空白项目(项目名称="目录设切换生命周期模板", 生命周期名称='系统默认生命周期')
        self.项目管理页面.进入点击项目设置(项目名称='目录设切换生命周期模板',项目生命周期模板设置=True)
        已配置生命周期=[]
        elelists=self.driver.getelements(项目设置页面.已配置生命周期列表)
        for ele in elelists:
            已配置生命周期.append(ele.text)
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="目录设置生命周期模板")
        self.项目页面.创建文件目录(目录名称="目录1", 目录父节点名称="目录设置生命周期模板")
        self.click(项目对象库.目录节点.format("目录设置生命周期模板"))
        素材1 = ['TestData', 'FrontData', '项目页', '素材1.png']
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        #设置生命周期模板后，切换生命周期模板，则该目录下切换生命周期前已经存在的文件继续使用原来的生命周期、切换生命周期后上传的文件使用最新的生命周期
        self.项目页面.目录设置生命周期(目录名称='目录2', 生命周期名称='生命周期')
        self.项目页面.按路径展开目录(目录路径=['目录设置生命周期模板', '目录1', '目录2'])
        self.项目页面.上传单个文件(目录路径=['批量撤销归档'], 文件路径=素材1)
        self.项目页面.按路径展开目录(目录路径=['目录设置生命周期模板', '目录1'])
        self.项目页面.目录设置生命周期(目录名称='目录2', 生命周期名称='切换生命周期')
        self.项目页面.按路径展开目录(目录路径=['目录设置生命周期模板', '目录1', '目录2'])
        self.项目页面.上传单个文件(目录路径=['批量撤销归档'], 文件路径=素材2)
        elestat1 = self.driver.getelement(项目对象库.生命周期状态.format('素材2.jpg')).text
        if elestat1 != "aa":
            raise AssertionError("目录切换生命周期后，新上传的文件并没有使用新的生命周期")
        self.项目页面.改变文件状态(文件名='素材1.png',状态名称='22')
        elestat1 = self.driver.getelement(项目对象库.生命周期状态.format('素材1.png')).text
        if elestat1 != "22":
            raise AssertionError("切换生命周期模板，则该目录下切换生命周期前已经存在的文件没有继续使用原来的生命周期")

    def 生命周期节点人员管理(self):
        self.权限设置数据准备()
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="权限设置")
        self.项目页面.按路径展开目录(目录路径=['权限设置', '一级目录'])
        self.项目页面.进入目录设置(目录名称="二级目录")
        self.click(项目对象库.目录设置.生命周期列表框)
        self.click(公共元素对象库.列表框选项.format("生命周期"))
        # 进入生命周期tab页，显示当前生命周期的节点信息
        for 节点 in ['11', '22', '33']:
            if not self.wait(项目对象库.目录设置.生命周期节点.format(节点), 3):
                raise AssertionError(f"在项目生命周期控制tab页未查看到{节点}节点")
        self.click(项目对象库.目录设置.添加人员按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("请先选择生命周期节点"), 3):
            raise AssertionError("没有选择生命周期节点，点击添加人员按钮，没有出现提示信息")
        # 点击节点名称，点击添加人员按钮，进入选择人员弹窗
        self.click(项目对象库.目录设置.生命周期节点.format("11"))
        self.click(项目对象库.目录设置.添加人员按钮)
        if not self.wait(对话框对象库.弹框标题.format("选择人员"), 3):
            raise AssertionError("选择生命周期节点后，点击添加人员按钮，未进入到选择人员弹框")
        # 选择人员弹窗内列表显示当前项目的所有项目成员，已经被添加的成员置灰
        if not self.wait(项目对象库.目录设置.未选_成员复选框.format('18942178870'), 3):
            raise AssertionError("选择人员弹框中，未被选择的成员处于不可用状态")
        if not self.wait(项目对象库.目录设置.未选_成员复选框.format('18942178871'), 3):
            raise AssertionError("选择人员弹框中，未被选择的成员处于不可用状态")
        # 选择人员弹窗不选择任何成员，点击确定
        self.click(对话框对象库.弹框按钮.format('选择人员', '确定'))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("请选择人员"), 3):
            raise AssertionError("在人员选择弹窗内，没有选择任何成员，点击确定，没有出现提示信息")
        # 选择成员后，点击关闭选择人员的弹窗，查看成员是否被添加
        self.click(项目对象库.目录设置.未选_成员复选框.format('18942178870'))
        self.click(对话框对象库.关闭弹框.format("选择人员"))
        if self.wait(项目对象库.目录设置.节点下成员.format('18942178871'), 3):
            raise AssertionError("在选择成员弹窗，选择成员后点击关闭弹窗，人员被添加")
        # 选择成员后，点击取消按钮，查看选择的成员是否被添加
        self.click(项目对象库.目录设置.生命周期节点.format("11"))
        self.click(项目对象库.目录设置.添加人员按钮)
        self.wait(对话框对象库.弹框标题.format("选择人员"), 3)
        self.click(项目对象库.目录设置.未选_成员复选框.format('18942178871'))
        self.click(对话框对象库.弹框按钮.format("选择人员", "取消"))
        if self.wait(项目对象库.目录设置.节点下成员.format('18942178871'), 3):
            raise AssertionError("在选择成员弹窗，选择成员后点击取消按钮，人员被添加")
        # 勾选列表中的成员，点击确定，可以在节点的成员列表中查看到新添加的成员
        self.click(项目对象库.目录设置.生命周期节点.format("11"))
        self.click(项目对象库.目录设置.添加人员按钮)
        self.wait(对话框对象库.弹框标题.format("选择人员"), 3)
        self.click(项目对象库.目录设置.未选_成员复选框.format('18942178871'))
        self.click(对话框对象库.弹框按钮.format("选择人员", "确定"))
        if not self.wait(项目对象库.目录设置.节点下成员.format('18942178871'), 3):
            raise AssertionError("在选择成员弹窗，选择成员后点击确定按钮，人员未被添加")
        # 点击成员的移除按钮，人员被移除
        self.click(项目对象库.目录设置.移除成员按钮.format('18942178871'))
        self.wait(公共元素对象库.系统提示信息弹框.format("18942178871"), 3)
        self.click(对话框对象库.删除确认按钮)
        if self.wait(项目对象库.目录设置.节点下成员.format('18942178871'), 3):
            raise AssertionError("进行移除节点成员成功后，节点成员列表仍然能看到被移除的成员")

    def 验证所有人提交后可进入下一节点(self):
        self.权限设置数据准备()
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="权限设置")
        self.项目页面.按路径展开目录(目录路径=['权限设置', '一级目录'])
        self.项目页面.进入目录设置(目录名称="二级目录")
        self.click(项目对象库.目录设置.生命周期列表框)
        self.click(公共元素对象库.列表框选项.format("生命周期"))
        self.项目页面.添加节点人员(节点名称='11', 成员名称='18942178871', 所有人提交后可进入下一节点=False)
        # 所有人提交后进入下一节点按钮关闭时，该节点下成员只要有一个成员完成提交，生命周期就可以进入下个节点
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="权限编辑")
        self.项目页面.改变文件状态(目录路径=['权限编辑', '一级目录', '二级目录'], 文件名='素材2.jpg', 状态名称='22')
        生命周期状态1 = self.driver.getelement(项目对象库.生命周期状态.format('素材2.jpg')).text
        if 生命周期状态1 != '22':
            raise AssertionError("所有人提交后进入下一节点按钮关闭时，该节点下成员下有一个成员完成提交，生命周期未进入下个节点")
        # 所有人提交后进入下一节点按钮开启时，该节点下一个成员提交后，该文件生命周期状态为中间态
        self.项目页面.按路径展开目录(目录路径=['权限设置', '一级目录'])
        self.项目页面.进入目录设置(目录名称="二级目录")
        self.项目页面.添加节点人员(节点名称='11', 所有人提交后可进入下一节点=True)
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="权限编辑")
        self.项目页面.改变文件状态(目录路径=['权限编辑', '一级目录', '二级目录'], 文件名='素材3.jpg', 状态名称='22')
        lines = ''
        elems = self.driver.getelements(项目对象库.生命周期状态.format('素材3.jpg'))
        # for elem in elems:
        #     lines=lines+elem.text
        # if lines!='11 -> 22':
        if len(elems) != 2:
            raise AssertionError("开启所有人提交后可进入下一节点后，改变生命周期状态后，生命周期中间态未出现")
        # 所有人提交后进入下一节点按钮开启时，该节点下一个成员提交后，其他成员未提交的情况下改变生命周期状态
        序号 = self.公共操作.获取文件在列表中的行号(文件名称='素材3.jpg')
        self.click(项目对象库.悬浮列行操作.format(序号))
        self.click(项目对象库.行操作选项.format("改变状态"))
        self.click(项目对象库.行操作选项.format('22'))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("生命周期状态已提交过,不可重复提交"), 3):
            raise AssertionError("开启所有人提交后可进入下一节点后，用户重复操作，未出现提示信息")
        # 所有人提交后进入下一节点按钮开启时，该节点下一个成员提交后。所有人提交后进入下一节点按钮不可被关闭
        self.项目页面.按路径展开目录(目录路径=['权限设置', '一级目录'])
        self.项目页面.进入目录设置(目录名称="二级目录")
        self.click(项目对象库.目录设置.已选_所有人提交后可进入下一节点按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("当前项目中存在文件正处于当前流程节点，不允许操作"), 3):
            raise AssertionError("所有人提交后进入下一节点按钮开启时，该节点下一个成员提交后。所有人提交后进入下一节点按钮可以被关闭")
        # 所有人提交后进入下一节点按钮开启时，该节点下一个成员提交后，切换生命周期，系统给出对应的提示信息
        self.click(公共元素对象库.列表框.format("生命周期"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("当前项目存在正在进行的生命周期流程节点，不允许变更生命周期模板"), 3):
            raise AssertionError("所有人提交后进入下一节点按钮开启时，该节点下一个成员提交后，切换生命周期，系统没有给出对应的提示信息")
        # 所有人提交后进入下一节点按钮开启时，该节点下所有成员都提交后才能进入下个节点
        self.登录页面.退出登录()
        # self.登录页面.短信快捷登录(手机号='18942178871')
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="权限编辑")
        self.项目页面.改变文件状态(目录路径=['权限编辑', '一级目录', '二级目录'], 文件名='素材3.jpg', 状态名称='22')
        生命周期状态1 = self.driver.getelement(项目对象库.生命周期状态.format('素材3.jpg')).text
        if 生命周期状态1 != '22':
            raise AssertionError("所有人提交后进入下一节点按钮开启时，该节点下所有成员都提交后生命周期没有进入下个节点")

    def 验证所有人提交后可进入下一节点(self):
        self.权限设置数据准备()

    def 新增会签(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="新增会签")
        self.项目管理页面.创建空白项目(项目名称="新增会签")
        self.项目管理页面.邀请项目成员(项目名称='新增会签', 当前用户手机号='18942178870', 成员手机号='18942178871', 角色='PROJECT MANAGER')
        self.项目管理页面.点击进入项目(项目名称="新增会签")
        self.wait(项目对象库.目录节点.format("新增会签"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="新增会签")
        self.项目页面.进入目录设置(目录名称="一级目录")
        self.click(项目对象库.目录设置.目录设置tab页.format("会签设置"))
        #在会签tab页，点击新增按钮，弹出新增会签弹窗
        self.click(项目对象库.目录设置.新增会签)
        if not self.wait(对话框对象库.弹框标题.format("新增"),3):
            raise AssertionError("点击会签新增按钮，未弹出会签新增界面")
        #专业&人员空值校验
        self.click(对话框对象库.弹框按钮.format("新增","确定"))
        if not self.wait(公共元素对象库.输入框错误信息提示.format("专业不能为空"),3) or \
            not self.wait(公共元素对象库.输入框错误信息提示.format("请选择人员"),3):
            raise AssertionError("对专业和人员进行空值校验，为弹出正确的提示信息")
        #点击人员，显示项目成员
        self.send_keys(公共元素对象库.输入框.format("专业:"), "金融")
        self.click(公共元素对象库.列表框.format("人员:"))
        if not self.wait(公共元素对象库.列表框选项.format("18942178870"),3) or \
            not self.wait(公共元素对象库.列表框选项.format("18942178871"),3):
            raise AssertionError("人员列表中显示的成员不完整")
        #填写专业和人员后，点击确定，提示操作成功，会签列表中出现新增的会签行
        self.click(公共元素对象库.列表框选项.format("18942178870"))
        self.click(对话框对象库.弹框按钮.format("新增","确定"))
        if not self.wait(项目对象库.目录设置.会签行.format("金融","18942178870"),3):
            raise AssertionError("新增的会签行在会签列表中未查看到")
        #不同人员不同专业可以保存成功
        self.click(项目对象库.目录设置.新增会签)
        self.wait(对话框对象库.弹框标题.format("新增"), 3)
        self.send_keys(公共元素对象库.输入框.format("专业:"), "矿业")
        self.click(公共元素对象库.列表框.format("人员:"))
        self.click(公共元素对象库.列表框选项.format("18942178871"))
        self.click(对话框对象库.弹框按钮.format("新增", "确定"))
        if not self.wait(项目对象库.目录设置.会签行.format("金融", "18942178871"), 3):
            raise AssertionError("不同人员不同专业的会签行没有保存成功")
        # 同一专业不同人员可以保存成功
        self.click(项目对象库.目录设置.新增会签)
        self.wait(对话框对象库.弹框标题.format("新增"), 3)
        self.send_keys(公共元素对象库.输入框.format("专业:"), "金融")
        self.click(公共元素对象库.列表框.format("人员:"))
        self.click(公共元素对象库.列表框选项.format("18942178871"))
        self.click(对话框对象库.弹框按钮.format("新增", "确定"))
        if not self.wait(项目对象库.目录设置.会签行.format("金融","18942178871"),3):
            raise AssertionError("同一专业不同人员的会签行没有保存成功")
        #同一人员不同专业可以保存成功
        self.click(项目对象库.目录设置.新增会签)
        self.wait(对话框对象库.弹框标题.format("新增"), 3)
        self.send_keys(公共元素对象库.输入框.format("专业:"), "能源")
        self.click(公共元素对象库.列表框.format("人员:"))
        self.click(公共元素对象库.列表框选项.format("18942178871"))
        self.click(对话框对象库.弹框按钮.format("新增", "确定"))
        if not self.wait(项目对象库.目录设置.会签行.format("能源", "18942178871"), 3):
            raise AssertionError("同一人员不同专业的会签行没有保存成功")
        #专业&人员重名校验
        self.click(项目对象库.目录设置.新增会签)
        self.wait(对话框对象库.弹框标题.format("新增"), 3)
        self.send_keys(公共元素对象库.输入框.format("专业:"),"金融")
        self.click(公共元素对象库.列表框.format("人员:"))
        self.click(公共元素对象库.列表框选项.format("18942178870"))
        self.click(对话框对象库.弹框按钮.format("新增", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("同专业会签人员重复"),3):
            raise AssertionError("同一专业同一人员新增，未出现提示信息")
        #填写专业和人员后，关闭新增窗口，会签列表中没有出现新增的会签行
        self.click(项目对象库.目录设置.新增会签)
        self.wait(对话框对象库.弹框标题.format("新增"), 3)
        self.send_keys(公共元素对象库.输入框.format("专业:"), "车辆")
        self.click(公共元素对象库.列表框.format("人员:"))
        self.click(公共元素对象库.列表框选项.format("18942178870"))
        self.click(对话框对象库.弹框按钮.format("新增", "取消"))
        if self.wait(项目对象库.目录设置.会签行.format("车辆", "18942178870"), 3):
            raise AssertionError("填写专业和人员后，关闭新增窗口，会签列表中出现了取消新增的会签行")

    def 编辑会签(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="新增会签")
        self.项目管理页面.创建空白项目(项目名称="新增会签")
        self.项目管理页面.邀请项目成员(项目名称='新增会签', 当前用户手机号='18942178870', 成员手机号='18942178871', 角色='PROJECT MANAGER')
        self.项目管理页面.点击进入项目(项目名称="新增会签")
        self.wait(项目对象库.目录节点.format("新增会签"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="新增会签")
        self.项目页面.进入目录设置(目录名称="一级目录")
        self.click(项目对象库.目录设置.目录设置tab页.format("会签设置"))
        self.项目页面.新增会签(专业='金融',人员='18942178870')
        self.项目页面.新增会签(专业='金融', 人员='18942178871')
        self.项目页面.新增会签(专业='地产', 人员='18942178870')
        #点击会签行的编辑按钮，弹出会签编辑弹窗
        self.click(项目对象库.目录设置.编辑会签.format("金融","18942178870"))
        if not self.wait(对话框对象库.弹框标题.format("编辑"), 3):
            raise AssertionError("点击编辑会签，未弹出编辑会签弹窗")
        #对专业和人员进行空值
        self.click(项目对象库.目录设置.编辑会签.format("金融", "18942178870"))
        self.clear(公共元素对象库.输入框.format("专业:"))
        self.click(对话框对象库.弹框按钮.format("编辑", "确定"))
        if not self.wait(公共元素对象库.输入框错误信息提示.format("专业不能为空"),3):
            raise AssertionError("编辑会签行时，专业为空点击保存，未出现提示信息")
        #重名校验
        self.send_keys(公共元素对象库.输入框.format("专业:"),"地产")
        self.click(对话框对象库.弹框按钮.format("编辑", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("同专业会签人员重复"),3):
            raise AssertionError("编辑相同专业，保存会签，未出现提示信息")
        self.click(对话框对象库.弹框按钮.format("编辑", "取消"))
        self.click(项目对象库.目录设置.编辑会签.format("金融", "18942178870"))
        self.click(公共元素对象库.列表框.format("人员:"))
        self.click(公共元素对象库.列表框选项.format("18942178870"))
        self.click(对话框对象库.弹框按钮.format("编辑", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("同专业会签人员重复"), 3):
            raise AssertionError("编辑相同人员，保存会签，未出现提示信息")
        #点击人员，显示项目成员
        self.click(项目对象库.目录设置.编辑会签.format("地产", "18942178871"))
        self.click(公共元素对象库.列表框.format("人员:"))
        if not self.wait(公共元素对象库.列表框选项.format("18942178870"),3) or \
            not self.wait(公共元素对象库.列表框选项.format("18942178871"),3):
            raise AssertionError("编辑会签，点击人员列表框，未查看到项目下成员")
        #编辑专业和人员后，点击确定，提示操作成功，会签列表中出现编辑后的会签行
        self.click(公共元素对象库.列表框选项.format("18942178870"))
        self.clear(公共元素对象库.输入框.format("专业:"))
        self.send_keys(公共元素对象库.输入框.format("专业:"), "能源")
        self.click(对话框对象库.弹框按钮.format("编辑", "确定"))
        if not self.wait(项目对象库.目录设置.编辑会签.format("能源", "18942178870"),3):
            raise AssertionError("编辑专业和人员后，点击保存，未查看到编辑后的会签行")
        #编辑专业和人员后，点击取消，会签列表中没有出现编辑后的会签行
        self.click(项目对象库.目录设置.编辑会签.format("地产", "18942178871"))
        self.clear(公共元素对象库.输入框.format("专业:"))
        self.send_keys(公共元素对象库.输入框.format("专业:"), "能源")
        self.click(对话框对象库.弹框按钮.format("编辑", "取消"))
        if not self.wait(项目对象库.目录设置.编辑会签.format("地产", "18942178871"),3):
            raise AssertionError("编辑专业和人员后，点击取消，未查看到取消编辑的会签行")
        #填写专业和人员后，关闭新增窗口，会签列表中没有出现编辑后的会签行
        self.click(项目对象库.目录设置.编辑会签.format("地产", "18942178871"))
        self.clear(公共元素对象库.输入框.format("专业:"))
        self.send_keys(公共元素对象库.输入框.format("专业:"), "能源")
        self.click(对话框对象库.关闭弹框.format("编辑"))
        if not self.wait(项目对象库.目录设置.编辑会签.format("地产", "18942178871"), 3):
            raise AssertionError("编辑专业和人员后，点击关闭，未查看到取消编辑的会签行")

    def 删除单个会签(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="删除会签")
        self.项目管理页面.创建空白项目(项目名称="删除会签")
        self.项目管理页面.邀请项目成员(项目名称='删除会签', 当前用户手机号='18942178870', 成员手机号='18942178871', 角色='PROJECT MANAGER')
        self.项目管理页面.点击进入项目(项目名称="删除会签")
        self.wait(项目对象库.目录节点.format("删除会签"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="删除会签")
        self.项目页面.进入目录设置(目录名称="一级目录")
        self.click(项目对象库.目录设置.目录设置tab页.format("会签设置"))
        self.项目页面.新增会签(专业='金融',人员='18942178870')
        self.项目页面.新增会签(专业='金融', 人员='18942178871')
        self.项目页面.新增会签(专业='地产', 人员='18942178870')
        #点击会签行删除按钮，弹出删除确认对话框，点击确定，会签行被删除
        self.click(项目对象库.目录设置.删除单个会签.format("金融","18942178870"))
        self.wait(对话框对象库.对话框标题.format("提示"))
        self.click(对话框对象库.对话框按钮.format("提示","确定"))
        if self.wait(项目对象库.目录设置.会签行.format("金融", "18942178870"), 3):
            raise AssertionError("删除的会签行仍然可以在会签列表中查看到")
        #击会签行删除按钮，弹出删除确认对话框，点击取消，会签行没有被删除
        self.click(项目对象库.目录设置.删除单个会签.format("金融", "18942178871"))
        self.wait(对话框对象库.对话框标题.format("提示"))
        self.click(对话框对象库.对话框按钮.format("提示", "取消"))
        if not self.wait(项目对象库.目录设置.会签行.format("金融", "18942178871"), 3):
            raise AssertionError("取消删除的会签行没有在会签列表中查看到")
        #点击会签行删除按钮，弹出删除确认对话框，关闭提示对话框，会签行没有被删除
        self.click(项目对象库.目录设置.删除单个会签.format("金融", "18942178871"))
        self.wait(对话框对象库.对话框标题.format("提示"))
        self.click(对话框对象库.关闭对话框.format("提示"))
        if not self.wait(项目对象库.目录设置.会签行.format("金融", "18942178871"), 3):
            raise AssertionError("取消删除的会签行没有在会签列表中查看到")

    def 批量删除会签(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="删除会签")
        self.项目管理页面.创建空白项目(项目名称="删除会签")
        self.项目管理页面.邀请项目成员(项目名称='删除会签', 当前用户手机号='18942178870', 成员手机号='18942178871', 角色='PROJECT MANAGER')
        self.项目管理页面.点击进入项目(项目名称="删除会签")
        self.wait(项目对象库.目录节点.format("删除会签"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="删除会签")
        self.项目页面.进入目录设置(目录名称="一级目录")
        self.click(项目对象库.目录设置.目录设置tab页.format("会签设置"))
        self.项目页面.新增会签(专业='金融', 人员='18942178870')
        self.项目页面.新增会签(专业='金融', 人员='18942178871')
        self.项目页面.新增会签(专业='地产', 人员='18942178870')
        #批量勾选会签行，点击批量删除按钮，出现删除确认对话框
        self.click(项目对象库.目录设置.会签行复选框.format("金融","18942178870"))
        self.click(项目对象库.目录设置.批量删除会签)
        if not self.wait(对话框对象库.对话框标题.format("提示"),3):
            raise AssertionError("点击批量删除按钮，未出现删除提示对话框")
        #删除确认对话框中点击取消，被删除的会签行没有消失
        self.click(对话框对象库.对话框按钮.format("提示", "取消"))
        if not self.wait(项目对象库.目录设置.会签行.format("金融", "18942178870"), 3):
            raise AssertionError("取消删除的会签行不能在会签列表中查看到")
        #删除确认对话框中点击关闭，被删除的会签行没有消失
        self.click(项目对象库.目录设置.批量删除会签)
        self.wait(对话框对象库.对话框标题.format("提示"))
        self.click(对话框对象库.关闭对话框.format("提示"))
        if not self.wait(项目对象库.目录设置.会签行.format("金融", "18942178870"), 3):
            raise AssertionError("取消删除的会签行没有在会签列表中查看到")
        #删除确认对话框中点击确定，出现删除成功提示，被删除的会签行消失
        self.click(项目对象库.目录设置.批量删除会签)
        self.wait(对话框对象库.对话框标题.format("提示"))
        self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if self.wait(项目对象库.目录设置.会签行.format("金融", "18942178870"), 3):
            raise AssertionError("删除的会签行在会签列表中被查看到")
        #不勾选任何会签行，点击删除，删除按钮不可用
        if not self.wait(项目对象库.目录设置.置灰_批量删除会签,3):
            raise AssertionError("不勾选任何会签行，点击删除，删除按钮可用")

