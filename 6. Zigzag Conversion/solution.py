class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res_arr = [[] for _ in range(numRows)]
        cur_row = 0
        for i in s:
            res_arr[cur_row].append(i)
            if cur_row == 0:
                step = 1
            elif cur_row == numRows-1:
                step = -1
            cur_row += step
        return "".join(["".join(i) for i in res_arr])


Solution().convert("PAYPALISHIRING", 3)
print("PAHNAPLSIIGYIR")
Solution().convert("AV", 1)