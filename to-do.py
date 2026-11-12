tasks = []

while True:
    print("\n1 - Добавить задачу")
    print("2 - Показать задачи")
    print("3 - Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        task = input("Введите задачу: ")
        tasks.append(task)

    elif choice == "2":
        print("\nСписок задач:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

    elif choice == "3":
        break

    else:
        print("Неверный выбор")
