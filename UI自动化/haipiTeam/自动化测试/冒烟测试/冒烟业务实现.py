import random
from ..基础操作.用户信息页面 import *
from ..基础操作.登录页面 import *
from ..基础操作.滑块验证 import *
from ..元素对象库.登录页 import *
from ..元素对象库.收藏页 import *
from ..基础操作.项目页面 import *
from ..元素对象库.公共元素 import *
from ..基础操作.设置页面 import *
from HNtest.testcasesec.testcasesec import page
from HNtest.Secselenium.secdriver import Secdriver

class 登录页冒烟实现(page):
    def __init__(self,Secdriver = None):
        page.__init__(self,secdriver=Secdriver)
        self.滑块验证=滑块验证(Secdriver=Secdriver)
        self.登录页面 = 登录页面(Secdriver=Secdriver)
        self.用户信息页面 = 用户信息页面(Secdriver=Secdriver)

    def 数据准备(self):
        # 注册账号1:18942178870 pw:user8870
        # self.登录页面.短信快捷登录(手机号='18942178870')
        # self.用户信息页面.进入账号信息页面()
        # self.用户信息页面.维护用户账号信息(用户名='user8870',用户密码='user8870')
        # #注册账号2:18942178871 pw:user0000
        # self.登录页面.退出登录()
        # self.登录页面.短信快捷登录(手机号='18942178871')
        # self.用户信息页面.进入账号信息页面()
        # self.用户信息页面.维护用户账号信息(用户名='user8871', 用户密码='user0000')
        pass

    def 短信快捷登录(self):
        self.default_content()
        self.clear(登录页对象库.手机号输入框)
        self.send_keys(登录页对象库.手机号输入框, '18942178870')
        self.click(登录页对象库.验证码按钮)
        self.default_content()
        self.滑块验证.滑块验证操作()
        self.wait(登录页对象库.开始使用, 30)
        self.click(登录页对象库.验证码输入框)
        self.clear(登录页对象库.验证码输入框)
        self.send_keys(登录页对象库.验证码输入框, '888888')
        self.click(登录页对象库.开始使用)
        self.default_content()
        if not self.wait('//div[@id="project"]', 3):
            raise AssertionError("输入正确手机号和验证码，未进入到项目首页")

    def 账号密码登录(self):
        self.default_content()
        self.click(登录页对象库.账号密码登录)
        if not self.wait(登录页对象库.账号输入框,3):
            raise AssertionError("在短信快捷登录页点击账号密码登录按钮，页面未切换到账号密码登录页")
        self.click(登录页对象库.账号输入框)
        self.clear(登录页对象库.账号输入框)
        self.send_keys(登录页对象库.账号输入框, 'user8870')
        self.click(登录页对象库.密码输入框)
        self.clear(登录页对象库.密码输入框)
        self.send_keys(登录页对象库.密码输入框,'user@8870')
        self.click(登录页对象库.登录按钮)
        self.default_content()
        self.滑块验证.滑块验证操作()
        self.default_content()
        if not self.wait('//div[@id="project"]', 3):
            raise AssertionError("输入账号和密码登录，未进入到项目首页")

    def 忘记密码(self):
        num = random.randint(1000, 9999)
        self.default_content()
        self.click(登录页对象库.账号密码登录)
        self.click(登录页对象库.短信快捷登录)
        self.default_content()
        if not self.wait(登录页对象库.账号密码登录, 3):
            raise AssertionError("在账号密码登录页点击短信快捷登录按钮，页面自动跳转到短信快捷登录页")
        self.click(登录页对象库.账号密码登录)
        self.wait(登录页对象库.忘记密码, 30)
        self.click(登录页对象库.忘记密码)
        self.wait(登录页对象库.忘记密码对象库.重置密码弹窗标题, 30)
        self.clear(登录页对象库.手机号输入框)
        self.send_keys(登录页对象库.手机号输入框, '18942178871')
        self.click(登录页对象库.验证码按钮)
        self.default_content()
        self.滑块验证.滑块验证操作()
        self.wait(登录页对象库.验证码输入框, 30)
        self.clear(登录页对象库.验证码输入框)
        self.send_keys(登录页对象库.验证码输入框, '888888')
        self.click(登录页对象库.忘记密码对象库.重置密码按钮)
        self.clear(登录页对象库.忘记密码对象库.密码输入框)
        self.send_keys(登录页对象库.忘记密码对象库.密码输入框,"user@"+str(num))
        self.clear(登录页对象库.忘记密码对象库.确认密码输入框)
        self.send_keys(登录页对象库.忘记密码对象库.确认密码输入框, "user@"+str(num))
        self.click(登录页对象库.忘记密码对象库.提交按钮)
        self.default_content()
        self.wait(公共元素对象库.系统提示信息弹框.format("重置成功,请重新登录"), 30)
        self.clear(登录页对象库.账号输入框)
        self.send_keys(登录页对象库.账号输入框, 'user8871')
        self.clear(登录页对象库.密码输入框)
        self.send_keys(登录页对象库.密码输入框, "user@" + str(num))
        self.click(登录页对象库.登录按钮)
        self.default_content()
        self.滑块验证.滑块验证操作()
        self.default_content()
        if not self.wait('//div[@id="project"]', 5):
            raise AssertionError("被重置的密码无法登录到系统")


