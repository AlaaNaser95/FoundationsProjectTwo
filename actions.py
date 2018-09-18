# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "www.Tasawaq.com"  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!
    for s in stores:
      print ("- "+s.name)

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!
    for store in stores:
        if store.name==store_name:
            return store;
    return False;


def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!
    print_stores()
    user_input_store=input("Pick a store by typing its name. Or type \"checkout\" to pay your bills and say your goodbyes.\n")
    user_input_store=str(user_input_store).capitalize()
    print ("-"*50)
    while user_input_store=="":
        user_input_store=input()
        user_input_store=str(user_input_store).capitalize()
    if (user_input_store=="Checkout"):
        return "checkout"
   
    elif get_store(user_input_store)==False:
        print("No store with that name. Please try again.")
        return False
    else:
        return get_store(user_input_store)





def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    # your code goes here!
    
    if True:
        print(picked_store.name +":")
        for prod in picked_store.products:
            print(str(prod))
        user_item=input("Pick the items you'd like to add in your cart by typing the product name exactly as it was spelled above.\nType \"back\" to go back to the main menue where you can checkout.\n")
        user_item=str(user_item)
        while user_item!= "back":
            for prod in picked_store.products:
                if prod.name==user_item:
                    cart.add_to_cart(prod)
            user_item=str(input())
        


        
    
    
    

    

def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    # your code goes here!
    picked_store=pick_store()
    while picked_store!="checkout":
        if picked_store==False:
            picked_store=pick_store()
        else:
            pick_products(cart,picked_store)
            picked_store=pick_store()           
    else:
        cart.checkout()

    

    

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
