# TODO Найдите количество книг, которое можно разместить на дискете

disk_volume = 1.44 #Объем диска в Мб
num_pages = 100
lines = 50
symbols = 25
weight_symbol = 4 #Вес страницы в б

weight_book = (weight_symbol * symbols * lines * num_pages / 1024 ** 2)

num_books = (round(disk_volume // weight_book))

print("Количество книг, помещающихся на дискету:", num_books)
