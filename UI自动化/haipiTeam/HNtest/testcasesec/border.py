'''
此类主要是定义一些枚举变量，定义元素边缘、部分、中心、象限的各个位置点
'''
from enum import IntEnum

class BorderPoints(IntEnum):
    LEFT_TOP=1#左上角
    TOP=2#上边缘中间
    RIGHT_TOP=3#右上角
    LEFT=4#左边缘中间
    CENTER=5#中心
    RIGHT=6#右边缘中间
    LEFT_BOTTOM=7#左下角
    BOTTOM=8#下边缘中间
    RIGHT_BOTTOM=9#右下角
    PART_UP=10#上半部
    PART_DOWN=11#下半部
    PART_RIGHT=12#右半部
    PART_LEFT=13#左半部
    QUARORANT_A=14#第一象限
    QUARORANT_B = 15#第二象限
    QUARORANT_C = 16#第三象限
    QUARORANT_D = 17#第四象限