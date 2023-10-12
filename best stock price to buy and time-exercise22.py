'''consider the below list is a stock price data.first index is operating price of the day
and next index is pricen taken after 30mins. and the last index is closing price of he day.
in this please specify the best price to buy and sell along with the time positions(index)

ex: input=[77,43,10,105,300,50,6,26,89,200,300,11]
ourput: Best price to buy:6:6 Sell:10:300'''

price = [77,43,10,105,300,50,6,26,89,200,300,11]
print(f"stock price data:",price)
x = sorted(price)
print("x: ",x)
b = x[0]
s = x[-1]
indices = [i for i in range(len(price)) if price[i] == s]
print("indices: ",indices)
max_index = max(indices)
print("max_index: ",max_index)
print("Best price to buy: ",b,":",price.index(b),"sell:",s,":",max_index)