class 公共元素对象库:
    手机号地区列表框='//span[@class="el-input__suffix"]//i'
    手机号地区列表框选项='//li[contains(@class,"dropdown__item")]/span[contains(text(),"{}")]'
    列表框='//*[text()="{}"]/following-sibling::div//i'
    列表框选项='//ul/li[contains(@class,"dropdown__item")]/span[text()="{}"]'
    输入框='//*[text()="{}"]/following-sibling::div//input'
    禁用_输入框='//*[text()="{}"]/following-sibling::div//input[@disabled="disabled"]'
    文本框='//*[text()="{}"]/following-sibling::div//textarea'
    单选按钮='//span[text()="{}"]/preceding-sibling::span'
    系统提示信息弹框='//div[contains(@class,"el-message")]//*[contains(text(),"{}")]'
    输入框错误信息提示='//div[@class="el-form-item__error" and contains(text(),"{}")]'

class 对话框对象库:
    对话框标题='//div[@class="el-message-box__title"]/span[text()="{}"]'
    关闭对话框 = '//span[text()="{}"]/parent::div/following-sibling::button'
    对话框内容 = '//span[text()="{}"]/ancestor::div/following-sibling::div//p[contains(text(),"{}")]'
    对话框按钮 = '//span[text()="{}"]/ancestor::div/following-sibling::div//button/span[contains(text(),"{}")]'
    对话框按钮2='//span[contains(text(),"{}")]/following-sibling::div//button/span[contains(text(),"{}")]'

    弹框标题='//div[@class="el-dialog__header"]/span[text()="{}"]'
    弹框按钮='//span[text()="{}"]/ancestor::div/following-sibling::div//button/span[contains(text(),"{}")]'
    弹框按钮2='//span[text()="{}"]/ancestor::div/following-sibling::div//button[contains(text(),"{}")]'
    关闭弹框='//span[text()="{}"]/following-sibling::button[@aria-label="Close"]'
    关闭弹框1='//span[text()="{}"]/following-sibling::button'

