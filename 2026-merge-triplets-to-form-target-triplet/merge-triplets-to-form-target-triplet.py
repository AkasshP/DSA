class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        #step 1 valid triplets:
        valid_triplets = [t for t in triplets if all(t[i] <= target[i] for i in range(3))]
        
        if valid_triplets:
            #Step 2 filter based on the indexes basis
            set_A = [t[0] for t in valid_triplets]
            set_B = [t[1] for t in valid_triplets]
            set_C = [t[2] for t in valid_triplets]

            #step 3 match the target
            for val, s in zip(target, [set_A, set_B, set_C]):
                if val not in s:
                    return False
            return True
        else:
            return False

