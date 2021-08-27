# Josephus problem when size of step is 2(fixed). 
# Returns position of survivor among a 
# circle of n number of prisoners and every second 
# prisoner being killed
def josephus(n): 
    p = 1
    while p <= n: 
        p *= 2
    return (2 * n) - p + 1
  
n = int(input("How many prisoners: "))
print ("The surviving place is: ", josephus(n)) 