testcases = int(input())

for t in range(testcases):
    rounds = int(input())

    
    
    chef_points = 0
    morty_points = 0

    for round in range(rounds):
        chef, morty = list(map(int, input().split()))

        chef_sum = 0
        morty_sum = 0    

        while(chef != 0):
            r = int(chef % 10)
            chef = int(chef / 10)

            chef_sum += r

        while(morty != 0):
            r = int(morty % 10)
            morty = int(morty / 10)

            morty_sum += r

        if(chef_sum > morty_sum):
            chef_points += 1
            #print(str(0) + " " + str(chef_sum))
        elif(chef_sum < morty_sum):
            morty_points += 1
            #print(str(1) + " " + str(morty_sum))
        else:
            chef_points += 1
            morty_points += 1
            #print(str(2) + " " + str(morty_sum))
    
    print('0 ' + str(chef_points) if chef_points > morty_points else '1 ' + str(morty_points) if chef_points < morty_points else '2 ' + str(morty_points))
    