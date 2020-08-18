import sys                       #导入python中的sys模块
import csv                       #导入python中的csv模块

input_file=sys.argv[1]              #使用sys模块中的argv参数，传递给命令行的参数，也就是在命令行输入的内容
output_file=sys.argv[2]           #同上


with open(input_file,'r',newline='') as csv_in_file:
# 将“input_file”打开为一个文件对象“csv_in_file”，“r”表示只读模式，说明打开“input_file”是为了读取数据
    with open(output_file,'w',newline='') as csv_out_file:
    # 将“output_file”打开为一个文件对象“csv_out_file”，“w”表示可写模式，说明打开“input_file”是为了写入数据
        filereader=csv.reader(csv_in_file)
        # 使用csv模块中的reader函数创建一个名为“filereader”的文件读取对象，来读取输入文件里的行
        filewriter=csv.writer(csv_out_file)
        # 使用csv模块中的writer函数创建一个名为“filereader”的文件写入对象，来将数据写入输出文件
        for row in filereader:               #创建一个for循环，在输入文件剩余各行里进行迭代
            ass=[]                           #创建一个名为"ass"的空列表，用来增加元素
            ass.append(row[3])
            ass.append(row[4])
            ass.append(row[5])
            #因为要求加入后三列的元素，则加入下标为3，4，5列的个元素
            filewriter.writerow(row)            #满足条件的写入输出文件
