class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        val = "123456789"
        res = []
        n = len(val)

        for length in range(1, n + 1):
            for i in range(n - length + 1):
                num = int(val[i:i+length])
                if low <= num <= high:
                    res.append(num)
        
        return res