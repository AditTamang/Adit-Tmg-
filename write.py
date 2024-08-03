import datetime

def update_stock(filename, furniture_list):
    with open(filename, 'w') as file:
        for furniture in furniture_list:
            file.write(f"{furniture['id']}, {furniture['manufacturer']}, {furniture['name']}, {furniture['quantity']}, ${furniture['price']:.2f}\n")

def generate_invoice(invoice_data, transaction_type):
    filename = f"{transaction_type}_invoice_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
    with open(filename, 'w') as file:
        file.write(f"{transaction_type.capitalize()} Invoice\n")
        file.write(f"Date: {invoice_data['Date']}\n")
        if transaction_type == "purchase":
            file.write(f"Employee Name: {invoice_data['Employee Name']}\n")
        else:
            file.write(f"Customer Name: {invoice_data['Customer Name']}\n")
        file.write("\nItems:\n")
        for item in invoice_data['Items']:
            file.write(f"  - {item['Furniture ID']}: {item['Manufacturer']} - {item['Product Name']} | Quantity: {item['Quantity']} | Total Amount: {item['Total Amount']}\n")
        if transaction_type == "sale":
            file.write(f"\nTotal Amount Without VAT: {invoice_data['Total Amount Without VAT']}\n")
            file.write(f"VAT Amount: {invoice_data['VAT Amount']}\n")
            file.write(f"Shipping Cost: {invoice_data['Shipping Cost']}\n")
            file.write(f"Total Amount Due: {invoice_data['Total Amount Due']}\n")
        else:
            file.write(f"\nTotal Amount Without VAT: {invoice_data['Total Amount Without VAT']}\n")
            file.write(f"VAT Amount: {invoice_data['VAT Amount']}\n")
            file.write(f"Shipping Cost: {invoice_data['Shipping Cost']}\n")
            file.write(f"Total Amount: {invoice_data['Total Amount']}\n")
    print(f"Invoice generated: {filename}")
