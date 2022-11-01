#a-z  kavita@gmail.com,^ using for start dis sign
#0-9 ?=dis use for only show 1 character
#. _time 1
#@ time 1 \w=are used to search special chr like@
# . 2nd,3rd $=use for search last to first
import re
email_condition="^[a-z]+[\._]?[a-z 0-9+[@]\w+[.]\w{2,3}$"
user_email=input("Enter your Email : ")

if re.search(email_condition,user_email):
    print("Right Email")
else:
    print("Wrong Email")