print("initializing...")
from pynput.keyboard import Key, Listener, KeyCode
from car import Car

car = Car()

def main():

    print("ready...")
    print("use WASD or arrow keys to drive, press escape to cancel")

    with Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()

def on_press(key):
    #print '{0} pressed'.format(key)

    if key == KeyCode.from_char('w') or key == Key.up:
        car.forward()
    if key == KeyCode.from_char('s') or key == Key.down:
        car.backward()
    if key == KeyCode.from_char('a') or key == Key.left:
        car.left()
    if key == KeyCode.from_char('d') or key == Key.right:
        car.right()

def on_release(key):
    car.stop()

    if key == Key.esc:
        # Stop listener
        return False


if __name__=="__main__":
    main()
