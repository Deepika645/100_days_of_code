#Given an expression string x. Examine whether the pairs and the orders of {,},(,),[,] are correct in exp.
class Solution:
    def ispar(self,x):
        stack = []
        for elem in x:
            if elem in ("{","(","["):
                stack.append(elem)
            else:
                if not stack:
                    return False
                
                elif self.isMatch(stack[-1],elem) == False:
                    return False
                
                else:
                    stack.pop()
                
        if stack:
            return False
        else:
            return True
            
    def isMatch(self,a,b):
        if (a == "(" and b ==")" ) or (a == "[" and b =="]" ) or (a == "{" and b =="}" ):
            return True
        else: 
            return False