class Client:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Имя: {self.name}, Телефон: {self.phone}, Email: {self.email}"


class ClientManager:
    def __init__(self):
        self.clients = []

    def add_client(self, client):
        self.clients.append(client)
        print(f"Клиент {client.name} добавлен.")

    def list_clients(self):
        if not self.clients:
            print("Нет записанных клиентов.")
            return
        for i, client in enumerate(self.clients, start=1):
            print(f"{i}. {client}")

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for client in self.clients:
                f.write(f"{client.name},{client.phone},{client.email}\n")
        print(f"Данные сохранены в {filename}.")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                for line in f:
                    name, phone, email = line.strip().split(',')
                    self.add_client(Client(name, phone, email))
            print(f"Данные загружены из {filename}.")
        except FileNotFoundError:
            print(f"Файл {filename} не найден.")


def main():
    manager = ClientManager()

    while True:
        print("\n1. Добавить клиента")
        print("2. Показать всех клиентов")
        print("3. Сохранить клиентов в файл")
        print("4. Загрузить клиентов из файла")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            name = input("Введите имя клиента: ")
            phone = input("Введите телефон клиента: ")
            email = input("Введите email клиента: ")
            client = Client(name, phone, email)
            manager.add_client(client)

        elif choice == '2':
            manager.list_clients()

        elif choice == '3':
            filename = input("Введите имя файла для сохранения: ")
            manager.save_to_file(filename)

        elif choice == '4':
            filename = input("Введите имя файла для загрузки: ")
            manager.load_from_file(filename)

        elif choice == '5':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()
