MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money=0.0




while True:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    print('Please insert coins.')
    quaters = int(input('how many quarters?: ')) * 25.0
    dime = int(input('how many dimes?: ')) * 10.0
    nickels = int(input('how many nickles?: ')) * 5.0
    penny = int(input('how many pennies?:')) * 1.0
    cents = quaters + dime + nickels + penny
    dollor = cents / 100
    if order == 'off':
        break
    elif order == 'report':
        print('Water: ', resources['water'])
        print('Milk: ', resources['milk'])
        print('Coffee: ', resources['coffee'])
        print(f'Money: $', money)
    elif order=='espresso':
        if dollor>=MENU['espresso']['cost']:
            if resources['water'] >= MENU['espresso']['ingredients']['water']:
                resources['water'] = resources['water'] - MENU['espresso']['ingredients']['water']
                if resources['coffee'] >= MENU['espresso']['ingredients']['coffee']:
                    resources['coffee'] = resources['coffee'] - MENU['espresso']['ingredients']['coffee']
                    print('here id your coffee ☕')
                    print('Here is your Change $',dollor-MENU['espresso']['cost'])
                else:
                    print('Not Enough Coffee')
            else:
                print('Not Enough Water')
        else:
            print('Does Not have enough money')

    elif order=='latte':
        if dollor >= MENU['latte']['cost']:
            if resources['water'] >= MENU['latte']['ingredients']['water']:
                resources['water'] = resources['water'] - MENU['latte']['ingredients']['water']
                if resources['coffee'] >= MENU['latte']['ingredients']['coffee']:
                    resources['coffee'] = resources['coffee'] - MENU['latte']['ingredients']['coffee']

                    if resources['milk'] >= MENU['latte']['ingredients']['milk']:
                        resources['milk'] = resources['milk'] - MENU['latte']['ingredients']['milk']
                        print('here id your coffee ☕')
                        print('Here is your Change $', dollor - MENU['latte']['cost'])
                    else:
                        print('Not Enough milk')
                else:
                    print('Not Enough coffee')
            else:
                print('Not Enough water')
        else:
            print("Not Enough Money")

    elif order=='cappuccino':
        if dollor >= MENU['cappuccino']['cost']:
            if resources['water'] >= MENU['cappuccino']['ingredients']['water']:
                resources['water'] = resources['water'] - MENU['cappuccino']['ingredients']['water']
                if resources['coffee'] >= MENU['cappuccino']['ingredients']['coffee']:
                    resources['coffee'] = resources['coffee'] - MENU['cappuccino']['ingredients']['coffee']

                    if resources['milk'] >= MENU['cappuccino']['ingredients']['milk']:
                        resources['milk'] = resources['milk'] - MENU['cappuccino']['ingredients']['milk']
                        print('here id your coffee ☕')
                        print('Here is your Change $', dollor - MENU['cappuccino']['cost'])
                    else:
                        print('Not Enough milk')
                else:
                    print('Not Enough coffee')
            else:
                print('Not Enough water')
        else:
            print('Not Enough Money')

    else:
        print("not valid")