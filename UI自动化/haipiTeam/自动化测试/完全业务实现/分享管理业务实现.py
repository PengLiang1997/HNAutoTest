import os.path
import os
import random
import time
from HNtest.Log.Logger import Logger

from ..基础操作.用户信息页面 import *
from ..基础操作.登录页面 import *
from ..基础操作.滑块验证 import *
from ..基础操作.项目页面 import *
from ..元素对象库.分享管理页 import *
from ..元素对象库.公共元素 import *
from ..基础操作.分享管理页面 import *
from HNtest.testcasesec.testcasesec import page

class 分享管理工作区(page):
    def __init__(self,Secdriver = None):
        page.__init__(self,secdriver=Secdriver)
        self.滑块验证=滑块验证(Secdriver=Secdriver)
        self.公共操作 = 公共操作(Secdriver=Secdriver)
        self.登录页面 = 登录页面(Secdriver=Secdriver)
        self.项目页面 = 项目页面(Secdriver=Secdriver)
        self.项目管理页面 = 项目管理页面(Secdriver=Secdriver)
        self.分享管理页面 = 分享管理页面(Secdriver=Secdriver)
        self.进入到操作位置 = 进入到操作位置(Secdriver=Secdriver)

    def 数据准备(self):
        self.进入到操作位置.进入我的分享页()
        self.分享管理页面.取消所有分享()
        self.进入到操作位置.进入访问记录页()
        self.分享管理页面.清除所有访问记录()
        self.进入到操作位置.进入项目管理页()
        self.项目管理页面.删除项目(项目名称="分享管理")
        self.项目管理页面.创建空白项目(项目名称="分享管理")
        self.项目管理页面.点击进入项目(项目名称="分享管理")
        self.wait(项目对象库.目录节点.format("分享管理"), 3)
        self.driver.refrsh()
        self.项目页面.创建文件目录(目录名称="一级目录", 目录父节点名称="分享管理")
        素材1 = ['TestData', 'FrontData', '项目页', '素材1.png']
        素材2 = ['TestData', 'FrontData', '项目页', '素材2.jpg']
        self.click(项目对象库.目录节点.format("分享管理"))
        self.项目页面.批量上传文件(目录路径=['分享管理', '一级目录'], 文件路径列表=[素材1, 素材2])
        self.项目页面.分享文件(目录路径=['分享管理', '一级目录'],资源名称='素材1.png')

    def 分享列表显示(self):
        self.进入到操作位置.进入我的分享页()
        #在文件目录列表中创建分享后，在分享列表中可以查看到该分享
        if not self.wait(分享管理对象库.分享内容名称.format("素材1.png"),3):
            raise AssertionError("用户创建分享后，在分享管理我的分享列表中未查看到创建的分享")
        #分享记录列表中有分享内容、类型、过期时间、是否生效、分享创建人、访问记录、访问次数统计、操作列
        elems=self.driver.getelements('//table[@class="el-table__header"]//tr/th[position()>1]//div')
        表头=[]
        for elem in elems:
            表头.append(elem.text)
        if 表头!=['分享内容','类型','过期时间','是否生效','分享人','访问记录','访问次数','浏览次数','下载次数','操作']:
            raise AssertionError("我的分享列表显示不全")

    def 查看分享内容(self):
        self.进入到操作位置.进入我的分享页()
        #点击分享记录名称，可以进入到分享页，查看到分享文件
        self.click(分享管理对象库.分享内容名称.format("素材1.png"))
        time.sleep(3)
        self.switch_to_new_window()
        if not self.wait(项目对象库.分享查看页面.列表文件名称.format("素材1.png"), 3):
            raise AssertionError("在我的分享页点击查看分享内容，页面没有跳转到文件分享页面")

    def 编辑分享状态(self):
        self.进入到操作位置.进入我的分享页()
        self.分享管理页面.取消单个分享(分享内容名称='素材2.jpg')
        self.项目管理页面.点击进入项目(项目名称="分享管理")
        self.项目页面.分享文件(目录路径=['分享管理', '一级目录'], 资源名称='素材2.jpg')
        self.进入到操作位置.进入我的分享页()
        链接 = self.公共操作.获取剪切板内容()
        #编辑生效按钮为失效，可以编辑成功
        self.click(分享管理对象库.生效_是否生效按钮.format("素材2.jpg"))
        if not self.wait(分享管理对象库.失效_是否生效按钮.format("素材2.jpg"),3):
            raise AssertionError("点击编辑分享的状态，分享状态未发生变化")
        #生效按钮为失效后，访问该分享链接，提示分享失效
        self.driver.driver.execute_script("window.open('');")
        self.switch_to_new_window()
        self.driver.driver.get(链接)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("分享链接不合法或已过期"), 3):
            raise AssertionError("编辑分享状态为失效后，访问分享链接，未查看到分享失效的提示信息")
        #编辑生效按钮为失效，分享内容置灰
        self.driver.close()
        self.switch_to_window_byTagName("HAPYTEAM 管理您的设计数据")
        self.进入到操作位置.进入我的分享页()
        if not self.wait(分享管理对象库.置灰_分享内容名称.format("素材2.jpg"),3):
            raise AssertionError("编辑分享状态为失效后，分享名称没有置灰")
        #编辑生效按钮为生效，分享内容没有置灰
        self.click(分享管理对象库.失效_是否生效按钮.format("素材2.jpg"))
        if not self.wait(分享管理对象库.分享内容名称.format("素材2.jpg"),3):
            raise AssertionError("点击编辑分享状态为生效后，分享名称还是在置灰状态")
        #编辑生效按钮为生效，点击分享内容，可以访问该分享页面
        self.driver.driver.execute_script("window.open('');")
        self.switch_to_new_window()
        self.driver.driver.get(链接)
        if self.wait(公共元素对象库.系统提示信息弹框.format("分享链接不合法或已过期"), 3):
            raise AssertionError("编辑分享状态为生效后，访问分享链接，仍然弹出分享失效的提示信息")

    def 编辑过期时间(self):
        self.进入到操作位置.进入我的分享页()
        self.分享管理页面.取消单个分享(分享内容名称='素材2.jpg')
        self.项目管理页面.点击进入项目(项目名称="分享管理")
        self.项目页面.分享文件(目录路径=['分享管理', '一级目录'], 资源名称='素材2.jpg')
        self.进入到操作位置.进入我的分享页()
        链接 = self.公共操作.获取剪切板内容()
        #点击操作列编辑过期时间按钮，过期时间处于编辑状态
        self.click(分享管理对象库.编辑过期时间.format("素材2.jpg"))
        if not self.wait(分享管理对象库.过期时间输入框.format("素材2.jpg"),3):
            raise AssertionError("点击编辑分享过期时间，分享过期时间列未处于编辑状态")
        #点击过期时间栏，弹出过期时间编辑窗口
        self.click(分享管理对象库.过期时间输入框.format("素材2.jpg"))
        if not self.wait('//div[contains(@class,"has-time date_picker")]',3):
            raise AssertionError("点击过期时间编辑列，未弹出时间选择按钮")
        #过期时间不可以选择过去的时间
        self.clear(分享管理对象库.过期时间输入框.format("素材2.jpg"))
        self.send_keys(分享管理对象库.过期时间输入框.format("素材2.jpg"),"2023-06-20 09:40:10")
        self.click(分享管理对象库.访问次数.format("素材2.jpg"))
        if self.wait(公共元素对象库.系统提示信息弹框.format("2023-06-20 09:40:10"),3):
            raise AssertionError("过期时间不可以选择过去的时间")
        #编辑过期时间，点击确定，过期时间生效，然后查看到达该时间后，分享链接是否过期
        self.clear(分享管理对象库.过期时间输入框.format("素材2.jpg"))
        time_now = time.time() + 60
        time_lost = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time_now))
        self.send_keys(分享管理对象库.过期时间输入框.format("素材2.jpg"), time_lost)
        self.click(分享管理对象库.访问次数.format("素材2.jpg"))
        time.sleep(70)
        self.click(分享管理对象库.分享内容名称.format("素材2.jpg"))
        self.switch_to_new_window()
        if not self.wait(公共元素对象库.系统提示信息弹框.format("分享链接不合法或已过期"), 3):
            raise AssertionError("编辑分享过期时间，超过过期时间后访问分享链接，未弹出提示信息")
        self.driver.close()
        self.switch_to_window_byTagName("HAPYTEAM 管理您的设计数据")
        self.进入到操作位置.进入我的分享页()
        #编辑过期时间，点击取消编辑按钮，不保存编辑结果
        原过期时间=self.driver.getelement(分享管理对象库.过期时间)
        self.click(分享管理对象库.编辑过期时间.format("素材2.jpg"))
        self.clear(分享管理对象库.过期时间输入框.format("素材2.jpg"))
        time_now = time.time() + 60
        time_lost = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time_now))
        self.send_keys(分享管理对象库.过期时间输入框.format("素材2.jpg"), time_lost)
        self.click(分享管理对象库.取消编辑过期时间.format("素材2.jpg"))
        现过期时间 = self.driver.getelement(分享管理对象库.过期时间)
        if 原过期时间!=现过期时间:
            raise AssertionError("编辑分享过期时间时，点击取消编辑后，编辑的过期时间还是被保存")

    def 查看访问记录(self):
        self.进入到操作位置.进入我的分享页()
        self.分享管理页面.取消单个分享(分享内容名称='一级目录')
        self.项目管理页面.点击进入项目(项目名称="分享管理")
        self.项目页面.分享文件(目录路径=['分享管理'], 资源名称='一级目录',下载=True,资源类型="文件目录")
        链接 = self.公共操作.获取剪切板内容()
        self.公共操作.清空浏览器下载目录()
        self.driver.driver.execute_script("window.open('');")
        self.switch_to_new_window()
        self.driver.driver.get(链接)
        self.driver.refrsh()
        #对分享资源进行访问，浏览，下载操作，查看对应的统计数量是否正确
        self.click(项目对象库.分享查看页面.下载文件.format("素材2.jpg"))
        time.sleep(3)
        downpath = self.公共操作.检查文件是否下载完成()
        self.click(项目对象库.分享查看页面.下载文件.format("素材2.jpg"))
        time.sleep(3)
        downpath = self.公共操作.检查文件是否下载完成()
        self.driver.refrsh()
        self.click(项目对象库.分享查看页面.预览文件.format("素材2.jpg"))
        time.sleep(2)
        self.driver.close()
        self.driver.switch_to_window_byTitle("素材2.jpg")
        self.driver.close()
        self.switch_to_window_byTagName("HAPYTEAM 管理您的设计数据")
        self.进入到操作位置.进入我的分享页()
        访问次数=self.driver.getelement(分享管理对象库.访问次数.format("一级目录"))
        浏览次数=self.driver.getelement(分享管理对象库.浏览次数.format("一级目录"))
        下载次数=self.driver.getelement(分享管理对象库.下载次数.format("一级目录"))
        if 访问次数!='2':
            raise AssertionError("分享访问次数统计不正确")
        if 浏览次数!='1':
            raise AssertionError("分享浏览次数统计不正确")
        if 下载次数!='2':
            raise AssertionError("分享下载次数统计不正确")
        #弹出分享访问记录，弹出我的访问记录弹窗
        self.click(分享管理对象库.访问记录.format("一级目录"))
        if not self.wait(对话框对象库.弹框标题.format("访问记录"),3):
            raise AssertionError("点击访问记录按钮，没有弹出访问记录弹窗")
        #记录列表显示查看人对分享资源的操作记录，有访问人ip地址、ip地理位置、操作类型、操作人、记录时间
        elems = self.driver.getelements('//div[@aria-label="我的访问记录"]//table[@class="el-table__header"]//tr/th//div')
        表头 = []
        for elem in elems:
            表头.append(elem.text)
        if 表头 != ['IP地址', '地理位置', '操作类型', '操作人', '记录时间']:
            raise AssertionError("分享访问记录列表显示不全")
        #可以根据操作过滤显示访问记录，过滤条件默认全部
        self.click(分享管理对象库.操作类型列表框)
        if not self.wait('//ul/li[contains(@class,"dropdown__item selected")]/span[text()="全部"]',3):
            raise AssertionError("过滤条件默认没有选择全部")
        #过滤条件有全部、查看、下载、浏览
        if not self.wait(公共元素对象库.列表框选项.format("全部"),3) or not\
            self.wait(公共元素对象库.列表框选项.format("查看"),3) or not  \
            self.wait(公共元素对象库.列表框选项.format("下载"), 3) or not \
            self.wait(公共元素对象库.列表框选项.format("浏览"), 3):
            raise AssertionError("分享访问记录过滤选项不全")
        #选择不同的过滤条件，查看过滤结果是否正确
        self.click(公共元素对象库.列表框选项.format("浏览"))
        eles=self.driver.getelements('//div[@aria-label="我的访问记录"]//tr/td[3]//span[text()="浏览" and not(@style="display: none;")]')
        if len(eles)!=1:
            raise AssertionError("分享访问记录过滤显示结果不正确")

    def 取消分享(self):
        self.进入到操作位置.进入我的分享页()
        self.分享管理页面.取消单个分享(分享内容名称='一级目录')
        self.分享管理页面.取消单个分享(分享内容名称='素材2.jpg')
        self.项目管理页面.点击进入项目(项目名称="分享管理")
        self.项目页面.分享文件(目录路径=['分享管理'], 资源名称='一级目录', 下载=True,资源类型="文件目录")
        链接1 = self.公共操作.获取剪切板内容()
        self.项目页面.分享文件(目录路径=['分享管理', '一级目录'], 资源名称='素材2.jpg')
        链接2 = self.公共操作.获取剪切板内容()
        self.进入到操作位置.进入我的分享页()
        #点击取消分享按钮，分享列表中该条记录被清除，访问分享链接，显示链接失效
        self.click(分享管理对象库.取消分享.format("素材2.jpg"))
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 3)
        self.driver.driver.execute_script("window.open('');")
        self.switch_to_new_window()
        self.driver.driver.get(链接2)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("分享链接不合法或已过期"), 3):
            raise AssertionError("取消分享后，访问分享链接，未查看到分享失效的提示信息")
        self.driver.close()
        self.switch_to_window_byTagName("HAPYTEAM 管理您的设计数据")
        self.进入到操作位置.进入我的分享页()
        #勾选多条分享记录，点击取消分享，分享列表中该条记录被清除，访问分享链接，显示链接失效
        self.click(分享管理对象库.全选复选框)
        self.click(分享管理对象库.批量取消分享)
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 3)
        self.driver.driver.execute_script("window.open('');")
        self.switch_to_new_window()
        self.driver.driver.get(链接1)
        if not self.wait(公共元素对象库.系统提示信息弹框.format("分享链接不合法或已过期"), 3):
            raise AssertionError("批量取消分享后，访问分享链接，未查看到分享失效的提示信息")

    def 访问列表显示(self):
        self.进入到操作位置.进入我的分享页()
        self.分享管理页面.取消单个分享(分享内容名称='一级目录')
        self.分享管理页面.取消单个分享(分享内容名称='素材2.jpg')
        self.项目管理页面.点击进入项目(项目名称="分享管理")
        self.项目页面.分享文件(目录路径=['分享管理'], 资源名称='一级目录', 下载=True,资源类型="文件目录")
        链接1 = self.公共操作.获取剪切板内容()
        self.项目页面.分享文件(目录路径=['分享管理', '一级目录'], 资源名称='素材2.jpg')
        链接2 = self.公共操作.获取剪切板内容()
        self.进入到操作位置.进入访问记录页()
        self.分享管理页面.清除所有访问记录()
        self.driver.driver.execute_script("window.open('');")
        self.switch_to_new_window()
        self.driver.driver.get(链接1)
        time.sleep(3)
        self.driver.close()
        self.switch_to_window_byTagName("HAPYTEAM 管理您的设计数据")
        self.driver.driver.execute_script("window.open('');")
        self.switch_to_new_window()
        self.driver.driver.get(链接2)
        time.sleep(3)
        self.driver.close()
        self.switch_to_window_byTagName("HAPYTEAM 管理您的设计数据")
        self.driver.refrsh()
        self.进入到操作位置.进入访问记录页()
        #访问列表显示的是当前用户访问的分享链接的记录
        if not self.wait(分享管理对象库.访问记录名称.format("一级目录"),3) or not \
            self.wait(分享管理对象库.访问记录名称.format("素材2.jpg"),3):
            raise AssertionError("访问列表没有显示的是当前用户访问的分享链接的记录")
        #访问记录列表有分享内容、类型、分享创建人、创建时间、最后一次访问时间、操作列
        elems = self.driver.getelements('//table[@class="el-table__header"]//tr/th[position()>1]//div')
        表头 = []
        for elem in elems:
            表头.append(elem.text)
        if 表头 != ['分享内容', '类型', '分享创建人', '分享创建时间', '最后一次访问时间', '操作']:
            raise AssertionError("我的访问记录列表显示不全")

    def 点击查看访问(self):
        self.进入到操作位置.进入我的分享页()
        self.分享管理页面.取消单个分享(分享内容名称='一级目录')
        self.项目管理页面.点击进入项目(项目名称="分享管理")
        self.项目页面.分享文件(目录路径=['分享管理'], 资源名称='一级目录', 下载=True,资源类型="文件目录")
        链接1 = self.公共操作.获取剪切板内容()
        self.进入到操作位置.进入访问记录页()
        self.分享管理页面.清除所有访问记录()
        self.driver.driver.execute_script("window.open('');")
        self.switch_to_new_window()
        self.driver.driver.get(链接1)
        time.sleep(3)
        self.driver.close()
        self.switch_to_window_byTagName("HAPYTEAM 管理您的设计数据")
        self.driver.refrsh()
        self.进入到操作位置.进入访问记录页()
        #点击分享内容，可以查看到分享内容
        self.click(分享管理对象库.访问记录名称.format("一级目录"))
        time_now = time.time()
        self.switch_to_new_window()
        if not self.wait(项目对象库.分享查看页面.列表文件名称.format("素材2.jpg"),3):
            raise AssertionError("在我的访问记录页面，点击分享内容名称，没有进入分享查看页面")
        #查看分享内容后，点击查看列表中最后一次访问时间是否正确
        self.driver.refrsh()
        self.进入到操作位置.进入访问记录页()
        最后一次访问时间=self.driver.getelement(分享管理对象库.最后一次访问时间.format("一级目录")).text
        timearray = time.strptime(最后一次访问时间[1:-1], "%Y-%m-%d %H:%M:%S")
        分享过期时间 = time.mktime(timearray)
        if 分享过期时间 - 最后一次访问时间 > 10:
            raise AssertionError("我的访问记录列表最后一次访问时间记录不正确")

    def 删除访问记录(self):
        self.进入到操作位置.进入我的分享页()
        self.分享管理页面.取消单个分享(分享内容名称='一级目录')
        self.分享管理页面.取消单个分享(分享内容名称='素材2.jpg')
        self.项目管理页面.点击进入项目(项目名称="分享管理")
        self.项目页面.分享文件(目录路径=['分享管理'], 资源名称='一级目录', 下载=True,资源类型="文件目录")
        链接1 = self.公共操作.获取剪切板内容()
        self.项目页面.分享文件(目录路径=['分享管理', '一级目录'], 资源名称='素材2.jpg')
        链接2 = self.公共操作.获取剪切板内容()
        self.进入到操作位置.进入访问记录页()
        self.分享管理页面.清除所有访问记录()
        self.driver.driver.execute_script("window.open('');")
        self.switch_to_new_window()
        self.driver.driver.get(链接1)
        time.sleep(3)
        self.driver.close()
        self.switch_to_window_byTagName("HAPYTEAM 管理您的设计数据")
        self.driver.driver.execute_script("window.open('');")
        self.switch_to_new_window()
        self.driver.driver.get(链接2)
        time.sleep(3)
        self.driver.close()
        self.switch_to_window_byTagName("HAPYTEAM 管理您的设计数据")
        self.driver.refrsh()
        self.进入到操作位置.进入访问记录页()
        #点击删除按钮，访问记录从列表中移除
        self.click(分享管理对象库.删除访问记录.format("素材2.jpg"))
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 3)
        if self.wait(分享管理对象库.访问记录名称.format("素材2.jpg"),3):
            raise AssertionError("删除我的访问记录后，访问记录列表中还能查看到访问记录")
        #勾选多个访问记录，点击删除，勾选的访问记录从访问列表中移除
        self.click(分享管理对象库.全选复选框)
        self.click(分享管理对象库.批量删除访问记录)
        self.wait(公共元素对象库.系统提示信息弹框.format("成功"), 3)
        if self.wait(分享管理对象库.访问记录名称.format("一级目录"),3):
            raise AssertionError("批量删除我的访问记录后，访问记录列表中还能查看到访问记录")