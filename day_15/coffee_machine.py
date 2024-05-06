menu ={
    "espresso":{
     "ingredients": {  
        "water":50,
        "coffee":18,
            },
            "cost": 1.5,
    },
    "latte": {
        "ingridients":{
            "water": 200,
            "milk":150,
            "coffee": 24,
        },
        "cost":2.5
    },
    "cappuccino":{
        "ingridients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
    "cost":3.0,
    },
}
profit =0
resource = {
    "water": 300,
    "milk": 200,
    "coffee":100,
}

def process_coins():
    print("please insert coins. ")
    total = (int(input("how many quarters?: ")) *25)
    total += (int(input("how many di?: "))*10)
    total += (int(input("how many quarters?: "))*5)
    total += (int(input("how many quarters?: "))*1)
    return total

def is_resource_sufficient(order_ingridients):
    for item in order_ingridients:
      if  (order_ingridients[item]) >= (resource[item]):
         print(f"Sorry there is not enough {item}")
         return False
    return True

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = (money_received-drink_cost)
        print(f"Here is this many ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
def make_coffee(drink_name, order_ingridient):
    for item in order_ingridient:
        resource[item]-=order_ingridient[item]    
    print(f"Here is your {drink_name} , Enjoy .")
is_on=True
while is_on:
 choice=input("what do you want (cappuccino\latte\espresso):  ")
 if choice == "off":
    is_on=False
 elif choice == "report":
    print(f"water:{resource[ 'water']}ml")
    print(f"milk: {resource['milk']}ml")
    print(f"coffee{resource['coffee']}ml" )
    print(f"money:{profit}")
 else:
    drink=menu[choice]
    if is_resource_sufficient((drink["ingridients"])):
        payment= process_coins()
        if is_transaction_successful( payment,drink["cost"]):
           make_coffee(choice,(drink["ingridients"]))
