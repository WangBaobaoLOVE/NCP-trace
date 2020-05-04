from pyecharts.charts import Map
from pyecharts import options as opts
#将数据处理成列表
locate = ['北京','天津','河北','山西','内蒙古','辽宁','吉林','黑龙江','上海','江苏','浙江','安徽','福建','江西','山东','河南','湖北','湖南','广东','广西','海南','重庆','四川','贵州','云南','陕西','甘肃','青海','宁夏','新疆','西藏']
popu = [10,8,18,8,5,29,8,17,27,24,12,11,6,7,22,16,11,14,18,5,1,7,14,4,6,8,6,15,13,39,25,21]
list1 = [[locate[i],popu[i]] for i in range(len(locate))]
map_1 = Map()
map_1.set_global_opts(
    title_opts=opts.TitleOpts(title="全国疫情确诊人数分布图"),
    visualmap_opts=opts.VisualMapOpts(max_=50)  #最大数据范围
    )
map_1.add("确诊人数", list1, maptype="china")
map_1.render('map1.html')