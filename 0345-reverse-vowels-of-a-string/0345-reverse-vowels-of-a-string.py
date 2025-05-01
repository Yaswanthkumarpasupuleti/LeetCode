class Solution:
    def reverseVowels(self, s: str) -> str:
        str1 = list(s)
        #print(str1)
        vowels = "aeiouAEIOU"
        left = 0
        right = len(str1)-1
        while left <= right:
            if (str1[left] in vowels) and (str1[right] in vowels):
                str1[left] , str1[right] = str1[right] , str1[left]
                left+=1
                right-=1
                #pass
            elif str1[left] in vowels:
                right -= 1
                #pass
            elif str1[right] in vowels:
                left +=1
            else:
                left += 1
                right -= 1

        return "".join(str1)


        