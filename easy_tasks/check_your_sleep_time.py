recommend_sleep = int(input())
unrecommend_sleep = int(input())
ann_sleep = int(input())

if ann_sleep >= recommend_sleep and ann_sleep < unrecommend_sleep:
    print('Это нормально')
elif ann_sleep < recommend_sleep:
    print('Недосып')
elif ann_sleep >= recommend_sleep and ann_sleep >= unrecommend_sleep:
    print('Пересып')
