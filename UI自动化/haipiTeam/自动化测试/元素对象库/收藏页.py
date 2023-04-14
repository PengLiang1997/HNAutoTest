class 收藏对象库:
    收藏条件列表框='//div[@class="project_top comm_bgc"]//input[@placeholder="请选择"]'
    收藏条件列表选项='//ul[contains(@class,"dropdown__list")]//li/span[contains(text(),"{}")]'
    收藏资源名称='//table//tr/td/div[text()="{}"]'
    资源类型='//table//tr/td/div[text()="{}"]/parent::td/following-sibling::td[1]/div[text()="{}"]'
    取消收藏按钮='//table//tr/td/div[text()="{}"]/parent::td/following-sibling::td[last()]//i[1]'
    查看收藏按钮='//table//tr/td/div[text()="{}"]/parent::td/following-sibling::td[last()]//i[2]'
    收藏资源类型='//div[@role="tablist"]//div[contains(text(),"{}")]/I[1]'