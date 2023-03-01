def reverse(x:int) -> int:
    is_neg = False
    if(x < 0):
        is_neg = True
        x *= -1
    
    x_rev = int(str(x)[::-1])
    if(is_neg):
        x_rev *= -1
    
    if( (x_rev > ((2**31) - 1)) or (x_rev < (-2**31))):
        return 0
    else:
        return x_rev
    

if __name__ == "__main__":
    test_val1 = 123
    test_val2 = -123
    test_val3 = 120

    print(reverse(test_val1))
    print(reverse(test_val2))
    print(reverse(test_val3))
