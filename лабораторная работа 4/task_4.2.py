# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # TODO считать содержимое csv файла
    data = []
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    # TODO Сериализовать в файл с отступами равными 4
    json_string = json.dumps(data, indent=4)
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as outfile:
        outfile.write(json_string)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
