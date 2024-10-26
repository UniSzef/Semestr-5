with open('text.txt', 'r', encoding='utf-8') as input_file:
    line_count = 0
    dog_counter = 0
    for line in input_file.readlines():
        line_count += 1
        # Task 2: Check for the presence of the word "pies"
        if "pies" in line.lower():
            dog_counter += 1
        # Task 1: Display every 3rd line
        if line_count % 3 == 0:
            print(line.capitalize())  # lub linia.capitalize() w zależności od potrzeby
    print(f"Liczba linii zawierających słowo 'pies': {dog_counter}")

# Task 3: Print sentences ending with a period
with open('text.txt', 'r', encoding='utf-8') as input_file:
    print("\n\nZadanie 3\n\n")
    text = input_file.read().replace('\n', ' ')
    sentences = text.split('.')
    for sentence in sentences:
        s = sentence.strip()
        if len(s) > 0:
            print(s + ".")

print("\n\nZadanie 4\n\n")
with open('text.txt', 'r', encoding='utf-8') as input_file:
    lines = input_file.readlines()
if len(lines) >= 2:
    list_4 = [word.capitalize() for word in lines[1].split() if word.isalpha()]
    with open("result.txt", "w", encoding="utf-8") as output_file:
        for word in list_4:
            output_file.write(word + "\n")
    with open("result.txt", "r", encoding="utf-8") as output_file:
        print(output_file.read())
else:
    print("Plik nie zawiera drugiej linii.")

print("\n\nZadanie 5\n\n")
with open('text.txt', 'r', encoding='utf-8') as input_file:
    lines = input_file.readlines()
    list_5 = [word for line in lines for word in line.split() if word.isdigit()]
print(", ".join(list_5))
