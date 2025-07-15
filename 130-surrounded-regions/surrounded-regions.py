class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rlen = len(board)
        clen = len(board[0])
        visited = set()

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                m,n = q.popleft()
                dirns = [[0,1], [0,-1], [1,0], [-1,0]]
                for dr, dc in dirns:
                    nu_r = m+dr
                    nu_c = n+dc
                    if (nu_r in range(rlen) and nu_c in range(clen)) and board[nu_r][nu_c] == 'O' and (nu_r, nu_c) not in visited:
                        q.append((nu_r, nu_c))
                        visited.add((nu_r, nu_c))

        for r in range(rlen):
            for c in range(clen):
                if (r == 0 or r == rlen -1 or c == 0 or c == clen -1) and board[r][c] == 'O' and (r, c) not in visited:
                    bfs(r,c)

        for r in range(rlen):
            for c in range(clen):
                if board[r][c] == 'O' and (r,c) not in visited:
                    board[r][c] = 'X'



        