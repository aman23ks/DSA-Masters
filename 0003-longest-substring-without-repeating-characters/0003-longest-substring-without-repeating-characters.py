class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = ""
        i = 0
        length = 0
        maxi = 0
        while i < len(s):
            if s[i] in st:
                while st[0] != s[i]:
                    st = st[1:]
                    length -= 1
            if st != "" and st[0] == s[i]:
                st = st[1:]
                length -= 1
            st += s[i]
            i += 1
            length += 1
            maxi = max(length, maxi)
        return maxi