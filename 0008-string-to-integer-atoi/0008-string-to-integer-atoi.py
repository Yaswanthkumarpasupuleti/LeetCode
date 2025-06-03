class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        i = 0
        n = len(s)
        #  Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        # Handle optional sign
        negative = False
        if i < n and (s[i] == '+' or s[i] == '-'):
            negative = (s[i] == '-')
            i += 1
        
        # Step 3: Skip leading zeros
        while i < n and s[i] == '0':
            i += 1
        
        # Step 4: Convert digits to number
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            # Step 5: Check overflow
            if not negative and (result > (INT_MAX - digit) // 10):
                return INT_MAX
            if negative and (result > (-INT_MIN - digit) // 10):
                return INT_MIN
            
            result = result * 10 + digit
            i += 1
        
        return -result if negative else result