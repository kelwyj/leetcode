class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        lensum=max(len(a),len(b))+1
        Sum=['0' for x in range(lensum)]
        if len(a)>=len(b):
            b='0'*(len(a)-len(b))+b
        if len(a)<len(b):
            a='0'*(len(b)-len(a))+a
        i=len(a)-1
        flag=0
        while i>=0:
            if int(a[i])+int(b[i])+flag==1:
                Sum[i+1]='1'
                flag=0
            elif int(a[i])+int(b[i])+flag==2:
                Sum[i+1]='0'
                flag=1
            elif int(a[i])+int(b[i])+flag==3:
                Sum[i+1]='1'
                flag=1
            else:
                Sum[i+1]='0' 
                flag=0
            i=i-1
        if flag==1:
            Sum[0]='1'
        if flag==0:
            Sum=Sum[1:lensum]
        Sum = ''.join(Sum)
        return Sum
