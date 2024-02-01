class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        if len(nums)<3:
            return []
        flag = 1
        res = []
        sub = []
        count = 0
        nums.sort()
        while count!= len(nums)/3:
            j = count*3
            for i in range(count*3,(count*3)+3):
                sub.append(nums[i])
                j = count*3
                if i==j:
                    continue
                if i>j:
                    while i!=j:
                        if abs(nums[i]-nums[j])>k:
                            flag=-1
                        j+=1
            if flag==-1:
                return []
            count += 1
            res.append(sub)
            sub = []
        return res