#Best price to buy and sell along with time position(index)

Input=[77,43,10,105,300,50,6,26,89,200,300,11]
myDict={k:v for k,v in enumerate(Input)}
print(myDict)
minimum=min(Input)
maximum=max(Input)

for k,v in myDict.items():
    if myDict[k]==minimum:
        print(f"Best price to buy: {k}:{v}")
        
    if myDict[k]==maximum:
        print(f"Best price to sell: {k}:{v}")
    