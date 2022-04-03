
import random
import signal
import sys
import time

from pynput.keyboard import Controller, Key, Listener, KeyCode

# global vars
generate_random_num = False
stop_program = False
keyboard = Controller()

def main():
    beg, end, delay = verify_args()
    listener = Listener(on_release=on_release)
    listener.start()

    # main loop
    while not stop_program:
        if generate_random_num == True:
            press_num(str(random.randint(beg, end)))
            time.sleep(delay)

# press passed number key
def press_num(num):
    keyboard.press(num)
    keyboard.release(num)

# handle keyboard release
def on_release(key):
    # toggle key
    if key == Key.f10:
        global generate_random_num
        generate_random_num = not generate_random_num
        print(f"randomize state: {generate_random_num}")
    # exit
    if key == Key.esc:
        print("exiting program!")
        global stop_program
        stop_program = True

# verify that args are valid parameters
def verify_args():

    # verify args length
    if len(sys.argv) not in range(3,5):
        print("Invalid syntax!")
        print("Run via: python .\\BlockRandomizer.py start_slot end_slot")
        sys.exit(1)

    default_delay = .1
    if len(sys.argv) == 4:
        default_delay = sys.argv[3]

    # check that 1 <= start_slot < 10
    if int(sys.argv[1]) in range(1,10):
        # check that start_slot+1 < end_slot < 10
        if int(sys.argv[2]) in range(int(sys.argv[1])+1, 10):
            return int(sys.argv[1]), int(sys.argv[2]), int(default_delay)
        else:
            sys.exit(f"Invalid end_slot: start_slot < {sys.argv[2]} < 10")

    else:
        sys.exit(f"Invalid start_slot: 1 <= start_slot < 10")

if __name__ == "__main__":
    main()