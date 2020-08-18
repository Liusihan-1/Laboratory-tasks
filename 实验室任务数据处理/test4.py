import csv               #导入python中的csv模块
import sys               #导入python中的sys模块

input_file = sys.argv[1]        #使用sys模块中的argv参数，传递给命令行的参数，也就是在命令行输入的内容
output_file = sys.argv[2]       #同上

i=0
row_list = []                  #创建一个名为"row_list"的空列表，来保存所有的数据行

with open(input_file,'r',newline='') as csv_in_file:
# 将“input_file”打开为一个文件对象“csv_in_file”，“r”表示只读模式，说明打开“input_file”是为了读取数据
    with open(output_file,'w',newline='') as csv_out_file:
    # 将“output_file”打开为一个文件对象“csv_out_file”，“w”表示可写模式，说明打开“input_file”是为了写入数据
        filereader = csv.reader(csv_in_file,delimiter=" ")
        # 使用csv模块中的reader函数创建一个名为“filereader”的文件读取对象，来读取输入文件里的行
        filewriter = csv.writer(csv_out_file,delimiter=" ")
        # 将“output_file”打开为一个文件对象“csv_out_file”，“w”表示可写模式，说明打开“input_file”是为了写入数据
        for row in filereader:
        # 创建一个for循环，在输入文件剩余各行里进行迭代
            i=i+1
            row_list.append(row)
            if i==20:
                filewriter.writerow(row_list)
                i=0
                row_list = []
            #遍历列表，当a等于20时，然后把数据添加到列表中。列表长度为20，这时就需要把元素添加到输出列表中，然后将i归零，将列表清空，继续下一轮拆分。
            # 拆分完成之后，逐行写入输出文件即可。
