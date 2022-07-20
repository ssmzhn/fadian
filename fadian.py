import json
import random

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
    name = input("请输入发病对象：")
    textLength = int(input("请输入生成文字的长度："))
    print(makeText(source, name, textLength))
if __name__ == "__main__":
    main()
