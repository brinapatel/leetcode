class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        output = []
        output.append([1])
        if numRows == 1:
            return output
        else:
            output.append([1,1])
            for i in range(1,numRows-1):
                inner_list = []
                inner_list.append(1)
                for j in range(1, len(output[i])):
                    inner_list.append(output[i][j-1]+output[i][j])
                inner_list.append(1)
                output.append(inner_list)
        return output
            