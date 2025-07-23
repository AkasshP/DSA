class TimeMap:

    def __init__(self):
        self.hash={}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hash:
            self.hash[key] += [(value,timestamp)]
        else:
            self.hash[key] = [(value,timestamp)]
    def get(self, key: str, timestamp: int) -> str:
        if key in self.hash:
            main_arr = self.hash[key]
            left = 0
            right = len(main_arr) - 1
            result = ""
            while left <= right:
                mid = (left + right) // 2
                i,j  = main_arr[mid] 
                if j == timestamp:
                    return i
                elif j < timestamp:
                    result = i
                    left = mid + 1
                else:
                    right = mid - 1
                
            return result 
        else:
            return ""
        


        
            

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)