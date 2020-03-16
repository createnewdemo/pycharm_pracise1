#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 17:16
import json
import re
from pyecharts.charts import Line, Pie, Map, Page
from pyecharts import options as opts


def get_province_status(month, day):
    json_array = get_province_data(month, day)
    data = []
    for province in json_array:
        data.append((province['provinceShortName'], province['confirmedCount']))
    data.sort(key=lambda x: x[1], reverse=True)

    labels = [d[0] for d in data]

    counts = [d[1] for d in data]

    return labels, counts


def get_total_statistic(month, day):
    file = open('jsons/%d%d-总计.json' % (month, day), 'r', encoding='UTF-8')
    json_object = json.loads(file.read())
    file.close()
    return json_object


def get_default_pieces():
    return [
        {'min': 1000, 'color': '#450704'},
        {'max': 999, 'min': 100, 'color': '#75140B'},
        {'max': 99, 'min': 10, 'color': '#AD2217'},
        {'max': 9, 'min': 1, 'color': '#DE605B'},
        {'max': 0, 'color': '#FFFEE7'},
    ]


def get_html(month, day):
    import requests
    url = 'http://3g.dxy.cn/newh5/view/pneumonia'
    response = requests.get(url)
    html = str(response.content, 'UTF-8')
    html_file = open('htmls/%d%d.html' % (month, day), 'w', encoding='UTF-8')
    html_file.write(html)
    html_file.close()
    # 省份数据
    json_file = open('jsons/%d%d.json' % (month, day), 'w', encoding='UTF-8')
    matches = re.findall('\[[^>]+\]', html)
    for match in matches:
        try:
            json_array = json.loads(match)
            json_object = json_array[0]
            if 'provinceName' in json_object and json_object['provinceName'] == '湖北省':
                json_file.write(match)
                break
        except:
            continue
    json_file.close()

    # 总体统计数据
    total_statistic_file = open('jsons/%d%d-总计.json' % (month, day), 'w', encoding='UTF-8')
    matches = re.findall('\{"id":1,[^(>})]+\}', html)
    for match in matches:
        if "infectSource" in match:
            index = match.find(',"marquee":[')
            if index != -1:
                match = match[:index] + '}'
            total_statistic_file.write(match)
            break
    total_statistic_file.close()


def get_province_data(month, day):
    file = open('jsons/%d%d.json' % (month, day), 'r', encoding='UTF-8')
    json_array = json.loads(file.read())
    file.close()
    sort_arr = [json_obj for json_obj in json_array]
    return sorted(sort_arr, key=lambda x: x['confirmedCount'], reverse=True)


def get_map(labels, counts, where, title, size, pieces):
    my_map = Map(init_opts=opts.InitOpts(width=size[0], height=size[1]))
    my_map.add("新冠数据", [list(z) for z in zip(labels, counts)], where)  # 实现鼠标地方的数据
    my_map.set_series_opts(label_opts=opts.LabelOpts(font_size=8))
    my_map.set_global_opts(
        title_opts=opts.TitleOpts(title=title),
        legend_opts=opts.LegendOpts(is_show=False),
        visualmap_opts=opts.VisualMapOpts(
            pieces=pieces,
            is_piecewise=True,
            is_show=False
        ),
    )
    return my_map


def draw_multiple_map(month, day):
    page = Page(layout=Page.SimplePageLayout)
    size = ('1000px', '1000px')

    # 全国疫情地图
    labels, counts = get_province_status(month, day)
    country_map = get_map(labels=labels, counts=counts,
                          title='全国-%s例' % get_total_statistic(month, day)['confirmedCount'], size=size, where='china',
                          pieces=get_default_pieces())
    page.add(country_map)
    country_map.render('地图.html')


if __name__ == '__main__':
    m, d = 3, 16
    get_html(m, d)
    draw_multiple_map(m, d)
