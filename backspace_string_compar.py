class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # start from the end of both strings
        i = len(s) - 1
        j = len(t) - 1

        # keep going while any string still has characters
        while i >= 0 or j >= 0:

            # find next valid character in s
            skip_s = 0
            while i >= 0:
                if s[i] == '#':
                    skip_s += 1      # one character must be skipped
                    i -= 1
                elif skip_s > 0:
                    skip_s -= 1      # skip current character
                    i -= 1
                else:
                    break            # valid character found

            # find next valid character in t
            skip_t = 0
            while j >= 0:
                if t[j] == '#':
                    skip_t += 1
                    j -= 1
                elif skip_t > 0:
                    skip_t -= 1
                    j -= 1
                else:
                    break

            # compare valid characters
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False

            # one string ended before the other
            elif i >= 0 or j >= 0:
                return False

            # move to next character
            i -= 1
            j -= 1

        return True