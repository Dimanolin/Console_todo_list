# todo.py
#Изменение

import sqlite3

conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

def init_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            priority TEXT,
            completed BOOLEAN NOT NULL CHECK (completed IN (0, 1))
        )
    ''')
    conn.commit()

def add_task():
    task_name = input("Введите задачу: ")
    priority = input("Введите приоритет (высокий/средний/низкий): ").lower()
    cursor.execute("INSERT INTO tasks (name, priority, completed) VALUES (?, ?, ?)",
                   (task_name, priority, 0))
    conn.commit()
    print("Задача добавлена!")

def show_tasks():
    cursor.execute("SELECT id, name, priority, completed FROM tasks")
    tasks = cursor.fetchall()
    if tasks:
        print("\nСписок задач:")
        for task in tasks:
            status = "Выполнена" if task[3] else "Не выполнена"
            print(f"{task[0]}. {task[1]}(Приоритет: {task[2]}, Статус: {status})")
    else:
        print("Список задач пуст.")

def delete_task():
    show_tasks()
    task_id = input("Введите ID задачи для удаления: ")
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    print("Задача удалена!")

def mark_status_completed():
    show_tasks()
    task_id = input("Введите ID задачи для отметки как выполненной: ")
    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    print("Задача отмечена как выполненная")

def main():
    init_db()
    while True:
        print("\n1. Добавить задачу")
        print("2. Показать все задачи")
        print("3. Удалить задачу")
        print("4. Отметить задачу как выполненную")
        print("5. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            mark_status_completed()
        elif choice == "5":
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите 1, 2 или 3.")

if __name__ == "__main__":
    main()

conn.close()