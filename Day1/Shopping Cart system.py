cart={}
def add_item(name,price,qty):
    bill=price*qty
    print(f"Added {qty} x {name}\nTotal Bill : {bill}")
for i in range (3):
    add_item(input("Item :"),int(input("price :")),int(input("Qty :")))
