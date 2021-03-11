drive = input('請問你有開過車嗎?')
if drive != '有' and drive != '沒有':
    print('只能輸入 有/沒有')
    raise SystemExit
age = input('你的年齡是?')
age = int(age)
if drive == '有':
    if age >= 18:
    	print('你通過測驗')
    else:
        print('你怎麼會開過車')
elif drive == '沒有':
    if age >= 18:
    	print('你考完駕照就可以開車喔')
    else:
    	print('滿18歲後考駕照就能開車了')


   









    
