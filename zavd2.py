def create_text_file():
    text = """This    is   an example    of  a  text   file  with    extra spaces."""
    with open("text_input.txt", "w", encoding="utf-8") as file:
        file.write(text)
    print("Файл text_input.txt створено з тестовим текстом.")
def remove_extra_spaces():
    with open("text_input.txt", "r", encoding="utf-8") as file:
        content = file.read()
    
    cleaned_content = ' '.join(content.split())  
    
    with open("text_output.txt", "w", encoding="utf-8") as file:
        file.write(cleaned_content)
    print("Очищений текст збережено у файл text_output.txt.")

    print("\nОригінальний текст:")
    print(content)
    print("\nОчищений текст:")
    print(cleaned_content)

if __name__ == "__main__":

    create_text_file()
    remove_extra_spaces()
