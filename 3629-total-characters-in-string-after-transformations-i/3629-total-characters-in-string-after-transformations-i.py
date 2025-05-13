class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mp = {}
        m = 10**9 + 7
        for char in s:
            if char in mp:
                mp[char] += 1
            else:
                mp[char] = 1
        for i in range(t):
            temp = {}
            for char,freq in mp.items():
                if char != "z":
                    if chr(ord(char)+1) in temp:
                        temp[chr(ord(char)+1)] = (temp[chr(ord(char)+1)]+freq)%m
                    else:
                        temp[chr(ord(char)+1)] = freq % m
                    
                else:
                    if "a" in temp:
                        temp["a"] = (temp["a"]+freq) % m
                    else:
                        temp["a"] = freq % m
                    if "b" in temp:
                        temp["b"] = (temp["b"]+freq) % m
                    else:
                        temp["b"] = freq % m
            mp = temp
        res = 0
        for val in mp.values():
            res = (res + val) % m
        return res


   