class 用户信息对象库:
    账号信息='//div[@class="fz_l_gray"]//a[text()="账号信息"]'
    基本信息='//div[@class="fz_l_gray"]//a[text()="基本信息"]'
    class 账号信息对象库:
        非编辑状态手机号输入框='//label[text()="手机号"]/following-sibling::div/div[contains(@class,"is-disabled")]'
        切换手机号按钮='//span[text()="切换手机号"]'
        切换手机号弹窗保存='//div[@aria-label="切换手机号"]//button/span[text()="保存"]'
        电子邮箱输入框='//label[@for="userEmail"]/following-sibling::div//input'
        绑定邮箱按钮='//span[text()="绑定邮箱"]'
        切换邮箱按钮='//span[text()="切换邮箱"]'
        用户名输入框='//label[text()="用户名"]/following-sibling::div//input'
        修改密码按钮='//button/span[text()="修改密码"]'
        保存='//button/span[text()="保存"]'

    class 基本信息对象库:
        更改头像按钮='//span[text()="更改头像"]'
        姓输入框='//label[text()="姓名"]/following-sibling::div//input[@placeholder="姓"]'
        名输入框='//label[text()="姓名"]/following-sibling::div//input[@placeholder="名"]'

