class Solution:
    def reverseBits(self, n: int) -> int:
        #approach take the number as binary
        back_to_bin = format(n, '032b')
        new_arr = list(back_to_bin)
        orgin_bin = "".join(new_arr)
        decimal = int(orgin_bin,2)
        new_arr.reverse()
        neworgn_bin = "".join(new_arr)
        decimal = int(neworgn_bin,2)
        return decimal