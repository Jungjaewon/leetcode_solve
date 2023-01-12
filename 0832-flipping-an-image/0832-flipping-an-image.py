class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        m,n = len(image), len(image[0])
        for i in range(m):
            for j in range(n):
                image[i][j] = 1 if image[i][j] == 0 else 0
            image[i] = image[i][::-1]
        return image