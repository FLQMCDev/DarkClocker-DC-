import time
import threading
import os
import platform

class AutoClicker:
    def __init__(self):
        self.running = False

    def auto_click(self, interval, button, clicks):
        self.running = True
        print(f"\nAuto-clicking every {interval} seconds with {button} button for {clicks} times.\n")
        for i in range(clicks):
            if not self.running:
                break
            pyautogui.click(button=button)
            print(f"Click {i + 1}/{clicks}")
            time.sleep(interval)
        print("\nDone!")
        print("\nProject by FLQMZECLIENT, I have been working on this project for 3 months.\n")
        self.running = False

    def start_clicking(self, interval, button, clicks):
        if not self.running:
            click_thread = threading.Thread(target=self.auto_click, args=(interval, button, clicks))
            click_thread.start()
        else:
            print("Auto-clicker is already running.")

    def stop_clicking(self):
        if self.running:
            self.running = False
            print("\nAuto-clicker stopped.")
        else:
            print("Auto-clicker is not running.")

    def is_admin(self):
        if platform.system() == 'Windows':
            try:
                return os.getuid() == 0
            except AttributeError:
                import ctypes
                return ctypes.windll.shell32.IsUserAnAdmin() != 0
        else:
            return os.getuid() == 0

if __name__ == "__main__":
    def main():
        auto_clicker = AutoClicker()

        print("Welcome to Darkling Clicker\n")

        # Check if running with administrative privileges
        if not auto_clicker.is_admin():
            print("Warning: Darkling Clicker may not function correctly without admin rights on this platform.")

        interval = None
        button = None
        clicks = None

        while interval is None:
            try:
                interval = float(input("Enter click interval (in seconds): "))
                if interval <= 0:
                    print("Interval must be greater than 0.")
                    interval = None
            except ValueError:
                print("Please enter a valid number.")

        while button not in ["left", "right", "middle"]:
            button = input("Enter button to click (left, right, middle): ").lower()
            if button not in ["left", "right", "middle"]:
                print("Please enter 'left', 'right', or 'middle'.")

        while clicks is None:
            try:
                clicks = int(input("Enter number of clicks: "))
                if clicks <= 0:
                    print("Number of clicks must be greater than 0.")
                    clicks = None
            except ValueError:
                print("Please enter a valid integer.")

        while True:
            command = input("Enter 'start' to start clicking or 'stop' to stop: ").strip().lower()
            if command == 'start':
                auto_clicker.start_clicking(interval, button, clicks)
            elif command == 'stop':
                auto_clicker.stop_clicking()
                break
            else:
                print("Invalid command. Please enter 'start' or 'stop'.")

    main()
