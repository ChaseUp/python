from datetime import datetime, timedelta
now = datetime.now()
print(now)

# 指定日期时间
dt = datetime(2017, 11, 5, 12, 00)
print(dt)

# datetime转为时间戳(timestamp)，注意Python中的时间戳是秒数，js中的时间戳是毫秒数
dt = dt.timestamp()
print(dt)

# timestamp转为datetime
ts = 1475650043
print(datetime.fromtimestamp(ts))

# string转为datetime
print(datetime.strptime('2017/11/7 14:45:00', '%Y/%m/%d %H:%M:%S')) # 第二个参数是第一个参数的格式说明，前后需对应

# datetime转为str
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M:%S'))

#datetime加减
print(now + timedelta(hours = 10))
print(now - timedelta(days = 1))
print(now + timedelta(days = 2, hours = 3))
