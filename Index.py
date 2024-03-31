import pandas as pd
import akshare as ak
import matplotlib.pyplot as plt

# new = ak.energy_carbon_domestic(symbol='成')

# print(new)
# new.to_csv('test.csv')

# citys = ['湖北','重庆','上海','北京','天津','福建']
# for city in citys:
#     new = ak.energy_carbon_domestic(symbol='{}'.format(city))
#     new.to_csv('carbon_{}.csv'.format(city))
#     print(city,'写入完成')

# new = ak.macro_china_energy_index()
# new = ak.air_quality_hist(city='北京', start_date='20200101', end_date='20231231')
# new = ak.energy_carbon_domestic()
# new.to_csv('data/crobon_domestic.csv', index=False)
new = pd.read_csv('data/crobon_domestic.csv')
print(new)
plt.plot(new['成交价'])
plt.show()