class 项目管理对象库:
    #显示设置
    显示设置按钮='//div[contains(@class,"project_top comm_bgc")]//i'
    显示设置选项='//ul[contains(@id,"dropdown-menu")]//span[text()="{}"]'#参数为显示设置选项

    创建新项目='//div[@class="project_box"]//span[contains(text(),"创建新项目")]'
    项目卡片='//div[@class="project_box"]//span[text()="{}"]'
    项目详情按钮='//div[@title="{}"]//following-sibling::div/div[@class="el-dropdown"]'
    项目详情信息='//div/span[text()="{}:"]/following-sibling::span[contains(text(),"{}")]'
    #项目列表
    列表项目名称='//span[contains(text(),"{}")]'
    列表内容='//span[contains(text(),"{}")]/ancestor::tr/td[{}]/div'

    项目成员按钮='//div[@title="{}"]//following-sibling::div/div[@class="card_b_r"]//i[contains(@class,"team")]'
    #项目成员
    添加项目成员='//ul[contains(@id,"dropdown-menu")]//div[@class="invitation"]/i[contains(@class,"add")]'
    移除项目成员='//ul[contains(@id,"dropdown-menu")]//span[text()="{}"]/following-sibling::i'#参数为成员名称
    项目成员名称='//ul[contains(@id,"dropdown-menu")]//span[text()="{}"]'
    #更多操作
    更多操作按钮='//div[@title="{}"]//following-sibling::div/div[@class="card_b_r"]//i[contains(@class,"more")]'
    更多操作选项='//ul[contains(@id,"dropdown-menu")]/li[not(contains(@class,"is-disabled"))]//*[text()=" {} "]'#参数为选项名称
    置灰_更多操作选项='//li[contains(@class,"is-disabled")]//*[text()=" {} "]'
    更多操作选项2 = '//ul[contains(@id,"dropdown-menu")]/li//*[text()="{}"]'  # 参数为选项名称，标签、项目节点等选项
    展开操作选项='//ul[contains(@id,"dropdown-menu")]/li//*[text()="{}"]/following-sibling::div/i'
    #标签
    标签='//ul[contains(@id,"dropdown-menu")]/li[{}]/div[@class="tip_bgc" and contains(@style,"background-color")]'#参数为标签序号

    #存为模板
    目录文件复选框 = '//tr/td[2]/div[text()="{}"]/ancestor::tr/td[1]'
    保留层级='//span[text()="保留的层级 "]//input'

    class 项目动态页:
        项目动态页标题='//div[@class="project_dyn "]//h4[text()="项目动态"]'
        用户名称='//li//span[contains(text(),"{}")]'
        操作1='//li//span[contains(text(),"{}")]'
        操作2='//li//span[contains(text(),"{}")]/following-sibling::span[contains(text(),"{}")]'#参数1为用户名，参数2为操作名称


