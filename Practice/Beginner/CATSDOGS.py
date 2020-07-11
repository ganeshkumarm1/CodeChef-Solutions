t = int(input())

for i in range(t):
    cats, dogs, legs = list(map(int, input().split()))

    max_legs = 4 * (cats + dogs)
    min_legs = 4 * dogs if cats <= 2 * dogs else 4 * (cats - dogs)

    if legs % 4 != 0:
        print("no")
    else:
        if min_legs <= legs <= max_legs:
            print("yes")
        else:
            print("no")
    
