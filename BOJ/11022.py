import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print("Case #%d: %d + %d = %d"%(i+1, a, b, a+b))