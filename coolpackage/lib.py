from termcolor import colored

def try_me(your_name, your_age):
    print(f'Today is your lucky day {your_name}!!!!!!!!!!')
    for i in range(1,int(your_age)+1):
        print(colored(f'Try to high-five with {i} people for more luck','yellow'))

    return your_name, your_age