class 项目对象库:
    搜索框='//input[@placeholder="搜索"]'
    搜索按钮='//div[@class="pBtnGroup"]//i[contains(@class,"el-icon-search")]'
    新建目录 = '//div[@id="pTableHeader"]/div[@class="pBtnGroup"]//span[text()="新建目录"]'
    上传 = '//div[@id="pTableHeader"]/div[@class="pBtnGroup"]//span[text()="上传文件"]'
    目录节点='//div[@role="treeitem"]//span[@title="{}"]'#参数为目录名称
    目录节点2 = '//div[@role="treeitem"]//span[text()="{}"]'  # 参数为目录名称
    节点收起按钮='//div[@role="treeitem"]//span[contains(@title,"{}")]/preceding-sibling::span[contains(@class,"expanded")]'
    节点展开按钮='//div[@role="treeitem"]//span[contains(@title,"{}")]/preceding-sibling::span[not( contains(@class,"expanded"))]'
    节点展开按钮2='//div[@role="treeitem"]//span[contains(text(),"{}")]/preceding-sibling::span[not( contains(@class,"expanded"))]'
    子节点='//span[contains(@title,"{}")]/parent::div/following-sibling::div//span[contains(@title,"{}")]'#参数1为父节点，参数2为子节点


    #新建目录弹框
    提交按钮='//span[text()="新建文件目录"]/parent::div/following-sibling::div//button'
    #上传文件弹框
    上传文件按钮='//span[text()="上传文件"]/parent::div/following-sibling::div//button'
    点击上传按钮='//span[text()="上传文件"]/parent::div/following-sibling::div//em'
    待上传文件='//span[text()="上传文件"]/parent::div/following-sibling::div//ul//a[contains(text(),"{}")]'#参数为文件名
    移除待上传文件='//ul//a[contains(text(),"{}")]/parent::li/i[@class="el-icon-close"]'
    #工具栏按钮
    工具栏按钮='//button/span[text()="{}"]'#参数为按钮名称
    正在打包按钮='//button[contains(@class,"is--loading")]/span[text()="打包"]'
    刷新列表='//button[contains(@class,"el-icon-refresh")]'

    #文件列表元素
    列显示管理='//div/button[@title="列设置"]'
    列显示弹窗名称='//div/button[@title="列设置"]/following-sibling::div'
    关闭按钮='//span[text()="设置显示内容"]/following-sibling::button/i'
    列显示单选钮='//div/button[@title="列设置"]/following-sibling::div//li[@title="{}"]/span[1]'
    已选中按钮='//span[text()="{}"]/ancestor::div[contains(@class,"checked")]/span[1]'
    未选中按钮='//span[text()="{}"]/ancestor::div[not(contains(@class,"checked"))]/span[1]'
    保存设置按钮='//div/button[@title="列设置"]/following-sibling::div//button[text()="确认"]'

    #
    列表复选框 = '//table//tr/td[2 or 3]//span[text()="{}"]/ancestor::tr/td[1]//span'
    文件目录复选框='//table//tr/td[4]//span[text()="{}"]/ancestor::tr/td[1]//span[contains(@class,"vxe-checkbox")]'
    检出按钮='//table//tr/td[2 or 3]//span[text()="{}"]/ancestor::tr/td[2]//i[@class="iconfont icon-correct" or @class="iconfont icon-wrong"]'
    归档按钮='//table//tr/td[2 or 3]//span[text()="{}"]/ancestor::tr/td[2]//i[@title="已归档"]'
    列表文件名称='//table//tr/td[2 or 3]//span[text()="{}"]'#参数为文件名称
    生命周期状态='//div[contains(@class,"pane-one")]//td[2 or 3]//span[text()="{}"]/ancestor::tr/td[11]//span'
    文件状态='//div[contains(@class,"pane-one")]//td[2 or 3]//span[text()="{}"]/ancestor::tr/td[5]//span'
    收藏按钮='//table//tr/td[2 or 3]//span[text()="{}"]/ancestor::td/following-sibling::td[last()]/div/div/i[contains(@class,"shoucang-yellow")]'
    未收藏按钮='//table//tr/td[2 or 3]//span[text()="{}"]/ancestor::td/following-sibling::td[last()]/div/div/i[contains(@class,"icon-shoucang1")]'
    列表行操作='//table//tr/td[2 or 3]//span[text()="{}"]/ancestor::td/following-sibling::td[last()]//span/i'#参数为文件名称
    列表文件序号='//table//tr/td[2 or 3]//span[text()="{}"]/ancestor::tr'#参数为文件名称
    悬浮列行操作='//table//tr[{}]//i[contains(@class,"icon-index_more")]'#参数为行号
    悬浮列收藏='//table//tr[{}]//i[contains(@class,"icon-shoucang1")]'#参数为行号
    已选_悬浮列收藏='//table//tr[{}]//i[contains(@class,"shoucang-yellow")]'#参数为行号
    未选_悬浮列收藏='//table//tr[{}]//i[contains(@class,"icon-shoucang1")]'#参数为行号


    行操作选项='//ul[contains(@id,"dropdown-menu") and @x-placement="bottom-end"]//span[text()="{}"]'#参数为操作名称
    置灰_行操作选项='//ul[contains(@id,"dropdown-menu") and @x-placement="bottom-end"]/li[contains(@class,"is-disabled")]/span[text()="{}"]'

    #版本列表
    文件版本='//div[@id="pane-edition"]//tr/td[4]//span[text()="{}"]'#参数为版本号
    版本标签标志='//div[@id="pane-edition"]//tr/td[4]//span[text()="{}"]//ancestor::tr/td[14]//i[@title="标签"]'
    #可清理版本列表
    可清理版本='//div[@aria-label="清理版本"]//tr/td[5]/div[text()="{}"]'
    可清理版本复选框='//div[@aria-label="清理版本"]//tr/td[5]/div[text()="{}"]/ancestor::tr/td[1]'

    #附加文件弹窗
    class 附加文件:
        树资源节点='//div[@aria-label="附加文件"]//div[@role="treeitem"]//span[contains(text(),"{}")]'
        节点收起按钮='//div[@aria-label="附加文件"]//div[@role="treeitem"]//span[contains(text(),"{}")]/preceding-sibling::span[contains(@class,"expanded")]'
        节点展开按钮='//div[@aria-label="附加文件"]//div[@role="treeitem"]//span[contains(text(),"{}")]/preceding-sibling::span[not(contains(@class,"expanded"))]'
        列表单选按钮='//table//tr/td[2]//div[contains(text(),"{}")]/ancestor::tr/td[1]//span'
        附加按钮='//div[@aria-label="附加文件"]/div[@class="el-dialog__footer"]//button/span[text()="附加"]'
        取消按钮='//div[@aria-label="附加文件"]/div[@class="el-dialog__footer"]//button/span[text()="取消"]'

    class 文件信息:
        版本tab页='//div[@id="tab-edition"]'
        引用tab页='//div[@id="tab-quote"]'
        被引用tab页='//div[@id="tab-quoted"]'
        升级记录tab页='//div[@id="tab-upgradeRecord"]'

        #版本tab页
        版本更多操作='//tr/td[4]//span[text()="{}"]/ancestor::tr/td[last()]//i[@title="更多操作"]'#参数为版本号
        版本更多操作选项='//ul[contains(@id,"dropdown-menu") and contains(@x-placement,"-end")]//li[text()="{}"]'

        #引用tab页文件列表
        引用文件名称='//div[@id="pane-quote"]//table[@class="el-table__body"]//tr/td[1]/div[text()="{}"]'
        #被引用tab页文件列表
        被引用文件名称='//div[@id="pane-quoted"]//table[@class="el-table__body"]//tr/td[1]/div[text()="{}"]'

    class 目录设置:
        目录设置tab页='//div[@role="tablist"]/div[text()="{}"]'
        生命周期列表框='//div[@id="pane-cyclePlanning"]//input[@placeholder="请选择"]'
        生命周期节点 = '//tr/td/div[text()="{}"]'
        添加人员按钮 = '//button/span[text()="添加人员"]'
        所有人提交后可进入下一节点按钮 = '//div[contains(text(),"所有人提交后可进入下一节点")]//span'
        已选_所有人提交后可进入下一节点按钮 = '//div[contains(text()," 所有人提交后可进入下一节点 ")]/div[contains(@class,"checked")]//span'
        未选_所有人提交后可进入下一节点按钮 = '//div[contains(text()," 所有人提交后可进入下一节点 ")]/div[not(contains(@class,"checked"))]//span'
        节点下成员 = '//tr/td/div[text()="{}"]'
        移除成员按钮 = '//tr/td/div[text()="{}"]/ancestor::tr/td[last()]//i'
        已选_成员复选框 = '//div[text()="{}"]/ancestor::tr/td[1]//span[contains(@class,"checked")]'
        未选_成员复选框 = '//div[text()="{}"]/ancestor::tr/td[1]//span[not(contains(@class,"checked"))]'
        权限复选框 = '//div[text()="{}"]/ancestor::tr/td[1]//spans'
        禁用_成员复选框 = '//div[text()="{}"]/ancestor::tr/td[1]//span[contains(@class,"disabled")]'

        #会签设置
        是否会签='//div[text()=" 是否会签 "]//span'
        新增会签='//div[@class="container_btns"]//span[text()=" 新增"]'
        批量删除会签='//div[@class="container_btns"]//span[text()="删除"]'
        置灰_批量删除会签='//div[@class="container_btns"]//button[contains(@class,"is-disable")]/span[text()="删除"]'
        编辑会签='//div[text()="{}"]/ancestor::tr/td[3]/div[text()="{}"]/ancestor::tr/td[last()]//i[1]'#参数1为专业，参数2为人员
        删除单个会签='//div[text()="{}"]/ancestor::tr/td[3]/div[text()="{}"]/ancestor::tr/td[last()]//i[2]'#参数1为专业，参数2为人员
        会签行='//div[text()="{}"]/ancestor::tr/td[3]/div[text()="{}"]'#参数1为专业，参数2为人员
        会签行复选框='//div[text()="{}"]/ancestor::tr/td[3]/div[text()="{}"]/ancestor::tr/td[1]'

        #权限设置
        成员名称='//div[contains(@class,"el-table__body-wrapper")]//tr/td[1]/div[text()="{}"]'
        已授权复选框='//div[contains(@class,"el-table__body-wrapper")]//tr/td[1]/div[text()="{}"]/ancestor::tr/td[{}]//label[contains(@class,"checked")]'
        未授权复选框='//div[contains(@class,"el-table__body-wrapper")]//tr/td[1]/div[text()="{}"]/ancestor::tr/td[{}]//label[not(contains(@class,"checked"))]'
        禁用复选框='//div[contains(@class,"el-table__body-wrapper")]//tr/td[1]/div[text()="{}"]/ancestor::tr/td[{}]//label[contains(@class,"disabled")]'



