''
'''
date: 2020-12-30
level: 6 kyu
topic: Stop gninnipS My sdroW!
'''

# 自提版本
def spin_words(sentence):
    newlist = []
    for item in sentence.split(' '):
        if len(item) >= 5 :
            newitems = []
            for i in range(len(item)):
                newitems.append(item[-(i+1)])
            item = ''.join(newitems)
        newlist.append(item)
    return ' '.join(newlist)

## 一句话版本
def spin_words_simple(sentence):
    return ' '.join(word if len(word)<5 else word[::-1] for word in sentence.split(' '))


if __name__ == '__main__':
    #print(spin_words('this is a test'))
    print(spin_words_simple('this is another test'))
    print('another'[::-1])