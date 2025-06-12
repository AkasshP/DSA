class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointer:
        l_ptr = 0
        r_ptr = len(numbers) - 1
        while l_ptr < r_ptr:
            current_sum = numbers[l_ptr] + numbers[r_ptr]
            if current_sum == target:
                return [l_ptr + 1, r_ptr + 1]  # 1-indexed as per problem requirement
            elif current_sum < target:
                l_ptr += 1 
            else:
                r_ptr -= 1  

        # brute force
        #hi
        # for i in range(len(numbers)):
        #     for j in range(i+1,len(numbers)):
        #             if numbers[i] + numbers[j] == target:
        #                 print(numbers[i],numbers[j])
        #                 return [i+1,j+1]



 
            
