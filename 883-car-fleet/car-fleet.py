class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        new_arr = []
        car_dict = {}
        fleet = []
        for i,j in zip(position,speed):
            car_dict[i] = j
        for i in sorted(car_dict, reverse = True):
            new_arr.append((target - i) / car_dict[i])

        print(new_arr,'new_arr')
        i = 0
        new_fleet = []
        while i < len(new_arr):
            if not new_fleet:
                new_fleet.append(new_arr[i])
            else:
                if new_fleet[0] >= new_arr[i]:
                    new_fleet.append(new_arr[i])
                else:
                    fleet.append(tuple(new_fleet))
                    new_fleet.clear()#reset
                    new_fleet.append(new_arr[i])#new_fleet
            i += 1

        if new_fleet:
           fleet.append(tuple(new_fleet)) 

        return len(fleet)
