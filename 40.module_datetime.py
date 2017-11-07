from datetime import datetime
now = datetime.now()
print(now)

# 指定日期时间
dt = datetime(2017, 11, 5, 12, 00)
print(dt)

# datetime转为时间戳，注意Python中的时间戳是秒数，js中的时间戳是毫秒数
dt = dt.timestamp()
print(dt)

# timestamp转为datetime
ts = 1475650043
print(datetime.fromtimestamp(ts))
