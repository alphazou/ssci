from itertools import product
from itertools import combinations
from dictionary import BaiduChineseWordDictionary, NULL_STORAGE
from search import search


chars = '窄踏碎织纱衫乞著愁询陶醉企权颠势凭职呈屈攻撤威衰滔途旋竖纹弦纤催促披娇恰齿柴杏焦躁汁' \
            '禁茂旺昌咏眠赠宣眨饮浆递陆彼托帆辰均裹胶栽拣磨介绍肤摩律损逐渐痕迹征隐蔽侦莫乏滥赞审' \
            '刘恨案套遵挨摄述援社捐款返贫魔择毅慰尚膜恢康聋遗签昔践宗旨旬抚源燃章凶脱逃逗端措悟控' \
            '漠敏陷储蓄营维枕撒扩范符合甚染寸倍繁殖植蒸浮聚冈漫岭盐泽宜碍彻罗盯贯武奴置乃炼钢斜诵' \
            '腾驾陡朴素滋庭狂歇赢惯拥恒欲旦恐徒魂乳凤咽脂膏泣敲叙蚊扰稀叮嘱搜'
char_list = list(chars)
word_list = product(char_list, repeat=2)

word_list = list(word_list)
# word_list = ['发疯', '幸福', '羡慕', '慷慨', '受宠若惊']
usefull_words = []
# bd_dic = BaiduChineseWordDictionary()

n = 0
m = 0
total = len(word_list)
for w in word_list:
    m += 1
    word = w[0] + w[1]
    result = search(word)
    print('\n')
    print('正在判断第{}/{}个二字词:  '.format(m,total) + word + '.....')

    if result['释义']:
        n += 1
        print('\n^-^-^-^-^-^-^-^-^-^-^')
        print('哈哈！找到第{}个双生词：'.format(n) + word)
        print(result)
        print('-'*20)
        usefull_words.append(word)

print('-'*200)
print('共找到{}个符合条件的双生词！'.format(len(usefull_words)))
print(usefull_words)
with open('/home/xiaozi/文档/双生词.txt', 'w') as f:
    f.write(str(usefull_words))
