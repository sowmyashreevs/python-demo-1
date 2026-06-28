restaurant_name = input("Enter the restaurant name: ")
veg_nonveg = input("Would you like to order Veg or Non-veg: ")
price = float(input("Price of the item: "))
items_count = int(input("Enter the quantity: "))
item_value = price * items_count
gst = 18
gst_value = item_value * (gst/100)
delivery_charges = 40
total_cost = item_value + gst_value + delivery_charges

print(f"Selected restaurant is: {restaurant_name}\nVeg or Non-veg: {veg_nonveg}\nPer item price: {price}\nTotal qty: {items_count}\nGST(18%): {gst_value}\nDelivery Charges: {delivery_charges}\nTotal amount: {total_cost:.2f}")
