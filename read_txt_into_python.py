#Tom said make another line
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

#also learned 
# 1079  git status
# 1080  git status -s
# 1082  git add read_txt_into_python.py
# 1083  git status -s
# 1084  git status 
# 1085  git commit -m "add new file and practice how to use git"
# 1086  git status
# 1087  git config --global user.name "Xiaodong"
# 1088  git config --global user.email "xzy50@psu.edu"
# 1089  git config --list
# 1090  git log
# 1091  git commit --amend --reset-author
# 1092  git log
# 1093  git status
# 1094  git config --list
# 1096  git config core.editor "nano"
# 1097  git config --list
# 1098  nano read_txt_into_python.py 
#git branch
#git remote -v
#git push origin master
