class TimeMap:

    def __init__(self):
        self.maps = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.maps:
            self.maps[key].append([value,timestamp])
        else:
            self.maps[key] = [[value,timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.maps:
            return ""
        else:
            ary = self.maps[key]
            res = ""
            l,r = 0,len(ary)-1
            while l<=r:
                mid = (l+r)//2
                if ary[mid][1] == timestamp:
                    return ary[mid][0]
                elif ary[mid][1] < timestamp:
                    res = ary[mid][0]
                    l = mid+1
                else:
                    r = mid-1
            return res