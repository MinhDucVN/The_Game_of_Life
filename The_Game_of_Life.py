class LifeGrid :
    DEAD_CELL = 0
    LIVE_CELL = 1

    def __init__( self ):
        self.numRows = self.ip_numRows()
        self.numCols = self.ip_numCols()
        coordList = self.ip_coordList()
        self._grid = [[0 for j in range(self.numCols + 2)] for i in range(self.numRows + 2)]
        self.configure( coordList )
    
    def ip_numRows( self ):
        n_rows = int(input("Nhập số hàng của lưới: "))
        return n_rows
    
    def ip_numCols( self ):
        n_cols = int(input("Nhập số cột của lưới: "))
        return n_cols
    
    def ip_coordList( self ):
        n_alive = int(input("Nhập số tế bào còn sống: "))
        coordList = []
        for i in range(n_alive):
            row = list(map(int, input("Tọa độ tế bào thứ %2d: " %(i+1)).split()))
            coordList.append(row)
        return coordList

    def configure( self, coordList ):
        for i in range( self.numRows +2 ):
            for j in range( self.numCols +2 ):
                self.clearCell( i, j )
        for coord in coordList :
            self.setCell( coord[0], coord[1] )
        self._numLiveNeighbors = self.count_numLiveNeighbors()

    def isLiveCell( self, row, col ):
        return self._grid[row][col] == LifeGrid.LIVE_CELL

    def clearCell( self, row, col ):
        self._grid[row][col] = LifeGrid.DEAD_CELL

    def setCell( self, row, col ):
        self._grid[row][col] = LifeGrid.LIVE_CELL

    def count_numLiveNeighbors( self ):
        arr = [[0 for j in range(self.numCols + 2)] for i in range(self.numRows + 2)]
        for i in range(1, self.numRows + 1):
            for j in range(1, self.numCols +1 ):
                if( self.isLiveCell( i, j ) ):
                    arr[i-1][j-1] += 1 
                    arr[i-1][j] += 1
                    arr[i-1][j+1] += 1
                    arr[i][j-1] += 1
                    arr[i][j+1] += 1
                    arr[i+1][j-1] += 1
                    arr[i+1][j] += 1
                    arr[i+1][j+1] += 1
        return arr
    
    
    def numLiveNeighbors( self, row, col ):
        return self._numLiveNeighbors[row][col]
    
    def evolve( self ):
        liveCells = list()
        for i in range(1, self.numRows +1 ):
            for j in range(1, self.numCols +1 ):
                neighbors = self._numLiveNeighbors[i][j]
                if (neighbors == 2 and self.isLiveCell( i, j )) or (neighbors == 3 ):
                    liveCells.append( [i, j] )
        self.configure( liveCells )

    def draw( self ):
        for i in range(1, self.numRows +1 ):
            for j in range(1, self.numCols +1 ):
                print( self._grid[i][j], end=' ' )
            print()
        print()

GameGrid = LifeGrid( )
while( True ):
    choice = int(input("Lựa chọn tác vụ: \n\
1. In ra cấu hình hiện tại. \n\
2. Kiểm tra xem tế bào tại tọa độ xác định còn sống không? \n\
3. Chuyển sang thế hệ kế tiếp!!! \n\
4. Số lượng hàng xóm của tế bào tại tọa độ xác định? \n\
0. Kết thúc. \n"))
    print()
    if choice == 1:
        GameGrid.draw()
    elif choice == 2:
        coord = list(map(int, input("Tọa độ tế cần kiểm tra: ").split()))
        if GameGrid.isLiveCell( coord[0], coord[1] ):
            print ("Tế bào có tọa độ [%2d,%2d] còn sống. " %(coord[0], coord[1]))
        else: print ("Tế bào có tọa độ [%2d,%2d] đã chết. " %(coord[0], coord[1]))
        print()
    elif choice == 3:
        GameGrid.evolve()
        print ("Đã chuyển sang thế hệ kế tiếp!!! ")
        print()
    elif choice == 4:
        coord = list(map(int, input("Tọa độ tế cần kiểm tra: ").split()))
        print("Tế bào tọa độ [%2d,%2d] có %2d hàng xóm." %(coord[0], coord[1], GameGrid.numLiveNeighbors(coord[0], coord[1])))
    elif choice == 0:
        print("Bye bye :>")
        break
