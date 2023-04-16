
cup=int(input())
tablespoons=int(input())
teaspoons=int(input())
def convert(cup,tablespoons,teaspoons):
    cup=cup+teaspoons//48
    teaspoons=teaspoons%48
    tablespoons=tablespoons+teaspoons//3
    teaspoons=teaspoons%3
    cup=cup+tablespoons//16
    tablespoons=tablespoons%16
    print(cup,' ',tablespoons,' ',teaspoons)

convert(cup,tablespoons,teaspoons)
    