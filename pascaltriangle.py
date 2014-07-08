import sys

def generate_pascals_triangle(n):
    triangle = [[1], [1, 1]]
    if n == 1:
        return triangle[0]
    else:
        for numRow in range(2,n):
            triangle.append([1]*numRow)
            for number in range(1, numRow):
                triangle[numRow][number] = triangle[numRow-1][number-1]+triangle[numRow-1][number]
            triangle[numRow].append(1)
        return triangle


            
if __name__ == '__main__':  
    n = 6
    print(generate_pascals_triangle(n))
    
