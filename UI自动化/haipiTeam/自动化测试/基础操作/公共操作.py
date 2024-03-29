import os
import sys
import time

import win32clipboard as w
import win32con
import zipfile
import shutil

from HNtest.testcasesec.testcasesec import page
from HNtest.Secselenium.secdriver import Secdriver
from selenium.webdriver.common.keys import Keys
from ..元素对象库.用户信息 import *
from ..元素对象库.公共元素 import *
from .进入到操作位置 import *
from ..基础操作.滑块验证 import *
from ..元素对象库.项目 import *


class 公共操作(page):
    def __init__(self,Secdriver=None):
        page.__init__(self,secdriver=Secdriver)

    def win上传文件(self,文件路径):
        '''
        此方法用于从系统中选取文件上传
        :param 文件路径: [] example:['TestData','BaseData',moudel,file]
        '''
        path=sys.path[0]
        file=''
        for i in 文件路径:
            file=file+'\\'+i
        filepath=str(path)+'\\自动化测试'+file
        if os.path.exists(filepath):
            self.driver.win_dialog(path=filepath)
        else:
            raise AssertionError("未找到对应的文件")

    def 清空当前元素(self,xpath):
        element = self.driver.getelement(xpath)
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.BACKSPACE)

    def 获取剪切板内容(self):
        w.OpenClipboard()
        d = w.GetClipboardData(win32con.CF_TEXT)
        w.CloseClipboard()
        return d.decode('GBK')

    def 修改文件内容(self,文件路径,内容):
        '''
        :param 文件路径:  [] example:['TestData','BaseData',moudel,file]
        :param 内容:
        :return:
        '''
        path = sys.path[0]
        file = ''
        for i in 文件路径:
            file = file + '\\' + i
        filepath = str(path) + '\\自动化测试' + file
        if os.path.exists(filepath):
            file=open(filepath,"w")
            file.write(内容)
            file.close()

    def 检查文件是否下载完成(self):
        user=os.path.expanduser('~')
        downloadpath=user+'\Downloads'
        if os.path.exists(downloadpath):
            if os.listdir(downloadpath):
                lists=os.listdir(downloadpath)
                temppath=None
                for i in lists:
                    if 'crdownload' in i:
                        temppath=downloadpath+'\\'+i
                        while True:
                            if not os.path.exists(temppath):
                                break
        else:
            raise RuntimeError("文件下载目录不存在")
        return downloadpath

    def 解压zip到指定目录(self,zip文件路径,目标路径):
        zfile=zipfile.ZipFile(file=zip文件路径,mode='r')
        zfile.extractall(目标路径)
        zfile.close()

    def 查看zip文件(self,zip文件路径):
        zfile = zipfile.ZipFile(file=zip文件路径, mode='r')
        return zfile.namelist()

    def 清空浏览器下载目录(self):
        user = os.path.expanduser('~')
        downloadpath = user + '\Downloads'
        if os.path.exists(downloadpath):
            if os.listdir(downloadpath):
                for j in os.listdir(downloadpath):
                    filedata = downloadpath + "\\" + j
                    try:
                        os.remove(filedata)
                    except:
                        shutil.rmtree(filedata)

    def 获取文件在列表中的行号(self,文件名称,列表xpath='//table//tr/td[2 or 3]/div/span/span[not(contains(@class,"checkbox"))]'):
        文件列表=[]
        元素列表=self.driver.getelements(列表xpath)
        for 文件元素 in 元素列表:
            文件列表.append(文件元素.text)
        return int(文件列表.index(文件名称))+1

    def 滚动选择列表框选项(self,选项名称):
        flage = True
        已选中的选项=self.driver.getelement('//ul/li[contains(@class,"dropdown__item selected")]/span')
        self.move_to_by_pyautogui(公共元素对象库.列表框选项.format(已选中的选项.text), y_offset=0)
        self.scroll_by_pyautogui(1000)
        选项list=self.driver.getelements('//ul/li[contains(@class,"dropdown__item")]/span')
        self.move_to_by_pyautogui(公共元素对象库.列表框选项.format(选项list[0].text), y_offset=50)
        time1=time.time()
        while (flage):
            try:
                flage = False
                self.click(公共元素对象库.列表框选项.format(选项名称))
            except:
                flage = True
                self.scroll_by_pyautogui(-5)
            time2=time.time()
            if time2-time1>300:
                raise RuntimeError("操作超时")

    def 项目下按路径展开目录(self,目录路径):
        '''
        :param 目录路径: 路径列表 ['根节点名称','','']
        '''
        for path in 目录路径:
            if self.wait(项目对象库.节点展开按钮.format(path),1):
                self.click(项目对象库.节点展开按钮.format(path))
        self.click(项目对象库.目录节点.format(目录路径[-1]))
        time.sleep(2)
