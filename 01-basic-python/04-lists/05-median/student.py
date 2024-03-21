# Write your code here
def median(ns):
    sorted_ns=  sorted(ns) # sorteert de lijst van klein naar groot
    if len(sorted_ns) % 2 != 0:
        return (sorted_ns[len(sorted_ns) // 2]) 
    
    elif len(sorted_ns) % 2 == 0:
        return (sorted_ns[len(sorted_ns) // 2 - 1] + sorted_ns[len(sorted_ns) // 2]) / 2

