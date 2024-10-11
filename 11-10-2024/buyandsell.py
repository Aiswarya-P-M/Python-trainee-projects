# Given list of prices
a = [7, 1, 3, 4]

max_diff = 0 #max_diff is initialized to 0 to track the maximum price difference found.
buy_day = -1  # Initialize to -1 to indicate no valid day found
sell_day = -1  # Initialize to -1 to indicate no valid day found

# Iterate through the list to find max difference
for i in range(len(a)): #The outer loop iterates through each price in the list using index i.
    for j in range(i + 1, len(a)): #The inner loop iterates through the prices that come after the current price (using index j), specifically starting from i + 1. 
        #This ensures that we only look at future prices to simulate buying first and then selling later.
        diff = a[j] - a[i] #For each pair of prices a[i] (buy price) and a[j] (sell price), the code calculates the price difference:
        if diff > max_diff: #If the calculated difference (diff) is greater than the current max_diff
            #max_diff to the new maximum difference.
            # buy_day to the current index i (the index of the buying day).
            #sell_day to the current index j (the index of the selling day).
            max_diff = diff
            buy_day = i  # Index of buy day
            sell_day = j  # Index of sell day

# Print the best day to buy and sell
if buy_day != -1 and sell_day != -1:
    print(f"Best day to buy: Day {buy_day + 1} (Price: {a[buy_day]})")
    print(f"Best day to sell: Day {sell_day + 1} (Price: {a[sell_day]})")
else:
    print("No profitable buy/sell days found.")
