# CLASSES AND METHODS
class Store():
    def __init__(self, name):
        """
        Initializes a new store with a name.
        """
        # your code goes here!
        self.name=name
        self.products=[]

    def add_product(self, product):
        """
        Adds a product to the list of products in this store.
        """
        # your code goes here!
        self.products.append(product)

    def print_products(self):
        """
        Prints all the products of this store in a nice readable format.
        """
        # your code goes here!
        s= self.name+":\n"
        for prod in self.products:
            s+= str(self.products[prod])+"\n"
        print (s)


class Product():
    def __init__(self, name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        # your code goes here!
        self.name=name
        self.description=description
        self.price=price

    def __str__(self):
        # your code goes here!
        prod_string= "\tProduct name: "+self.name+"\n"+"\tDescription: "+self.description+"\n\tPrice: "+str(self.price)+"\n"
        return prod_string


class Cart():
    def __init__(self):
        """
        Initializes a new cart with an empty list of products.
        """
        # your code goes here!
        self.items=[]

    def add_to_cart(self, product):
        """
        Adds a product to this cart.
        """
        # your code goes here!
        self.items.append(product)

    def get_total_price(self):
        """
        Returns the total price of all the products in this cart.
        """
        # your code goes here!
        total=0;
        for item in self.items:
            total+=item.price
        return total

    def print_receipt(self):
        """
        Prints the receipt in a nice readable format.
        """
        # your code goes here!
        print("Here's your reciept:")
        for i in self.items:
            print(str(i))
        pri=self.get_total_price()
        print("Your total price is : KD %.3f" % pri)

    def checkout(self):
        """
        Does the checkout.
        """
        # your code goes here!
        self.print_receipt()
        confirm=str(input("Confirm?(yes/no)"))
        if(confirm=="yes"):
            print ("your order has been placed.")
        else:
            print("your order has been cancelled.")
