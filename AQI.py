import json
import pandas as pd

AQI = pd.DataFrame(columns=['Date', 'AQI'])

if __name__ == '__main__':
    with open('AQI.CQ.json', 'r') as file:
        data = json.load(file)

    # 提取数据
    for entry in data['Data']:
        day = entry['day']
        value = entry['value']
        temp = [day, value]
        # print(temp)
        new_row = pd.DataFrame([[day, value]], columns=AQI.columns)
        # print(new_row)
        AQI = pd.concat([AQI, new_row], ignore_index=True)

    # print(data)
    print(AQI)
    AQI.to_csv('AQI.CQ.csv')