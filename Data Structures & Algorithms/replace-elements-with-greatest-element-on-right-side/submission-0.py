class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        max_sofar = -1
        for i in range (len(arr)-1,-1,-1):
            current = arr[i]
            arr[i] = max_sofar
            max_sofar = max(max_sofar, current)
        return arr
        