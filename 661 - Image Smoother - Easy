class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        matrix_size = len( img )
        row_size = len( img[ 0 ] ) 
        #List Comprehension to initialize ans matrix values to 0
        ans = [ [ 0 for i in range( row_size ) ] for j in range( matrix_size ) ]

        for i in range(matrix_size):
            for j in range(row_size):
                position = 0
                counter = 0 #counting the number of cells around the number
                for x in range( max( 0, i-1 ), min( matrix_size, i+2 ) ):
                    for y in range( max( 0, j-1 ), min( row_size, j+2 ) ):
                        position += img[ x ][ y ]
                        counter += 1
                ans[ i ][ j ] = position // counter #taking the average and updating each cell of ans matrix
        return ans
