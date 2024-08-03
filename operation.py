import datetime
from write import generate_invoice

def display_stock(furniture_list):
    print("Available Furniture:")
    for item in furniture_list:
        print(f"{item['id']}: {item['manufacturer']} - {item['name']} | Quantity: {item['quantity']} | Price: ${item['price']}")

def purchase_furniture(furniture_list):
    cart = []
    total_amount = 0
    employee_name = input("Enter employee name: ")
    vat_rate = 0.13  # VAT rate as 13%
    shipping_cost = float(input("Enter shipping cost: "))  # Shipping cost input before purchase
    
    while True:
        furniture_id = int(input("Enter furniture ID to purchase: "))
        quantity = int(input("Enter quantity: "))

        for furniture in furniture_list:
            if furniture['id'] == furniture_id:
                total_amount += quantity * furniture['price']
                furniture['quantity'] += quantity
                cart.append({
                    'Furniture ID': furniture['id'],
                    'Manufacturer': furniture['manufacturer'],
                    'Product Name': furniture['name'],
                    'Quantity': quantity,
                    'Total Amount': f"${quantity * furniture['price']:.2f}"
                })
                break
        else:
            print("Furniture ID not found!")

        more = input("Do you want to add more products to the purchase (yes/no)? ")
        if more.lower() != 'yes':
            break

    vat_amount = total_amount * vat_rate
    total_due = total_amount + vat_amount + shipping_cost

    invoice_data = {
        'Employee Name': employee_name,
        'Date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'Total Amount Without VAT': f"${total_amount:.2f}",
        'VAT Amount': f"${vat_amount:.2f}",
        'Shipping Cost': f"${shipping_cost:.2f}",
        'Total Amount': f"${total_due:.2f}",
        'Items': cart
    }
    generate_invoice(invoice_data, "purchase")
    print("Purchase(s) successful!")

def sell_furniture(furniture_list):
    cart = []
    total_amount = 0
    customer_name = input("Enter customer name: ")
    vat_rate = 0.13  # VAT rate as 13%
    
    while True:
        furniture_id = int(input("Enter furniture ID to sell: "))
        quantity = int(input("Enter quantity: "))
        
        for furniture in furniture_list:
            if furniture['id'] == furniture_id:
                if quantity <= furniture['quantity']:
                    total_amount += quantity * furniture['price']
                    furniture['quantity'] -= quantity
                    cart.append({
                        'Furniture ID': furniture['id'],
                        'Manufacturer': furniture['manufacturer'],
                        'Product Name': furniture['name'],
                        'Quantity': quantity,
                        'Price': f"${furniture['price']:.2f}",
                        'Total Amount Without VAT': f"${quantity * furniture['price']:.2f}"
                    })
                else:
                    print("Insufficient stock!")
                break
        else:
            print("Furniture ID not found!")

        more = input("Do you want to add more products to the sale (yes/no)? ")
        if more.lower() != 'yes':
            break

    vat_amount = total_amount * vat_rate
    shipping_cost = float(input("Enter shipping cost: "))  # Shipping cost input after sale
    total_due = total_amount + vat_amount + shipping_cost

    invoice_data = {
        'Customer Name': customer_name,
        'Date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'Total Amount Without VAT': f"${total_amount:.2f}",
        'VAT Amount': f"${vat_amount:.2f}",
        'Shipping Cost': f"${shipping_cost:.2f}",
        'Total Amount Due': f"${total_due:.2f}",
        'Items': cart
    }
    generate_invoice(invoice_data, "sale")
    print("Sale(s) successful!")
