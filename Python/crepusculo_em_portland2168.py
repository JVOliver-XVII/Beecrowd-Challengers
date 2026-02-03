class PortlandMap:
    def __init__ (self, size):
        self.n = size
        self.corners = []
        self._load_camera_data()
    
    def _load_camera_data(self):
        for _ in range(self.n + 1):
            row = list(map(int, input().split()))
            self.corners.append(row)
    
    def _is_block_safe(self, row, col):
        camera_count = (
            self.corners[row][col] +
            self.corners[row][col + 1] +
            self.corners[row + 1][col] +
            self.corners[row + 1][col + 1]
        )
        return camera_count >= 2
    
    def display_security_status(self):
        for i in range(self.n):
            row_output = ""
            for j in range(self.n):
                if self._is_block_safe(i, j):
                    row_output += "S"
                else:
                    row_output += "U"
            print(row_output)

if __name__ == "__main__":
    try:
        n_input = int(input())
        city_center = PortlandMap(n_input)
        city_center.display_security_status()
    except EOFError:
        pass