import traceback
def test():
    hello()
def hello():
    error()
def error():
    try:
        raise Exception("错错错错错错错！！！！")
    except Exception:
        errorfile=open("errorlog.txt","w")
        errorfile.write(traceback.format_exc())
        errorfile.close()
        print("已写入错误日志")

test()