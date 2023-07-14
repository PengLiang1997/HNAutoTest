class 分享管理对象库:
    我的分享tab页='//div[@class="share_main"]//div[text()=" 我的分享 "]'
    访问记录tab页='//div[@class="share_main"]//div[text()=" 访问记录 "]'
    全选复选框='//table[@class="el-table__header"]//tr/th[1]//span'
    #我的分享
    分享内容名称='//table[@class="el-table__body"]//tr/td[2]//a[not(contains(@class,"disabled"))]/span[text()="{}"]'
    置灰_分享内容名称='//table[@class="el-table__body"]//tr/td[2]//a[contains(@class,"disabled")]/span[text()="{}"]'
    我的分享复选框='//span[text()="{}"]//ancestor::tr/td[1]//span'
    过期时间='//span[text()="{}"]//ancestor::tr/td[4]//span'
    过期时间输入框='//span[text()="{}"]//ancestor::tr/td[4]//input[@placeholder="选择日期时间"]'
    生效_是否生效按钮='//span[text()="{}"]//ancestor::tr/td[5]/div/div[contains(@class,"checked")]'
    失效_是否生效按钮='//span[text()="{}"]//ancestor::tr/td[5]/div/div[not(contains(@class,"checked"))]'
    访问记录='//span[text()="{}"]//ancestor::tr/td[7]//span'
    访问次数='//span[text()="{}"]//ancestor::tr/td[8]/div'
    浏览次数='//span[text()="{}"]//ancestor::tr/td[9]/div'
    下载次数='//span[text()="{}"]//ancestor::tr/td[10]/div'
    编辑过期时间='//span[text()="{}"]//ancestor::tr/td[last()]//a[@title="编辑"]'
    取消编辑过期时间='//span[text()="{}"]//ancestor::tr/td[last()]//a[@title="取消编辑"]'
    取消分享='//span[text()="{}"]//ancestor::tr/td[last()]//a[@title="取消分享"]'
    批量取消分享='//button/span[text()="取消分享"]'
    操作类型列表框 = '//*[@placeholder="操作类型"]/following-sibling::span//i'


    #访问记录

    访问记录名称='//table[@class="el-table__body"]//tr/td[2]//span[text()=" {} "]'
    分享类型='//span[text()=" {} "]//ancestor::tr/td[3]//div'
    分享创建时间='//span[text()=" {} "]//ancestor::tr/td[5]//div'
    最后一次访问时间='//span[text()=" {} "]//ancestor::tr/td[6]//div'
    删除访问记录='//span[text()=" {} "]//ancestor::tr/td[last()]//span'
    批量删除访问记录='//button/span[text()="删除"]'