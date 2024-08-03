from read import load_furniture_data
from write import update_stock
from operation import display_stock, purchase_furniture, sell_furniture

def main():
    furniture_list = load_furniture_data('furniture.txt')
    
    while True:
        print("Click 1 and Enter: Show all available items in the store")
        print("Click 2 and Enter: Purchase from Manufacturer")
        print("Click 3 and Enter: Sell items to Customer")
        print("Click 4 and Enter: Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            display_stock(furniture_list)
        elif choice == '2':
            purchase_furniture(furniture_list)
            update_stock('furniture.txt', furniture_list)
        elif choice == '3':
            sell_furniture(furniture_list)
            update_stock('furniture.txt', furniture_list)
        elif choice == '4':
            update_stock('furniture.txt', furniture_list)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
