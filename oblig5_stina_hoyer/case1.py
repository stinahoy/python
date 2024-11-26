


#oppg1

def print_ware(ware):
    print(f"Name: {ware[ 'name' ]}")
    print(f"Price: {ware[ 'price' ]},-")
    print(f"Number in stock: {ware[ 'stock' ]}")
    print(f"Description: {ware[ 'description' ]}")

#oppg2

def kalkuler_average_ware_rating(ware):
    ratings = ware.get('ratings', [])
    if not ratings:
        raise ZeroDivisionError ("No rating available")
    return round(sum(ratings) / len(ratings), 1)

#oppg3

def fa_alle_wares_i_stock(all_wares):
    return {key: value for key, value in all_wares.item() if value ['stock'] > 0}

#oppg4

def er_nummer_av_wares_i_stock(ware, number_of_ware):
    return ware ['stock'] >= number_of_ware

#oppg5

def leggtil_eller_ware_til_shoppingcart(ware_key, shopping_cart, number_of_ware):
    tilgjengelig_stock = ware ['stock']
    if tilgjengelig_stock >= number_of_ware:
        shopping_cart [ware_key] = shopping_cart.get(ware_key, 0) + number_of_ware
        print(f"Added {number_of_ware} of {ware['name']} to the shopping cart.")
    else:
        if tilgjengelig_stock > 0:
            shopping_cart[ware_key] = shopping_cart.get (ware_key, 0) + tilgjengelig_stock
            print(f"Added {tilgjengelig_stock} of {ware[ 'name' ]} to the shopping cart.")
        else:
            print(f"{ware[ 'name' ]} is out of stock. ")

#oppg6

def kalkuler_shopping_cart_pris(shopping_cart, all_wares, )