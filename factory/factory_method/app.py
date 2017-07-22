from ny_style_pizza_store import NYStylePizzaStore
from chicago_style_pizza_store import ChicagoStylePizzaStore

def main():
    ny_pizza_store = NYStylePizzaStore()
    chicago_pizza_store = ChicagoStylePizzaStore()

    pizza = ny_pizza_store.order_pizza('cheese')
    print('Ethan ordered a', pizza.get_name(), '\n')

    pizza = chicago_pizza_store.order_pizza('cheese')
    print('Joel ordered a', pizza.get_name(), '\n')
  
if __name__ == '__main__':
    main()