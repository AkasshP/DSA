class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        arr_str = {1:[],
        2:['a','b','c'],
        3:['d','e','f'],
        4:['g','h','i'],
        5:['j','k','l'],
        6:['m','n','o'],
        7:['p','q','r','s'],
        8:['t','u','v'],
        9:['w','x','y','z']}

        main_array = []
        final_result = []
        for i in digits:
            main_array.append(arr_str[int(i)])

        def combinations(temp,i):
            if len(temp) == len(digits):
                final_result.append(''.join(temp))
                return 

            if i < len(main_array):
                for j in main_array[i]:
                    temp.append(j)

                    if i < len(main_array):
                        i += 1
                    combinations(temp,i)
                    temp.pop()
                    i -= 1

        if main_array:
            if  len(main_array) > 1:
                c = 1
                for i in main_array[0]:
                    temp = []
                    temp.append(i)
                    combinations(temp,c)
            else:
                return main_array[0]
        else:
            return main_array

        return final_result