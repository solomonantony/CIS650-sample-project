import pprint
def get_integer(prompt,low,high):
    while True:
        try:
            user_input = int(input(f'{prompt} {low}-{high}: '))
            if user_input >= low and user_input <= high:
                return user_input
            else:
                return None
        except ValueError:
            print(f"Enter an integer value in the range {low}-{high} ")


