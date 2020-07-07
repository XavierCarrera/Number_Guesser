import random

def run(): 
    random_num = random.randint(1, 100)
    user_num = int(input("Choose a number between 1 and 100: "))
    while user_num != random_num:
        if user_num < random_num:
            print("Choose a higher number")
        else:
            print("Choose a lower number")
        user_num = int(input("Choose another number: "))
    print("You win!")

if __name__ == '__main__':
    run()