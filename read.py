

def load_furniture_data(filename):
    furniture_list = []
    with open(filename, 'r') as file:
        for line in file:
            elements = line.strip().split(', ')
            furniture = {
                'id': int(elements[0]),
                'manufacturer': elements[1],
                'name': elements[2],
                'quantity': int(elements[3]),
                'price': float(elements[4].replace('$', ''))
            }
            furniture_list.append(furniture)
    return furniture_list
