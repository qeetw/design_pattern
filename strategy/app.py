from mallard_duck import MallardDuck
from fly_no_way import FlyNoWay
from squeak import Squeak

def main():
    duck = MallardDuck()
    duck.swin()
    duck.display()
    duck.performFly()
    duck.performQuack()
    duck.setFlyBehavior(FlyNoWay())
    duck.setQuackBehavior(Squeak())
    duck.performFly()
    duck.performQuack()

if __name__ == '__main__':
    main()
