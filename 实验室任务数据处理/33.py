import csv
import sys

input_file=sys.argv[1]
output_file=sys.argv[2]

with open(input_file,"r",newline='') as csv_input:
    with open(output_file,'w',newline='') as csv_out: 
        filereader=csv.reader(csv_input,delimiter=" ")
        filewriter=csv.writer(csv_out,delimiter=",")
        for row_list in filereader :
            if len(str(row_list[2]))!=14 or(len(row_list)!=6)\
            or len(str(row_list[3]))>7 or len(str(row_list[4]))>=7 \
            or len(str(row_list[5]))>=7 :
                continue
            else:
                filewriter.writerow(row_list)