# recursive solution, works with any numbers

def josephus(p, k): 
  
    if (p == 1): 
        return 1
    else: 
        return (josephus(p - 1, k) + k-1) % p + 1
  
p = int(input("\nHow many prisoners : ")) # p as prisoners
k = int(input("\nSkipped number     : ")) # number of prisoners are skipped
  
print("\nThe chosen place is: ", josephus(p, k)) 
