
# odd even game
# for odd numbers print "Odd"
# for even numbers print "Even"
def odd_even(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(f"{i} is Even")
        else:
            print(f"{i} is Odd")
odd_even(10)