class 用户信息冒烟实现(page):
    def __init__(self,Secdriver = None):
        page.__init__(self,secdriver=Secdriver)
        self.用户信息页面=用户信息页面(Secdriver=Secdriver)
        self.滑块验证 = 滑块验证(Secdriver=self.driver)
        self.登录页面 = 登录页面(Secdriver=self.driver)
    def 数据准备(self):
        #创建用户18942178870 pw:user8870 name:user8870 绑定邮箱123456@qq.com
        self.登录页面.退出登录()
        self.登录页面.忘记密码(手机号='18942178871',验证码='888888',新密码='user@8871')

    def 用户基本信息维护(self):
        self.用户信息页面.进入基本信息页面()
        # 点击更换头像，选择头像图片，点击确定
        self.用户信息页面.更换头像(文件路径=['TestData', 'FrontData', '用户信息', '头像.png'])
        if self.wait(公共元素对象库.系统提示信息弹框.format("请上传图片类型"), 3):
            raise AssertionError("头像上图片文件，系统现提示信息")
        time.sleep(3)
        self.clear(公共元素对象库.输入框.format("用户昵称"))
        self.send_keys(公共元素对象库.输入框.format("用户昵称"), "user8870")
        self.click(公共元素对象库.列表框.format("国家"))
        if not self.wait(公共元素对象库.列表框选项.format("中国"), 3):
            raise AssertionError("点击国家列表框，未发现对应的列表框选项")
        self.click(公共元素对象库.列表框选项.format("中国"))
        # 输入对应合法信息后点击保存，系统提示保存成功
        self.clear(用户信息对象库.基本信息对象库.姓输入框)
        self.send_keys(用户信息对象库.基本信息对象库.姓输入框, "admin")
        self.clear(用户信息对象库.基本信息对象库.名输入框)
        self.send_keys(用户信息对象库.基本信息对象库.名输入框, "admin")
        self.clear(公共元素对象库.输入框.format("职位"))
        self.send_keys(公共元素对象库.输入框.format("职位"), "用户职位")
        self.clear(公共元素对象库.输入框.format("办公电话"))
        self.send_keys(公共元素对象库.输入框.format("办公电话"), "12345678901")
        self.clear(公共元素对象库.输入框.format("办公地址"))
        self.send_keys(公共元素对象库.输入框.format("办公地址"), "办公地址")
        self.clear(公共元素对象库.输入框.format("公司名称"))
        self.send_keys(公共元素对象库.输入框.format("公司名称"), "公司名称")
        self.clear(公共元素对象库.输入框.format("城市"))
        self.send_keys(公共元素对象库.输入框.format("城市"), "城市")
        # 省/市/自治区下拉校验
        self.click(公共元素对象库.列表框.format("省/直辖市/自治区"))
        if not self.wait(公共元素对象库.列表框选项.format("上海"), 3):
            raise AssertionError("点击省/直辖市/自治区列表框，未发现对应的列表框选项")
        self.click(公共元素对象库.列表框选项.format("上海"))
        self.clear(公共元素对象库.输入框.format("邮编"))
        self.send_keys(公共元素对象库.输入框.format("邮编"), "123456")
        # 合法信息点击保存是否保存成功
        flage = True
        self.move_to_by_pyautogui(用户信息对象库.基本信息对象库.更改头像按钮, y_offset=0)
        while (flage):
            try:
                flage = False
                self.click(用户信息对象库.账号信息对象库.保存)
            except:
                flage = True
                self.scroll_by_pyautogui(-5)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("保存成功"), 3):
            raise AssertionError("当用户信息输入合法时点击保存，系统未出现保存成功提示信息")

    def 账号信息维护(self):
        self.登录页面.退出登录()
        # self.登录页面.短信快捷登录(手机号='18942178871')
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.用户信息页面.进入账号信息页面()
        #点击修改密码按钮，弹出修改密码对话框
        self.click(用户信息对象库.账号信息对象库.修改密码按钮)
        self.default_content()
        if not self.wait(对话框对象库.弹框标题.format('修改密码'),3):
            raise AssertionError("点击修改密码按钮，未弹出修改密码弹窗")
        self.send_keys(公共元素对象库.输入框.format("当前密码"),'user@8871')
        self.send_keys(公共元素对象库.输入框.format("新密码"), 'user@8888')
        self.send_keys(公共元素对象库.输入框.format("确认密码"), 'user@8888')
        self.click(对话框对象库.对话框按钮.format("修改密码","保存"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("保存成功"),3):
            raise AssertionError("修改密成功后未出现提示信息")
        self.登录页面.退出登录()
        self.default_content()
        self.click(登录页对象库.账号密码登录)
        #使用手机号
        self.send_keys(登录页对象库.账号输入框, "18942178871")
        self.click(登录页对象库.密码输入框)
        self.clear(登录页对象库.密码输入框)
        self.send_keys(登录页对象库.密码输入框, "user@8888")
        self.click(登录页对象库.登录按钮)
        self.default_content()
        self.滑块验证.滑块验证操作()
        self.default_content()
        if not self.wait(首页对象库.项目, 30):
            raise AssertionError("用户账号信息维护成功后，不能使用手机号密码登录")
        #邮箱登录系统
        self.登录页面.退出登录()
        self.default_content()
        self.click(登录页对象库.账号密码登录)
        self.send_keys(登录页对象库.账号输入框, "2503209673@qq.com")
        self.send_keys(登录页对象库.密码输入框, "user@8888")
        self.click(登录页对象库.登录按钮)
        self.default_content()
        self.滑块验证.滑块验证操作()
        self.default_content()
        if not self.wait(首页对象库.项目, 30):
            raise AssertionError("用户账号信息维护成功后，不能使用邮箱密码登录")
        #用户名
        self.登录页面.退出登录()
        self.default_content()
        self.click(登录页对象库.账号密码登录)
        self.send_keys(登录页对象库.账号输入框, "user8871")
        self.send_keys(登录页对象库.密码输入框, "user@8888")
        self.click(登录页对象库.登录按钮)
        self.default_content()
        self.滑块验证.滑块验证操作()
        self.default_content()
        if not self.wait(首页对象库.项目, 30):
            raise AssertionError("用户账号信息维护成功后，不能使用用户名密码登录")


class 项目页冒烟实现(page):
    def __init__(self,Secdriver = None):
        page.__init__(self,secdriver=Secdriver)
        self.公共操作=公共操作(Secdriver=Secdriver)
        self.登录页面 = 登录页面(Secdriver=Secdriver)
        self.用户信息页面 = 用户信息页面(Secdriver=Secdriver)
        self.项目管理页面 = 项目管理页面(Secdriver=Secdriver)
        self.项目页面 = 项目页面(Secdriver=Secdriver)
        self.进入到操作位置 = 进入到操作位置(Secdriver=Secdriver)
        self.生命周期管理页面 = 生命周期管理页面(Secdriver=Secdriver)
        self.版次管理页面 = 版次管理页面(Secdriver=Secdriver)
        self.属性管理页面 = 属性管理页面(Secdriver=Secdriver)
        self.项目设置页面 = 项目管理页面.项目设置页面(Secdriver=Secdriver)


    def 数据准备(self):
        self.项目管理页面.删除所有项目()
        self.登录页面.退出登录()
        # self.登录页面.短信快捷登录(手机号='18942178871')
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        self.用户信息页面.进入基本信息页面()
        self.用户信息页面.维护用户基本信息(用户昵称='18942178871')
        self.登录页面.退出登录()
        # self.登录页面.短信快捷登录(手机号='18942178870')
        self.登录页面.账号密码登录(账号='18942178870', 密码='user@8870')
        self.用户信息页面.进入基本信息页面()
        self.用户信息页面.维护用户基本信息(用户昵称='18942178870')
        self.进入到操作位置.进入生命周期工作区()
        self.生命周期管理页面.删除生命周期('生命周期')
        self.生命周期管理页面.删除生命周期('切换生命周期')
        self.生命周期管理页面.进入新增生命周期弹框(生命周期名称='生命周期')
        self.生命周期管理页面.添加生命周期节点(节点名称='11')
        self.生命周期管理页面.添加生命周期节点(节点名称='22')
        self.生命周期管理页面.添加生命周期节点(节点名称='33')
        self.生命周期管理页面.设置升版流程(节点名称='11', 开始节点='11', 结束节点='22')
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
        self.进入到操作位置.进入属性工作区()
        self.属性管理页面.创建属性系统(属性系统名称='属性')
        self.属性管理页面.创建属性系统(属性系统名称='切换属性')

    def 获取文件大小(self,文件路径):
        fsize=os.path.getsize(文件路径)
        return fsize

    def 收藏页清理所有收藏(self):
        while(True):
            if self.wait('//tr/td//i[contains(@class,"icon-shoucang shoucang-yellow")]',3):
                self.click('//tr/td//i[contains(@class,"icon-shoucang shoucang-yellow")]')
            else:
                break


####################以下为业务实现方法########################

    def 创建空白项目(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="创建项目1")
        self.click(项目管理对象库.创建新项目)
        self.wait(创建项目页面.页面名称,3)
        self.click(创建项目页面.创建空白项目)
        self.wait(对话框对象库.弹框标题.format("项目名称"),3)
        self.clear(公共元素对象库.输入框.format("项目名称"))
        self.send_keys(公共元素对象库.输入框.format("项目名称"),"创建项目1")
        self.click(创建项目页面.提交按钮)
        self.default_content()
        if not self.wait(项目设置页面.项目成员tab页,3):
            raise AssertionError("创建项目后没有自动跳转到项目设置页面")
        self.进入到操作位置.进入项目管理页()
        if not self.wait(项目管理对象库.项目卡片.format("创建项目1"),3):
            raise AssertionError("项目创建成功后，在项目管理页面未查看到新创建的项目的卡片")

    def 邀请项目成员(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="邀请成员项目")
        self.项目管理页面.创建空白项目(项目名称="邀请成员项目")
        #点击项目详情按钮，悬浮显示项目名称、创建人、创建日期、团队人数、文件数量、项目状态、备注等信息
        self.click(项目管理对象库.项目详情按钮.format("邀请成员项目"))
        if not self.wait('//div/span[text()="项目名称:"]/following-sibling::span[text()="邀请成员项目"]',3):
            raise AssertionError("点击查看项目详情，项目详情弹窗未出现")
        #点击项目成员按钮，在悬浮页点击添加成员按钮，弹出项目协作弹窗
        self.click(项目管理对象库.项目成员按钮.format("邀请成员项目"))
        self.default_content()
        self.click(项目管理对象库.添加项目成员)
        if not self.wait(对话框对象库.弹框标题.format("项目协作"),3):
            raise AssertionError("点击添加项目成员，项目协作弹框未出现")
        self.click(公共元素对象库.列表框.format("角色"))
        self.公共操作.滚动选择列表框选项(选项名称="PROJECT MANAGER")
        self.click(对话框对象库.弹框按钮.format("项目协作","复制链接"))
        self.click(对话框对象库.关闭弹框.format("项目协作"))
        链接=self.公共操作.获取剪切板内容()
        self.登录页面.退出登录()
        # self.登录页面.短信快捷登录(手机号='18942178871')
        self.登录页面.账号密码登录(账号='18942178871', 密码='user@8871')
        #新开标签页
        self.driver.driver.execute_script("window.open('');")
        self.switch_to_new_window()
        self.driver.driver.get(链接)
        time.sleep(3)
        #打开链接，可以查看到配置的信息，点击加入，项目成员可以看到加入的项目
        self.click(对话框对象库.对话框按钮2.format("邀请你参加“邀请成员项目”","加入"))
        if not self.wait(项目对象库.目录节点.format("邀请成员项目"),3):
            raise AssertionError("成员加入项目后，没有跳转到项目内容页面")
        self.进入到操作位置.进入项目管理页()
        #点击项目成员按钮，悬浮显示项目成员用户名列表
        self.click(项目管理对象库.项目成员按钮.format("邀请成员项目"))
        if not self.wait(项目管理对象库.项目成员名称.format("18942178870"),5) or not self.wait(项目管理对象库.项目成员名称.format("18942178871"),5):
            raise AssertionError("点击项目成员按钮，未查看到当前项目多有的项目成员")

    def 移除项目成员(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="移除成员项目")
        self.项目管理页面.创建空白项目(项目名称="移除成员项目")
        self.项目管理页面.邀请项目成员(项目名称='移除成员项目',当前用户手机号='18942178870',成员手机号='18942178871',角色='PROJECT MANAGER')
        self.click(项目管理对象库.项目成员按钮.format("移除成员项目"))
        self.click(项目管理对象库.移除项目成员.format("18942178871"))
        self.wait(公共元素对象库.系统提示信息弹框.format("操作成功"),3)
        self.click(项目管理对象库.项目成员按钮.format("移除成员项目"))
        if self.wait(项目管理对象库.移除项目成员.format("18942178871"),3):
            raise AssertionError("执行项目成员移除操作后，项目成员列表内仍然能看到被移除的成员")

    def 删除项目(self):
        self.进入到操作位置.进入项目管理页()
        #创建项目
        if not self.wait(项目管理对象库.项目卡片.format("删除项目1"), 3):
            self.项目管理页面.创建空白项目(项目名称="删除项目1")
        self.click(项目管理对象库.更多操作按钮.format("删除项目1"))
        self.click(项目管理对象库.更多操作选项.format("删除项目"))
        self.default_content()
        if not self.wait(对话框对象库.对话框标题.format("提示"), 3):
            raise AssertionError("点击删除项目，未查看到删除确认的对话框")
        self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("删除"), 3)
        if self.wait(项目管理对象库.项目卡片.format("删除项目1"), 3):
            raise AssertionError("删除项目成功后项目管理页面仍然能查看到被删除项目卡片")

    def 查看项目动态(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="查看项目动态")
        self.项目管理页面.创建空白项目(项目名称="查看项目动态")
        self.项目管理页面.邀请项目成员(项目名称='查看项目动态',当前用户手机号='18942178870',成员手机号='18942178871',角色='PROJECT MANAGER')
        self.项目管理页面.移除项目成员(项目名称="查看项目动态",移除成员名称="18942178871")
        self.click(项目管理对象库.更多操作按钮.format("查看项目动态"))
        self.click(项目管理对象库.更多操作选项.format("项目动态"))
        if not self.wait(项目管理对象库.项目动态页.项目动态页标题,3):
            raise AssertionError("点击项目动态未跳转到项目动态页面")
        if not self.wait(项目管理对象库.项目动态页.操作1.format("18942178870 创建了"),3) or not \
                self.wait(项目管理对象库.项目动态页.操作1.format("18942178870  邀请了"),3):
            raise AssertionError("项目动态内容显示有误")

    def 存为模板(self):
        self.项目管理页面.删除项目(项目名称="存为模板")
        self.项目管理页面.创建空白项目(项目名称="存为模板")
        self.项目管理页面.邀请项目成员(项目名称='存为模板', 当前用户手机号='18942178870', 成员手机号='18942178871',角色='PROJECT MANAGER')
        self.项目管理页面.点击进入项目(项目名称="存为模板")
        self.wait(项目对象库.目录节点.format("存为模板"), 3)
        self.driver.refrsh()
        # 创建文件目录
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="存为模板")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        # 上传文件
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        self.click(项目对象库.目录节点.format("一级目录"))
        self.项目页面.批量上传文件(目录路径=['存为模板', '一级目录'], 文件路径列表=[素材2, 素材3])
        self.项目管理页面.删除项目模板(模板名称='保存模板冒烟')
        self.项目管理页面.删除项目模板(模板名称='保存模板2')
        self.进入到操作位置.进入项目管理页()
        self.click(项目管理对象库.更多操作按钮.format("存为模板"))
        self.click(项目管理对象库.更多操作选项.format("存为模板"))
        self.wait(对话框对象库.弹框标题.format("存为模板"), 3)
        self.send_keys(公共元素对象库.输入框.format("模板名称"),"保存模板冒烟")
        self.click(公共元素对象库.单选按钮.format("保留团队成员"))
        self.click(公共元素对象库.单选按钮.format("保留项目文件"))
        self.click(对话框对象库.弹框按钮.format("存为模板","确定"))
        #勾选保留团队成员，保存模板，查看保存的模板的项目成员tab页
        self.click(项目管理对象库.创建新项目)
        self.click(创建项目页面.预览.format("保存模板冒烟"))
        if not self.wait(创建项目页面.节点展开按钮.format("保存模板冒烟"), 3):
            raise AssertionError("保存的项目模板的项目结构未保存")
        self.click(创建项目页面.节点展开按钮.format("保存模板冒烟"))
        if not self.wait(创建项目页面.节点展开按钮.format("一级目录"), 3):
            raise AssertionError("保存的项目模板的项目结构未保存")
        self.click(创建项目页面.节点展开按钮.format("一级目录"))
        if not self.wait(创建项目页面.节点名称.format("二级目录"), 3):
            raise AssertionError("保存的项目模板的项目结构未保存")
        self.click(创建项目页面.模板tab页.format("团队成员"))
        if not self.wait(创建项目页面.模板团队成员.format("18942178870", "INDIVIDUAL ADMINISTRATOR"), 3) or not \
                self.wait(创建项目页面.模板团队成员.format("18942178871", "ENTERPRISE MANAGER"), 3):
            raise AssertionError("保存模板时勾选保存项目成员，预览模板时项目成员没有被保存")
        self.click(对话框对象库.关闭弹框.format("模板预览"))
        #使用模板创建项目，查看模板下的文件和成员是否存在
        self.click(创建项目页面.使用.format("保存模板冒烟"))
        self.wait(对话框对象库.弹框标题.format("项目名称"), 3)
        self.send_keys(公共元素对象库.输入框.format("项目名称"),"项目模板冒烟")
        self.click(创建项目页面.提交按钮)
        if not self.wait(项目管理对象库.项目卡片.format("项目模板冒烟"), 3):
            raise AssertionError("使用项目模板创建项目失败")
        self.click(项目管理对象库.项目成员按钮.format("项目模板冒烟"))
        if not self.wait(项目管理对象库.移除项目成员.format("18942178871"), 3) or not self.wait(项目管理对象库.移除项目成员.format("18942178870"), 3):
            raise AssertionError("使用项目模板创建项目，项目中的项目成员未被保存")
        self.项目管理页面.点击进入项目(项目名称="项目模板冒烟")
        self.项目页面.按路径展开目录(目录路径=['项目模板冒烟','一级目录'])
        for i in ['二级目录','素材2.jpg','素材3.jpg']:
            if not self.wait(项目对象库.列表文件名称.format(i),3):
                raise AssertionError(f"使用项目模板创建项目后，模板中的文件：{i}在新项目中不存在")

    def 项目设置操作(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="项目设置")
        self.项目管理页面.删除项目(项目名称="更改项目名称")
        self.项目管理页面.创建空白项目(项目名称="项目设置")
        self.click(项目管理对象库.更多操作按钮.format("项目设置"))
        self.click(项目管理对象库.更多操作选项.format("项目设置"))
        self.clear(公共元素对象库.输入框.format("项目名称"))
        self.send_keys(公共元素对象库.输入框.format("项目名称"), "更改项目名称")
        self.clear(公共元素对象库.文本框.format("项目简介"))
        self.send_keys(公共元素对象库.文本框.format("项目简介"), "项目简介")
        self.click(项目设置页面.项目成员tab页)
        self.进入到操作位置.进入项目管理页()
        self.wait(公共元素对象库.系统提示信息弹框.format("修改成功"), 3)
        if not self.wait(项目管理对象库.项目卡片.format("更改项目名称"), 3):
            raise AssertionError("在项目修改页面修改项目名称，修改成功后未查看到被修改的项目卡片")
        self.click(项目管理对象库.项目详情按钮.format("更改项目名称"))
        if not self.wait('//div/span[text()="备注:"]/following-sibling::span[contains(text(),"项目简介")]',3):
            raise AssertionError("点击查看项目详情，未查看到被修改的项目简介")
        self.项目管理页面.进入点击项目设置(项目名称='更改项目名称')
        self.click(项目设置页面.收藏按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("收藏成功"),3):
            raise AssertionError("设置页点击收藏成功后，未出现收藏成功提示信息")
        self.进入到操作位置.进入收藏页()
        if not self.wait(收藏对象库.收藏资源名称.format("更改项目名称"),3):
            raise AssertionError("在设置页点击收藏项目，在收藏页未查看到对应的项目")
        self.项目管理页面.进入点击项目设置(项目名称='更改项目名称')
        self.click(项目设置页面.查看项目目录)
        if not self.wait(项目对象库.目录节点.format("更改项目名称"),3):
            raise AssertionError("在项目页点击查看项目目录按钮后，页面未跳转到项目文件目录页面")
        self.项目管理页面.进入点击项目设置(项目名称='更改项目名称')
        self.click(项目设置页面.收藏按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("取消收藏成功"), 3):
            raise AssertionError("设置页点击取消收藏成功后，未出现取消收藏成功提示信息")
        self.进入到操作位置.进入收藏页()
        if self.wait(收藏对象库.收藏资源名称.format("更改项目名称"), 3):
            raise AssertionError("在设置页点击取消收藏项目，在收藏页还能查看到对应的项目")
        self.项目管理页面.进入点击项目设置(项目名称='更改项目名称')
        self.click(项目设置页面.删除项目)
        if not self.wait(对话框对象库.对话框标题.format("提示"),3):
            raise AssertionError("在设置页点击删除项目，未出现删除确认对话框")
        self.click(对话框对象库.对话框按钮.format("提示","确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("删除成功"),3)
        self.进入到操作位置.进入项目管理页()
        if self.wait(项目管理对象库.项目卡片.format("更改项目名称"), 3):
            raise AssertionError("在项目设置页点击删除项目，删除成功后仍然可以查看到该项目的卡片")

    def 切换生命周期(self):
        self.进入到操作位置.进入设置页()
        self.进入到操作位置.进入生命周期工作区()
        生命周期lists = []
        elements = self.driver.getelements("//table//tr/td[2]//span[1]")
        for element in elements:
            生命周期lists.append(element.text)
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="切换生命周期")
        self.项目管理页面.创建空白项目(项目名称="切换生命周期", 生命周期名称='切换生命周期')
        # 点击生命周期下拉列表，列表显示所有的生命周期模板，选择对应的生命周期设置
        self.click(项目管理对象库.更多操作按钮.format("切换生命周期"))
        self.click(项目管理对象库.更多操作选项.format("项目设置"))
        self.click(公共元素对象库.列表框.format("生命周期"))
        列表框list = self.driver.getelements('//ul/li[contains(@class,"dropdown__item")]/span')
        for 列表框 in 列表框list:
            if 列表框.text not in 生命周期lists or len(生命周期lists) != len(列表框list):
                raise AssertionError(f"{列表框.text}不在生命周期列表中")
        # 空白项目点击切换生命周期可以直接切换
        self.公共操作.滚动选择列表框选项(选项名称='生命周期')
        self.click(公共元素对象库.列表框.format("生命周期"))
        if not self.wait('//ul/li[contains(@class,"el-select-dropdown__item selected")]/span[text()="生命周期"]', 3):
            raise AssertionError("空白项目点击切换生命周期没有直接切换")
        # 如果项目中已经存在文件，点击切换生命周期时会弹出修改生命周期预览弹窗
        self.click(项目设置页面.查看项目目录)
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="切换生命周期")
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        self.click(项目对象库.目录节点.format("一级目录"))
        self.项目页面.批量上传文件(目录路径=['查看项目动态', '一级目录'], 文件路径列表=[素材2, 素材3])
        self.进入到操作位置.进入项目管理页()
        self.click(项目管理对象库.更多操作按钮.format("切换生命周期"))
        self.click(项目管理对象库.更多操作选项.format("项目设置"))
        self.click(公共元素对象库.列表框.format("生命周期"))
        self.公共操作.滚动选择列表框选项(选项名称='切换生命周期')
        if not self.wait(对话框对象库.弹框标题.format("修改生命周期预览"), 3):
            raise AssertionError("如果项目中已经存在文件，点击切换生命周期时没有弹出修改生命周期预览弹窗")
        if not self.wait(项目设置页面.当前节点名称.format("11")) or not self.wait(项目设置页面.当前节点名称.format("22")):
            raise AssertionError("修改生命周期预览弹窗中列表没有显示当前生命周期的全部节点")
        self.click(项目设置页面.变更节点列表框.format("11"))
        节点elems=self.driver.getelements('//ul/li[contains(@class,"dropdown__item")]/span')
        for 节点 in 节点elems:
            if 节点.text not in ['aa','bb'] or len(节点elems)!=2:
                raise AssertionError("点击变更后节点名称下拉列表，列表框中没有显示目标生命周期的全部节点")
        self.click(项目设置页面.变更节点列表框.format("11"))
        self.click(公共元素对象库.列表框选项.format("aa"))
        self.click(项目设置页面.变更节点列表框.format("22"))
        self.click(公共元素对象库.列表框选项.format("bb"))
        self.click(项目设置页面.变更节点列表框.format("33"))
        self.click(公共元素对象库.列表框选项.format("aa"))
        self.click(对话框对象库.弹框按钮.format("修改生命周期预览", "确定"))
        self.click(公共元素对象库.列表框.format("生命周期"))
        if not self.wait('//ul/li[contains(@class,"el-select-dropdown__item selected")]/span[text()="切换生命周期"]', 3):
            raise AssertionError("进行生命周期节点变更操作后，点击确定按钮，项目生命周期没有变更")

    def 切换版次(self):
        self.进入到操作位置.进入设置页()
        self.进入到操作位置.进入版次工作区()
        版次lists = []
        elements = self.driver.getelements("//table//tr/td[2]//span[1]")
        for element in elements:
            版次lists.append(element.text)
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="切换版次")
        self.项目管理页面.创建空白项目(项目名称="切换版次", 版次名称='切换版次')
        # 点击版次下拉列表，列表显示所有的版次模板，选择对应的版次
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
        # 修改版次预览弹窗列表显示当前与使用版次和变更后对应版次的信息
        if not self.wait('//div[text()="A"]/ancestor::tr/td[last()]/div[text()="E"]', 3):
            raise AssertionError("修改版次弹框显示版次变更选项不正确")
        self.wait(对话框对象库.弹框标题.format("修改版次预览"), 3)
        self.click(对话框对象库.弹框按钮.format("修改版次预览", "确定"))
        self.click(公共元素对象库.列表框.format("版次"))
        if not self.wait('//ul/li[contains(@class,"el-select-dropdown__item selected")]/span[text()="切换版次"]', 3):
            raise AssertionError("修改版次预览弹窗中点击确定，版次未发生变更")

    def 切换属性(self):
        self.进入到操作位置.进入设置页()
        self.进入到操作位置.进入属性工作区()
        版次lists = []
        elements = self.driver.getelements("//table//tr/td[2]//span[1]")
        for element in elements:
            版次lists.append(element.text)
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="切换属性")
        self.项目管理页面.创建空白项目(项目名称="切换属性", 属性名称='切换属性')
        # 点击版次下拉列表，列表显示所有的版次模板，选择对应的版次
        self.click(项目管理对象库.更多操作按钮.format("切换属性"))
        self.click(项目管理对象库.更多操作选项.format("项目设置"))
        self.click(公共元素对象库.列表框.format("属性"))
        列表框list = self.driver.getelements('//ul/li[contains(@class,"dropdown__item")]/span')
        for 列表框 in 列表框list:
            if 列表框.text not in 版次lists or len(版次lists) != len(列表框list):
                raise AssertionError(f"{列表框.text}不在属性列表中")
        self.公共操作.滚动选择列表框选项(选项名称='属性')
        self.click(公共元素对象库.列表框.format("属性"))
        if not self.wait('//ul/li[contains(@class,"el-select-dropdown__item selected")]/span[text()="属性"]', 3):
            raise AssertionError("点击切换属性系统，属性系统没有被切换")

    def 权限管理(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="权限编辑")
        self.项目管理页面.创建空白项目(项目名称="权限编辑", 生命周期名称='生命周期')
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
        self.项目页面.批量上传文件(目录路径=['权限编辑', '一级目录', '二级目录'], 文件路径列表=[素材2, 素材3])
        self.进入到操作位置.进入项目管理页()
        self.click(项目管理对象库.更多操作按钮.format("权限编辑"))
        self.click(项目管理对象库.更多操作选项.format("项目设置"))
        # 点击成员tab页，显示当前项目下的所有项目成员
        if not self.wait(项目设置页面.项目成员名称.format('18942178870', 'INDIVIDUAL ADMINISTRATOR'), 3) or not \
                self.wait(项目设置页面.项目成员名称.format('18942178871', 'INDIVIDUAL ADMINISTRATOR'), 3):
            raise AssertionError("项目设置中，项目成员tab页下项目成员信息显示不正确")
        # 点击成员列表中的权限编辑按钮，出现权限编辑弹框
        self.click(项目设置页面.权限编辑按钮.format('18942178871'))
        if not self.wait(对话框对象库.弹框标题.format("权限编辑"), 3):
            raise AssertionError("点击权限编辑按钮，未弹出权限编辑弹框")
        # 权限编辑弹窗下，左侧显示当前项目的项目文件目录结构
        基准数据 = ['权限编辑', '一级目录', '二级目录', '三级目录']
        j = 0
        for i in 基准数据[:-1]:
            if self.wait(项目设置页面.节点展开按钮.format(i), 3):
                self.click(项目设置页面.节点展开按钮.format(i))
            if not self.wait(项目设置页面.子节点.format(基准数据[j], 基准数据[j + 1]), 3):
                raise AssertionError(f"在权限编辑弹框，未查看到文件目录{基准数据[j]}和它的子目录{基准数据[j + 1]}")
            j += 1
        self.click(对话框对象库.关闭弹框.format("权限编辑"))
        # 编辑权限时，只对上级目录进行权限操作时，下级目录自动继承上级目录的权限操作结果
        self.项目设置页面.撤回用户授权(成员名称='18942178871', 目录列表=['权限编辑', '一级目录'], 权限列表=['目录新增', '目录删除'])
        self.click(项目设置页面.权限编辑按钮.format('18942178871'))
        self.项目设置页面.展开并点击最后一项目录(结构目录=['权限编辑', '一级目录', '二级目录'])
        if not self.wait(项目设置页面.禁用_权限复选框.format("目录新增"), 3) or \
                not self.wait(项目设置页面.禁用_权限复选框.format("目录删除"), 3):
            raise AssertionError("对父级节点授权后，子级节点未继承父级节点的授权结果")
        # 编辑下级目录权限时，上级目录权限不收影响
        self.click(对话框对象库.关闭弹框.format("权限编辑"))
        self.项目设置页面.撤回用户授权(成员名称='18942178871', 目录列表=['权限编辑', '一级目录', '二级目录'], 权限列表=['目录打包', '目录下载'])
        self.click(项目设置页面.权限编辑按钮.format('18942178871'))
        self.项目设置页面.展开并点击最后一项目录(结构目录=['权限编辑', '一级目录'])
        if not self.wait(项目设置页面.已选_权限复选框.format("目录打包"), 3) or \
                not self.wait(项目设置页面.已选_权限复选框.format("目录下载"), 3):
            raise AssertionError("对子级节点授权后，父级节点的权限被改变")
        self.click(项目设置页面.已选_权限复选框.format("目录修改"))
        self.click(对话框对象库.弹框按钮.format("权限编辑","确定"))
        self.click(项目设置页面.权限编辑按钮.format('18942178871'))
        self.项目设置页面.展开并点击最后一项目录(结构目录=['权限编辑', '一级目录'])
        if self.wait(项目设置页面.已选_权限复选框.format("目录修改"), 3):
            raise AssertionError("对节点授权后，点击确定，授权结果未被保存")

    def 生命周期控制(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="权限编辑")
        self.项目管理页面.创建空白项目(项目名称="权限编辑", 生命周期名称='生命周期')
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
        self.项目页面.批量上传文件(目录路径=['权限编辑', '一级目录', '二级目录'], 文件路径列表=[素材2, 素材3])
        self.进入到操作位置.进入项目管理页()
        self.click(项目管理对象库.更多操作按钮.format("权限编辑"))
        self.click(项目管理对象库.更多操作选项.format("项目设置"))
        self.click(项目设置页面.生命周期控制tab页)
        # 进入生命周期tab页，显示当前生命周期的节点信息
        for 节点 in ['11', '22', '33']:
            if not self.wait(项目设置页面.生命周期节点.format(节点), 3):
                raise AssertionError(f"在项目生命周期控制tab页未查看到{节点}节点")
        self.click(项目设置页面.添加人员按钮)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("请先选择生命周期节点"), 3):
            raise AssertionError("没有选择生命周期节点，点击添加人员按钮，没有出现提示信息")
        # 成员列表默认存在项目创建人
        self.click(项目设置页面.生命周期节点.format("11"))
        if not self.wait(项目设置页面.节点下成员.format("18942178870"), 3):
            raise AssertionError("点击生命周期节点，项目创建者没有默然存在于该节点的成员中")
        # 点击节点名称，点击添加人员按钮，进入选择人员弹窗
        self.click(项目设置页面.添加人员按钮)
        if not self.wait(对话框对象库.弹框标题.format("选择人员"), 3):
            raise AssertionError("选择生命周期节点后，点击添加人员按钮，未进入到选择人员弹框")
        # 选择人员弹窗内列表显示当前项目的所有项目成员，已经被添加的成员置灰
        if not self.wait(项目设置页面.禁用_成员复选框.format('18942178870'), 3):
            raise AssertionError("选择人员弹框中，已经被选择的成员没有被置灰")
        if not self.wait(项目设置页面.未选_成员复选框.format('18942178871'), 3):
            raise AssertionError("选择人员弹框中，未被选择的成员处于不可用状态")
        # 勾选列表中的成员，点击确定，可以在节点的成员列表中查看到新添加的成员
        self.click(项目设置页面.未选_成员复选框.format('18942178871'))
        self.click(对话框对象库.弹框按钮.format("选择人员", "确定"))
        if not self.wait(项目设置页面.节点下成员.format('18942178871'), 3):
            raise AssertionError("在选择成员弹窗，选择成员后点击确定按钮，人员未被添加")
        # 点击成员的移除按钮，人员被移除
        self.click(项目设置页面.移除成员按钮.format('18942178871'))
        self.wait(公共元素对象库.系统提示信息弹框.format("18942178871"), 3)
        if self.wait(项目设置页面.节点下成员.format('18942178871'), 3):
            raise AssertionError("进行移除节点成员成功后，节点成员列表仍然能看到被移除的成员")
        # 项目创建人不可以被移除
        self.click(项目设置页面.移除成员按钮.format('18942178870'))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("该控制用户不可移除"),3):
            raise AssertionError("进行移除项目节点下默认节点成员时，没有出现提示信息")
        if not self.wait(项目设置页面.节点下成员.format('18942178870'), 3):
            raise AssertionError("项目创建人在生命周期节点下不可以被移除")

    def 生命周期节点人员提交设置(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="权限编辑")
        self.项目管理页面.创建空白项目(项目名称="权限编辑", 生命周期名称='生命周期')
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
        self.项目页面.批量上传文件(目录路径=['权限编辑', '一级目录', '二级目录'], 文件路径列表=[素材2, 素材3])
        self.项目管理页面.进入点击项目设置(项目名称='权限编辑', 生命周期控制tab页=True)
        self.项目设置页面.添加节点人员(节点名称='11', 成员名称='18942178871', 所有人提交后可进入下一节点=False)
        # 所有人提交后进入下一节点按钮关闭时，该节点下成员只要有一个成员完成提交，生命周期就可以进入下个节点
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="权限编辑")
        self.项目页面.改变文件状态(目录路径=['权限编辑', '一级目录', '二级目录'], 文件名='素材2.jpg', 状态名称='22')
        生命周期状态1 = self.driver.getelement(项目对象库.生命周期状态.format('素材2.jpg')).text
        if 生命周期状态1 != '22':
            raise AssertionError("所有人提交后进入下一节点按钮关闭时，该节点下成员下有一个成员完成提交，生命周期未进入下个节点")
        # 所有人提交后进入下一节点按钮开启时，该节点下一个成员提交后，该文件生命周期状态为中间态
        self.项目管理页面.进入点击项目设置(项目名称='权限编辑', 生命周期控制tab页=True)
        self.项目设置页面.添加节点人员(节点名称='11', 所有人提交后可进入下一节点=True)
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.点击进入项目(项目名称="权限编辑")
        self.项目页面.改变文件状态(目录路径=['权限编辑', '一级目录', '二级目录'], 文件名='素材3.jpg', 状态名称='22')
        lines = ''
        elems = self.driver.getelements(项目对象库.生命周期状态.format('素材3.jpg'))
        # for elem in elems:
        #     lines = lines + elem.text
        # if lines != '11 -> 22':
        if len(elems) !=2:
            raise AssertionError("开启所有人提交后可进入下一节点后，改变生命周期状态后，生命周期中间态未出现")
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

    def 创建文件目录(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="创建文件目录")
        self.项目管理页面.创建空白项目(项目名称="创建文件目录")
        self.项目管理页面.点击进入项目(项目名称="创建文件目录")
        self.wait(项目对象库.目录节点.format("创建文件目录"),3)
        self.driver.refrsh()
        self.click(项目对象库.新建目录)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新建文件目录"), 3)
        self.clear(公共元素对象库.输入框.format("文件目录名称"))
        self.send_keys(公共元素对象库.输入框.format("文件目录名称"), "一级目录")
        self.click(对话框对象库.对话框按钮.format("新建文件目录", "提交"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        #创建二级目录
        self.click(项目对象库.目录节点.format("一级目录"))
        self.click(项目对象库.新建目录)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新建文件目录"), 3)
        self.clear(公共元素对象库.输入框.format("文件目录名称"))
        self.send_keys(公共元素对象库.输入框.format("文件目录名称"), "二级目录")
        self.click(对话框对象库.对话框按钮.format("新建文件目录", "提交"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        if not self.wait(项目对象库.子节点.format("创建文件目录","一级目录"),3) \
                or not self.wait(项目对象库.子节点.format("一级目录","二级目录"),3):
            raise AssertionError("未查看到创建的文件目录，或文件目录的父子关系不正确")
        self.进入到操作位置.进入项目管理页()
        #点击展开和收缩各级资源节点，资源节点可以被正常展开和收缩
        self.项目管理页面.点击进入项目(项目名称="创建文件目录")
        self.click(项目对象库.节点展开按钮.format("一级目录"))
        if not self.wait(项目对象库.目录节点.format("二级目录"), 3):
            raise AssertionError("节点展开按钮，目录未被正常展开")
        self.click(项目对象库.节点收起按钮.format("一级目录"))
        if self.wait(项目对象库.目录节点.format("二级目录"),3):
            raise AssertionError("点击目录收起按钮，目录未被正常收起")


    def 上传单个文件(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="上传文件项目")
        self.项目管理页面.创建空白项目(项目名称="上传文件项目")
        self.项目管理页面.点击进入项目(项目名称="上传文件项目")
        self.wait(项目对象库.目录节点.format("上传文件项目"), 3)
        self.driver.refrsh()
        #创建文件目录
        self.项目页面.创建文件目录(目录名称="一级目录",目录父节点名称="上传文件项目")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        #上传文件
        self.click(项目对象库.目录节点.format("一级目录"))
        #点击上传按钮，弹窗上传文件对话框
        self.click(项目对象库.上传)
        if not self.wait(对话框对象库.弹框标题.format("上传文件"),3):
            raise AssertionError("点击上传按钮，未弹出上传文件弹窗")
        # 点击上传按钮，选择单个文件，点击上传
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=['TestData','FrontData','项目页','素材1.png'])
        if not self.wait(项目对象库.待上传文件.format("素材1.png"),5):
            raise AssertionError("选择上传文件后，弹窗内未发现被选中的待上传文件")
        self.click(项目对象库.上传文件按钮)
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"),300)
        if not self.wait(项目对象库.列表文件名称.format("素材1.png"), 3):
            raise AssertionError("上传文件失败，未发现上传的文件：素材1.png")
        self.click(项目对象库.目录节点.format("一级目录"))
        #点击资源树任意节点，右侧列表显示该节点下的所有资源和子分组
        if not self.wait(项目对象库.列表文件名称.format("二级目录"),3) or not \
                self.wait(项目对象库.列表文件名称.format("素材1.png"),3):
            raise AssertionError("点击资源树任意节点，右侧列表未发现该节点下的子分组和文件资源")

    def 批量上传文件(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="上传文件项目")
        self.项目管理页面.创建空白项目(项目名称="上传文件项目")
        self.项目管理页面.点击进入项目(项目名称="上传文件项目")
        self.wait(项目对象库.目录节点.format("上传文件项目"), 3)
        self.driver.refrsh()
        # 创建文件目录
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="上传文件项目")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        # 上传文件
        self.click(项目对象库.目录节点.format("一级目录"))
        # 点击上传按钮，弹窗上传文件对话框
        self.click(项目对象库.上传)
        self.wait(对话框对象库.弹框标题.format("上传文件"), 3)
        # 选择多个待上传文件，在弹窗中清除部分待上传文件，文件被清除
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=['TestData', 'FrontData', '项目页', '素材2.jpg'])
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=['TestData', 'FrontData', '项目页', '素材3.jpg'])
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=['TestData', 'FrontData', '项目页', '素材4.png'])
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=['TestData', 'FrontData', '项目页', '素材5.png'])
        self.move_to_by_pyautogui(项目对象库.待上传文件.format("素材5.png"))
        self.click(项目对象库.移除待上传文件.format("素材5.png"))
        if self.wait(项目对象库.列表文件名称.format("素材5.png"), 3):
            raise AssertionError("移除待上传文件：素材5.png后，仍然在待上传文件列表中能查看到：素材5.png")
        self.click(项目对象库.上传文件按钮)
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 300)
        if not self.wait(项目对象库.列表文件名称.format("素材2.jpg"),3) or not \
                self.wait(项目对象库.列表文件名称.format("素材3.jpg"),3)or not \
                self.wait(项目对象库.列表文件名称.format("素材4.png"),3):
            raise AssertionError("批量上传资源后，在目标目录下未查看到批量上传的资源")

    def 列表显示管理(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="列表显示项目")
        self.项目管理页面.创建空白项目(项目名称="列表显示项目")
        self.项目管理页面.点击进入项目(项目名称="列表显示项目")
        self.wait(项目对象库.目录节点.format("列表显示项目"), 3)
        self.driver.refrsh()
        # 创建文件目录
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="列表显示项目")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        self.click(项目对象库.目录节点.format("一级目录"))
        titles=[]
        mxpath='//div[contains(@class,"header-wrapper")]//table[@class="vxe-table--header"]//tr/th'
        elements=self.driver.getelements(mxpath)
        for element in elements:
            if element.text!="":
                titles.append(element.text)
        基准数据=['文件名称','文件类型','文件大小','作者', '创建时间', '版本', '版次','生命周期状态','检出人','检出时间','检入人','检入时间','备注','操作']
        if titles!=基准数据:
           raise AssertionError(f"列表默认显示列错误,基准数据为：{基准数据}，页面数据为：{titles}")

    def 批量操作工具栏显示(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="批量操作")
        self.项目管理页面.创建空白项目(项目名称="批量操作")
        self.项目管理页面.点击进入项目(项目名称="批量操作")
        self.wait(项目对象库.目录节点.format("批量操作"), 3)
        self.driver.refrsh()
        # 创建文件目录
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="批量操作")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        self.项目页面.批量上传文件(目录路径=['批量操作','一级目录'],文件路径列表=[['TestData', 'FrontData', '项目页', '素材2.jpg'],['TestData', 'FrontData', '项目页', '素材3.jpg']])
        self.click(项目对象库.目录节点.format("一级目录"))
        if self.wait(项目对象库.工具栏按钮.format("删除"),3):
            raise AssertionError("进入文件列表可以查看到工具栏按钮，工具栏按钮默认不显示")
        self.click(项目对象库.列表复选框.format("素材2.jpg"))
        self.click(项目对象库.列表复选框.format("素材3.jpg"))
        if not self.wait(项目对象库.工具栏按钮.format("删除"),3):
            raise AssertionError("选中多个文件后，工具栏未出现")

    def 收藏文件或文件目录(self):
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
        self.项目页面.批量上传文件(目录路径=['收藏资源', '一级目录'], 文件路径列表=[['TestData', 'FrontData', '项目页', '素材1.png'],
                                                        ['TestData', 'FrontData', '项目页', '素材2.jpg']])
        # 点击资源行操作的收藏按钮，可以对文件或文件目录收藏成功
        # 序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]',
        #                            文件名称='素材1.png')
        # self.click(项目对象库.未选_悬浮列收藏.format(序号))
        self.click(项目对象库.未收藏按钮.format("素材1.png"))
        self.wait(公共元素对象库.系统提示信息弹框.format("收藏成功"))
        # if not self.wait(项目对象库.已选_悬浮列收藏.format(序号), 3):
        #     raise AssertionError("点击收藏文件成功后，文件的收藏按钮未被点亮")
        if not self.wait(项目对象库.收藏按钮.format("素材1.png"), 3):
             raise AssertionError("点击收藏文件成功后，文件的收藏按钮未被点亮")
        # 序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]',
        #                            文件名称='二级目录')
        # self.click(项目对象库.未选_悬浮列收藏.format(序号))
        self.click(项目对象库.未收藏按钮.format("二级目录"))
        self.wait(公共元素对象库.系统提示信息弹框.format("收藏成功"))
        # if not self.wait(项目对象库.已选_悬浮列收藏.format(序号), 3):
        #     raise AssertionError("点击收藏目录成功后，目录的收藏按钮未被点亮")
        if self.wait(项目对象库.未收藏按钮.format("二级目录"), 3):
            raise AssertionError("点击收藏文件成功后，文件的收藏按钮未被点亮")
        self.进入到操作位置.进入收藏页()
        if not self.wait(收藏对象库.资源类型.format("素材1.png", "收藏资源"), 3):
            raise AssertionError("点击文件行操作的收藏按钮，文件没有被收藏")
        if not self.wait(收藏对象库.资源类型.format("二级目录", "收藏资源"), 3):
            raise AssertionError("点击目录行操作的收藏按钮，文件没有被收藏")
        # 点击资源行操作的收藏按钮，可以对文件或文件目录取消收藏成功
        self.click(收藏对象库.查看收藏按钮.format("二级目录"))
        # 序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]',
        #                            文件名称='素材1.png')
        # self.click(项目对象库.已选_悬浮列收藏.format(序号))
        self.click(项目对象库.目录节点.format("一级目录"))
        self.click(项目对象库.收藏按钮.format("素材1.png"))
        self.wait(公共元素对象库.系统提示信息弹框.format("取消收藏成功"))
        if not self.wait(项目对象库.未收藏按钮.format("素材1.png"),3):
            raise AssertionError("文件取消收藏操作成功后，收藏按钮仍是点亮状态")
        # 序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]',
        #                            文件名称='二级目录')
        self.click(项目对象库.收藏按钮.format("二级目录"))
        # self.click(项目对象库.已选_悬浮列收藏.format(序号))
        self.wait(公共元素对象库.系统提示信息弹框.format("取消收藏成功"))
        # if not self.wait(项目对象库.未选_悬浮列收藏.format(序号)):
        #     raise AssertionError("目录取消收藏操作成功后，收藏按钮仍是点亮状态")
        if not self.wait(项目对象库.未收藏按钮.format("二级目录")):
            raise AssertionError("目录取消收藏操作成功后，收藏按钮仍是点亮状态")
        self.进入到操作位置.进入收藏页()
        if self.wait(收藏对象库.资源类型.format("素材1.png", "收藏资源"), 3):
            raise AssertionError("取消收藏文件后，文件仍然在收藏页")
        if self.wait(收藏对象库.资源类型.format("二级目录", "收藏资源"), 3):
            raise AssertionError("取消收藏目录后，目录仍然在收藏页")

    def 文件检出和撤销检出(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="文件检出")
        self.项目管理页面.创建空白项目(项目名称="文件检出")
        self.项目管理页面.点击进入项目(项目名称="文件检出")
        self.wait(项目对象库.目录节点.format("文件检出"), 3)
        self.driver.refrsh()
        # 创建文件目录
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="文件检出")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        self.项目页面.上传单个文件(目录路径=['文件检出', '一级目录'], 文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'])
        self.click(项目对象库.目录节点.format("一级目录"))
        #检出
        self.click(项目对象库.列表行操作.format("检入检出素材.txt"))
        self.click(项目对象库.行操作选项.format("检出"))
        if not self.wait(项目对象库.检出按钮.format("检入检出素材.txt"),3):
            raise AssertionError("对文件执行检出操作后，列表未出现文件检出标志")
        #撤销检出
        self.driver.refrsh()
        self.click(项目对象库.列表行操作.format("检入检出素材.txt"))
        self.click(项目对象库.行操作选项.format("撤销检出"))
        if self.wait(项目对象库.检出按钮.format("检入检出素材.txt"), 3):
            raise AssertionError("对文件执行撤销检出操作后，列表仍然有文件检出标志")

    def 文件检入(self):
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
        self.项目页面.检出资源(目录路径=['文件检入', '一级目录'], 资源名称='检入检出素材.txt')
        self.driver.refrsh()
        self.click(项目对象库.列表行操作.format('检入检出素材.txt'))
        self.click(项目对象库.行操作选项.format("检入"))
        self.公共操作.修改文件内容(文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'],内容=str(int(time.time())))
        self.click(项目对象库.点击上传按钮)
        self.公共操作.win上传文件(文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'])
        self.wait(项目对象库.待上传文件.format("检入检出素材.txt"), 5)
        self.click(项目对象库.上传文件按钮)
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 300)
        if self.wait(项目对象库.检出按钮.format("检入检出素材.txt"), 3):
            raise AssertionError("对已检出的文件进行检入操作后，列表仍然有文件检出标志")

    def 改变状态(self):
        pass

    def 文件或目录删除(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="文件删除")
        self.项目管理页面.创建空白项目(项目名称="文件删除")
        self.项目管理页面.点击进入项目(项目名称="文件删除")
        self.wait(项目对象库.目录节点.format("文件删除"), 3)
        self.driver.refrsh()
        # 创建文件目录
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="文件删除")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        self.项目页面.上传单个文件(目录路径=['文件检入', '一级目录'], 文件路径=['TestData', 'FrontData', '项目页', '素材1.png'])
        #删除文件
        self.click(项目对象库.列表行操作.format('素材1.png'))
        self.click(项目对象库.行操作选项.format("删除"))
        self.click(对话框对象库.对话框按钮.format("提示","确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("删除成功"),3)
        if self.wait(项目对象库.列表文件名称.format("素材1.png"),3):
            raise AssertionError("删除文件失败，删除文件后列表中仍然能查看到该文件")
        #删除目录
        self.click(项目对象库.列表行操作.format('二级目录'))
        self.click(项目对象库.行操作选项.format("删除"))
        self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("删除成功"), 3)
        if self.wait(项目对象库.列表文件名称.format("二级目录"), 3):
            raise AssertionError("删除目录失败，删除目录后列表中仍然能查看到该目录")

    def 批量上传文件并下载校验(self):
        self.公共操作.清空浏览器下载目录()
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="批量上传校验")
        self.项目管理页面.创建空白项目(项目名称="批量上传校验")
        self.项目管理页面.点击进入项目(项目名称="批量上传校验")
        self.wait(项目对象库.目录节点.format("批量上传校验"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="批量上传校验")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        素材1 = ['TestData', 'FrontData', '项目页', '素材1.png']
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        素材4 = ['TestData', 'FrontData', '项目页', '素材4.png']
        素材5 = ['TestData', 'FrontData', '项目页', '素材5.png']
        素材6 = ['TestData', 'FrontData', '项目页', '素材6.png']
        素材7 = ['TestData', 'FrontData', '项目页', '头像2.txt']
        素材8 = ['TestData', 'FrontData', '项目页', '检入检出素材.txt']
        self.项目页面.批量上传文件(目录路径=['批量检出', '一级目录'], 文件路径列表=[素材1,素材2,素材3,素材4,素材5,素材6,素材7,素材8])
        文件列表=['素材1.png','素材2.jpg','素材3.jpg','素材4.png','素材5.png','素材6.png','头像2.txt','检入检出素材.txt']
        size={'素材1.png':1748 ,'素材2.jpg':1713301,'素材3.jpg':5336917,'素材4.png':12812063,'素材5.png':5746131,'素材6.png':1690428,'头像2.txt':10,'检入检出素材.txt':10}
        for 文件 in 文件列表:
            if not self.wait(项目对象库.列表文件名称.format(文件),3):
                raise AssertionError(f"批量上传文件出现问题，文件：{文件}上传完成后未在文件列表中")
            self.driver.refrsh()
            self.click(项目对象库.列表行操作.format(文件))
            self.click(项目对象库.行操作选项.format("下载"))
            downpath = self.公共操作.检查文件是否下载完成()
            filepath = downpath + f'\{文件}'
            time.sleep(4)
            文件大小=self.获取文件大小(文件路径=filepath)
            if 文件大小!=size[文件]:
                raise AssertionError(f"文件{文件}上传后下载的大小异常，基准大小为{size[文件]}，下载后的大小为{文件大小}")

    def 批量上传文件并下载校验2(self):
        self.公共操作.清空浏览器下载目录()
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="批量上传校验")
        self.项目管理页面.创建空白项目(项目名称="批量上传校验")
        self.项目管理页面.点击进入项目(项目名称="批量上传校验")
        self.wait(项目对象库.目录节点.format("批量上传校验"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="批量上传校验")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        素材1 = ['TestData', 'FrontData', '文件上传下载', '10k.png']
        素材2 = ['TestData', 'FrontData', '文件上传下载', '11k.png']
        素材3 = ['TestData', 'FrontData', '文件上传下载', '14k.png']
        素材4 = ['TestData', 'FrontData', '文件上传下载', '17k.png']
        素材5 = ['TestData', 'FrontData', '文件上传下载', '20k.png']
        素材6 = ['TestData', 'FrontData', '文件上传下载', '22k.png']
        素材7 = ['TestData', 'FrontData', '文件上传下载', '26k.png']
        self.项目页面.批量上传文件(目录路径=['批量检出', '一级目录'], 文件路径列表=[素材1,素材2,素材3,素材4,素材5,素材6,素材7])
        文件列表=['10k.png','11k.png','14k.png','17k.png','20k.png','22k.png','26k.png']
        size={'10k.png':10285770 ,'11k.png':11198638,'14k.png':15043975,'17k.png':17632913,'20k.png':20699057,'22k.png':23061428,'26k.png':26767938}
        for 文件 in 文件列表:
            if not self.wait(项目对象库.列表文件名称.format(文件),3):
                raise AssertionError(f"批量上传文件出现问题，文件：{文件}上传完成后未在文件列表中")
            self.driver.refrsh()
            self.click(项目对象库.列表行操作.format(文件))
            self.click(项目对象库.行操作选项.format("下载"))
            downpath = self.公共操作.检查文件是否下载完成()
            filepath = downpath + f'\{文件}'
            time.sleep(4)
            文件大小=self.获取文件大小(文件路径=filepath)
            if 文件大小!=size[文件]:
                raise AssertionError(f"文件{文件}上传后下载的大小异常，基准大小为{size[文件]}，下载后的大小为{文件大小}")

    def 附加文件(self):
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
        self.项目页面.批量上传文件(目录路径=['附加文件', '一级目录'], 文件路径列表=[素材1, 素材2, 素材3, 素材4, 素材5, 素材6])
        # 点击文件行操作中的添加附件操作，弹出附件文件弹窗
        self.click(项目对象库.目录节点.format("一级目录"))
        self.click(项目对象库.列表行操作.format('素材1.png'))
        self.click(项目对象库.行操作选项.format("附加文件"))
        self.click(对话框对象库.弹框标题.format("附加文件"))
        if not self.wait(对话框对象库.弹框标题.format("附加文件"), 3):
            raise AssertionError("点击文件的附加文件操作，未查看到附加文件弹窗")
        # 左侧资源树默认全部展开，点击目录，右侧列表显示该目录下全部文件
        self.click(项目对象库.附加文件.树资源节点.format("一级目录"))
        for 文件 in ['素材2', '素材3', '素材4', '素材5', '素材6']:
            if not self.wait(项目对象库.附加文件.列表单选按钮.format(文件), 3):
                raise AssertionError(f"附加文件弹窗显示文件目录下的文件时{文件}未被显示")
        self.click(项目对象库.附加文件.列表单选按钮.format("素材2"))
        self.click(项目对象库.附加文件.附加按钮)
        self.default_content()
        if not self.wait(公共元素对象库.系统提示信息弹框.format("操作成功"), 3):
            raise AssertionError("附加文件操作时选择文件点击附加后，系统未给出附加成功的提示")
        self.click(项目对象库.列表文件名称.format('素材1.png'))
        self.click(项目对象库.文件信息.引用tab页)
        if not self.wait(项目对象库.文件信息.引用文件名称.format("素材2.jpg"), 3):
            raise AssertionError("对文件设置附加文件后，在文件信息中查看不到该文件的引用文件信息")
        self.click(项目对象库.列表文件名称.format('素材2.jpg'))
        self.click(项目对象库.文件信息.被引用tab页)
        if not self.wait(项目对象库.文件信息.被引用文件名称.format("素材1.png"), 3):
            raise AssertionError("对文件设置附加文件后，在被引用文件信息中查看不到该文件的被引用信息")
        # 勾选多个文件点击附加，系统提示附加成功，在文件的引用tab页可以查看到该文件被引用文件名称
        self.click(项目对象库.列表行操作.format('素材1.png'))
        self.click(项目对象库.行操作选项.format("附加文件"))
        self.wait(对话框对象库.弹框标题.format("附加文件"), 3)
        self.click(项目对象库.附加文件.树资源节点.format("一级目录"))
        self.click(项目对象库.附加文件.列表单选按钮.format("素材3"))
        self.click(项目对象库.附加文件.列表单选按钮.format("素材4"))
        self.click(项目对象库.附加文件.列表单选按钮.format("素材5"))
        self.click(项目对象库.附加文件.附加按钮)
        self.default_content()
        self.wait(公共元素对象库.系统提示信息弹框.format("操作成功"), 3)
        for 文件名 in ['素材3.jpg', '素材4.png', '素材5.png']:
            self.click(项目对象库.列表文件名称.format('素材1.png'))
            self.click(项目对象库.文件信息.引用tab页)
            if not self.wait(项目对象库.文件信息.引用文件名称.format(文件名), 3):
                raise AssertionError(f"对文件设置附加文件后，在文件信息中查看不到该文件的引用{文件名}的信息")
            self.click(项目对象库.列表文件名称.format(文件名))
            self.click(项目对象库.文件信息.被引用tab页)
            if not self.wait(项目对象库.文件信息.被引用文件名称.format("素材1.png"), 3):
                raise AssertionError(f"对文件设置附加文件后，在被引用文件{文件名}的信息中查看不到该文件的被引用信息")

    def 文件打包(self):
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
        # 文件行操作，点击打包，自动下载打包后的压缩包，压缩包名为被打包的文件名，压缩包内容为被打包的文件
        self.click(项目对象库.列表行操作.format('素材1.png'))
        self.click(项目对象库.行操作选项.format("打包"))
        downpath = self.公共操作.检查文件是否下载完成()
        filepath = downpath + '\素材1.png.zip'
        time.sleep(3)
        if not os.path.exists(filepath):
            raise AssertionError("在下载目录下未查看到打包的文件")
        namelist = self.公共操作.查看zip文件(zip文件路径=filepath)
        if not '素材1.png' in namelist:
            raise AssertionError("在打包的文件中未查看到被打包的文件")
        # 目录行操作，点击打包，自动下载打包后的压缩包，压缩包名为被打包的目录的名称，压缩包内容未被打包的目录及目录下的全部资源
        self.公共操作.清空浏览器下载目录()
        self.click(项目对象库.目录节点.format("文件或目录打包"))
        self.click(项目对象库.列表行操作.format('一级目录'))
        self.click(项目对象库.行操作选项.format("打包"))
        downpath = self.公共操作.检查文件是否下载完成()
        filepath = downpath + '\一级目录.zip'
        time.sleep(3)
        if not os.path.exists(filepath):
            raise AssertionError("在下载目录下未查看到打包的文件目录")
        self.公共操作.解压zip到指定目录(zip文件路径=filepath, 目标路径=downpath)
        文件目录 = os.listdir(downpath + '\一级目录')
        if not '素材1.png' in 文件目录 or not '素材2.jpg' in 文件目录:
            raise AssertionError("在打包的文件中未查看到被打包的文件")

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
        # 点击下载，文件可以被正常下载
        self.click(项目对象库.列表行操作.format('素材1.png'))
        self.click(项目对象库.行操作选项.format("下载"))
        downpath = self.公共操作.检查文件是否下载完成()
        filepath = downpath + '\素材1.png'
        time.sleep(3)
        if not os.path.exists(filepath):
            raise AssertionError("在下载目录下未查看到被下载的文件")

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

    def 批量检出(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="批量检出")
        self.项目管理页面.创建空白项目(项目名称="批量检出")
        self.项目管理页面.点击进入项目(项目名称="批量检出")
        self.wait(项目对象库.目录节点.format("批量检出"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="批量检出")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        素材1 = ['TestData', 'FrontData', '项目页', '素材1.png']
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        self.项目页面.批量上传文件(目录路径=['批量检出', '一级目录'], 文件路径列表=[素材1, 素材2, 素材3])
        素材6 = ['TestData', 'FrontData', '项目页', '检入检出素材.txt']
        self.项目页面.批量上传文件(目录路径=['批量检出', '一级目录', '二级目录'], 文件路径列表=[素材6])
        # 批量选择文件，点击检出，可以检出成功
        self.click(项目对象库.目录节点.format('一级目录'))
        self.click(项目对象库.列表复选框.format('素材1.png'))
        self.click(项目对象库.列表复选框.format('素材2.jpg'))
        self.click(项目对象库.工具栏按钮.format('检出'))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 3):
            raise AssertionError("对文件进行批量检出操作，未查看到系统提示信息")
        if not self.wait(项目对象库.检出按钮.format('素材1.png'), 3) or not \
                self.wait(项目对象库.检出按钮.format('素材2.jpg'), 3):
            raise AssertionError("进行批量检出操作后，文件列表中文件未被标记为检出状态")
        #批量选择目录和文件，点击检出，可以检出成功
        self.click(项目对象库.列表复选框.format('二级目录'))
        self.click(项目对象库.列表复选框.format('素材3.jpg'))
        self.click(项目对象库.工具栏按钮.format('检出'))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("操作成功"), 3):
            raise AssertionError("对文件和文件目录进行批量检出操作，未查看到系统提示信息")
        if not self.wait(项目对象库.检出按钮.format('素材3.jpg'), 3):
            raise AssertionError("进行文件和文件目录批量检出操作后，文件列表中文件未被标记为检出状态")
        self.click(项目对象库.目录节点.format('二级目录'))
        if not self.wait(项目对象库.检出按钮.format('检入检出素材.txt'), 3):
            raise AssertionError("进行文件和文件目录批量检出操作后，文件目录中文件未被标记为检出状态")

    def 批量撤销检出(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="批量撤销检出")
        self.项目管理页面.创建空白项目(项目名称="批量撤销检出")
        self.项目管理页面.点击进入项目(项目名称="批量撤销检出")
        self.wait(项目对象库.目录节点.format("批量撤销检出"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="批量撤销检出")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        素材1 = ['TestData', 'FrontData', '项目页', '素材1.png']
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材3 = ['TestData', 'FrontData', '项目页', '素材3.jpg']
        self.项目页面.批量上传文件(目录路径=['批量撤销检出', '一级目录'], 文件路径列表=[素材1, 素材2, 素材3])
        self.项目页面.检出资源(目录路径=['批量撤销检出', '一级目录'], 资源名称='素材1.png')
        self.项目页面.检出资源(目录路径=['批量撤销检出', '一级目录'], 资源名称='素材2.jpg')
        self.项目页面.检出资源(目录路径=['批量撤销检出', '一级目录'], 资源名称='素材3.jpg')
        素材6 = ['TestData', 'FrontData', '项目页', '检入检出素材.txt']
        self.项目页面.批量上传文件(目录路径=['批量撤销检出', '一级目录', '二级目录'], 文件路径列表=[素材6])
        self.项目页面.检出资源(目录路径=['批量撤销检出', '一级目录'], 资源名称='二级目录')
        ## 批量选择已检出的文件，点击撤销检出，可以撤销检出成功
        self.click(项目对象库.目录节点.format('一级目录'))
        self.click(项目对象库.列表复选框.format('素材1.png'))
        self.click(项目对象库.列表复选框.format('素材2.jpg'))
        self.click(项目对象库.工具栏按钮.format('撤销检出'))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("撤销检出成功"), 3):
            raise AssertionError("对文件进行批量撤销检出操作，未查看到系统提示信息")
        if self.wait(项目对象库.检出按钮.format('素材1.png'), 3) or\
                self.wait(项目对象库.检出按钮.format('素材2.jpg'), 3):
            raise AssertionError("进行批量撤销检出操作后，文件列表中文件仍被标记为检出状态")
        # 批量选择文件和目录，点击撤销检出，可以撤销成功
        self.click(项目对象库.列表复选框.format('素材3.jpg'))
        self.click(项目对象库.列表复选框.format('二级目录'))
        self.click(项目对象库.工具栏按钮.format('撤销检出'))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("撤销检出成功"), 3):
            raise AssertionError("对文件和目录进行批量撤销检出操作，未查看到系统提示信息")
        if self.wait(项目对象库.检出按钮.format('素材3.jpg'), 3):
            raise AssertionError("对文件和目录进行批量撤销检出操作后，文件列表中文件未被撤销检出")
        self.click(项目对象库.目录节点.format('二级目录'))
        if self.wait(项目对象库.检出按钮.format('检入检出素材.txt'), 3):
            raise AssertionError("对文件和目录进行批量撤销检出操作后，目录中的文件未被撤销检出")

    def 批量删除(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="批量删除")
        self.项目管理页面.创建空白项目(项目名称="批量删除")
        self.项目管理页面.点击进入项目(项目名称="批量删除")
        self.wait(项目对象库.目录节点.format("批量删除"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="批量删除")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        素材1 = ['TestData', 'FrontData', '项目页', '素材1.png']
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        素材4 = ['TestData', 'FrontData', '项目页', '素材4.png']
        self.项目页面.批量上传文件(目录路径=['批量删除', '一级目录'], 文件路径列表=[素材1, 素材2, 素材4])
        素材6 = ['TestData', 'FrontData', '项目页', '检入检出素材.txt']
        self.项目页面.批量上传文件(目录路径=['批量删除', '一级目录', '二级目录'], 文件路径列表=[素材6])
        # 勾选多个文件，点击删除，弹出删除确认对话框
        self.click(项目对象库.目录节点.format('一级目录'))
        self.click(项目对象库.列表复选框.format('素材1.png'))
        self.click(项目对象库.列表复选框.format('素材2.jpg'))
        self.click(项目对象库.工具栏按钮.format('删除'))
        if not self.wait(对话框对象库.对话框标题.format("提示"), 3):
            raise AssertionError("勾选多个文件时，点击批量删除按钮未出现删除确认对话框")
        # 勾选多个文件，点击删除，可以删除
        self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("删除成功!"), 3):
            raise AssertionError("在删除确认对话框中点击确定，未查看到删除提示信息")
        if self.wait(项目对象库.列表文件名称.format("素材1.png"), 3) or \
                self.wait(项目对象库.列表文件名称.format("素材2.jpg"), 3):
            raise AssertionError("在删除确认对话框中点击确定，列表中被选中的文件未被删除")
        # 勾选多个文件和目录，点击删除，可以删除成功
        self.click(项目对象库.目录节点.format('一级目录'))
        self.click(项目对象库.列表复选框.format('素材4.png'))
        self.click(项目对象库.列表复选框.format('二级目录'))
        self.click(项目对象库.工具栏按钮.format('删除'))
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("删除成功!"), 3):
            raise AssertionError("勾选多个文件和目录，点击删除，未查看到删除提示信息")
        if self.wait(项目对象库.列表文件名称.format("素材4.png"), 3) or \
                self.wait(项目对象库.列表文件名称.format("二级目录"), 3):
            raise AssertionError("勾选多个文件和目录，点击删除，列表中被选中的文件或目录未被删除")

    def 批量打包(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="批量打包")
        self.项目管理页面.创建空白项目(项目名称="批量打包")
        self.项目管理页面.点击进入项目(项目名称="批量打包")
        self.wait(项目对象库.目录节点.format("批量打包"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="批量打包")
        self.项目页面.创建文件目录(目录名称="二级目录", 目录父节点名称="一级目录")
        素材1 = ['TestData', 'FrontData', '项目页', '素材1.png']
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        self.项目页面.批量上传文件(目录路径=['批量打包', '一级目录'], 文件路径列表=[素材1, 素材2])
        素材6 = ['TestData', 'FrontData', '项目页', '检入检出素材.txt']
        self.项目页面.批量上传文件(目录路径=['批量打包', '一级目录', '二级目录'], 文件路径列表=[素材6])
        # 勾选多个文件，点击打包，压缩包中含有被勾选文件
        self.公共操作.清空浏览器下载目录()
        self.click(项目对象库.目录节点.format('一级目录'))
        self.click(项目对象库.列表复选框.format('素材1.png'))
        self.click(项目对象库.列表复选框.format('素材2.jpg'))
        self.click(项目对象库.工具栏按钮.format('打包'))
        downpath = self.公共操作.检查文件是否下载完成()
        filepath = downpath + '\批量打包.zip'
        time.sleep(4)
        namelist = self.公共操作.查看zip文件(zip文件路径=filepath)
        for name in ['素材1.png', '素材2.jpg']:
            if not name in namelist or len(namelist) != 2:
                raise AssertionError("在打包的文件中未查看到被打包的文件")
        #选文件和目录，点击打包，压缩包中含有被勾选的文件和目录，目录下的文件页被打包
        self.公共操作.清空浏览器下载目录()
        self.click(项目对象库.目录节点.format('批量打包'))
        self.click(项目对象库.目录节点.format('一级目录'))
        self.click(项目对象库.列表复选框.format('素材1.png'))
        self.click(项目对象库.列表复选框.format('二级目录'))
        self.click(项目对象库.工具栏按钮.format('打包'))
        downpath = self.公共操作.检查文件是否下载完成()
        filepath = downpath + '\批量打包.zip'
        time.sleep(4)
        namelist = self.公共操作.查看zip文件(zip文件路径=filepath)
        for name in ['素材1.png', '二级目录/检入检出素材.txt']:
            if not name in namelist or len(namelist) != 2:
                raise AssertionError("在打包的文件中未查看到被打包的文件或目录")

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
        # 勾选多个文件，点击收藏，可以收藏成功
        self.click(项目对象库.目录节点.format('1'))
        self.click(项目对象库.列表复选框.format('素材1.png'))
        self.click(项目对象库.列表复选框.format('素材2.jpg'))
        self.click(项目对象库.工具栏按钮.format("收藏"))
        self.wait(公共元素对象库.系统提示信息弹框.format("收藏成功"), 3)
        序号 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]',
                                   文件名称='素材1.png')
        序号2 = self.公共操作.获取文件在列表中的行号(列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]',
                                    文件名称='素材2.jpg')
        if not self.wait(项目对象库.已选_悬浮列收藏.format(序号), 3) or not self.wait(项目对象库.已选_悬浮列收藏.format(序号), 3):
            raise AssertionError("点击收藏文件成功后，文件的收藏按钮未被点亮")
        self.进入到操作位置.进入收藏页()
        if not self.wait(收藏对象库.资源类型.format("素材1.png", "批量收藏资源"), 3) or not \
                self.wait(收藏对象库.资源类型.format("素材2.jpg", "批量收藏资源"), 3):
            raise AssertionError("点击文件批量收藏按钮，文件没有被收藏")
        # 勾选多个目录，点击收藏，可以收藏成功
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
        # 勾选文件和目录，点击收藏，可以收藏成功
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


