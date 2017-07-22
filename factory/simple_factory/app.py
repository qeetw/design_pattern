from pizza_store import PizzaStore
from simple_pizza_factory import SimplePizzaFactory

def main():
    pizza_store = PizzaStore(SimplePizzaFactory())

    pizza = pizza_store.order_pizza("cheese")
    print("pizza type is", pizza.get_name())

    pizza = pizza_store.order_pizza("pepperoni")
    print("pizza type is", pizza.get_name())

    pizza = pizza_store.order_pizza("clam")
    print("pizza type is", pizza.get_name())

if __name__ == "__main__":
    main()