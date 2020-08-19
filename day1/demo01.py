# 练习1：
#
# 编写一个函数,传入一个单词,返回该单词的解释
#
# 思路提示：
# * 利用单词本完成 dict.txt
# * 如果单词不存在 返回 None
# * 每行一个单词,单词和解释之间有空格,单词从小到大排序
def find_word(word):
    """
    :param word: 要查询的单词
    :return: 查询结果
    """
    file = open('dict.txt')
    for line in file:
        # 每次获取一行
        tmp = line.split(' ', 1)
        if tmp[0]>word:
            break
        elif word == tmp[0]:
            file.close()
            return tmp[1].strip()
    file.close()

print("%s:%s" % ("china", find_word("china")))
