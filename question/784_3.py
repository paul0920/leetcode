
class Solution:
    def __init__(self, S):
        self.res=[]
        self.dfs(S,'',0)

    def dfs(self,S,path,index):
        if index==len(S):
            self.res.append(path)
            return

        if S[index].isalpha():
            self.dfs(S,path+S[index].lower(),index+1)
            self.dfs(S,path+S[index].upper(),index+1)
        else:
            self.dfs(S,path+S[index],index+1)

ins = "a1b2"
data = Solution(ins)

print data.res