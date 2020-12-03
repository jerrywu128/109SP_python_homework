import re
import sys



def continuous(m):
    
    l = list(m)

    for i in range(0,len(l)-1):
        if ord(l[i+1]) - ord(l[i]) == 1:
            return 1
    return 0

if __name__ == '__main__':
     if len(sys.argv) < 2:
        print("no argument")
        sys.exit()
     m = sys.argv[1]
     al = re.search('[a-z]+',m)
     ma = re.search('[0-9]+',m)
     sy = re.search('\W+',m)
     bal = re.search('[A-Z]+',m)
     print(m)

                
     check = continuous(m)

     if (((len(m) >=8 )and(len(m) <=16 ))and
        (((al!=None)or(bal!=None)) and (ma!=None) and (sy!=None) and (bal!=None))and 
        (check==0)):

                 print("success")
     else:
            print("fail")
            if((al==None)and (bal==None)):
                 print("缺少英文字母")
            elif((al!=None)and (bal==None)):
                 print("缺少大寫字母")
            if(ma==None):
                 print("缺少數字")
            if(sy==None):
                 print("缺少符號")
            if (len(m)<8):

                 print("長度小於8")
            elif (len(m)>16):
   
                 print("長度大於16") 
            if(check==1):
                 print("英文字母、數字不可連續")     
