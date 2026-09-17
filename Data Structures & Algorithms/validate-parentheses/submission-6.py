class Solution:
    def isValid(self, s: str) -> bool:

        charDict = {
            '(' : ')',
            '[' : ']',
            '{' : '}',
        }
        myStack = []

        for i, val in enumerate(s):
            if not myStack:
                if( val not in charDict):
                    myStack.append(val)
                    break
                else:
                    myStack.append(val)
            else:
                if( (val not in charDict) and ( charDict[myStack[-1]] != val)):
                    break
                elif ( (val not in charDict) and ( charDict[myStack[-1]] == val)):
                    myStack.pop()
                else:
                    myStack.append(val)

        if (len(myStack) == 0):
            return True
        else:
            return False



        