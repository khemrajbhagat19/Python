from datetime import datetime

def not_during_night(func):
    def inner():
        if 7<=datetime.now().hour<22:
            func()
        else:
            print("Sorry! unable to play music at night")
    return inner

@not_during_night
def music():
    print("Playing music")

music()