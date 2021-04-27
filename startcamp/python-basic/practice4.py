# 151 ~ 매우 나쁨
# 81 ~ 150 나쁨
# 31 ~ 80 보통
# 0 ~ 30 좋음

dust = 60

if dust > 150:
    print('매우 나쁨')
elif dust > 80 and dust <=150 :
    print('나쁨')
elif dust > 30 and dust <= 80:
    print('보통')
else:
    print('좋음')
