import pandas as pd

data = pd.DataFrame()
htl1 = 'https://www.travelchinaguide.com/tourism/2017statistics/'
htl = []
htl2 = 'https://www.travelchinaguide.com/tourism/2006statistics/inbound/'
htl.append(htl2)
for i in range(2008, 2017):
    url1 = 'https://www.travelchinaguide.com/tourism/%sstatistics/inbound.htm' % i
htl.append(url1)
htl.append(htl1)
print(htl)
for url in htl:
    data = data.append(pd.read_html(url), ignore_index=True)
print(data)
data.to_csv('Tourism.csv')
