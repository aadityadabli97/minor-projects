#coffee machine program

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
off=False
while not off:
    quater=0.25
    dime=0.10
    nickle=0.05
    penny=0.01
    def coffee():
        choice=input("What would you like ? (espresso : $1.5 | latte : $2.5 |cappuccino: $3.0 | report)")
        if choice=="report":
            for items in resources:
                print(f"{items}:{resources[items]}")

        elif choice=="espresso":
            if MENU["espresso"]["ingredients"]["water"] > resources["water"]:
                print("Sorry there is not enough water")
                exit()
            elif MENU["espresso"]["ingredients"]["coffee"] > resources["coffee"]:
                print("Sorry there is not enough coffee")
                exit()
            else:
                print("Thanks , Please insert coins")
            t=calc()
            if t<MENU["espresso"]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            elif t>MENU["espresso"]["cost"]:
                change=t-MENU["espresso"]["cost"]
                print(f"Please take your coffee,Here is ${round(change,2)} dollars in change.")
                resources["water"]=resources["water"]-MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
            elif t==MENU["espresso"]["cost"]:
                print("Please take your coffee")
                resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
        elif choice=="latte":
            if MENU["latte"]["ingredients"]["water"] > resources["water"]:
                print("Sorry there is not enough water")
                exit()
            elif MENU["latte"]["ingredients"]["coffee"] > resources["coffee"]:
                print("Sorry there is not enough coffee")
                exit()
            elif MENU["latte"]["ingredients"]["milk"] > resources["milk"]:
                print("Sorry there is not enough milk")
                exit()
            else:
                print("Thanks , Please insert coins")
            t=calc()
            if t<MENU["latte"]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            elif t>MENU["latte"]["cost"]:
                change=t-MENU["latte"]["cost"]
                print(f"Please take your coffee,Here is ${round(change,2)} dollars in change.")
                resources["water"]=resources["water"]-MENU["latte"]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
            elif t==MENU["latte"]["cost"]:
                print("Please take your coffee")
                resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]

        elif choice=="cappuccino":
            if MENU["cappuccino"]["ingredients"]["water"] > resources["water"]:
                print("Sorry there is not enough water")
                exit()
            elif MENU["cappuccino"]["ingredients"]["coffee"] > resources["coffee"]:
                print("Sorry there is not enough coffee")
                exit()
            elif MENU["cappuccino"]["ingredients"]["milk"] > resources["milk"]:
                print("Sorry there is not enough milk")
                exit()
            else:
                print("Thanks , Please insert coins")
            t=calc()
            if t<MENU["cappuccino"]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            elif t>MENU["cappuccino"]["cost"]:
                change=t-MENU["cappuccino"]["cost"]
                print(f"Please take your coffee,Here is ${round(change,2)} dollars in change.")
                resources["water"]=resources["water"]-MENU["cappuccino"]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
            elif t==MENU["cappuccino"]["cost"]:
                print("Please take your coffee")
                resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
    def calc():
        q=int(input("quarters : $"))
        d=int(input("dimes : $"))
        n=int(input("nickles : $"))
        p=int(input("pennies : $"))
        total=q*quater+d*dime+n*nickle+p*penny
        return total

    coffee()
    if input("Order again ? press 'y' or 'n'")=="y":
        coffee()
    else:
        off=True