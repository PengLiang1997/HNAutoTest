class 设置页对象库:
    生命周期页='//div[contains(@class,"tab_left fz14") and contains(text(),"生命周期")]'
    版次页='//div[contains(@class,"tab_left fz14") and contains(text(),"版次")]'
    属性页='//div[contains(@class,"tab_left fz14") and contains(text(),"属性")]'

    class 生命周期管理工作区:
        新增='//div[@class="life_cycle_btns comm_bgc"]//span[text()="新增"]'
        编辑='//div[@class="life_cycle_btns comm_bgc"]//span[text()="编辑"]'
        复制='//div[@class="life_cycle_btns comm_bgc"]//span[text()="复制"]'
        删除='//div[@class="life_cycle_btns comm_bgc"]//span[text()="删除"]'

        #新增生命周期弹窗
            #生命周期节点列表
        添加生命周期节点='//div[text()="生命周期节点"]/following-sibling::div//button[contains(@class,"jiahao")]'
        删除生命周期节点='//div[text()="生命周期节点"]/following-sibling::div//button[contains(@class,"jianhao")]'
        上移生命周期节点='//div[text()="生命周期节点"]/following-sibling::div//button[contains(@class,"xiangshangjiantou")]'
        下移生命周期节点='//div[text()="生命周期节点"]/following-sibling::div//button[contains(@class,"xiangxiajiantou")]'

        生命周期节点名称='//div[text()="生命周期节点"]/following-sibling::div//tr/td[1]//span[text()="{}"]'
        编辑生命周期节点按钮='//div[text()="生命周期节点"]/following-sibling::div//tr/td[1]//span[text()="{}"]/ancestor::tr/td[3]//i'
        生命周期节点名称输入框='//div[text()="生命周期节点"]/following-sibling::div//tr/td[1]//input'
        生命周期节点描述输入框='//div[text()="生命周期节点"]/following-sibling::div//tr/td[2]//input'
        生命周期节点保存按钮='//div[text()="生命周期节点"]/following-sibling::div//tr[last()]/td[3]//i'
        生命周期节点保存按钮2='//div[text()="生命周期节点"]/following-sibling::div//tr/td[3]//i[@class="el-icon-check"]'
        生命周期节点编辑按钮='//div[text()="生命周期节点"]/following-sibling::div//span[text()="{}"]/ancestor::tr//i[@class="el-icon-edit"]'
            #节点流程列表
        开始节点和结束节点='//tr/td/div[text()="{}"]/parent::td/following-sibling::td/div[text()="{}"]'#参数1为起始节点名称，参数2为结束节点名称
        节点流程单选启用按钮='//tr/td/div[text()="{}"]/parent::td/following-sibling::td/div[text()="{}"]/parent::td/following-sibling::td//span'

        #生命周期列表
        生命周期列表全选按钮='//table//tr/th[1]//label'
        生命周期名称='//table//tr/td[2]//span[text()="{}"]'
        生命周期列表复选框='//table//tr/td[2]//span[text()="{}"]/ancestor::tr/td[1]//span'
        设置默认单选框='//table//tr/td[2]//span[text()="{}"]/ancestor::tr/td[last()]//span'

        #生命周期明细
            #生命周期节点
        生命周期节点 = '//div[text()="生命周期节点"]/following-sibling::div//tr/td[1]//div[text()="{}"]'
        节点流程='//div[text()="节点流程"]/following-sibling::div//tr/td[1]/div[text()="{}"]/ancestor::tr/td[3]/div[text()="{}"]'

    class 版次管理工作区:
        新增='//div[@class="edition_btns comm_bgc"]//span[text()="新增"]'
        编辑='//div[@class="edition_btns comm_bgc"]//span[text()="编辑"]'
        删除='//div[@class="edition_btns comm_bgc"]//span[text()="删除"]'
        置灰_删除='//div[@class="edition_btns comm_bgc"]/button[@disabled="disabled"]/span[text()="删除"]'
        #版次列表
        版次名称='//table//tr/td[2]//span[text()="{}"]'
        版次复选框='//table//tr/td[2]//span[text()="{}"]/ancestor::tr/td[1]//span'
        禁用_版次复选框 = '//table//tr/td[2]/div/span[text()="{}"]/ancestor::tr/td[1]//span[contains(@class,"disabled")]'
        是否默认单选框='//table//tr/td[2]//span[text()="{}"]/ancestor::tr/td[last()]//span'

        #版次
        添加版次节点='//div/button[contains(@class,"jiahao")]'
        删除版次节点='//div/button[contains(@class,"jianhao")]'
        上移版次节点='//div/button[contains(@class,"xiangshangjiantou")]'
        置灰_上移版次节点='//div/button[contains(@class,"xiangshangjiantou") and @disabled="disabled"]'
        下移版次节点='//div/button[contains(@class,"xiangxiajiantou")]'
        置灰_下移版次节点='//div/button[contains(@class,"xiangxiajiantou") and @disabled="disabled"]'

        版次内容='//div[@aria-label="编辑" or @aria-label="新增"]//tr/td//span[text()="{}"]'
        版次内容输入框='//tr/td[2]//input'
        保存版次节点='//div/div//tr/td[3]//i[@class="el-icon-check"]'
        编辑版次节点按钮='//div/div//tr/td[2]//span[text()="{}"]/ancestor::tr/td[3]//i[@class="el-icon-edit"]'

        #版次明细
        版次明细节点='//div[text()="版次明细"]/ancestor::div[@class="edition_b comm_bgc"]//table//tr/td[2]//span[text()="{}"]'
    class 属性管理工作区:
        新增 = '//div[@class="attr_btns comm_bgc"]//span[text()="新增"]'
        编辑 = '//div[@class="attr_btns comm_bgc"]//span[text()="编辑"]'
        删除 = '//div[@class="attr_btns comm_bgc"]//span[text()="删除"]'
        置灰_删除按钮='//div[@class="attr_btns comm_bgc"]//button[@disabled="disabled"]/span[text()="删除"]'

        #属性列表
        属性系统全选复选框 = '//div[@class="attr_main_t"]//tr/th//span'
        属性系统名称='//table//tr/td[2]/div/span[text()="{}"]'
        属性系统复选框='//table//tr/td[2]//span[text()="{}"]/ancestor::tr/td[1]'
        禁用_属性系统复选框='//table//tr/td[2]/div/span[text()="{}"]/ancestor::tr/td[1]//span[contains(@class,"disabled")]'
        属性系统名称输入框='//table[@class="el-table__body"]//tr/td[2]//input'
        属性系统描述输入框='//table[@class="el-table__body"]//tr/td[3]//input'
        属性系统保存按钮='//table[@class="el-table__body"]//tr/td[3]//i'

        #属性明细
        添加属性='//button/span[contains(text(),"添加属性")]'
        导入属性 = '//button/span//div[contains(text(),"导入属性")]'
        下载模板 = '//button/span[contains(text(),"下载模板")]'
        删除属性 = '//div[@class="fzcolor top_btn"]//button/span[contains(text(),"删除")]'

        属性行复选框 = '//div[@class="attr_b"]//table[@class="el-table__body"]//tr[{}]/td[1]//span'  # 参数为行号
        服务类别输入框 = '//div[@class="attr_b"]//table[@class="el-table__body"]//tr[{}]/td[2]//input'  # 参数为行号
        属性类别输入框 = '//div[@class="attr_b"]//table[@class="el-table__body"]//tr[{}]/td[3]//input'  # 参数为行号
        属性名称输入框 = '//div[@class="attr_b"]//table[@class="el-table__body"]//tr[{}]/td[4]//input'  # 参数为行号
        属性描述输入框 = '//div[@class="attr_b"]//table[@class="el-table__body"]//tr[{}]/td[5]//input'  # 参数为行号
        行删除按钮 = '//div[@class="attr_b"]//table[@class="el-table__body"]//tr[{}]/td[last()]//span'  # 参数为行号
        行保存按钮 = '//div[@class="attr_b"]//table[@class="el-table__body"]//tr[{}]/td[last()]/div/button'  # 参数为行号

        删除对话框='//div[contains(@id,"el-popover")]//p[contains(text(),"确定删除吗?")]'
        删除取消按钮='//div[contains(@id,"el-popover")]//button/span[contains(text(),"取消")]'
        删除确认按钮='//div[contains(@id,"el-popover")]//button/span[contains(text(),"确定")]'