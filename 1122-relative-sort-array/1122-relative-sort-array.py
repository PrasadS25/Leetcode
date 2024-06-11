class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        def partition(arr,l,r):
            piv = arr[r]
            j = l-1
            for i in range(l,r):
                k = arr[i]
                if maps[k] <= maps[piv]:
                    j+=1
                    arr[i],arr[j] = arr[j],arr[i]
            j+=1
            arr[j],arr[r] = arr[r],arr[j]
            return j
        
        def quickSort(arr,l,r):
            if l<r:
                part = partition(arr,l,r)
                quickSort(arr,l,part-1)
                quickSort(arr,part+1,r)

        maps = {}
        n = 0
        for i in arr2:
            maps[i] = n
            n+=1

        tmp = []
        ab = arr1[::]
        for i in ab:
            if i not in arr2:
                tmp.append(i)
                arr1.remove(i)
        tmp.sort()

        quickSort(arr1,0,len(arr1)-1)
        return arr1+tmp