

import time
import tushare as ts

# obtain current date
cur_date = time.strftime('%Y-%m-%d')
outfile = 'stock_list_' + cur_date + '.csv'

pro = ts.pro_api()
stock_list = pro.stock_basic(
        exchange='',
        list_status='L',
        fields='ts_code,symbol,name,area,industry,list_date')

stock_list.to_csv(outfile, encoding='gbk')

