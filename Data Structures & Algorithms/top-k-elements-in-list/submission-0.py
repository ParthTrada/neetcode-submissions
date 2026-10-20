class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        myDict = {}
        myList = [[] for _ in range(len(nums) + 1)]

        ans = []

        for nu in nums:
            myDict[nu] = 1 + myDict.get(nu, 0)

        for key, value in myDict.items():
            myList[value].append(key)


        for i in range(len(nums), 0, -1):
            if myList[i]:
                for j in myList[i]:
                    if len(ans) == k:
                        break
                    else:
                        ans.append(j)

        return ans