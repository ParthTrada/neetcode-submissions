class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        res = 1
        s_freq_dict = {}
        t_freq_dict = {}
        
        if (len(s) != len(t)):
            res = 0
        else:
            str_len = len(s)

            for i in range(str_len):
                # frequency mapping for string s
                if (s_freq_dict.get(s[i])):
                    s_freq_dict.update({s[i]: s_freq_dict[s[i]] + 1  })
                else:
                    s_freq_dict[s[i]] = 1

                    
            for i in range(str_len):
                # frequency mapping for string t
                if (t_freq_dict.get(t[i])):
                    t_freq_dict.update({t[i]: (t_freq_dict[t[i]] + 1) })
                else:
                    t_freq_dict[t[i]] = 1

                
            if s_freq_dict == t_freq_dict:
                res = 1
            else:
                res = 0
                        
        return bool(res)
        
        