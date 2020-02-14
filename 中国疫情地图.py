from pyecharts.charts import Map, Line
from pyecharts import options as opts
from pyecharts.globals import ThemeType#主题
from getData import *
import pygal

#将数据处理成列表
list1 = [[i, j] for i, j in zip(data['省份'], data['累计确认'])]
total_pupo = data['累计确认'].sum()

#  创建国家地图
map_1 = Map(init_opts=opts.InitOpts(bg_color="#FFFAFA", theme=ThemeType.ROMANTIC))
map_1.set_global_opts(
    title_opts=opts.TitleOpts(title="全国疫情确诊人数分布图——"+str(total_pupo)),
    visualmap_opts=opts.VisualMapOpts(
        is_piecewise=True,#设置是否为分段显示
        # 自定义的每一段的范围，以及每一段的文字，以及每一段的特别的样式。例如：
        pieces=[
            {"min": 1000, "label": '>1000人', "color": "#FF3030"}, # 不指定 max，表示 max 为无限大（Infinity）。
            {"min": 500, "max": 1000, "label": '500-1000人', "color": "#FF4500"},
            {"min": 100, "max": 499, "label": '100-499人', "color": "#FF7F50"},
            {"min": 10, "max": 99, "label": '10-99人', "color": "#FFA500"},
            {"min": 1, "max": 9, "label": '1-9人', "color": "#FFDEAD"},
        ],
     ),
)
map_1.add("确诊人数", list1, maptype="china", is_map_symbol_show=False)
map_1.render('./pages/中国疫情地图.html')

#  创建中国省份地图
province_names = data[data['省份'].duplicated()==False]['省份']

for province_name in province_names:
    province_ncp_data = data[data['省份']==province_name]
    city_ncp_data = [[i, j] for i, j in zip(province_ncp_data['市'], province_ncp_data['累计确认'])]

    map_province = Map(init_opts=opts.InitOpts(bg_color="#FFFAFA", theme=ThemeType.ROMANTIC))
    map_province.add("确诊人数", city_ncp_data, maptype=province_name)
    map_province.set_global_opts(
        title_opts=opts.TitleOpts(title=province_name+"疫情确诊人数分布图——" + str(province_ncp_data['累计确认'].sum())),
        visualmap_opts=opts.VisualMapOpts(
            is_piecewise=True,  # 设置是否为分段显示
            # 自定义的每一段的范围，以及每一段的文字，以及每一段的特别的样式。例如：
            pieces=[
                {"min": 1000, "label": '>1000人', "color": "#FF3030"},  # 不指定 max，表示 max 为无限大（Infinity）。
                {"min": 500, "max": 1000, "label": '500-1000人', "color": "#FF4500"},
                {"min": 100, "max": 499, "label": '100-499人', "color": "#FF7F50"},
                {"min": 10, "max": 99, "label": '10-99人', "color": "#FFA500"},
                {"min": 1, "max": 9, "label": '1-9人', "color": "#FFDEAD"},
            ],
        ),
    )

    map_province.render('./pages/'+province_name+'疫情地图.html')

#  创建世界疫情地图
world_ncp_data = [[i, j] for i, j in zip(world_data['country'], world_data['累计确认'])]

map_world = Map(init_opts=opts.InitOpts(bg_color="#FFFAFA", theme=ThemeType.ROMANTIC))
map_world.add("确诊人数", world_ncp_data, maptype="world", is_map_symbol_show=False)
map_world.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
map_world.set_global_opts(
    title_opts=opts.TitleOpts(title="世界疫情确诊人数分布图——"+str(world_data['累计确认'].sum())),
    visualmap_opts=opts.VisualMapOpts(
        is_piecewise=True,#设置是否为分段显示
        # 自定义的每一段的范围，以及每一段的文字，以及每一段的特别的样式。例如：
        pieces=[
            {"min": 1000, "label": '>1000人', "color": "#FF3030"}, # 不指定 max，表示 max 为无限大（Infinity）。
            {"min": 500, "max": 1000, "label": '500-1000人', "color": "#FF4500"},
            {"min": 100, "max": 499, "label": '100-499人', "color": "#FF7F50"},
            {"min": 10, "max": 99, "label": '10-99人', "color": "#FFA500"},
            {"min": 1, "max": 9, "label": '1-9人', "color": "#FFDEAD"},
        ],
     ),
)

map_world.render('./pages/世界疫情地图.html')

# 累计趋势
dayAddLine = pygal.Line(x_label_rotation=20, show_y_guides=False,show_minor_x_labels=False)
dayAddLine.title = '累计趋势(全国)'
dayAddLine.x_labels = daliy_data['date']
dayAddLine.add("确诊", daliy_data['confirm'])
dayAddLine.add("疑似", daliy_data['suspect'])
dayAddLine.add("死亡", daliy_data['dead'], secondary=True)
dayAddLine.add("治愈", daliy_data['heal'], secondary=True)
dayAddLine.x_labels_major = list(daliy_data['date'])[::5]
dayAddLine.render_to_file('./images/累计趋势.svg')

# 新增趋势
dayAddLine = pygal.Line(x_label_rotation=20, show_y_guides=False,show_minor_x_labels=False)
dayAddLine.title = '新增趋势(全国)'
dayAddLine.x_labels = daliyadd_data['date']
dayAddLine.add("确诊", daliyadd_data['confirm'])
dayAddLine.add("疑似", daliyadd_data['suspect'])
dayAddLine.add("死亡", daliyadd_data['dead'], secondary=True)
dayAddLine.add("治愈", daliyadd_data['heal'], secondary=True)
dayAddLine.x_labels_major = list(daliyadd_data['date'])[::5]
dayAddLine.render_to_file('./images/新增趋势.svg')
