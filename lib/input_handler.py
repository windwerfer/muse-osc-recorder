# Collect events until released

import time

from lib.input_get_key_pressed import get_key_pressed
from lib.record_to_file import gracefully_end
from lib.record_to_file import close_and_zip_files
from lib.statistics import is_run_in_pycharm


def start_input(data):

    # user_input = input(" Exit: x (+Enter) | new rec: n | reset nod: n0 \n")
    # print(" \n to interact with the script press the Command + ENTER (sometimes needs 2 presses :-)")
    print("\n Commands: x = Exit | r = rec new file | 0 = reset ∞nod \n")

    time.sleep(3)       # needs to wait shortly (pycharm sends the input to record_to_file.py thread otherwise..)

    while True:

        if is_run_in_pycharm():
            user_input = input("\r ")           # this method works better in pycharm, the get_key_pressed() will receive ALL key events (the whole ide+windows is blocked)
        else:
            user_input = get_key_pressed()      # this method works in win + linux + termux (termux is the complicated one)


        if user_input == '0':
            data['stats']['moved_continuous'] = 0


        if user_input == 'x':
            gracefully_end(data)


        if user_input == 'r':
            if data['folder']['tmp'] == '':
                print('nothing is recorded right now. returning to normal programm')
            else:
                # print('not yet working.')
                close_and_zip_files(data)


        if user_input == 'n':
            data['stats']['pause'] = True
            note = input("\n enter the note to save and press Enter:")
            data['folder']['note'].append( f"{note}" )

            data['stats']['pause'] = False

        time.sleep(0.3)  # Add a small delay to reduce CPU usage

        # if user_input == '':
        #     print('no command entered.')

       # sys.stdout.write(f"\rYou typed: {user_input}                      \n")
       # sys.stdout.flush()
