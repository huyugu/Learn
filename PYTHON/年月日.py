def nowtime():
    import time
    yyyy = time.time()//(60*60*24*365)+1970
    mm = (time.time()-(60*60*24*365)*(yyyy-1970))//(60*60*24*30)+1
    print(mm)


nowtime()

