import os, datetime, re

frapses_path = "FRAPS PATH HERE"


def main():
    frapses = os.listdir(frapses_path)
    old_fraps = datetime.datetime.now() - datetime.timedelta(5)
    data = get_data(frapses)
    
    clear_memory = 0
    clear_items = 0
        
    for fraps, date in data.items():
        dt_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        
        if dt_date < old_fraps:
            
            try:
            
                stats = os.stat(frapses_path + "\\" + fraps)
                os.remove(frapses_path + "\\" + fraps)
                
                clear_memory += stats.st_size / 1073741824
                clear_items += 1
            
            except PermissionError:
                print(f"Нельзя удалить файл \"{fraps}\" так как он занят другой программой!")
                continue
                
    if clear_memory and clear_items:
        print(f"Очистка прошла успешно!\nОчищено памяти: {round(clear_memory, 1)}GB\nУдалено файлов: {clear_items}")
    else:
        print("Файлов для удаления не нашлось!")
    input("Закрыть? ")
    
    
def get_data(frapses):
    data = {}
    for fraps in frapses:
        try:
            match = re.search(r"\d{4}-\d{1,2}-\d{1,2}", fraps)
            data[fraps] = match.group(0)
        except AttributeError:
            continue
        
    return data


main()
