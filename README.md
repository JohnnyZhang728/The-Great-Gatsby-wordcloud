# The-Great-Gatsby-wordcloud
## the English and Chinese versions of the great Gatsby word cloud
<br>1.English version: The Great Gatsby.txt && 中文文本：了不起的盖茨比.txt
<br>2.英文文本中使用的词云背景图:bgpic.png && 中文文本中使用的词云背景图:butterfly.png
<br>3.中文文本使用jieba库进行分词
<br>4.由于中译本出现诸多语气词、虚词、人名等高频但不利于文章分析的词，故需将此类词先进行预处理再进行词云绘制。由于笔者此时尚未学会tf-idf算法，故这里采用创建exclude{},进行手动筛选剔除词。
