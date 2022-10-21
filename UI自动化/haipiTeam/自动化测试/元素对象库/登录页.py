class 登录页对象库:
    语言='//span[@class="el-link--inner" and text()="中文"]'
    主题='//span[text()=" 主题 "]'
    手机号输入框='//input[@placeholder="请输入手机号"]'
    验证码输入框='//input[@placeholder="验证码"]'
    验证码按钮='//button//span[text()="获取验证码 "]'
    开始使用='//button//span[text()="开始使用"]'
    账号密码登录='//a//span[text()="账号密码登录"]'
    账号输入框='//input[@placeholder="请输入用户名或邮箱"]'
    密码输入框='//input[@placeholder="请输入密码"]'
    登录按钮='//button/span[text()="登录"]'
    短信快捷登录='//a//span[text()="短信快捷登录"]'
    忘记密码='//a//span[text()="忘记密码"]'

    class 忘记密码对象库:
        重置密码弹窗标题='//div[@class="forget_pwd_t"]/h3[text()="重置密码"]'
        重置密码按钮='//button/span[text()="重置密码"]'
        密码输入框='//form/div[1]//input[@placeholder="请输入密码"]'
        确认密码输入框='//form/div[2]//input[@placeholder="请再次输入"]'
        提交按钮='//button/span[text()="提交"]'

class 人机验证弹窗对象库:
    弹窗标题='//div[text()=" 请完成安全验证 "]'
    关闭弹窗='//div[text()=" 请完成安全验证 "]/span'
    滑动按钮='//div[@class="verify-left-bar"]/div'
    背景图='//div[@class="verify-img-panel"]/img'
    拼图='//div[@class="verify-sub-block"]/img'