class 创建项目页面:
    #创建项目
    页面名称='//div[text()="创建项目" and @class="title fz_l_gray"]'
    创建空白项目='//div[@class="create_empty comm_bgc"]/i'
    #模板
    模板卡片='//div[@class="fz_l_gray revit_project_t" and @title="{}"]'
    预览='//div[@class="fz_l_gray revit_project_t" and @title="{}"]/following-sibling::div//span[text()="预览"]'
    使用='//div[@class="fz_l_gray revit_project_t" and @title="{}"]/following-sibling::div//span[text()="使用"]'
    删除='//div[@class="fz_l_gray revit_project_t" and @title="{}"]/following-sibling::i'
    节点展开按钮 = '//div[@role="treeitem"]//span[text()="{}"]/ancestor::span/preceding-sibling::span[not( contains(@class,"expanded"))]'
    节点名称='//div[@role="treeitem"]//span[text()="{}"]'

    模板tab页='//div[@role="tablist"]/div[text()="{}"]'
    模板团队成员='//div[text()="{}"]/ancestor::tr/td[2]/div[text()="{}"]'

    提交按钮='//span[text()="项目名称"]/parent::div/following-sibling::div//button'



class 项目设置页面:

    收藏按钮='//div[text()="项目名称"]/following-sibling::div/i[1]'
    查看项目目录='//div[text()="项目名称"]/following-sibling::div/i[2]'
    删除项目='//div[text()="项目名称"]/following-sibling::div/div/i'

    项目成员tab页='//div[@id="tab-projectMember"]'
    项目生命周期模板设置='//div[@id="tab-projectCyclePlan"]'
    项目成员名称='//div[text()="{}"]/ancestor::tr/td[5]/div[text()="{}"]'#参数1为成员名称，参数2为角色名称
    角色编辑按钮='//div[text()="{}"]/ancestor::tr/td[last()]//i[@title="编辑角色"]'
    权限编辑按钮='//div[text()="{}"]/ancestor::tr/td[last()]//i[@title="编辑权限"]'


    #切换生命周期弹框
    当前节点名称='//div[@aria-label="修改生命周期预览"]//table//tr/td/div[text()="{}"]'
    变更节点列表框='//div[@aria-label="修改生命周期预览"]//table//tr/td/div[text()="{}"]/ancestor::tr/td[3]//i'

    #用户权限编辑弹框
    节点收起按钮='//div[@role="treeitem"]//span[contains(text(),"{}")]/preceding-sibling::span[contains(@class,"expanded")]'
    节点展开按钮='//div[@role="treeitem"]//span[contains(text(),"{}")]/preceding-sibling::span[not( contains(@class,"expanded"))]'
    节点名称='//div[@role="treeitem"]//span[contains(text(),"{}")]'
    子节点='//span[contains(text(),"{}")]/parent::div/following-sibling::div//span[contains(text(),"{}")]'#参数1为父节点，参数2为子节点

    #权限列表
    已选_权限复选框='//div[text()="{}"]/ancestor::tr/td[1]//span[contains(@class,"checked")]'
    未选_权限复选框='//div[text()="{}"]/ancestor::tr/td[1]//span[not(contains(@class,"checked"))]'
    权限复选框='//div[text()="{}"]/ancestor::tr/td[1]//spans'
    禁用_权限复选框='//div[text()="{}"]/ancestor::tr/td[1]//span[contains(@class,"disabled")]'

    #目生命周期模板设置
    新增生命周期='//div[@id="pane-projectCyclePlan"]//span[text()="新增"]'
    删除生命周期='//div[@id="pane-projectCyclePlan"]//span[text()="删除"]'
    生命周期名称='//div[@id="pane-projectCyclePlan"]//tr/td[2]/div[text()="{}"]'
    生命周期复选框='//tr/td[2]/div[text()="{}"]/ancestor::tr/td[1]'
    查看生命周期='//tr/td[2]/div[text()="{}"]/ancestor::tr/td[3]'
    已配置生命周期列表='//div[@id="pane-projectCyclePlan"]//tr/td[2]/div'

    未配置生命周期名称='//div[@aria-label="新增项目生命周期模板"]//tr/td[2]/div[text()="{}"]'
    未配置生命周期复选框='//div[@aria-label="新增项目生命周期模板"]//tr/td[2]/div[text()="{}"]/ancestor::tr/td[1]'


    #项目成员列表
    已选_成员复选框 = '//div[text()="{}"]/ancestor::tr/td[1]//span[contains(@class,"checked")]'
    未选_成员复选框 = '//div[text()="{}"]/ancestor::tr/td[1]//span[not(contains(@class,"checked"))]'
    权限复选框 = '//div[text()="{}"]/ancestor::tr/td[1]//spans'
    禁用_成员复选框 = '//div[text()="{}"]/ancestor::tr/td[1]//span[contains(@class,"disabled")]'

