import requests, json, random
from faker import Faker
from department import Department
from address import Address
from contact_info import ContactInfo
from employee import Employee
from zakaznik import Zakaznik
from product import Product
from stock import Stock
from region import Region
from stock_product import StockProduct
from order import Order
from product_order import ProductOrder

fake = Faker()
FAKE_ADDRESSES = []
POZNAMKY = [
    'poznamka 1',
    'poznamka 2',
    'poznamka 3'
]
TITUL = ["ing", "mgr", "bc", ""]
FAKE_PRODUCTS = []
TYP_PLATBY = ["karta", "hotove", "prevodem"]

def phn():
    n = '0000000000'
    while '9' in n[3:6] or n[3:6]=='000' or n[6]==n[7]==n[8]==n[9]:
        n = str(random.randint(10**9, 10**10-1))
    return n[:3] + '-' + n[3:6] + '-' + n[6:]

def get_names(count: int) -> list:
    req = requests.get(f'http://names.drycodes.com/{count}?nameOptions=boy_names&format=json')
    data = json.loads(req.content)
    return data

def load_fake_addresses() -> list:
    with open('addresses/addresses-us-100.json', 'r') as f:
        addresses = f.read()
    return json.loads(addresses)

def load_fake_products() -> list:
    with open('products.json', 'r') as f:
        products = f.read()
    return json.loads(products)

def generate_employee_list(count: int) -> tuple:
    names = [[name.split('_')[0], name.split('_')[1]] for name in get_names(count)]
    employees = []
    addresses = []
    kontaktni_udaje = []
    departments = []
    for i in range(count):
        date = str(fake.date_between(start_date="-20y", end_date="today"))
        address = random.choice(FAKE_ADDRESSES)
        while "city" not in address:
            address = random.choice(FAKE_ADDRESSES)
        addresses.append(Address(address['city'], address['postalCode'], address['state']))
        kontaktni_udaje.append(ContactInfo(f"{names[i][0]}.{names[i][1]}@company.com", str(phn()), str(phn()), str(Employee.NUMBER_OF), str(Address.NUMBER_OF)))
        
        department = None
        for dep in departments:
            if dep.nazev == address['state']:
                department = dep
        if department == None:
            department = Department(address['state'])
            departments.append(department)

        employees.append(Employee(f'{date} 00:00:00', names[i][0], names[i][1], random.randint(15, 30)*1000, random.choice(POZNAMKY), str(random.randint(4, 15)), random.choice(TITUL), department.id, ContactInfo.NUMBER_OF))
    return employees, addresses, kontaktni_udaje, departments

def generate_zakaznik_list(count: int) -> tuple:
    names = [[name.split('_')[0], name.split('_')[1]] for name in get_names(count)]
    zakaznici = []
    addresses = []
    kontaktni_udaje = []
    regions = []
    for i in range(count):
        address = random.choice(FAKE_ADDRESSES)
        while "city" not in address:
            address = random.choice(FAKE_ADDRESSES)
        region = None
        for reg in regions:
            if reg.nazev == address['state']:
                region = reg
        if region == None:
            region = Region(address['state'])
            regions.append(region)
        addresses.append(Address(address['city'], address['postalCode'], region.id))
        kontaktni_udaje.append(ContactInfo(f"{names[i][0]}.{names[i][1]}@company.com", str(phn()), str(phn()), str(Employee.NUMBER_OF), str(Address.NUMBER_OF)))
        zakaznici.append(Zakaznik(f"{names[i][0]} {names[i][1]}", ContactInfo.NUMBER_OF, region.id))

    return zakaznici, addresses, kontaktni_udaje, regions

def generate_product_list(regions) -> tuple:
    count = len(FAKE_PRODUCTS)
    products = []
    stocks = []
    addresses = []
    kontaktni_udaje = []
    regions = regions
    stock_products = []
    for i in range(count):
        address = random.choice(FAKE_ADDRESSES)
        while "city" not in address:
            address = random.choice(FAKE_ADDRESSES)
        region = None
        for reg in regions:
            if reg.nazev == address['state']:
                region = reg
        if region == None:
            region = Region(address['state'])
            regions.append(region)
        addresses.append(Address(address['city'], address['postalCode'], address['state']))
        kontaktni_udaje.append(ContactInfo(f"{address['state']}@company.com", str(phn()), str(phn()), str(Employee.NUMBER_OF), str(Address.NUMBER_OF)))
        stocks.append(Stock(ContactInfo.NUMBER_OF, region.id))
        products.append(Product(FAKE_PRODUCTS[i]['price'], FAKE_PRODUCTS[i]['name'], FAKE_PRODUCTS[i]['description'], FAKE_PRODUCTS[i]['picture']))
        stock_products.append(StockProduct(Product.NUMBER_OF, random.randint(10, 50), Stock.NUMBER_OF, random.randint(50, 60)))
        
    return products, stocks, addresses, kontaktni_udaje, regions, stock_products

def generate_order_list(count, pocet_zakazniku, pocet_zamestnancu) -> tuple:
    orders = []
    product_orders = []
    addresses = []
    kontaktni_udaje = []
    for _ in range(count):
        date_1 = str(fake.date_between(start_date="-20d", end_date="+20d"))
        date_2 = str(fake.date_between(start_date="-20d", end_date="+20d"))
        address = random.choice(FAKE_ADDRESSES)
        while "city" not in address:
            address = random.choice(FAKE_ADDRESSES)
        address_2 = random.choice(FAKE_ADDRESSES)
        while "city" not in address_2:
            address_2 = random.choice(FAKE_ADDRESSES)
        addresses.append(Address(address['city'], address['postalCode'], address['state']))
        kontaktni_udaje.append(ContactInfo(f"{address['state']}@company.com", str(phn()), str(phn()), str(Employee.NUMBER_OF), str(Address.NUMBER_OF)))
        addresses.append(Address(address_2['city'], address_2['postalCode'], address_2['state']))
        kontaktni_udaje.append(ContactInfo(f"{address_2['state']}@company.com", str(phn()), str(phn()), str(Employee.NUMBER_OF), str(Address.NUMBER_OF)))
        orders.append(Order(date_1, date_2, random.choice(TYP_PLATBY), random.randint(1, pocet_zakazniku), random.randint(1, pocet_zamestnancu), ContactInfo.NUMBER_OF-1, ContactInfo.NUMBER_OF))
        p_id =  random.randint(1, len(FAKE_PRODUCTS)-1)
        product_orders.append(ProductOrder(Order.NUMBER_OF, random.randint(1, 30), p_id, FAKE_PRODUCTS[p_id]['price']))

    return orders, product_orders, addresses, kontaktni_udaje

def main() -> None:
    employee_list, addresses_list, kontaktni_udaje_list, department_list = generate_employee_list(100)
    zakaznik_list, a, k, regions = generate_zakaznik_list(100)
    addresses_list += a
    kontaktni_udaje_list += k
    products, stocks, a, k, r, stock_products = generate_product_list(regions)
    regions = r
    addresses_list += a
    kontaktni_udaje_list += k
    orders, product_orders, a, k = generate_order_list(200, 100, 100)
    addresses_list += a
    kontaktni_udaje_list += k
    #orders, product_orders = generate_order_list()

    data = [] + addresses_list + kontaktni_udaje_list + department_list + employee_list + zakaznik_list + products + regions + stocks + stock_products + orders + product_orders
    with open('query.sql', 'w') as f:
        for item in data:
            f.write(str(item) + "\n")

if __name__ == "__main__":
    FAKE_ADDRESSES = load_fake_addresses()['addresses']
    FAKE_PRODUCTS = load_fake_products()['products']
    main()