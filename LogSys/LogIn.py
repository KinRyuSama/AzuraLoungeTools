import datetime
import os

class ClockSystem:
    def __init__(self):
        self.employees = {}

    def clock_in(self, name):
        if name in self.employees:
            print("You are already clocked in.")
            return
        self.employees[name] = []
        self.log_event(name, "Clock-in", datetime.datetime.now())
        print(f"{name} clocked in at {datetime.datetime.now()}")

    def clock_out(self, name):
        if name not in self.employees:
            print("You are not clocked in.")
            return
        if not self.employees[name]:
            print("You are not clocked in.")
            return
        self.log_event(name, "Clock-out", datetime.datetime.now())
        print(f"{name} clocked out at {datetime.datetime.now()}")

    def log_event(self, name, event, time):
        filename = f"{name}.txt"
        with open(filename, "a") as f:
            f.write(f"{event} at {time}\n")
        self.employees[name].append((event, time))

    def view_log(self, name=None):
        if name:
            filename = f"{name}.txt"
            if os.path.exists(filename):
                with open(filename, "r") as f:
                    print(f"Clock log for {name}:")
                    print(f.read())
            else:
                print("Employee not found.")
        else:
            print("Clock log for all employees:")
            for filename in os.listdir():
                if filename.endswith(".txt"):
                    with open(filename, "r") as f:
                        print(f.read())

def main():
    clock_system = ClockSystem()
    while True:
        print("\n1. Clock in")
        print("2. Clock out")
        print("3. View log")
        print("4. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Enter your name: ")
            clock_system.clock_in(name)
        elif choice == "2":
            name = input("Enter your name: ")
            clock_system.clock_out(name)
        elif choice == "3":
            name = input("Enter your name (leave blank for all employees): ")
            if name.strip() == "":
                clock_system.view_log()
            else:
                clock_system.view_log(name)
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