class 标签管理对象库:
    页面名称='//span[text()="标签管理"]'
    新增标签按钮='//div[@class="clearfix"]//span[text()=" 新增标签 "]'
    批量操作按钮='//span[text()=" 标签列表"]//following-sibling::button//span[text()=" 批量操作 "]'
    批量删除按钮='//div[@class="clearfix"]//span[text()=" 批量删除 "]'
    取消按钮='//div[@class="clearfix"]//span[text()=" 取消 "]'


    标签复选框='//table//tr/td[2]//div[text()="{}"]//ancestor::tr/td[1]//span'
    标签名='//table//tr/td[1]//div[text()="{}"]'
    标签创建人='//table//tr/td[2]//div[text()="{}"]'
    标签创建时间='//table//tr/td[3]//div[text()="{}"]'
    编辑单个标签='//div[text()="{}"]//ancestor::tr/td[last()]//a[@title="编辑标签"]'
    删除单个标签 = '//div[text()="{}"]//ancestor::tr/td[last()]//a[@title="删除"]'


    新增文件按钮='//div[@class="clearfix"]//span[text()="新增文件"]'
    文件批量操作按钮='//span[text()="文件列表"]//following-sibling::button//span[text()=" 批量操作 "]'
    批量删除标签文件 = '//span[text()="文件列表"]//following-sibling::button//span[text()="批量删除"]'
    批量打包标签文件='//span[text()="文件列表"]//following-sibling::button//span[text()="批量打包"]'


    标签文件名称='//table//tr/td[2]/div[text()="{}"]'
    标签文件复选框='//table//tr/td[3]/div[text()="{}"]//ancestor::tr/td[1]//span'
    标签文件版本='//table//tr/td[2]/div[text()="{}"]//ancestor::tr/td[3]/div[text()="{}"]'#文件名和版本

    移除标签文件='//table//tr/td[2]/div[text()="{}"]//ancestor::tr/td[last()]//a[@title="删除"]'
    跳转查看文件='//table//tr/td[2]/div[text()="{}"]//ancestor::tr/td[last()]//a[@title="跳转到文件"]'

    class 新增标签文件:
        树资源节点 = '//div[@aria-label="选择文件"]//div[@role="treeitem"]//span[contains(text(),"{}")]'
        节点收起按钮 = '//div[@aria-label="选择文件"]//div[@role="treeitem"]//span[contains(text(),"{}")]/preceding-sibling::span[contains(@class,"expanded")]'
        节点展开按钮 = '//div[@aria-label="选择文件"]//div[@role="treeitem"]//span[contains(text(),"{}")]/preceding-sibling::span[not(contains(@class,"expanded"))]'
        列表单选按钮 = '//table//tr/td[2]//div[contains(text(),"{}")]/ancestor::tr/td[1]//span'
        保存按钮 = '//div[@aria-label="选择文件"]/div[@class="el-dialog__footer"]//button/span[text()="保存"]'
        取消按钮 = '//div[@aria-label="选择文件"]/div[@class="el-dialog__footer"]//button/span[text()="取消"]'