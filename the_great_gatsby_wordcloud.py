from random import choices
from string import ascii_letters, digits
import wordcloud
import matplotlib.colors as colors
import numpy as np
from PIL import Image

def show(s):
    # 根据指定的颜色创建colormap对象
    color = ['#000000', '#00FF00', '#0000FF', '#FF0000']
    colormap = colors.ListedColormap(color)
    maskIm = Image.open('bgpic.png')                        # 选取词云的背景图
    size = maskIm.size
    # 创建cloudword对象，使用自定义颜色表
    wc = wordcloud.WordCloud(
        r'C:\windows\fonts\simhei.ttf',                     # 词云图中文本的字体
        width=size[0], height=size[1],                      # 词云图大小
        background_color='white',                           # 背景色
        mask=np.array(maskIm),                              # 自定义形状
        max_font_size=380,                                  # 最大字号
        font_step=3,                                        # 相邻字号的步长
        colormap=colormap,                                  # 自定义文本颜色
        prefer_horizontal=0.5                               # 无法水平放置就垂直放置
    )
    # 创建并显示词云
    wc.generate(s).to_image().show()

# 按频率显示，频率越高的词越大
txt = open("The great Gatsby.txt", "r").read()              # 打开读入英文文档
txt = txt.lower()
s = txt.join(choices(ascii_letters+digits+' '*200, k=2000))
show(s)