class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a,b = nums1,nums2
        if len(nums2) < len(nums1):
            a,b = b,a
        total = len(nums1) + len(nums2)
        l,r = 0,len(a)-1
        half = total // 2
        while True:
            i = (l+r)//2
            j = half - i - 2

            aleft = a[i] if i >= 0 else float("-infinity")
            aright = a[i+1] if (i+1)<len(a) else float("infinity")
            bleft = b[j] if j >= 0 else float("-infinity")
            bright = b[j+1] if (j+1)<len(b) else float("infinity")

            if aleft <= bright and bleft <= aright:

                if total%2:
                    return min(aright,bright)
                else:
                    return (max(aleft,bleft)+min(aright,bright)) / 2
            elif aleft > bright:
                r = i-1
            else:
                l = i+1