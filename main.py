from abc import ABC,abstractmethod
def greet(name):
    return f"Hello, {name}!"

class Creator:
    @staticmethod
    def get_product(option):
        product = None
        if option == 1:
            product = ConcreteProduct1()
        elif option == 2:
            product = ConcreteProduct2()
        return product

class Product(ABC):
    @abstractmethod
    def get_product_info(self):
        raise NotImplementedError

class ConcreteProduct1(Product):
    def get_product_info(self):
        return 'ConcreteProduct1'

class ConcreteProduct2(Product):
    def get_product_info(self):
        return 'ConcreteProduct2'

class Client:
    @staticmethod
    def main():
        print('Product types:ConcreteProduct1(1),ConcreteProduct2(2)')
        option0 = int(input('Please select:'))
        print(Creator.get_product(option0).get_product_info())


if __name__ == "__main__":
    #name = input("Enter your name: ")
    #print(greet(name))
    print("你好")
    if True:
        print("True")
    else:
        print("False")
    Client.main()