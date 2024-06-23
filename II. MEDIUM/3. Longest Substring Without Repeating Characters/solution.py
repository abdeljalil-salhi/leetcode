class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mymap, maxLength, left = {}, 0, 0

        for right in range(len(s)):
            # If the current character is in the map and the index of the current character is greater than or equal to the left pointer
            # Then we have a duplicate character in the current substring
            # We need to move the left pointer to the right of the previous occurrence of the current character
            # This is because we want to maintain a substring with no duplicate characters
            if s[right] in mymap and mymap[s[right]] >= left:
                left = mymap[s[right]] + 1

            # Update the index of the current character in the map
            mymap[s[right]] = right
            # Update the maximum length of the substring
            maxLength = max(maxLength, right - left + 1)

        # Return the maximum length of the substring
        return maxLength
