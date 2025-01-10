def generate_coins(max, coins, start=0, sum=0):
    if sum >= max:
        if sum == max:
            yield 1
    else:
        for i in range(start,len(coins)):
            yield from generate_coins(max, coins,i, sum+coins[i])

            

coins = [200,100,50,20,10,5,2,1]
print(sum(generate_coins(200, coins)))

