import sys

for i, line in enumerate(sys.stdin):
    cost = line.strip()
    estimated_cost = len(cost)
    print(estimated_cost)
