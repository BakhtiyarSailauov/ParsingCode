import xlsxwriter

def data_entry(file_path, *parametrs):
    """
    Функция сохраняет данные из парсинга в Exsel файл

    Аргументы: 
              file_path(srting) - принимает от пользовотеля место для сохранение 
              *parametrs(List<>) - принимает в виде листа множества аргументов из парсинга
    Возвращает:
               null
    """
    try:
        book = xlsxwriter.Workbook(r"{}".format(file_path))
        page = book.add_worksheet("dates")

        row = 0
        column = 0

        page.set_column("A:A", 20)
        page.set_column("B:B", 20)
        page.set_column("C:C", 50)
        page.set_column("D:D", 50)

        for item in parametrs():
            page.write(row, column, item[0])
            page.write(row, column+1, item[1])
            page.write(row, column+2, item[2])
            page.write(row, column+3, item[3])
            row += 1

        book.close()
    except:
        book.close()