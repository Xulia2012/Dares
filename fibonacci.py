def main():
    n0 = 0
    n1 = 1
    for i in range(50):
        print(n0)
        nfibonacci = n0 + n1 
        n0 = n1
        n1 = nfibonacci
main()