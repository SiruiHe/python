#多重剪切板程序
import pyperclip,os,sys,shelve,pprint
mcbshelf=shelve.open("mcb")
if len(sys.argv)==3:
    if sys.argv[1] == "save":
        mcbshelf[sys.argv[2]]=pyperclip.paste()
elif len(sys.argv)==2:
    if sys.argv[1].lower()=='list':
        pyperclip.copy(str(list(mcbshelf.keys())))
        for item in list(mcbshelf.items()):
            print(item)
    elif sys.argv[1]=="help":
        help_info="".join(["python3 mcb.py [参数]\n",
                           "参数:\n","\thelp+--帮助\n",
                           "\tsave [助记符]--保存\n",
                           "\t[助记符]--读取\n",
                           "\tclear--清空"])
        print(help_info)
    elif sys.argv[1]=="clear":
        for one in mcbshelf.keys():
            del mcbshelf[one]
    else:
        try:
            pyperclip.copy(str(mcbshelf[sys.argv[1]]))
        except KeyError:
            print("没有相关数据。")
mcbshelf.close()
