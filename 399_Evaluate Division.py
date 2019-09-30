class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict
        g = defaultdict(set)
        for (x, y), v in zip(equations, values):
            g[x].add((y, v))
            g[y].add((x, 1/v))
        def bfs(src, dst):
            if not (src in g and dst in g): return -1.0
            q, seen = [(src, 1.0)], set()
            for x, v in q:
                if x == dst: return v
                seen.add(x)
                for y, k in g[x]:   
                    if y not in seen:
                        seen.add(y)
                        q.append((y, v*k))
            return -1.0
        return [bfs(s, d) for s, d in queries]