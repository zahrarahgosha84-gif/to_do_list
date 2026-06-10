import csv


# ------------------------
#   کلاس Task
# ------------------------
class Task:
    def __init__(self, name, tozih, olaviat):
        self.name = name
        self.tozih = tozih
        self.olaviat = olaviat

    def __str__(self):
        return f"{self.name} - {self.tozih} - اولویت: {self.olaviat}"


# ------------------------
#   کلاس To_Do_list
# ------------------------
class To_Do_list:
    def __init__(self):
        self.tasks = []

    def add_new(self, task):
        self.tasks.append(task)

    def remove(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task)
                print("کار حذف شد.")
                return
        print("کار پیدا نشد.")

    def show(self):
        if not self.tasks:
            print("هیچ کاری وجود ندارد.")
        for task in self.tasks:
            print(task)

    def save_csv(self, filename):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for task in self.tasks:
                writer.writerow([task.name, task.tozih, task.olaviat])
        print("فایل ذخیره شد.")

    def load_from_csv(self, filename):
        self.tasks = []
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                name, tozih, olaviat = row
                task = Task(name, tozih, olaviat)
                self.tasks.append(task)

    def sort_by_priority(self):
        olaviat_order = {"high": 1, "medium": 2, "low": 3}
        self.tasks.sort(key=lambda task: olaviat_order[task.olaviat])



todo = To_Do_list()

while True:
    print("\n1. افزودن کار جدید")
    print("2. مشاهده کارها")
    print("3. حذف کار")
    print("4. ذخیره در فایل و خروج")

    choice = input("انتخاب کنید: ")

    if choice == "1":
        name = input("نام کار: ")
        tozih = input("توضیح: ")
        olaviat = input("اولویت (high/medium/low): ")
        task = Task(name, tozih, olaviat)
        todo.add_new(task)

    elif choice == "2":
        todo.show()

    elif choice == "3":
        name = input("نام کار برای حذف: ")
        todo.remove(name)

    elif choice == "4":
        todo.sort_by_priority()
        todo.save_csv("tasks.csv")
        print("خروج...")
        break