class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        initial = 0
        for operation in operations:
            if "+" in operation:
                initial +=1
            else:
                initial -=1
        return initial
