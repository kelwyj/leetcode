class Solution(object):
    def getRow(self,rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
       if rowIndex==0:
          return [1]
       if rowIndex==1:
          return[1,1]
       if rowIndex>1:
          numRows=rowIndex+1
          list=[[] for x in range(numRows)]
          for i in range(numRows):
              list[i]=[1 for j in range(i+1)
          for i in range(2,numRows):
              for j in range(1,i):
                  list[i][j]=list[i-1][j-1]+list[i-1][j]
       return list[rowIndex]
