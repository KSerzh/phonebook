import tkinter as tk
from tkinter import messagebox

class PhonebookApp:
    def __init__(self):
        self.phone_book = []
        self.root = tk.Tk()
        self.load_from_txt()  # Загружаем данные из файла при запуске

        self.root = tk.Tk()
        self.root.title("Телефонный справочник")

        # Фамилия
        self.label_last_name = tk.Label(self.root, text="Фамилия:")
        self.label_last_name.pack()
        self.entry_last_name = tk.Entry(self.root)
        self.entry_last_name.pack()

        # Имя
        self.label_first_name = tk.Label(self.root, text="Имя:")
        self.label_first_name.pack()
        self.entry_first_name = tk.Entry(self.root)
        self.entry_first_name.pack()

        # Телефон
        self.label_phone_number = tk.Label(self.root, text="Телефон:")
        self.label_phone_number.pack()
        self.entry_phone_number = tk.Entry(self.root)
        self.entry_phone_number.pack()

        # Описание
        self.label_description = tk.Label(self.root, text="Описание:")
        self.label_description.pack()
        self.entry_description = tk.Entry(self.root)
        self.entry_description.pack()

        # Кнопки
        self.button_add = tk.Button(self.root, text="Добавить", command=self.add_contact)
        self.button_add.pack()
        self.button_delete = tk.Button(self.root, text="Удалить", command=self.delete_contact)
        self.button_delete.pack()
        self.button_modify = tk.Button(self.root, text="Изменить", command=self.modify_contact)
        self.button_modify.pack()
        self.button_search = tk.Button(self.root, text="Найти", command=self.search_contact)
        self.button_search.pack()

        # Список контактов
        self.listbox = tk.Listbox(self.root, height=1)
        self.listbox.pack()

        self.root.mainloop()

    def load_from_txt(self):
        try:
            with open("справочник.txt", "r", encoding="utf-8") as file:
                for line in file:
                    self.phone_book.append(line.strip())
        except FileNotFoundError:
            print("Файл справочника не найден. Создайте его перед добавлением контактов.")    

    def add_contact(self):
        last_name = self.entry_last_name.get()
        first_name = self.entry_first_name.get()
        phone_number = self.entry_phone_number.get()
        description = self.entry_description.get()
        if last_name and first_name and phone_number:
            contact = f"{last_name}, {first_name}, {phone_number}, {description}"
            self.phone_book.append(contact)
            self.listbox.insert(tk.END, contact)
            self.save_to_txt()
            messagebox.showinfo("Успех", "Контакт успешно добавлен!")
        else:
            messagebox.showerror("Ошибка", "Введите данные!")

    def delete_contact(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            self.listbox.delete(selected_index)
            del self.phone_book[selected_index[0]]
            self.save_to_txt()
            messagebox.showinfo("Успех", "Контакт успешно удален!")
        else:
            messagebox.showerror("Ошибка", "Выберите контакт для удаления!")

    def modify_contact(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            last_name = self.entry_last_name.get()
            first_name = self.entry_first_name.get()
            phone_number = self.entry_phone_number.get()
            description = self.entry_description.get()
            if last_name and first_name and phone_number:
                contact = f"{last_name}, {first_name}, {phone_number}, {description}"
                self.phone_book[selected_index[0]] = contact
                self.listbox.delete(selected_index)
                self.listbox.insert(selected_index, contact)
                self.save_to_txt()
                messagebox.showinfo("Успех", "Контакт успешно изменен!")
            else:
                messagebox.showerror("Ошибка", "Введите данные!")
        else:
            messagebox.showerror("Ошибка", "Выберите контакт для изменения!")

    # def search_contact(self):
    #     query = self.entry_last_name.get()
    #     found_contacts = []
    #     for contact in self.phone_book:
    #         if query.lower() in contact.lower():
    #          found_contacts.append(contact)

    #      # Очищаем список контактов в окне
    #     self.listbox.delete(0, tk.END)

    #      # Вставляем найденные контакты
    #     for contact in found_contacts:
    #          self.listbox.insert(tk.END, contact)
    def search_contact(self):
        query = self.entry_last_name.get().lower()  # Получаем запрос и приводим к нижнему регистру
        found_contacts = []
        for contact in self.phone_book:
            if query in contact.lower():  # Поиск по всем полям, игнорируя регистр
                 found_contacts.append(contact)

         # Очищаем список контактов в окне
        self.listbox.delete(0, tk.END)

         # Вставляем найденные контакты, отсортированные по алфавиту
        for contact in sorted(found_contacts):
             self.listbox.insert(tk.END, contact)


    def save_to_txt(self):
        with open("справочник.txt", "w", encoding="utf-8") as file:
            for contact in self.phone_book:
                file.write(f"{contact}\n")

if __name__ == "__main__":
    app = PhonebookApp()