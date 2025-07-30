class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        final_points = sorted(points, key=lambda interval: interval[1])
        st,end = final_points[0]
        shoot = 0
        main_check = {}
        print(final_points,'final_points')
        for i in range(len(final_points)):
            main_check[i] = False
        for i in range(1,len(final_points)):
            x,y =  final_points[i]

            if x <= end <= y:
                if main_check[i-1] == False:
                    shoot += 1
                main_check[i-1] = True
                main_check[i] = True
            else:
                end = y

        if all(i == True for i in main_check.values()):
            return shoot 
        else:
            if all(i == False for i in main_check.values()): #since everything needs a sperate arrow
                return len(final_points) 
            else:
                cnt  = 0
                for i in main_check.values():
                    if i == False:
                        cnt += 1

                return shoot + cnt