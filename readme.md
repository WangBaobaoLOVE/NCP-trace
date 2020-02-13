## 本文主要内容

- 目前困境
- 使用pyecharts搭建中国疫情地图
- 后续开发

## 困难

- 数据来源问题已经解决，原本是根据支付宝的肺炎实时追踪手敲的，并保存在data_2020_02_12.py中。现在使用腾讯数据接口获取疫情数据。

## pyecharts

### pyecharts的介绍

pyecharts是一个用于生成Echarts图表的类库，Echarts是百度开源的一个数据可视化JS库

### pyecharts的安装

- 安装库：pip install pyecharts
- 安装地图文件：
  - 全球国家地图: pip install echarts-countries-pypkg
  - 中国省级地图: pip install echarts-china-provinces-pypkg
  - 中国市级地图: pip install echarts-china-cities-pypkg

### pyecharts的使用

- [pyecharts官网](http://pyecharts.org/#/)
- [pyecharts效果图展示](http://pyecharts.herokuapp.com/)

### pyecharts的代码示例

``` python
from pyecharts.charts import Map
from pyecharts import options as opts
#将数据处理成列表
locate = ['北京','天津','河北','山西','内蒙古','辽宁','吉林','黑龙江','上海','江苏','浙江','安徽','福建','江西','山东','河南','湖北','湖南','广东','广西','海南','重庆','四川','贵州','云南','陕西','甘肃','青海','宁夏','新疆','西藏']
app_price = [10.84,8.65,18.06,8.90,5.04,29.20,8.98,17.80,27.81,24.24,12.72,11.10,6.30,7.00,22.45,16.92,11.00,14.99,18.85,5.85,1.40,7.32,14.61,4.62,6.05,8.07,6.73,15.54,13.00,39.07,25.61,21.3]
list1 = [[locate[i],app_price[i]] for i in range(len(locate))]
map_1 = Map()
map_1.set_global_opts(
    title_opts=opts.TitleOpts(title="2019年全国各省苹果价格表"),
    visualmap_opts=opts.VisualMapOpts(max_=50)  #最大数据范围
    )
map_1.add("2019年全国各省苹果价格", list1, maptype="china")
map_1.render('map1.html')
```

**示例效果图：**![](./images/示例效果图.png)

### 注意事项

<font color=red>**pyechart旧版本和新版本不兼容，且代码编写风格迥异，旧版本不再维护，鼓励大家使用新版本。**</font>

## 后续开发

- 累计趋势图
- 增长趋势图
- 疫情发展预测

## 参考资料

- [python绘制中国地图](https://zhuanlan.zhihu.com/p/45202403)
- [pyecharts官网](http://pyecharts.org/#/)
- [pyecharts效果图展示](http://pyecharts.herokuapp.com/)
- [python制作疫情实时分布图](https://www.zhihu.com/people/ji-jin-51-37)
- 疫情数据来自腾讯数据接口

