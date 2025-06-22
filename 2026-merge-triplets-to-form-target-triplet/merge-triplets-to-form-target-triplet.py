class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:


        #step 1 valid triplets:
        new_triplets = [[i[j] for j in range(len(i)) if i[j] <= target[j]] for i in triplets]
        final_triplets = list(filter(lambda x: len(x) == 3,new_triplets))
        if final_triplets:
            #Step 2 filter based on the indexes basis
            set_A = list(filter(lambda x: x <= target[0],list(map(lambda x: x[0],final_triplets))))
            set_B = list(filter(lambda x: x <= target[1],list(map(lambda x:x[1],final_triplets))))
            set_C = list(filter(lambda x: x <= target[2],list(map(lambda x:x[2],final_triplets))))
            #step 3 match the target
            for i in range(len(target)):
                if i == 0 :
                    if target[i] in set_A:
                        pass
                    else:
                        return False
                if i == 1:
                    if target[i] in set_B:
                        pass
                    else:
                        return False
                if i == 2:
                    if target[i] in set_C:
                        pass
                    else:
                        return False
            return True
        else:
            return False

