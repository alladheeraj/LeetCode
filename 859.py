class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return len(set(s)) < len(s)
        else:
            indices = [i for i in range(len(s)) if s[i] != goal[i]]
            if len(indices) == 2:
                i, j = indices
                if s[i] == goal[j] and s[j] == goal[i]:
                    return True
        return False
