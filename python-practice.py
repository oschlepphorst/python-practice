class Collatz:
    def solve(self, n):
        out = []
        out.append(n)
        while(n != 1):
            if(n % 2 == 0):
                n = n/2
                out.append(n)
            else:
                n = 3*n+1
                out.append(n)
            
        return len(out)