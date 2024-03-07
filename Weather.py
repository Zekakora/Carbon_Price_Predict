import re
import calendar
import numpy as np
import pandas as pd
from datetime import datetime
from time import sleep
import requests
from bs4 import BeautifulSoup
import openpyxl

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Cookie': 'lianjia_uuid=9d3277d3-58e4-440e-bade-5069cb5203a4; UM_distinctid=16ba37f7160390-05f17711c11c3e-454c0b2b-100200-16ba37f716618b; _smt_uid=5d176c66.5119839a; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216ba37f7a942a6-0671dfdde0398a-454c0b2b-1049088-16ba37f7a95409%22%2C%22%24device_id%22%3A%2216ba37f7a942a6-0671dfdde0398a-454c0b2b-1049088-16ba37f7a95409%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _ga=GA1.2.1772719071.1561816174; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1561822858; _jzqa=1.2532744094467475000.1561816167.1561822858.1561870561.3; CNZZDATA1253477573=987273979-1561811144-%7C1561865554; CNZZDATA1254525948=879163647-1561815364-%7C1561869382; CNZZDATA1255633284=1986996647-1561812900-%7C1561866923; CNZZDATA1255604082=891570058-1561813905-%7C1561866148; _qzja=1.1577983579.1561816168942.1561822857520.1561870561449.1561870561449.1561870847908.0.0.0.7.3; select_city=110000; lianjia_ssid=4e1fa281-1ebf-e1c1-ac56-32b3ec83f7ca; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiMzQ2MDU5ZTQ0OWY4N2RiOTE4NjQ5YmQ0ZGRlMDAyZmFhODZmNjI1ZDQyNWU0OGQ3MjE3Yzk5NzFiYTY4ODM4ZThiZDNhZjliNGU4ODM4M2M3ODZhNDNiNjM1NzMzNjQ4ODY3MWVhMWFmNzFjMDVmMDY4NWMyMTM3MjIxYjBmYzhkYWE1MzIyNzFlOGMyOWFiYmQwZjBjYjcyNmIwOWEwYTNlMTY2MDI1NjkyOTBkNjQ1ZDkwNGM5ZDhkYTIyODU0ZmQzZjhjODhlNGQ1NGRkZTA0ZTBlZDFiNmIxOTE2YmU1NTIxNzhhMGQ3Yzk0ZjQ4NDBlZWI0YjlhYzFiYmJlZjJlNDQ5MDdlNzcxMzAwMmM1ODBlZDJkNmIwZmY0NDAwYmQxNjNjZDlhNmJkNDk3NGMzOTQxNTdkYjZlMjJkYjAxYjIzNjdmYzhiNzMxZDA1MGJlNjBmNzQxMTZjNDIzNFwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCIzMGJlNDJiN1wifSIsInIiOiJodHRwczovL2JqLmxpYW5qaWEuY29tL3p1ZmFuZy9yY28zMS8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ=='
}


def time_convert(start, end):
    start = pd.Timestamp(start)
    end = pd.Timestamp(end)
    time = pd.date_range(start=start, end=end, freq='M')
    time = time.strftime('%Y%m')
    return time


def get_page(url, headers):
    html = requests.get(url, headers=headers)
    if html.status_code == 200:
        html.encoding = html.apparent_encoding
        return html.text
    else:
        print('None getpage')
        return None


def spider(url):
    html = get_page(url, headers)
    bs = BeautifulSoup(html, 'html.parser')
    data = bs.find_all(class_='thrui')
    # if data:
    return data
    # else:
    #     print('None spider')
    #     return None


# date_box = pd.DataFrame()
# city_box = pd.DataFrame()
# max_temp = pd.DataFrame()
# min_temp = pd.DataFrame()
# weh = pd.DataFrame()
# wind = pd.DataFrame()
# week_box = pd.DataFrame()

if __name__ == '__main__':
    baseurl = 'https://lishi.tianqi.com/'

    time_setting = ('20200101', '20231231')
    timerange = time_convert(time_setting[0], time_setting[1])

    cityes = ['guangzhou', 'shenzhen', 'chongqing']


    # url = 'https://lishi.tianqi.com/anda/202401.html'
    # data = spider(url)
    # print(data)
    for city in cityes:
        print(city)
        datas = pd.DataFrame(columns=['城市', '日期', '星期', '最高温度', '最低温度', '天气', '风向'])
        for needday in timerange:

            print(city, needday)
            date_box = []
            city_box = []
            max_temp = []
            min_temp = []
            weh = []
            wind = []
            week_box = []

            url = baseurl + city + '/' + needday +'.html'
            data = spider(url)
            if data:
                date = re.compile('class="th200">(.*?)</')
                tem = re.compile('class="th140">(.*?)</')
                time = re.findall(date, str(data))
                for item in time:
                    week = item[10:]
                    week_box.append(week)
                    date_box.append(item[:10])
                    city_box.append(city)
                    # print(item)
                temp = re.findall(tem, str(data))

                time_object = datetime.strptime(needday, '%Y%m')
                num_days = calendar.monthrange(time_object.year, time_object.month)[1]
                for i in range(num_days):
                    try:
                        max_temp.append(temp[i * 4 + 0])
                    except:
                        max_temp.append('NaN')

                    try:
                        min_temp.append(temp[i * 4 + 1])
                    except:
                        min_temp.append('NaN')

                    try:
                        weh.append(temp[i * 4 + 2])
                    except:
                        weh.append('NaN')

                    try:
                        wind.append(temp[i * 4 + 3])
                    except:
                        wind.append('NaN')

                print(url)
                print(len(wind), len(weh), len(max_temp), len(min_temp), len(date_box), len(city_box))

                datascol = pd.DataFrame(
                    {'城市': city_box, '日期': date_box, '星期': week_box, '最高温度': max_temp, '最低温度': min_temp, '天气': weh,
                     '风向': wind})
                print(datascol)
                del (city_box, date_box, week_box, max_temp, min_temp, temp)
                datas = datas._append(datascol)
            else:
                print(url)
                pass

        excel_file_path = 'weather_data{}.xlsx'.format(city)
        datas.to_excel(excel_file_path, index=False)
        print("{}数据已保存到Excel文件:".format(city), excel_file_path)

    # print(len(city_box))
    # print(len(date_box))
    # print(len(max_temp))
    # print(len(min_temp))
    # print(len(weh))
    # print(len(wind))

    # datas = pd.DataFrame(
    #     {'城市': city_box, '日期': date_box, '星期': week_box, '最高温度': max_temp, '最低温度': min_temp, '天气': weh,
    #      '风向': wind})
    # print(datas)
    # excel_file_path = 'weather_data{}.xlsx'.format(datas)
    # datas.to_excel(excel_file_path, index=False)
    # print("数据已保存到Excel文件:", excel_file_path)
