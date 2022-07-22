# 一键发癫机

用这个程序一键发癫！

## 依赖

- Python 3.x

## 用法
### 发情
```shell
python fadian.py [-h] [-o OBJECT] [-l LENGTH]
```

- 使用 `-h` 参数来显示帮助信息（虽然没啥用）
- 使用 `-o` 或 `--object` 来从命令行传入发情对象
- 使用 `-l` 或 `--length` 来从命令行传入字数。


- 若既传 `-o` 又传 `-l`，则直接生成对应字数的文本；
- 若只传 `-o` 不传 `-l`，则使用标准模板；
- 若只传 `-l` 不传 `-o`，则程序将询问发情对象；
- 若两者都不传，则进入交互模式。

> 生成的字数并非传入的字符串长度，大多数情况会比传入的字符串长度大一点（毕竟谁能凑巧凑到那个字数呢

#### 示例
```shell
python fadian.py -o 一刀斩
```

输出：

```
一刀斩……🤤嘿嘿………🤤……好可爱……嘿嘿……一刀斩🤤……一刀斩……我的🤤……嘿嘿……🤤………亲爱的……赶紧让我抱一抱……啊啊啊一刀斩软软的脸蛋🤤还有软软的小手手……🤤…一刀斩……不会有人来伤害你的…🤤你就让我保护你吧嘿嘿嘿嘿嘿嘿嘿嘿🤤……太可爱了……🤤……美丽可爱的一刀斩……像珍珠一样……🤤嘿嘿……一刀斩……🤤嘿嘿……🤤……好想一口吞掉……🤤……但是舍不得啊……我的一刀斩🤤……嘿嘿……🤤我的宝贝……我最可爱的一刀斩……🤤没有一刀斩……我就要死掉了呢……🤤我的……🤤嘿嘿……可爱的一刀斩……嘿嘿🤤……可爱的一刀斩……嘿嘿🤤🤤……可爱的一刀斩……🤤……嘿嘿🤤……可爱的一刀斩…（吸）身上的味道……好好闻～🤤…嘿嘿🤤……摸摸～……可爱的一刀斩……再贴近我一点嘛……（蹭蹭）嘿嘿🤤……可爱的一刀斩……嘿嘿🤤……～亲一口～……可爱的一刀斩……嘿嘿🤤……抱抱你～可爱的一刀斩～（舔）喜欢～真的好喜欢～……（蹭蹭）🤤脑袋要融化了呢～已经……除了一刀斩以外～什么都不会想了呢～🤤嘿嘿🤤……可爱的一刀斩……嘿嘿🤤……可爱的一刀斩……我的～……嘿嘿
```

### 嘉然小姐的🐶
```shell
python xxXiaoJieDeGou.py [-h] [-a ARGUMENTS]
```

- `-h` 作用同上。
- 使用 `-a` 或 `--arguments` 来传入发癫对象。若不传入，则程序运行时将主动询问。

#### 示例
```shell
python xxXiaoJieDeGou.py -a 池塘
```

输出：

```
我好想做池塘小姐的狗啊。
可是池塘小姐说她喜欢的是猫，我哭了。
我知道既不是狗也不是猫的我为什么要哭的。因为我其实是一只老鼠。
我从没奢望池塘小姐能喜欢自己。我明白的，所有人都喜欢理解余裕上手天才打钱的萌萌的狗狗或者猫猫，没有人会喜欢阴湿带病的老鼠。
但我还是问了池塘小姐:“我能不能做你的狗?”
我知道我是注定做不了狗的。但如果她喜欢狗，我就可以一直在身边看着她了，哪怕她怀里抱着的永远都是狗。
可是她说喜欢的是猫。
她现在还在看着我，还在逗我开心，是因为猫还没有出现，只有我这老鼠每天蹑手蹑脚地从洞里爬出来，远远地和她对视。
等她喜欢的猫来了的时候，我就该重新滚回我的洞了吧。
但我还是好喜欢她，她能在我还在她身边的时候多看我几眼吗?
池塘小姐说接下来的每个圣诞夜都要和大家一起过。我不知道大家指哪些人。好希望这个集合能够对我做一次胞吞。
猫猫还在害怕池塘小姐。
我会去把她爱的猫猫引来的。
我知道稍有不慎，我就会葬身猫口。
那时候池塘小姐大概会把我的身体好好地装起来扔到门外吧。
那我就成了一包鼠条，嘻嘻。
我希望她能把我扔得近一点，因为我还是好喜欢她。会一直喜欢下去的。
我的灵魂透过窗户向里面看去，挂着的铃铛在轻轻鸣响，池塘小姐慵懒地靠在沙发上，表演得非常温顺的橘猫坐在她的肩膀。壁炉的火光照在她的脸庞，我冻僵的心脏在风里微微发烫。
```

## 开源协议
GPL 3.0 License
