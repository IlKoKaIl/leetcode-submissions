class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = ['(', '[', '{']
        pair = {')':'(', ']':'[', '}':'{'}

        for char in s:
            if char in open:
                stack.append(char)
            
            else:
                if stack == []:
                    return False 

                if  pair[char] != stack.pop():
                    return False
        
        return stack == []



        