class 设置页冒烟实现(page):
    def __init__(self,Secdriver = None):
        page.__init__(self,secdriver=Secdriver)
        self.滑块验证=滑块验证(Secdriver=Secdriver)
        self.公共操作 = 公共操作(Secdriver=Secdriver)
        self.生命周期管理页面 = 生命周期管理页面(Secdriver=Secdriver)
        self.版次管理页面 = 版次管理页面(Secdriver=Secdriver)
        self.属性管理页面 = 属性管理页面(Secdriver=Secdriver)
        self.项目页面 = 项目页面(Secdriver=Secdriver)
        self.用户信息页面 = 用户信息页面(Secdriver=Secdriver)
        self.项目管理页面 = 项目管理页面(Secdriver=Secdriver)
        self.进入到操作位置 = 进入到操作位置(Secdriver=Secdriver)

    def 数据准备(self):
        self.项目管理页面.删除所有项目()

    def 创建生命周期(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="权限编辑")
        self.进入到操作位置.进入生命周期工作区()
        self.生命周期管理页面.删除生命周期(生命周期名称='创建生命周期')
        self.click(设置页对象库.生命周期管理工作区.新增)
        self.wait(对话框对象库.弹框标题.format("新增生命周期"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "创建生命周期")
        # 点击新增生命周期节点，生命周期节点列表中新增一行空白生命周期节点
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        if not self.wait(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, 3):
            raise AssertionError("点击添加生命周期节点按钮，未添加新的生命周期节点")
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "33")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        # 点击生命周期节点行的编辑按钮，生命周期行进入编辑状态
        self.click(设置页对象库.生命周期管理工作区.编辑生命周期节点按钮.format("33"))
        if not self.wait(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, 3) or not \
                self.wait(设置页对象库.生命周期管理工作区.生命周期节点描述输入框, 3):
            raise AssertionError("点击编辑生命周期节点按钮，生命周期节点未进入编辑状态")
        self.clear_by_key(设置页对象库.生命周期管理工作区.生命周期节点名称输入框)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, '44')
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        #点击生命周期节点行，点击删除按钮，生命周期行被删除
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("44"))
        self.click(设置页对象库.生命周期管理工作区.删除生命周期节点)
        if self.wait(设置页对象库.生命周期管理工作区.生命周期节点名称.format("44"), 3):
            raise AssertionError("进行删除生命周期节点操作后，在生命周期节点列表仍然能查看到被删除的生命周期节点")
        # 点击生命周期节点行，点击上移按钮，节点行上移一行，点击下移按钮，节点行下移一行
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
        self.click(设置页对象库.生命周期管理工作区.下移生命周期节点)
        text = self.driver.getelement('//div[text()="生命周期节点"]/following-sibling::div//tr[1]/td[1]//span').text
        if text == "11":
            raise AssertionError("点击下移生命周期节点，但是生命周期节点并未下移")
        self.click(设置页对象库.生命周期管理工作区.上移生命周期节点)
        text = self.driver.getelement('//div[text()="生命周期节点"]/following-sibling::div//tr[1]/td[1]//span').text
        if text != "11":
            raise AssertionError("点击上移生命周期节点，但是生命周期节点并未上移")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("22"))
        self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("22", "11"))
        self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        if not self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format("创建生命周期"), 3):
            raise AssertionError("创建生命周期时点击确定，生命周期未被保存")

    def 升版设置(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="升版测试")
        self.进入到操作位置.进入生命周期工作区()
        self.生命周期管理页面.删除生命周期('升版周期升版测试')
        self.click(设置页对象库.生命周期管理工作区.新增)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新增生命周期"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "升版周期升版测试")
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "33")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "44")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("22"))
        # 点击生命周期节点，右侧节点流程显示当前节点与上级节点的流程和当前节点与下级节点的流程
        if not self.wait(设置页对象库.生命周期管理工作区.开始节点和结束节点.format("22", "11"), 3) or not \
                self.wait(设置页对象库.生命周期管理工作区.开始节点和结束节点.format("22", "33"), 3) or not \
                self.wait(设置页对象库.生命周期管理工作区.开始节点和结束节点.format("22", "44"), 3):
            raise AssertionError("点击查看节点流程，跨节点的节点流程显示不全")
        # 不选择跨节点，右侧节点流程中不出现跨节点流程，选择跨节点，右侧节点流程出现跨节点流程
        self.click(公共元素对象库.单选按钮.format("是否跨节点"))
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("22"))
        if self.wait(设置页对象库.生命周期管理工作区.开始节点和结束节点.format("22", "44"), 3):
            raise AssertionError("点击查看节点流程，不勾选是否跨节点按钮，但是却显示跨节点流程")
        # 设置升版流程，项目生命周期经过此流程时，项目进行升版
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
        self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("11", "22"))
        self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.创建空白项目(项目名称="升版测试", 生命周期名称="升版周期升版测试")
        self.项目管理页面.点击进入项目(项目名称="升版测试")
        self.项目页面.上传单个文件(目录路径=['升版测试'], 文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'])
        self.项目页面.改变文件状态(目录路径=['升版测试'], 文件名='检入检出素材.txt', 状态名称='22')
        if not self.wait('//div[contains(@class,"pane-two")]//tr[1]/td[5]/div[text()="B"]', 30):
            raise AssertionError("设置升版流程，项目生命周期经过此流程时，项目并没有进行升版")
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="升版测试")

    def 编辑生命周期(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="权限编辑")
        self.进入到操作位置.进入生命周期工作区()
        self.生命周期管理页面.删除生命周期('生命周期')
        self.click(设置页对象库.生命周期管理工作区.新增)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新增生命周期"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "生命周期")
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
        self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("11", "22"))
        self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        # 选择生命周期后，点击编辑，进入编辑生命周期界面
        self.click(设置页对象库.生命周期管理工作区.生命周期名称.format("生命周期"))
        self.click(设置页对象库.生命周期管理工作区.编辑)
        if not self.wait(对话框对象库.弹框标题.format("编辑生命周期"), 3):
            raise AssertionError("选择生命周期后点击编辑，未弹出编辑生命周期的界面")
        self.click(公共元素对象库.输入框.format("名称"))
        self.clear_by_key(公共元素对象库.输入框.format("名称"))
        self.send_keys(公共元素对象库.输入框.format("名称"),"编辑生命周期")
        # 点击新增生命周期节点，生命周期节点列表中新增一行空白生命周期节点
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        if not self.wait(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, 3):
            raise AssertionError("点击添加生命周期节点按钮，未添加新的生命周期节点")
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "33")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        # 点击生命周期节点行的编辑按钮，生命周期行进入编辑状态
        self.click(设置页对象库.生命周期管理工作区.编辑生命周期节点按钮.format("33"))
        if not self.wait(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, 3) or not \
                self.wait(设置页对象库.生命周期管理工作区.生命周期节点描述输入框, 3):
            raise AssertionError("点击编辑生命周期节点按钮，生命周期节点未进入编辑状态")
        self.clear_by_key(设置页对象库.生命周期管理工作区.生命周期节点名称输入框)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, '44')
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        # 点击生命周期节点行，点击删除按钮，生命周期行被删除
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("44"))
        self.click(设置页对象库.生命周期管理工作区.删除生命周期节点)
        if self.wait(设置页对象库.生命周期管理工作区.生命周期节点名称.format("44"), 3):
            raise AssertionError("进行删除生命周期节点操作后，在生命周期节点列表仍然能查看到被删除的生命周期节点")
        # 点击生命周期节点行，点击上移按钮，节点行上移一行，点击下移按钮，节点行下移一行
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
        self.click(设置页对象库.生命周期管理工作区.下移生命周期节点)
        text = self.driver.getelement('//div[text()="生命周期节点"]/following-sibling::div//tr[1]/td[1]//span').text
        if text == "11":
            raise AssertionError("点击下移生命周期节点，但是生命周期节点并未下移")
        self.click(设置页对象库.生命周期管理工作区.上移生命周期节点)
        text = self.driver.getelement('//div[text()="生命周期节点"]/following-sibling::div//tr[1]/td[1]//span').text
        if text != "11":
            raise AssertionError("点击上移生命周期节点，但是生命周期节点并未上移")
        self.click(对话框对象库.弹框按钮.format("编辑生命周期", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        if not self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format("编辑生命周期"), 3):
            raise AssertionError("编辑生命周期时点击确定，生命周期未被保存")

    def 编辑生命周期升版流程(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="升版测试")
        self.进入到操作位置.进入生命周期工作区()
        self.生命周期管理页面.删除生命周期('test3')
        self.click(设置页对象库.生命周期管理工作区.新增)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新增生命周期"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test3")
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "33")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "44")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
        self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("11", "22"))
        self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
        self.click(设置页对象库.生命周期管理工作区.生命周期名称.format("test3"))
        self.click(设置页对象库.生命周期管理工作区.编辑)
        self.wait(对话框对象库.弹框标题.format("编辑生命周期"), 3)
        # 不选择跨节点，右侧节点流程中不出现跨节点流程，选择跨节点，右侧节点流程出现跨节点流程
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("22"))
        if not self.wait(设置页对象库.生命周期管理工作区.开始节点和结束节点.format("22", "11"), 3) or not \
                self.wait(设置页对象库.生命周期管理工作区.开始节点和结束节点.format("22", "33"), 3) or not \
                self.wait(设置页对象库.生命周期管理工作区.开始节点和结束节点.format("22", "44"), 3):
            raise AssertionError("点击查看节点流程，跨节点的节点流程显示不全")
        self.click(公共元素对象库.单选按钮.format("是否跨节点"))
        if self.wait(设置页对象库.生命周期管理工作区.开始节点和结束节点.format("22", "44"), 3):
            raise AssertionError("点击查看节点流程，不勾选是否跨节点按钮，但是却显示跨节点流程")
        # # 设置升版流程，项目生命周期经过此流程时，项目进行升版
        self.click(公共元素对象库.单选按钮.format("是否跨节点"))
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
        self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("11", "44"))
        self.click(对话框对象库.弹框按钮.format("编辑生命周期", "确定"))
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.创建空白项目(项目名称="升版测试", 生命周期名称="test3")
        self.项目管理页面.点击进入项目(项目名称="升版测试")
        self.项目页面.上传单个文件(目录路径=['升版测试'], 文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'])
        self.项目页面.改变文件状态(目录路径=['升版测试'], 文件名='检入检出素材.txt', 状态名称='44')
        if not self.wait('//div[contains(@class,"pane-two")]//tr[1]/td[5]/div[text()="B"]', 3):
            raise AssertionError("设置升版流程，项目生命周期经过此流程时，项目并没有进行升版")

    def 复制生命周期(self):
        self.进入到操作位置.进入生命周期工作区()
        self.生命周期管理页面.删除生命周期('生命周期')
        self.click(设置页对象库.生命周期管理工作区.新增)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新增生命周期"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "生命周期")
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "33")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "44")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
        self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("11", "22"))
        self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
        # 择生命周期后，点击复制，进入复制生命周期界面
        self.click(设置页对象库.生命周期管理工作区.生命周期名称.format("生命周期"))
        self.click(设置页对象库.生命周期管理工作区.复制)
        if not self.wait(对话框对象库.弹框标题.format("复制生命周期"), 3):
            raise AssertionError("选择生命周期后点击复制，未弹出复制生命周期界面")
        self.clear_by_key(公共元素对象库.输入框.format("名称"))
        self.send_keys(公共元素对象库.输入框.format("名称"), "复制生命周期")
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "55")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        # 点击生命周期节点行的编辑按钮，生命周期行进入编辑状态
        self.click(设置页对象库.生命周期管理工作区.编辑生命周期节点按钮.format("55"))
        if not self.wait(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, 3) or not \
                self.wait(设置页对象库.生命周期管理工作区.生命周期节点描述输入框, 3):
            raise AssertionError("点击编辑生命周期节点按钮，生命周期节点未进入编辑状态")
        self.clear_by_key(设置页对象库.生命周期管理工作区.生命周期节点名称输入框)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, '66')
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        # 点击生命周期节点行，点击删除按钮，生命周期行被删除
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("66"))
        self.click(设置页对象库.生命周期管理工作区.删除生命周期节点)
        if self.wait(设置页对象库.生命周期管理工作区.生命周期节点名称.format("66"), 3):
            raise AssertionError("进行删除生命周期节点操作后，在生命周期节点列表仍然能查看到被删除的生命周期节点")
        self.click(对话框对象库.弹框按钮.format("复制生命周期", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        if not self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format("复制生命周期"), 3):
            raise AssertionError("在复制生命周期界面，编辑生命周期名称后点击复制，没有复制成功")

    def 复制生命周期升版流程(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="升版测试")
        self.进入到操作位置.进入生命周期工作区()
        self.生命周期管理页面.删除生命周期('test6')
        self.click(设置页对象库.生命周期管理工作区.新增)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新增生命周期"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test6")
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "33")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "44")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
        self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("11", "22"))
        self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
        self.click(设置页对象库.生命周期管理工作区.生命周期名称.format("test6"))
        self.click(设置页对象库.生命周期管理工作区.复制)
        self.wait(对话框对象库.弹框标题.format("复制生命周期"), 3)
        # 不选择跨节点，右侧节点流程中不出现跨节点流程，选择跨节点，右侧节点流程出现跨节点流程
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("22"))
        if not self.wait(设置页对象库.生命周期管理工作区.开始节点和结束节点.format("22", "11"), 3) or not \
                self.wait(设置页对象库.生命周期管理工作区.开始节点和结束节点.format("22", "33"), 3) or not \
                self.wait(设置页对象库.生命周期管理工作区.开始节点和结束节点.format("22", "44"), 3):
            raise AssertionError("点击查看节点流程，跨节点的节点流程显示不全")
        self.click(公共元素对象库.单选按钮.format("是否跨节点"))
        if self.wait(设置页对象库.生命周期管理工作区.开始节点和结束节点.format("22", "44"), 3):
            raise AssertionError("点击查看节点流程，不勾选是否跨节点按钮，但是却显示跨节点流程")
        # 设置升版流程，项目生命周期经过此流程时，项目进行升版
        self.click(对话框对象库.弹框按钮.format("复制生命周期", "取消"))
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.创建空白项目(项目名称="升版测试", 生命周期名称="test6")
        self.项目管理页面.点击进入项目(项目名称="升版测试")
        self.项目页面.上传单个文件(目录路径=['升版测试'], 文件路径=['TestData', 'FrontData', '项目页', '检入检出素材.txt'])
        self.项目页面.改变文件状态(目录路径=['升版测试'], 文件名='检入检出素材.txt', 状态名称='22')
        if not self.wait('//div[contains(@class,"pane-two")]//tr[1]/td[5]/div[text()="B"]', 3):
            raise AssertionError("设置升版流程，项目生命周期经过此流程时，项目并没有进行升版")

    def 删除生命周期(self):
        self.进入到操作位置.进入生命周期工作区()
        if not self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format("delete1"), 3):
            self.click(设置页对象库.生命周期管理工作区.新增)
            self.default_content()
            self.wait(对话框对象库.弹框标题.format("新增生命周期"), 3)
            self.send_keys(公共元素对象库.输入框.format("名称"), "delete1")
            self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
            self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
            self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
            self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
            self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
            self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
            self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
            self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("11", "22"))
            self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
            self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        # 勾选单个生命周期，点击删除，弹出删除提示对话框
        self.click(设置页对象库.生命周期管理工作区.生命周期列表复选框.format("delete1"))
        self.click(设置页对象库.生命周期管理工作区.删除)
        if not self.wait(对话框对象库.对话框标题.format("提示"), 3):
            raise AssertionError("勾选单个生命周期，点击删除，系统未弹出删除确认对话框")
        # 点击确定删除提示对话框，查看生命周期是否被删除
        self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("删除成功"), 3)
        if self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format("delete1"), 3):
            raise AssertionError("点击确定删除确认对话框，被选择的生命周期未被删除")
        #系统上面周期不可以被删除
        self.click(设置页对象库.生命周期管理工作区.生命周期列表复选框.format("系统"))
        self.click(设置页对象库.生命周期管理工作区.删除)
        if self.wait(对话框对象库.对话框标题.format("提示"), 3):
            raise AssertionError("系统生命周期模板可以进行删除操作")

    def 批量删除生命周期(self):
        self.进入到操作位置.进入生命周期工作区()
        if not self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format("delete1"), 3):
            self.click(设置页对象库.生命周期管理工作区.新增)
            self.default_content()
            self.wait(对话框对象库.弹框标题.format("新增生命周期"), 3)
            self.send_keys(公共元素对象库.输入框.format("名称"), "delete1")
            self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
            self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
            self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
            self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
            self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
            self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
            self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
            self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("11", "22"))
            self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
            self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        if not self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format("delete2"), 3):
            self.click(设置页对象库.生命周期管理工作区.新增)
            self.default_content()
            self.wait(对话框对象库.弹框标题.format("新增生命周期"), 3)
            self.send_keys(公共元素对象库.输入框.format("名称"), "delete2")
            self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
            self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
            self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
            self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
            self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
            self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
            self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
            self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("11", "22"))
            self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
            self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        # 勾选多个生命周期，点击删除，弹出删除提示对话框
        self.click(设置页对象库.生命周期管理工作区.生命周期列表复选框.format("delete1"))
        self.click(设置页对象库.生命周期管理工作区.生命周期列表复选框.format("delete2"))
        self.click(设置页对象库.生命周期管理工作区.删除)
        if not self.wait(对话框对象库.对话框标题.format("提示"), 3):
            raise AssertionError("勾选多个生命周期，点击删除，系统未弹出删除确认对话框")
        self.click(对话框对象库.关闭对话框.format("提示"))
        # 当勾选的生命周期中含有系统生命周期时，删除按钮不可用
        self.click(设置页对象库.生命周期管理工作区.生命周期列表复选框.format("系统"))
        if not self.wait('//div[@class="life_cycle_btns comm_bgc"]//button[@disabled="disabled"]/span[text()="删除"]', 3):
            raise AssertionError("当勾选的生命周期中含有系统生命周期时，删除按钮应该不可用")
        # 点击确定删除提示对话框，查看生命周期是否被删除
        self.driver.refrsh()
        self.click(设置页对象库.生命周期管理工作区.生命周期列表复选框.format("delete1"))
        self.click(设置页对象库.生命周期管理工作区.生命周期列表复选框.format("delete2"))
        self.click(设置页对象库.生命周期管理工作区.删除)
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format("delete1"), 3) or \
                self.wait(设置页对象库.生命周期管理工作区.生命周期名称.format("delete2"), 3):
            raise AssertionError("点击确认删除确认对话框，被选择的生命周期未被删除")

    def 设置默认生命周期(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="升版测试")
        self.项目管理页面.删除项目(项目名称="系统默认生命周期")
        self.进入到操作位置.进入生命周期工作区()
        self.生命周期管理页面.删除生命周期('test7')
        self.click(设置页对象库.生命周期管理工作区.新增)
        self.default_content()
        self.wait(对话框对象库.弹框标题.format("新增生命周期"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test7")
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "11")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.添加生命周期节点)
        self.send_keys(设置页对象库.生命周期管理工作区.生命周期节点名称输入框, "22")
        self.click(设置页对象库.生命周期管理工作区.生命周期节点保存按钮)
        self.click(设置页对象库.生命周期管理工作区.生命周期节点名称.format("11"))
        self.click(设置页对象库.生命周期管理工作区.节点流程单选启用按钮.format("11", "22"))
        self.click(对话框对象库.弹框按钮.format("新增生命周期", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        # 点击生命周期列表中的生命周期，生命周期节点列表显示改生命周期下的生命周期节点
        self.click(设置页对象库.生命周期管理工作区.生命周期名称.format("test7"))
        if not self.wait(设置页对象库.生命周期管理工作区.生命周期节点.format("11"), 3) or \
                not self.wait(设置页对象库.生命周期管理工作区.生命周期节点.format("22"), 3):
            raise AssertionError("点击生命周期，在生命周期明细中并未查看到生命周期下的所有节点")
        # 点击对应的生命周期节点，节点流程列表显示该节点对应的节点流程
        self.click(设置页对象库.生命周期管理工作区.生命周期节点.format("11"))
        if not self.wait(设置页对象库.生命周期管理工作区.节点流程.format("11", "22"), 3):
            raise AssertionError("点击生命周期节点，节点流程列表未显示该节点下的节点流程")
        # 勾选生命周期列表，生命周期行的是否默认单选按钮，设置对应的生命周期为默认生命周期
        self.click(设置页对象库.生命周期管理工作区.设置默认单选框.format("test7"))
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="默认生命周期")
        self.click(项目管理对象库.创建新项目)
        self.wait(创建项目页面.页面名称, 3)
        self.click(创建项目页面.创建空白项目)
        self.wait(对话框对象库.弹框标题.format("项目名称"), 3)
        self.clear(公共元素对象库.输入框.format("项目名称"))
        self.send_keys(公共元素对象库.输入框.format("项目名称"), "默认生命周期")
        self.click(创建项目页面.提交按钮)
        self.default_content()
        self.wait(项目设置页面.项目成员tab页, 3)
        self.click(公共元素对象库.列表框.format("生命周期"))
        if not self.wait('//ul/li[contains(@class,"dropdown__item selected")]/span[text()="test7"]', 3):
            raise AssertionError("设置test7未默认生命周期，创建新项目，项目的生命周期未默认选择test7")


    def 新增版次(self):
        self.进入到操作位置.进入版次工作区()
        self.版次管理页面.删除版次(版次名称='test')
        self.click(设置页对象库.版次管理工作区.新增)
        if not self.wait(对话框对象库.弹框标题.format("新增"), 3):
            raise AssertionError("点击新增版次，未弹出新增版次界面")
        self.send_keys(公共元素对象库.输入框.format("名称"), "test")
        #添加节点
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "A")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        if not self.wait(设置页对象库.版次管理工作区.版次内容.format("A"),3):
            raise AssertionError("添加版次节点失败")
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "B")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        #移动版次节点
        self.click(设置页对象库.版次管理工作区.版次内容.format("A"))
        self.click(设置页对象库.版次管理工作区.下移版次节点)
        index1 = self.driver.getelement('//tr/td//span[text()="A"]/ancestor::tr/td[1]/div/div').text
        if index1 == '1':
            raise AssertionError("对版次节点进行下移操作，版次节点并未下移")
        self.click(设置页对象库.版次管理工作区.版次内容.format("A"))
        self.click(设置页对象库.版次管理工作区.上移版次节点)
        index1 = self.driver.getelement('//tr/td//span[text()="A"]/ancestor::tr/td[1]/div/div').text
        if index1 != '1':
            raise AssertionError("对版次节点进行上移操作，版次节点并未上移")
        #编辑节点
        self.click(设置页对象库.版次管理工作区.编辑版次节点按钮.format("B"))
        if not self.wait(设置页对象库.版次管理工作区.版次内容输入框, 3):
            raise AssertionError("点击版次节点编辑按钮，版次节点未进入编辑状态")
        self.clear_by_key(设置页对象库.版次管理工作区.版次内容输入框)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "C")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        if not self.wait(设置页对象库.版次管理工作区.版次内容.format("C"),3):
            raise AssertionError("编辑版次节点失败")
        #删除节点
        self.click(设置页对象库.版次管理工作区.版次内容.format("A"))
        self.click(设置页对象库.版次管理工作区.删除版次节点)
        if self.wait(设置页对象库.版次管理工作区.版次内容.format("A"),3):
            raise AssertionError("删除版次节点失败")
        self.click(对话框对象库.弹框按钮.format("新增", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"))
        if not self.wait(设置页对象库.版次管理工作区.版次名称.format("test"), 3):
            raise AssertionError("新增版次时，点击确定保存按钮，新增的版次未被保存")
        self.click(设置页对象库.版次管理工作区.版次名称.format("test"))
        if not self.wait(设置页对象库.版次管理工作区.版次明细节点.format("C"),3):
            raise AssertionError("点击版次后，版次明细未显示版次节点")

    def 编辑版次(self):
        self.进入到操作位置.进入版次工作区()
        self.版次管理页面.删除版次(版次名称='test')
        self.click(设置页对象库.版次管理工作区.新增)
        self.wait(对话框对象库.弹框标题.format("新增"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test")
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        self.wait(设置页对象库.版次管理工作区.版次内容输入框, 3)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "A")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        self.click(对话框对象库.弹框按钮.format("新增", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"))
        # 选择版次后，点击编辑，进入编辑版次界面
        self.click(设置页对象库.版次管理工作区.版次名称.format("test"))
        self.click(设置页对象库.版次管理工作区.编辑)
        if not self.wait(对话框对象库.弹框标题.format("编辑"), 3):
            raise AssertionError("选择版次，点击编辑按钮，未弹出编辑版次界面")
        self.clear_by_key(公共元素对象库.输入框.format("名称"))
        self.send_keys(公共元素对象库.输入框.format("名称"), "编辑版次")
        #编辑版次界面新增版次节点
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "B")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        if not self.wait(设置页对象库.版次管理工作区.版次内容.format("B"), 3):
            raise AssertionError("添加版次节点失败")
        # 移动版次节点
        self.click(设置页对象库.版次管理工作区.版次内容.format("A"))
        self.click(设置页对象库.版次管理工作区.下移版次节点)
        index1 = self.driver.getelement('//div[@aria-label="编辑"]//tr/td//span[text()="A"]/ancestor::tr/td[1]/div/div').text
        if index1 == '1':
            raise AssertionError("对版次节点进行下移操作，版次节点并未下移")
        self.click(设置页对象库.版次管理工作区.版次内容.format("A"))
        self.click(设置页对象库.版次管理工作区.上移版次节点)
        index1 = self.driver.getelement('//tr/td//span[text()="A"]/ancestor::tr/td[1]/div/div').text
        if index1 != '1':
            raise AssertionError("对版次节点进行上移操作，版次节点并未上移")
        # 编辑节点
        self.click(设置页对象库.版次管理工作区.编辑版次节点按钮.format("B"))
        if not self.wait(设置页对象库.版次管理工作区.版次内容输入框, 3):
            raise AssertionError("点击版次节点编辑按钮，版次节点未进入编辑状态")
        self.clear_by_key(设置页对象库.版次管理工作区.版次内容输入框)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "C")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        if not self.wait(设置页对象库.版次管理工作区.版次内容.format("C"), 3):
            raise AssertionError("编辑版次节点失败")
        # 删除节点
        self.click(设置页对象库.版次管理工作区.版次内容.format("A"))
        self.click(设置页对象库.版次管理工作区.删除版次节点)
        if self.wait(设置页对象库.版次管理工作区.版次内容.format("A"), 3):
            raise AssertionError("删除版次节点失败")
        self.click(对话框对象库.弹框按钮.format("编辑", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"))
        if not self.wait(设置页对象库.版次管理工作区.版次名称.format("编辑版次"), 3):
            raise AssertionError("编辑版次时，点击确定保存按钮，新增的版次未被保存")
        self.click(设置页对象库.版次管理工作区.版次名称.format("编辑版次"))
        if not self.wait(设置页对象库.版次管理工作区.版次明细节点.format("C"), 3):
            raise AssertionError("点击版次后，版次明细未显示版次节点")

    def 删除版次(self):
        self.进入到操作位置.进入版次工作区()
        self.版次管理页面.删除版次(版次名称='test')
        self.click(设置页对象库.版次管理工作区.新增)
        self.wait(对话框对象库.弹框标题.format("新增"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test")
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        self.wait(设置页对象库.版次管理工作区.版次内容输入框, 3)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "A")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        self.click(对话框对象库.弹框按钮.format("新增", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        # 勾选单个版次，点击删除，弹出删除提示对话框
        self.click(设置页对象库.版次管理工作区.版次复选框.format("test"))
        self.click(设置页对象库.版次管理工作区.删除)
        if not self.wait(对话框对象库.对话框标题.format("提示"), 3):
            raise AssertionError("勾选单个版次，点击删除，系统未弹出删除确认对话框")
        self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if self.wait(设置页对象库.版次管理工作区.版次名称.format("test"), 3):
            raise AssertionError("点击确定删除确认对话框，被选择的版次未被删除")
        #系统版次不可以被删除
        if not self.wait(设置页对象库.版次管理工作区.禁用_版次复选框.format("系统"),3):
            raise AssertionError("系统版次可以被删除成功")

    def 批量删除版次(self):
        self.进入到操作位置.进入版次工作区()
        self.版次管理页面.删除版次(版次名称='test')
        self.click(设置页对象库.版次管理工作区.新增)
        self.wait(对话框对象库.弹框标题.format("新增"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test")
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        self.wait(设置页对象库.版次管理工作区.版次内容输入框, 3)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "A")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        self.click(对话框对象库.弹框按钮.format("新增", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        self.版次管理页面.删除版次(版次名称='test1')
        self.click(设置页对象库.版次管理工作区.新增)
        self.wait(对话框对象库.弹框标题.format("新增"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "test1")
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        self.wait(设置页对象库.版次管理工作区.版次内容输入框, 3)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "A")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        self.click(对话框对象库.弹框按钮.format("新增", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        # 勾选多个版次，点击删除，弹出删除提示对话框
        self.click(设置页对象库.版次管理工作区.版次复选框.format("test"))
        self.click(设置页对象库.版次管理工作区.版次复选框.format("test1"))
        self.click(设置页对象库.版次管理工作区.删除)
        if not self.wait(对话框对象库.对话框标题.format("提示"), 3):
            raise AssertionError("勾选单个版次，点击删除，系统未弹出删除确认对话框")
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if self.wait(设置页对象库.版次管理工作区.版次名称.format("test"), 3) or \
                self.wait(设置页对象库.版次管理工作区.版次名称.format("test1"), 3):
            raise AssertionError("点击确定删除确认对话框，被选择的版次未被删除")

    def 设置默认版次(self):
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="默认版次")
        self.项目管理页面.删除项目(项目名称="默认生命周期")
        self.进入到操作位置.进入版次工作区()
        self.click(设置页对象库.版次管理工作区.是否默认单选框.format("系统"))
        self.版次管理页面.删除版次(版次名称='设置默认版次')
        self.click(设置页对象库.版次管理工作区.新增)
        self.wait(对话框对象库.弹框标题.format("新增"), 3)
        self.send_keys(公共元素对象库.输入框.format("名称"), "设置默认版次")
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        self.wait(设置页对象库.版次管理工作区.版次内容输入框, 3)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "A")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        self.click(设置页对象库.版次管理工作区.添加版次节点)
        self.wait(设置页对象库.版次管理工作区.版次内容输入框, 3)
        self.send_keys(设置页对象库.版次管理工作区.版次内容输入框, "B")
        self.click(设置页对象库.版次管理工作区.保存版次节点)
        self.click(对话框对象库.弹框按钮.format("新增", "确定"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        # 点击版次列表中的版次，版次明细列表显示该版次下的版次节点
        self.click(设置页对象库.版次管理工作区.版次名称.format("设置默认版次"))
        if not self.wait(设置页对象库.版次管理工作区.版次明细节点.format("A"), 3) or \
                not self.wait(设置页对象库.版次管理工作区.版次明细节点.format("B"), 3):
            raise AssertionError("点击版次，版次明细中未显示该版次下的所有版次节点")
        # 勾选版次列表，版次行的是否默认单选按钮，设置对应的版次为默认版次
        self.click(设置页对象库.版次管理工作区.是否默认单选框.format("设置默认版次"))
        self.进入到操作位置.进入项目管理页()
        self.click(项目管理对象库.创建新项目)
        self.wait(创建项目页面.页面名称, 3)
        self.click(创建项目页面.创建空白项目)
        self.wait(对话框对象库.弹框标题.format("项目名称"), 3)
        self.clear(公共元素对象库.输入框.format("项目名称"))
        self.send_keys(公共元素对象库.输入框.format("项目名称"), "默认版次")
        self.click(创建项目页面.提交按钮)
        self.default_content()
        self.wait(项目设置页面.项目成员tab页, 3)
        self.click(公共元素对象库.列表框.format("版次"))
        if not self.wait('//ul/li[contains(@class,"dropdown__item selected")]/span[text()="设置默认版次"]', 3):
            raise AssertionError("设置test2为默认版次，创建新项目，项目的版次未默认选择设置默认版次")


    def 属性系统管理(self):
        #新增属性系统
        self.进入到操作位置.进入属性工作区()
        self.属性管理页面.删除属性系统(属性系统名称="test")
        # 点击属性列表属性新增按钮，属性列表新增一行属性系统，属性系统处于编辑状态
        self.click(设置页对象库.属性管理工作区.新增)
        if not self.wait(设置页对象库.属性管理工作区.属性系统名称输入框, 3):
            raise AssertionError("点击新增属性系统，属性系统列表未新增一行属性系统")
        self.clear(设置页对象库.属性管理工作区.属性系统名称输入框)
        self.send_keys(设置页对象库.属性管理工作区.属性系统名称输入框, "test")
        self.click(设置页对象库.属性管理工作区.属性系统保存按钮)
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"))
        if self.wait(设置页对象库.属性管理工作区.属性系统名称输入框, 3):
            raise AssertionError("点击保存属性系统，属性系统列表中新增的属性系统行的编辑状态未改变")
        if not self.wait(设置页对象库.属性管理工作区.属性系统名称.format("test"), 3):
            raise AssertionError("新增属性系统失败")
        #编辑属性系统
        # 点击属性系统，点击编辑按钮，被选中的属性系统处于编辑状态
        self.click(设置页对象库.属性管理工作区.属性系统名称.format("test"))
        self.click(设置页对象库.属性管理工作区.编辑)
        if not self.wait(设置页对象库.属性管理工作区.属性系统名称输入框, 3):
            raise AssertionError("点击编辑属性系统，属性系统未进入编辑状态")
        self.clear_by_key(设置页对象库.属性管理工作区.属性系统名称输入框)
        self.send_keys(设置页对象库.属性管理工作区.属性系统名称输入框, "test2")
        self.click(设置页对象库.属性管理工作区.属性系统保存按钮)
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"))
        if self.wait(设置页对象库.属性管理工作区.属性系统名称输入框, 3):
            raise AssertionError("点击保存属性系统，属性系统列表中新增的属性系统行的编辑状态未改变")
        if not self.wait(设置页对象库.属性管理工作区.属性系统名称.format("test2"), 3):
            raise AssertionError("编辑属性系统后，点击保存，编辑的属性系统未被保存")
        #删除系统
        self.属性管理页面.创建属性系统(属性系统名称="test3")
        self.属性管理页面.创建属性系统(属性系统名称="test4")
        self.click(设置页对象库.属性管理工作区.属性系统复选框.format("test2"))
        self.click(设置页对象库.属性管理工作区.删除)
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if self.wait(设置页对象库.属性管理工作区.属性系统名称.format("test2"), 3):
            raise AssertionError("点击确定删除确认对话框，属性系统为被删除")
        self.click(设置页对象库.属性管理工作区.属性系统复选框.format("test3"))
        self.click(设置页对象库.属性管理工作区.属性系统复选框.format("test4"))
        self.click(设置页对象库.属性管理工作区.删除)
        self.wait(对话框对象库.对话框标题.format("提示"), 3)
        self.click(对话框对象库.对话框按钮.format("提示", "确定"))
        if self.wait(设置页对象库.属性管理工作区.属性系统名称.format("test3"), 3) or \
                self.wait(设置页对象库.属性管理工作区.属性系统名称.format("test4"), 3):
            raise AssertionError("点击确定删除确认对话框，属性系统未被删除")
        #系统属性模板不能被删除
        self.move_to_element(设置页对象库.属性管理工作区.属性系统复选框.format("系统"))
        if not self.wait(设置页对象库.属性管理工作区.禁用_属性系统复选框.format("系统"),3):
            raise AssertionError("系统模板属性可以进行删除操作")

    def 添加属性(self):
        self.进入到操作位置.进入属性工作区()
        self.属性管理页面.删除属性系统(属性系统名称="test")
        self.属性管理页面.创建属性系统(属性系统名称="test")
        self.click(设置页对象库.属性管理工作区.属性系统名称.format("test"))
        # 点击下载模板，属性模板可以正常下载
        self.click(设置页对象库.属性管理工作区.下载模板)
        downpath = self.公共操作.检查文件是否下载完成()
        filepath = downpath + '\项目属性模板表.xlsx'
        time.sleep(4)
        print(filepath)
        if not os.path.exists(filepath):
            raise AssertionError("在下载目录下未查看到下载的模板文件")
        ##正确填写模板，使用导入属性，可以正常导入
        self.click(设置页对象库.属性管理工作区.导入属性)
        self.公共操作.win上传文件(文件路径=['TestData', 'FrontData', '项目页', '项目属性模板表.xlsx'])
        if not self.wait(设置页对象库.属性管理工作区.行删除按钮.format("1"), 3):
            raise AssertionError("导入填写的属性模板后，未查看到导入的属性")
        # 属性列表中，点击删除属性行操作，出现属性删除提示框
        self.click(设置页对象库.属性管理工作区.行删除按钮.format("1"))
        if not self.wait(设置页对象库.属性管理工作区.删除对话框, 3):
            raise AssertionError("点击删除单个属性，未查看到删除确认对话框")
        # 属性删除提示框点击确定，属性被删除
        self.click(设置页对象库.属性管理工作区.删除确认按钮)
        if self.wait(设置页对象库.属性管理工作区.行删除按钮.format("1"), 3):
            raise AssertionError("点击删除单个属性，点击确认删除确认对话框后，该属性未被删除")
        # 点击添加属性，属性列表新增一行属性
        self.click(设置页对象库.属性管理工作区.添加属性)
        if not self.wait(设置页对象库.属性管理工作区.属性类别输入框.format("1"), 3):
            raise AssertionError("点击添加属性按钮，属性列表未新增一行属性")
        self.send_keys(设置页对象库.属性管理工作区.属性类别输入框.format("1"),'属性1')
        self.send_keys(设置页对象库.属性管理工作区.属性名称输入框.format("1"),'属性1')
        self.click(设置页对象库.属性管理工作区.行保存按钮.format("1"))
        if not self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3):
            raise AssertionError("添加属性成功后，没有提示信息")
        #编辑属性
        self.click(设置页对象库.属性管理工作区.行保存按钮.format("1"))
        if not self.wait(设置页对象库.属性管理工作区.属性类别输入框.format("1"), 3):
            raise AssertionError("点击编辑属性行，属性行未进入编辑状态")
        self.clear(设置页对象库.属性管理工作区.属性类别输入框.format("1"))
        self.clear(设置页对象库.属性管理工作区.属性名称输入框.format("1"))
        self.send_keys(设置页对象库.属性管理工作区.属性类别输入框.format("1"), 'test1')
        self.send_keys(设置页对象库.属性管理工作区.属性名称输入框.format("1"), 'test1')
        self.click(设置页对象库.属性管理工作区.行保存按钮.format("1"))
        self.driver.refrsh()
        self.进入到操作位置.进入属性工作区()
        self.click(设置页对象库.属性管理工作区.属性系统名称.format("test"))
        if not self.wait('//div[@class="el-card__body"]//table[@class="el-table__body"]//tr[1]/td[3]//span[text()="test1"]',3):
            raise AssertionError("编辑属性时，点击保存，属性信息被保存")
        #批量删除属性
        self.click(设置页对象库.属性管理工作区.添加属性)
        self.send_keys(设置页对象库.属性管理工作区.属性类别输入框.format("2"), '属性2')
        self.send_keys(设置页对象库.属性管理工作区.属性名称输入框.format("2"), '属性2')
        self.click(设置页对象库.属性管理工作区.行保存按钮.format("2"))
        self.wait(公共元素对象库.系统提示信息弹框.format("添加成功"), 3)
        self.click(设置页对象库.属性管理工作区.属性行复选框.format("1"))
        self.click(设置页对象库.属性管理工作区.属性行复选框.format("2"))
        self.click(设置页对象库.属性管理工作区.删除属性)
        if not self.wait(设置页对象库.属性管理工作区.删除对话框, 3):
            raise AssertionError("批量删除属性，点击删除，未查看到删除确认对话框")
        self.click(设置页对象库.属性管理工作区.删除确认按钮)
        if self.wait(设置页对象库.属性管理工作区.行删除按钮.format("1"), 3) or \
                self.wait(设置页对象库.属性管理工作区.行删除按钮.format("2"), 3):
            raise AssertionError("批量删除属性，点击确认删除确认对话框后，属性未被删除")











