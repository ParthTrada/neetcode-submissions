class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        index_dict = {}
        res = []

        for i in range(len(nums)):
            if (target - nums[i]) in index_dict:
                res.append(index_dict[target - nums[i]])
                res.append(i)
                break
            index_dict[nums[i]] = i

        return res
        

        ##### second method #####

        # for i in range(len(nums)):
        #     index_dict[nums[i]] = i

        # for i in range(len(nums)):
        #     if (index_dict.get(target - nums[i]) and i !=  index_dict[target - nums[i]]):
        #         res.append(i)
        #         res.append(index_dict[target - nums[i]])
        #         break
            
        # return res
        