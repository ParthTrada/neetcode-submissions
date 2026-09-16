class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        main_dict = {}
        freq_list = [0] * 26
        res = []

        for val in strs:
            for j in range(len(val)):
                idx = ord(val[j]) - ord('a')
                freq_list[idx]+=1

            key = tuple(freq_list)
            
            if key not in main_dict:
                main_dict[key] = [val]
            else:
                main_dict[key].append(val)

            freq_list = [0] * 26

        for keys in main_dict:
            res.append(main_dict[keys])

        return res











        