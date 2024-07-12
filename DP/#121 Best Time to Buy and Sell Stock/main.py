def solve(prices):
    min_price = 10**5
    profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price-min_price > profit:
            profit = price-min_price
    return profit
            
        
print(solve([7,1,5,3,6,4]))
