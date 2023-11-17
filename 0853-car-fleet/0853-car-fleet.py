class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        maps = {}
        for i in range(len(position)):
            maps[position[i]] = speed[i]
        stack = []
        for pos in sorted(maps, reverse=True):

            if not stack or ((target - pos)/maps[pos]) > stack[-1]:
                stack.append(((target - pos)/maps[pos]))
            
        return len(stack)