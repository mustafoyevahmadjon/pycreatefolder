import os

def create_folder_and_files():
    # Papka nomini foydalanuvchidan so'raymiz
    folder_name = input("Papka nomini kiriting: ")

    # Fayl sonini so'raymiz
    num_files = int(input("Nechta fayl ochishni xohlaysiz? "))

    # Fayl nomlari uchun prefiksni so'raymiz
    file_prefix = input("Fayl nomlari uchun prefiksni kiriting (masalan, 'begin'): ")

    # Fayl kengaytmasini so'raymiz (masalan, .py, .txt)
    file_extension = input("Fayl kengaytmasini kiriting (masalan, 'py', 'txt'): ")
    
    # Fayl kengaytmasini "." bilan to'ldiramiz, agar kerak bo'lsa
    if not file_extension.startswith('.'):
        file_extension = f".{file_extension}"

    # Papkani yaratamiz, agar mavjud bo'lmasa
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"{folder_name} papkasi yaratildi.")
    else:
        print(f"{folder_name} papkasi allaqachon mavjud.")
    
    # Fayl nomlarini avtomatik ravishda yaratamiz va fayllarni ochamiz
    for i in range(1, num_files + 1):
        file_name = f"{file_prefix}{i}{file_extension}"  # Kiritilgan kengaytmani ishlatamiz
        file_path = os.path.join(folder_name, file_name)
        with open(file_path, 'w') as file:
            file.write("")  # Bo'sh fayl yaratish
        print(f"{file_name} fayli yaratildi.")

# Foydalanish:
create_folder_and_files()
