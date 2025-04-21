n = int(input())
l = list(map(int, input().split()))

naj = max(l)
l.remove(naj)
print(max(l))