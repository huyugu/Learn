h = input("请输入您的身高（cm）:")
w = input("请输入您的体重（kg）:")
h = float(h)
w = float(w)
bim = w / (h * h/10000)
if bim > 32:
    print("您的体重严重肥胖")
elif bim > 28:
    print("您的体重肥胖")
elif bim > 25:
    print("您的体重过重")
elif bim >= 18:
    print("您的体重正常")
else:
    print("您的体重过轻")
print('您的BMI值为:', '%.2f' % (bim))
