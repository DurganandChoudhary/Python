name = input('What month is it? ')

thirty_days = ['April','June','September','November']
thirty_one_days = ['January','March','July','August','October','December']
feb = ['February']

if name in thirty_days:
    print('Number of days: 30')
elif name in thirty_one_days:
    print('Number of days: 31')
elif name in feb:
    print('Number of days: 28 or 29')
