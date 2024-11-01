# todo.py

tasks = []

def add_task():
    task = input("Введите задачу: ")
    tasks.append(task)
    print("Задача добавлена!")

def show_tasks():
    if tasks:
        print("\nСписок задач:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")
    else:
        print("Список задач пуст.")

def delete_task(deleted_task):
    if tasks:
        if deleted_task <= len(tasks):
            print(f"Задача {tasks[deleted_task - 1]} удалена!")
            tasks.pop(deleted_task - 1)
        else:
            print("Такого индекса в базе ещё нет.")
    else: 
        print("В списке нет задач. Удалять нечего.")

    

def main():
    while True:
        print("\n1. Добавить задачу")
        print("2. Показать все задачи")
        print("3. Удалить задачу")
        print("4. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            deleted_task = int(input("Введите индекс задачи, которую нужно удалить: "))
            delete_task(deleted_task)
        elif choice == "4":
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите 1, 2 или 3.")

if __name__ == "__main__":
    main()
