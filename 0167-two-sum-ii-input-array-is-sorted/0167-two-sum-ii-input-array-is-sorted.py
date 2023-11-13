class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        i,j = 0,len(numbers)-1
        while i<j:
            sum = numbers[i]+ numbers[j]
            if sum==target:
                
                return [i+1,j+1]
            elif sum > target:
                j-=1
            else:
                i+=1
        #using hashmaps
        # maps = {}  
        # for i in range(len(numbers)):
        #     num = target - numbers[i]
        #     if num in maps.keys():
        #         lis.append(maps[num]+1)
        #         lis.append(i+1)
        #         return lis
        #     else:
        #         maps[numbers[i]] = i
        # lis = []
