from singletion import Singleton

def main():
    first_instance = Singleton()
    second_instance = Singleton()

    if first_instance is second_instance:
        print('Same Instance')
    else:
        print('Difference Instance')

    print('first_data:', first_instance.get_data())
    print('second_data:', second_instance.get_data())

    first_instance.set_data(10)
    print('first_data:', first_instance.get_data())
    print('second_data:', second_instance.get_data())

    second_instance.set_data(15)
    print('first_data:', first_instance.get_data())
    print('second_data:', second_instance.get_data())

if __name__ == '__main__':
    main()
