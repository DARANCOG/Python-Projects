serie = 'N-02'

'''if serie == 'N-01':
    print('samsumg')
elif serie == 'N-02':
    print('nokia')
elif serie == 'N-03':
    print('motorola')
else:
    print('No existe ese producto')'''

match serie:
    case "N-01":
        print("samsung")
    case "N-02":
        print("nokia")
    case "N-03":
        print("motorola")
    case _:
        print("no existe producto")