import requests
import json
import pandas as pd

#  腾讯数据接口获取json格式疫情数据
def get_ncp_data():
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    data = requests.get(url).json()['data']
    return data

#  扁平化中国疫情数据
def flatten_ncp_data():
    all = json.loads(get_ncp_data())
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
                '市': city['name'],
                '新增确认': city['today']['confirm'],
                '新增治愈': city['today']['heal'],
                '新增死亡': city['today']['dead'],
                '累计确认': city['total']['confirm'],
                '累计治愈': city['total']['heal'],
                '累计死亡': city['total']['dead']
            }
            cities.append(city_ncp)
    return cities

data = pd.DataFrame(flatten_ncp_data())