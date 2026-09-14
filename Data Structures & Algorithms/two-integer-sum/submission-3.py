class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        index_dict = {}

        for i, val in enumerate(nums):
            diff = target - val

            if (diff in index_dict):
                return [index_dict[diff],i]
            
            index_dict[val] = i

    
        

        ##### second method #####

        # for i in range(len(nums)):
        #     index_dict[nums[i]] = i

        # for i in range(len(nums)):
        #     if (index_dict.get(target - nums[i]) and i !=  index_dict[target - nums[i]]):
        #         res.append(i)
        #         res.append(index_dict[target - nums[i]])
        #         break
            
        # return res
        