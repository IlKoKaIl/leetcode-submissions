from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        code_to_word = defaultdict(list)

        for word in strs:
            code = [0] * 26
            for c in word:
                code[ord(c) - ord('a')] += 1
            
            code_to_word[tuple(code)].append(word)
        
        res = []
        for key in code_to_word:
            res.append(code_to_word[key])
        
        return res

        