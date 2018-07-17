#This is my first Python script with Tom's help July 17th 2018!
####work only in /data2/FCHLFGMCCXY_L4_ARAkxqHAABCAAA/cdts-wh.genomics.cn/Upload_06132018/cov/read_txt_into_python.py
test = open("M-3-2.cov.CX_report.txt","r")
#print(len(test))
i=0
for line in test:
    #print(line)
    i=i+1

print(str(i))
#print(test[1:5])
