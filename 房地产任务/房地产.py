import sys
import csv
import re

input_file= "ori_data.txt"
output_file= "dea_data.txt"

with open(input_file,'r',encoding='utf_8',newline='') as test_input:
    with open(output_file, 'w', encoding='utf_8', newline='') as test_out:
        filereader=csv.reader(test_input)
        filewriter=csv.writer(test_out,delimiter=' ')
        for row_list in filereader:
            dea=[]

            dea.append(str(row_list[0])[:10])
            row_list[1]=''.join(row_list[1].split())
            row_list[1]=row_list[1].replace('>','').replace('租房',' ').replace('网','')
            row_list[3]=re.search('(\d*)元/月',row_list[3]).group()
            dea.append(row_list[1])

            dea.append(row_list[3])

            if row_list[5].strip()=='None':
                dea.append("NULL NULL NULL NULL NULL NULL NULL NULL NULL NULL NULL NULL NULL NULL")
            else:
                dea.append(re.search(r'\d*㎡',row_list[5]).group())
                dea.append(re.search(r'\d*室',row_list[5]).group())
                dea.append(re.search(r'\d*卫', row_list[5]).group())
                dea.append(re.search(r'\d*厅', row_list[5]).group())
                dea.append(re.search(r'朝\w', row_list[5]).group())
                #楼层
                if re.search(r'\d*/\d*层', row_list[5])==None:
                    dea.append('NULL')
                else:
                    dea.append(re.search('\d*/\d*层', row_list[5]).group())
                #租期
                if re.search(r'\d*~\d*年',row_list[5])==None:
                    dea.append('NULL')
                else:
                    dea.append(re.search(r'\d*~\d*年',row_list[5]).group())
                #入住
                if re.search(r'随时入住',row_list[5])==None:
                    dea.append('NULL')
                else:
                    dea.append(re.search(r'随时入住',row_list[5]).group())
                #电梯
                if re.search(r'电梯：有',row_list[5]):
                    dea.append('有')
                elif re.search(r'电梯：无',row_list[5]):
                    dea.append('无')
                elif re.search(r'电梯：暂无数据',row_list[5]):
                    dea.append('暂无')
                #车位
                if re.search(r'车位：暂无数据',row_list[5]):
                    dea.append('暂无')
                elif re.search(r'车位：免费',row_list[5]):
                    dea.append('免费')
                elif re.search(r'车位：租用', row_list[5]):
                    dea.append('租用')
                #水
                if re.search(r'用水：民水',row_list[5]):
                    dea.append('民水')
                elif re.search(r'用水：商水',row_list[5]):
                    dea.append('商水')
                elif re.search(r'用水：暂无数据',row_list[5]):
                    dea.append('暂无')
                #电
                if re.search(r'用电：民电',row_list[5]):
                    dea.append('民电')
                elif re.search(r'用电：商电',row_list[5]):
                    dea.append('商电')
                elif re.search(r'用电：暂无数据',row_list[5]):
                    dea.append('暂无')
                #燃气
                if re.search(r'燃气：有',row_list[5]):
                    dea.append('有')
                elif re.search(r'燃气：无',row_list[5]):
                    dea.append('无')
                elif re.search(r'燃气：暂无数据',row_list[5]):
                    dea.append('暂无')
                #采暖
                if re.search(r'采暖：自采暖',row_list[5]):
                    dea.append('自采暖')
                elif re.search(r'采暖：集中供暖',row_list[5]):
                    dea.append('集中')
                elif re.search(r'采暖：暂无数据',row_list[5]):
                    dea.append('暂无')

            str_result = ""
            for i in dea:
                print(i)
                str_result = str_result + " " + i

            test_out.write(str_result + '\n')








