from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        degree= {}
        dq = deque()
        src = set()
        value = []
        route = {}
        result = []
        visited = set()
        courseId = [i for i in range(numCourses)]

        if numCourses and prerequisites:
            for i,j in prerequisites:
                if degree.get(i) or degree.get(i) == 0:
                    degree[i] = degree[i] + 1
                else:
                    degree[i] = 1
                value.append(j) #src

            merge_values = value + courseId
            for i in merge_values:
                if degree.get(i) or degree.get(i) == 0 :
                    pass
                else:
                    degree[i] = 0
            for i ,j in prerequisites:
                if route.get(j) or route.get(j) == 0:
                    route[j] = route[j] + [i]
                else:
                    route[j] = [i]

            def src(): #degree updation
                for keys in degree.keys():
                    if degree[keys] == 0:
                        if keys not in visited:
                            dq.append(keys)
                            visited.add(keys)
                return dq

            def dfs(v): #dfs
                degree[v] = degree[v] - 1 
            def course(dq):
                while dq:
                    k = dq.popleft()
                    result.append(k)
                    if route.get(k):
                        for v in route[k]:
                            dfs(v)
                    s = src()
                    course(s)
                if len(result) == numCourses:
                    return True
                    
            s = src()

            if s:  #no source then false cycle
                if course(s):
                    return True
                else:
                    return False
            else:
                return False

        else:
            return True
        
        
        
            
                
