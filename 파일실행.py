# import __main__ as main
# print(main.__file__)

import os

dir_path = "D:/_Jay/_Doc/길림/VsCode/Python/test"     ## 프로그램 위치

for (root, directories, files) in os.walk(dir_path):
    # for file in files:
        # if '.py' in file:      ## 프로그램 필터링
            # file_path = os.path.join(root, file)
            # os.startfile(file_path)     ## 프로그램 실행
            # print(file_path)
    number = 0
    for i in files:
        number += 1
        # dic = {"%d" % number,i}
        print("%d" % number,i)
# print(dic)
a = input('입력:')
# print(dir_path+"/"+files[int(a)-1])

os.startfile(dir_path+"/"+files[int(a)-1]) # 실행이 됩니다.
