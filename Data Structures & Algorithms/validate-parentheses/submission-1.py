class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {')':'(', ']':'[', '}':'{'}

        for char in s:
            if char in pair.values():
                stack.append(char)
            
            else:
                if stack == []:
                    return False 

                if  pair[char] != stack.pop():
                    return False
        
        return stack == []



        