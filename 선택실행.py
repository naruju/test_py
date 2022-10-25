import os
dir_path = "D:/_Jay/_Doc/길림/VsCode/Python/test"     ## 프로그램 위치
file_list = os.listdir(dir_path)
counter = (len(file_list))


def foo():
    for (root, directories, files) in os.walk(dir_path):
        number = 0
        for i in files:
            number += 1
            print("%d" % number,i)
    a = int(input('입력:'))
    os.startfile(dir_path+"/"+files[int(a)-1])

foo()

# num = 0
# while num != counter+1:
#     foo()
#     num = int(input())




# def test():
#     return("hello",100)

# result=test()
# print(result[0])
# print(result[1])