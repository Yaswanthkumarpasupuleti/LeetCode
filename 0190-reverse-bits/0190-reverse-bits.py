class Solution:
    def reverseBits(self, n: int) -> int:
        bin_string=bin(n)[2:].zfill(32)
        my_list = list(bin_string   )
        my_list.reverse()
        numero=(''.join(map(str,my_list)))
        return int(numero,2)