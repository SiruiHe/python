import logging
logging.basicConfig(level=logging.DEBUG,format="%(asctime)s-%(levelname)s-%(message)s")
#logging.disable()  #禁用日志
logging.debug("Start!")

def func(n):
    logging.debug("Now start calculating!")
    total=1
    for i in range(1,n+1):
        total*=i
        logging.debug("i is "+str(i)+" and total is "+str(total))
    logging.debug("finish")
    return total

print(func(1000))
logging.debug("ok!")