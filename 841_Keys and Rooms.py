class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #  判断是不是连通图
        seen = [0] * len(rooms)
        seen[0] = 1
        stack = [0]
        
        while stack:
            node = stack.pop()
            for key in rooms[node]:
                if seen[key] == 0:
                    seen[key] = 1
                    stack.append(key)
        if 0 in seen:
            return False
        else:
            return True
        