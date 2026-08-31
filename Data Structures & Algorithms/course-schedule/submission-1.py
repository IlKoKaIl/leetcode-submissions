class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #map each course to prereq list
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        #visited set = all sources in the cur DFS path
        visitSet = set()
        def dfs(crs):
            if preMap[crs] == []:
                return True            
            if crs in visitSet:
                return False #loop detected

            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False

            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True

        