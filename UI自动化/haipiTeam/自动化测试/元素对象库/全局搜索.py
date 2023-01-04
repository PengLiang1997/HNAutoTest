class 全局搜索对象库:
    搜索框='//input[@placeholder="请输入内容"]'
    搜索按钮='//button/span[text()="搜索"]'

    文件tab页='//div[@id="tab-file"]'
    目录tab页='//div[@id="tab-folder"]'
    项目tab页='//div[@id="tab-project"]'
    项目成员tab页='//div[@id="tab-team_user"]'

    暂无数据提示='//span[text()="暂无数据"]'

    #文件搜索
    列表文件名称='//span[text()="{}"]'
    文件路径='//span[text()="{}"]/ancestor::tr/td[4]/div[text()="{}"]'#参数1文件名称，参数2文件路径
    文件版次='//span[text()="{}"]/ancestor::tr/td[6]/div[text()="{}"]'

    #目录搜索
    目录名称='//span[text()="{}"]'
    目录创建人='//span[text()="{}"]/ancestor::tr/td[2]/div[text()="{}"]'
    目录路径='//span[text()="{}"]/ancestor::tr/td[3]/div[text()="{}"]'

    #项目搜索
    项目名称='//span[text()="{}"]'
    项目创建人='//span[text()="{}"]/ancestor::tr/td[3]/div[text()="{}"]'
    项目路径='//span[text()="{}"]/ancestor::tr/td[5]/div[text()="{}"]'

    #项目成员搜索
    成员用户名='/span[text()="{}"]'
    成员项目名称='//span[text()="{}"]/ancestor::tr/td[2]/div[text()="{}"]'
    成员权限名称='//span[text()="{}"]/ancestor::tr/td[3]/div[text()="{}"]'