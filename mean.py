import sys
sum = 0
n= 0

# Sum input values
for num in sys.stdin:
  sum += float(num)
  n += 1

# I still think the octocat is disconcerting.
print sum/n
