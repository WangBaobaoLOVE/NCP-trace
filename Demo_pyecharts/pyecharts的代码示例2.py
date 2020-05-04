# -*- coding: utf-8 -*-
"""
@author: Dell Created on Mon Feb  3 11:22:25 2020
"""
from pyecharts.charts import Map
from pyecharts import options as opts
from pyecharts.globals import ThemeType#主题

# 使用snapshot-selenium渲染成图片
from snapshot_selenium import snapshot
from pyecharts.render import make_snapshot


# Map-VisualMap（分段型）
def map_visualmap() -> Map:
    ls = [['湖北', 9074], ['浙江', 661], ['广东', 632], ['河南', 493], ['湖南', 463], ['安徽', 340], ['江西', 333], ['重庆', 275], ['江苏', 236], ['四川', 231], ['山东', 230], ['北京', 191], ['上海', 182], ['福建', 159], ['陕西', 116], ['广西', 111], ['云南', 105], ['河北', 104], ['黑龙江', 95], ['辽宁', 69], ['海南', 64], ['山西', 56], ['天津', 48], ['甘肃', 40], ['贵州', 38], ['宁夏', 28], ['内蒙古', 27], ['吉林', 23], ['新疆', 21], ['香港', 14], ['青海', 11], ['台湾', 10], ['澳门', 8], ['西藏', 1]]
    #ls = [list(z) for z in zip(keys, values)]#列表推导式
    c = (
        #初始化配置项中可以设置画布宽高，背景色和主题
        Map(init_opts=opts.InitOpts(bg_color="#FFFAFA", theme=ThemeType.ROMANTIC))
        .add("确诊人数", ls, "china", is_map_symbol_show=False,)#设置是否显示地图上的小红点
        .set_global_opts(
            #标题配置项，pos_left可取值center、left、right、5%等等
            title_opts=opts.TitleOpts(title="全国疫情确诊人数分布图", pos_left="left"),
            visualmap_opts=opts.VisualMapOpts(
                is_piecewise=True,#设置是否为分段显示
                # 自定义的每一段的范围，以及每一段的文字，以及每一段的特别的样式。例如：
                pieces=[
                    {"min": 1000, "label": '>1000人', "color": "#FF3030"}, # 不指定 max，表示 max 为无限大（Infinity）。
                    {"min": 500, "max": 1000, "label": '500-1000人', "color": "#FF4500"},
                    {"min": 100, "max": 499, "label": '100-499人', "color": "#FF7F50"},
                    {"min": 10, "max": 99, "label": '10-99人', "color": "#FFA500"},
                    {"min": 1, "max": 9, "label": '1-9人', "color": "#FFDEAD"},
                    #{"value": 0.004, "label": '123（自定义特殊颜色）', "color": 'grey'},# //表示 value 等于 123 的情况
                    #{"max": 0, "color": "blue"}     # 不指定 min，表示 min 为无限大（-Infinity）。
                ],
                # 两端的文本，如['High', 'Low']。
                #range_text=['高', '低'],
            ),
        )
    )
    return c


if __name__ == "__main__":
    #map_visualmap().render_notebook()#这句代码是直接在notebook中显示图片的
    make_snapshot(snapshot, map_visualmap().render(), "全国疫情确诊人数分布图加背景色.png")# 保存为图片

"""JavascriptException: javascript error: echarts is not defined
  (Session info: headless chrome=79.0.3945.130)
出现这个错误是由于没有网络，渲染图片的js文件是从网上CDN获取的  
"""