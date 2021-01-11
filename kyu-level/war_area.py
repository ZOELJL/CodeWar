
import math
import datetime
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
def spin_words_perfect(sentence):
    return ' '.join(word if len(word)<5 else word[::-1] for word in sentence.split(' '))

'''
date : 2020-12-30
level: 6 kyu
topic: Who likes it?
'''

def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1 :
        return names[0] +' likes this'
    elif len(names) == 2:
        return names[0] +' and '+names[1] +' like this'
    elif len(names) == 3:
        return names[0] + ', ' + names[1] +' and '+names[2]+ ' like this'
    else:
        return names[0]+', ' +names[1] +' and '+str(len(names)-2) + ' ohters people like this'


'''
python中*号和**号的用法
1、当我们使用函数时，需要传入不定个数的位置参数时，就可以使用*号表示，即*args，以元组形式传入；需要传入不定个数的关键字参数时，
使用**表示，即**kwargs，以字典形式传入。
2、python中*号不仅用在形参中，也可以用在实参中。当某个函数中需要不定个位置参数时，但是我们传入的实参是一个列表或元组时，
就可以在列表或者元组前面加*号，python会自动为我们进行解包。
'''
def likes_perfect(names):
    return {
        0:'no one likes this',
        1:'{} likes this',
        2:'{} and {} like this',
        3:'{}, {} and {} like this',
        4:'{}, {} and {others} other like this'
    }[min(len(names),4)].format(*names,others= len(names)-2)

'''
date : 2020-12-30
level: 7 kyu
topic: Friend or Foe?
'''
# perfect
def friend(x):
    return [name  for name in x if len(name) == 4]

'''
date : 2020-12-30
level: 7 kyu
topic: Number of People in the Bus
'''
def number(bus_stops):
    get_num, off_num = 0, 0
    for i in bus_stops:
        get_num += i[0]
        off_num += i[1]
    return get_num-off_num

def number_perfect(bus_stops):
    return sum(i[0]-i[1] for i in bus_stops)


'''
date : 2020-12-30
level: 6 kyu
topic: Write Number in Expanded Form
'''
def expanded_form(num):
    num_str = str(num)
    result =[]
    for i in range(len(num_str)):
        print(i)
        if len(num_str) == 1:
             return num
        elif num_str[i] != '0':
            result.append(num_str[i].ljust(len(num_str)-i,'0'))
    return ' + '.join(result)

## enumerate 同时列出索引和数据
def expanded_form_perfect(num):
    nums = list(str(num))
    return ' + '.join(x + '0'*(len(nums)-y-1) for y,x in enumerate(nums) if x!= 0)

'''
date : 2020-12-31
level: 5 kyu
topic: Human Readable Time
'''
def make_readable(seconds):
    if seconds < 10:
        return '00:00:0{}'.format(seconds)
    elif seconds < 60:
        return '00:00:{}'.format(seconds)
    elif seconds <3600 :
        second =  seconds // 60
        if second < 10:
            second = '0'+str(second)
        minute = seconds % 60
        if minute < 10:
            minute = '0'+str(minute)
        return '00:{}:{}'.format(second,minute)
    else:
        hour = seconds // 3600
        if hour < 10:
            hour = '0'+str(hour)
        second = (seconds - hour*3600)// 60
        if second < 10:
            second = '0'+str(second)
        minute = (seconds - hour * 3600) % 60
        if minute < 10:
            minute = '0' + str(minute)
        return '{}:{}:{}'.format(hour,second, minute)

def make_readable_perfect(seconds):
    return '{:02}:{:02}:{:02}'.format(int(seconds / 3600) ,int(seconds /60 % 60) ,int(seconds %60))


'''
date : 2021-01-11
level: 6 kyu
topic: Unique In Order
'''

def unique_in_order(iterable):
    result = []
    for i in range(len(iterable)):
        if i == 0:
            result.append(iterable[i])
        elif iterable[i] != iterable[i-1]:
            result.append(iterable[i])
    return result



if __name__ == '__main__':
    #print(spin_words('this is a test'))
    #print(spin_words_simple('this is another test'))
    #print(make_readable_perfect(359999))
    print(unique_in_order([1,2,2,3,3]))

