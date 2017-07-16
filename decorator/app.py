from espresso import Espresso
from house_blend import HouseBlend
from mocha import Mocha
from whip import Whip

def main():
    beverage = Espresso()
    print(beverage.get_description(), '$', beverage.cost())

    beverage = HouseBlend()
    print(beverage.get_description(), '$', beverage.cost())
    beverage = Mocha(beverage)
    print(beverage.get_description(), '$', beverage.cost())
    beverage = Whip(beverage)
    print(beverage.get_description(), '$', beverage.cost())

if __name__ == '__main__':
    main()