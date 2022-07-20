import json
import random
import argparse

def makeText(source, obj, num=100):
    tmpList = []
    currentText = ""
    while len(currentText) <= num:
        tmpList.append(source[random.randrange(0, len(source) - 1)])
        currentText = "".join(tmpList)
    return currentText.format(name=obj)
def main():
    f=open("fadian.json")
    source = json.load(f)
    if args.arguments!=None:
        print(makeText(source, args.arguments[0], args.arguments[1]))
    else:
        name = input("请输入发癫对象：")
        textLength = int(input("请输入生成文字的长度："))
        print(makeText(source, name, textLength))
def str_and_int(x):
    try:
        return int(x)
    except:
        return x
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-a','--arguments',nargs=2,type=str_and_int,help=
            """在命令行中传入参数，而不是运行中传入参数。
            第一个参数表示发癫的对象，第二个参数表示字数。"""
    )
    args = parser.parse_args()
    main()
