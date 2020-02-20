import requests
import json
import pandas as pd

toEnglish = {
    '中国': 'China', '日本':'Japan', '新加坡':'Singapore', '泰国':'Thailand', '韩国': 'Korea',
    '马来西亚':'Malaysia', '越南':'Vietnam', '德国':'Germany','美国': 'United States','澳大利亚':'Australia',
    '法国':'France','英国':'United Kingdom','阿联酋':'United Arab Emirates','加拿大': 'Canada','印度':'India',
    '菲律宾':'Philippines','意大利':'Italy','西班牙':'Spain','俄罗斯': 'Russia','芬兰':'Finland',
    '斯里兰卡':'Sri Lanka', '瑞典':'Sweden', '柬埔寨':'Cambodia', '尼泊尔':'Nepal', '比利时':'Belgium',
    '伊朗':'Iran'
}

#  腾讯数据接口获取json格式疫情数据
def get_ncp_data():
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    data = requests.get(url).json()['data']
    return data

#  得到累计疫情数据
def get_dailyadd_data(all):
    return all['chinaDayAddList']

#  得到增长疫情数据
def get_daily_data(all):
    return all['chinaDayList']

#  扁平化中国疫情数据
def flatten_ncp_data(all):
    #  初始化结果链表
    cities = []
    #  数据最新更新时间
    date = all['lastUpdateTime']
    # 第一层：国家
    china = all['areaTree'][0]['children']  # 获得中国数据
    # 第二层：省
    for province in china:
        province_ncp = province['children']
        # 第三层：市
        for city in province_ncp:
            # 输出格式
            city_ncp = {
                '日期': date,
                '省份': province['name'],
                '市': city['name']+'市',
                # '新增确认': city['today']['confirm'],
                # '新增治愈': city['today']['heal'],
                # '新增死亡': city['today']['dead'],
                '累计确认': city['total']['confirm'],
                '累计治愈': city['total']['heal'],
                '累计死亡': city['total']['dead']
            }
            cities.append(city_ncp)
    return cities

def get_world_data(all):
    countries = []

    date = all['lastUpdateTime']
    world_ncp_data = all['areaTree']

    for country in world_ncp_data:
        country_ncp = {
            '日期': date,
            '国家': country['name'],
            'country': toEnglish[country['name']],
            '累计确认': country['total']['confirm'],
            '累计治愈': country['total']['heal'],
            '累计死亡': country['total']['dead']
        }
        countries.append(country_ncp)
    return countries


all = json.loads(get_ncp_data())
data = pd.DataFrame(flatten_ncp_data(all))
daliy_data = pd.DataFrame(get_daily_data(all))[['date','confirm','suspect','dead','heal']]
daliyadd_data = pd.DataFrame(get_dailyadd_data(all))[['date','confirm','suspect','dead','heal']]
world_data = pd.DataFrame(get_world_data(all))

