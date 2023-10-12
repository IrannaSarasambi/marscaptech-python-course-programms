'''
Substring sorting:
Sort mailids based on the compamy name
if input is in below order 
    gokul@zerodha.com Zephrinr@amazon.com Philips@cognizant.com
    Output expected is 
    Zephrinr@amazon.com
    Philips@cognizant.com
    gokul@zerodha.com
'''

getMailID = input("Enter the list of mailids :")
myList = getMailID.split()
print(myList)
ListSort = sorted(myList,key=lambda x:x.split('@')[1])
print(ListSort)
print(f"The mailid sorted based on company ID is {ListSort}")