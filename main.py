from typing import List

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Initialize an array to store in-degrees of all teams
        in_degree = [0] * n
        
        # Step 2: Process the edges to update in-degrees
        for u, v in edges:
            in_degree[v] += 1
        
        # Step 3: Find teams with in-degree 0
        candidates = [i for i in range(n) if in_degree[i] == 0]
        
        # Step 4: If there is exactly one team with in-degree 0, return it as the champion
        if len(candidates) == 1:
            return candidates[0]
        else:
            # If no team or more than one team has in-degree 0, return -1
            return -1

