# def read_loans():
#     with open("data.txt","r") as file:
#         for i in file:
#             print(i)

# def show_loans():
#     with open("data.txt","r") as file:
#         return file.readlines()


import write

def buy_items(furniture_data):
    id = int(input("Enter the ID of the furniture to buy from the manufacturers: "))
    for furniture in furniture_data:
        if furniture["id"] == id:
            quantity = int(input("Enter the quantity to buy: "))
            
            '''checks if the current item has enough stock to fulfill the requested quantity.'''
            if furniture["quantity"] >= quantity:
                
                '''It reduces the quantity by the amount of stock available'''
                furniture["quantity"] += quantity
                print(f"You have bought {quantity} {furniture['product']}s from {furniture['manufacturer']}.")
            else:
                print("The items is not available at this moment. Insufficient stock!")
            break
    else:
        '''If loop ends without finding the valid number then it will display the below output'''
        print("Furniture not found!")
   
