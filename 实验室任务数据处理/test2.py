#!/usr/bin/env python3                           #注释行，使脚本在不同的操作系统之间具有可移植性

import csv                           #导入python中的csv模块
import sys                           #导入python中的sys模块

input_file = sys.argv[1]            #使用sys模块中的argv参数，传递给命令行的参数，也就是在命令行输入的内容
output_file = sys.argv[2]           #同上

movementsDict = {}                  #创建一个名为"movementsDict"的空字典
inputData = []                      #创建一个名为"inputData"的空列表
with open(input_file, 'r', newline='') as csv_in_file:
# 将“input_file”打开为一个文件对象“csv_in_file”，“r”表示只读模式，说明打开“input_file”是为了读取数据
    filereader = csv.reader(csv_in_file)
    #使用csv模块中的reader函数创建一个名为“filereader”的文件读取对象，来读取输入文件里的行
    movementsList = []                  #创建一个名为"movementsList"的空列表
    for row_list in filereader:         #创建一个for循环，在输入文件剩余各行里进行迭代
        movementsList.append(row_list[1])               #应用列表里的qppend函数给列表里增加元素，我们所要增加的都是列表里各行索引为1的各个元素
    for movement in movementsList:
        if movement not in movementsDict:
            movementsDict[movement] = 1
        else:
            movementsDict[movement] += 1                    #通过字典对其中的元素来计数
    for movement, movementsDict[movement] in movementsDict.items():
        print('Movement: %-15s' % movement, end='')
        print('Amount: ' + str(movementsDict[movement]))
        movementsDict[movement] = movementsDict[movement] // 100 * 100
        #为了以100为精确度，我们进行movementsDict[movement] = movementsDict[movement] // 100 * 100的运算，将多余的删去
        inputData.append(movementsDict[movement])
        #将满足条件的写入字典中
    csv_in_file.seek(0, 0)
    with open(output_file, 'w', newline='') as csv_out_file:
    # 将“output_file”打开为一个文件对象“csv_out_file”，“w”表示可写模式，说明打开“input_file”是为了写入数据
        filewriter = csv.writer(csv_out_file)
        # 使用csv模块中的writer函数创建一个名为“filereader”的文件写入对象，来将数据写入输出文件
        countWalking = 0
        countJogging = 0
        countUpstairs = 0
        countDownstairs = 0
        countStanding = 0
        countSitting = 0
        #将每个元素的初始值都记为0，以便后面统计其个数
        for row_list in filereader:
        # 创建一个for循环，在输入文件剩余各行里进行迭代
            if row_list[1] == 'Walking':
                if countWalking < inputData[0]:
                    filewriter.writerow(row_list)
                    countWalking += 1
            #就拿这个Walking来举例，如果索引为1的元素是Walking，如果Walking的个数少于inputData[0]中统计的个数就写入输出文件中，个数加一，下面的都一样
            elif row_list[1] == 'Jogging':
                if countJogging < inputData[1]:
                    filewriter.writerow(row_list)
                    countJogging += 1
            elif row_list[1] == 'Upstairs':
                if countUpstairs < inputData[2]:
                    filewriter.writerow(row_list)
                    countUpstairs += 1
            elif row_list[1] == 'Downstairs':
                if countDownstairs < inputData[3]:
                    filewriter.writerow(row_list)
                    countDownstairs += 1
            elif row_list[1] == 'Standing':
                if countStanding < inputData[4]:
                    filewriter.writerow(row_list)
                    countStanding += 1
            else:
                if countSitting < inputData[5]:
                    filewriter.writerow(row_list)
                    countSitting += 1

