from pprint import pprint
with open('receipt.TXT', 'r', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        name = line.strip()
        amount = int(file.readline().strip())
        ingr = []
        for _ in range(amount):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            ingr.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        file.readline()
        cook_book[name] = ingr

def get_shop_list_by_dishes(dishes, person_count):
    k = []
    v = []
    for name, ingr in cook_book.items():
        if name in(dishes):
            for i in ingr:
                ingr_name = i.pop('ingredient_name')
                k.append(ingr_name)
                for key, val in i.items():
                    if key == 'quantity':
                        val = int(val) * person_count
                        i['quantity'] = val
                        v.append(i)
    shop_dict = {}
    for name, data in zip(k,v):
      if name in shop_dict:
        shop_dict[name]['quantity'] += data['quantity']
      else:
        shop_dict[name] = data
    pprint(shop_dict)

get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)




