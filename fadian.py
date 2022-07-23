import json
import random
import argparse

def makeText(source, obj, num=-1):
    currentText = ""
    if num > 0:
        tmpList = []
        while len(currentText) <= num:
            tmpList.append(source[random.randrange(0, len(source) - 1)])
            currentText = "".join(tmpList)
        return currentText.format(name=obj)
    else:
        currentText = "".join(source)
        return currentText.format(name=obj)
def main(argument):
    f=open("fadian.json",encoding='UTF-8')
    source = json.load(f)
    if argument.object:
        name = args.object[0]
        if argument.length:
            textLength = args.length[0] # 有o有l，随机语句
        else:
            textLength = -1             # 有o没l，标准模板
    else:
        name = input("请输入发癫对象：")
        if argument.length:
            textLength = args.length[0] # 没o有l，询问名字
        else:
            textLength = int(input("请输入生成文字的长度 (输入 -1 来使用标准模板)："))# 没o没l，完全交互
    print(makeText(source, name, textLength))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="一个发癫机！")
    parser.add_argument('-o','--object',nargs=1,help='在命令行传入发癫对象')
    parser.add_argument('-l','--length',nargs=1,type=int,help='在命令行传入字数 (若不选此项则使用标准模板)')
    args = parser.parse_args()
    main(args)
