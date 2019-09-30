class Solution:
    def build_path(self, from_vertex, to_vertex, path):
        the_path = []
        vertex = to_vertex
        while vertex is not -1:
            the_path.append(vertex)
            vertex = path[vertex]
        the_path.reverse()
        return the_path

    def dfs(self, vertex, graph, path, paths, visited, target_vertex):
        if vertex is target_vertex:
            the_path = self.build_path(vertex, target_vertex, path)
            paths.append(the_path)
            return
        for next_vertex in graph[vertex]:
            if next_vertex in visited:
                continue
            visited.add(next_vertex)
            path[next_vertex] = vertex
            self.dfs(next_vertex, graph, path, paths, visited, target_vertex)
            visited.remove(next_vertex)

    def allPathsSourceTarget(self, graph):
        visited = set()
        paths = []
        path = [-1] * len(graph)
        self.dfs(0, graph, path, paths, visited, len(graph) - 1)
        return paths


sol = Solution()

print(sol.allPathsSourceTarget([[1, 2], [3], [3], []]))
