class Solution:
    def isValid(self, s: str) -> bool:

        charDict = {
            ')' : '(',
            ']' : '[',
            '}' : '{',
        }
        myStack = []

        for i, val in enumerate(s):
            if val not in charDict:
                myStack.append(val)

            else:
                if (myStack and (myStack[-1] == charDict[val])):
                    myStack.pop()
                else:
                    return False
        
        return True if not myStack else False 
             