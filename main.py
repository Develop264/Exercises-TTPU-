"""
#5
print(f"{'small':<8}{'ASCII':<8}{'Capital':<8}{'ASCII':<8}")
print("-" * 32)

for i in range(26):
    small_a= ord('a') + i
    small_letter = chr(small_a)
    
    capital_a= ord('A') + i
    capital_letter = chr(capital_a)
    
    print(f"'{small_letter}'{small_a:>7}     '{capital_letter}'{capital_a:>7}")

#6
def check():
    n = int(input("Enter the number of elements (n): "))
    if n <=0:
        print("Please enter a positive integer.")
        return
    ascending = True
    descending = True
    prev = int(input("Enter number: "))
    for i in range(2, n + 1):
        current = int(input(f"Enter number {i}: "))
        if current <= prev:
            ascending = False
        if current >= prev:
            descending = False
        prev = current
    if n == 1:
        print("neither ascending nor descending sequence")
    elif ascending:
        print("ascending sequence")
    elif descending:
        print("descending sequence")
    else:
        print("neither ascending nor descending sequence")

check()
"""