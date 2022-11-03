import os.path

class Employees:

    __employees = list()
    __file = "employees.txt"

    def to_int(self, value):
        return int(value) if int(value) == value else value

    def load(self):
        if not os.path.isfile(self.__file):
            f = open(self.__file,"w")
            f.close()
            self.__employees.clear()
            return

        self.__employees.clear()
        with open(self.__file, "rt") as file:
            for line in file:
                self.__employees.append(line.split("%"))
                self.__employees[-1][1] = float(self.__employees[-1][1])
    
    def save(self):
        with open(self.__file, "wt") as file:
            for item in self.__employees:
                file.write(item[0] + "%" + str(item[1]) + "\n")
    
    def edit(self, name : str, value : float) -> bool:
        for item in self.__employees:
            if item[0] == name:
                item[1] = value
                self.save()
                return 1
        return 0
    
    def add(self, name : str, value : float) -> bool:
        for item in self.__employees:
            if item[0] == name:
                return 0
        self.__employees.append([name, value])
        self.save()
        return 1
    
    def remove(self, name : str) -> bool:
        for item in self.__employees:
            if item[0] == name:
                self.__employees.remove(item)
                self.save()
                return 1
        return 0
    
    def sum(self) -> float:
        result = 0.0
        for item in self.__employees:
            result += item[1]
        return self.to_int(result)
    
    def view(self):
        print("Name                     |Salary")
        print("-------------------------|------")

        for item in self.__employees:
            print(item[0],end="")
            print(" " * (25 - len(item[0])),end="")
            print("|",end="")
            print(self.to_int(item[1]))
        
        print("--------------------------------")



def main():

    employees = Employees()
    employees.load()

    while 1:

        print("--- Employee Manager ---\n")
        print("1) Add Employee")
        print("2) Edit Salary")
        print("3) Remove Employee")
        print("4) Total Expenses")
        print("5) View List")
        print("6) Exit\n")

        choice = input("Your choice: ")

        if choice == "1":
            name = input("Name: ")

            if len(name) > 25:
                print("Name length can not be more than 25 characters.")
                continue
            if len(name) == 0:
                print("Name length should be at least 1 character.")
                continue

            salary = float(input("Salary: "))
            print("Added successfully!" if employees.add(name, salary) else "Employee already exists.")
            continue

        if choice == "2":
            name = input("Name: ")
            salary = float(input("New Salary: "))
            print("Edited successfully!" if employees.edit(name, salary) else "Employee does not exist.")
            continue
        
        if choice == "3":
            name = input("Name: ")
            print("Removed successfully!" if employees.remove(name) else "Employee does not even exist.")
            continue
        
        if choice == "4":
            print(f"Total money we should pay for employees` salary: {employees.sum()}")
            continue
        
        if choice == "5":
            employees.view()
            continue

        if choice == "6":
            break

        print("Wrong choice.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Exception caught: {e}")