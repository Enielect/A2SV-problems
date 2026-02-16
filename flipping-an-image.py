class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
      # not-optimal
        for j in range(len(image)):
            for i in range(len(image[0])):
                cur = image[j][i]
                image[j][i] = abs(cur - 1)
            image[j].reverse()
        return image
