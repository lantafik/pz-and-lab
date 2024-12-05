#Задание 3
import wikipedia

# Устанавливаем пользовательский агент для взаимодействия с Википедией.
def set_user_agent():
    wikipedia.set_user_agent("my_wikipedia_searcher/1.0 (your_email@example.com)")

# Отображение параграфов статьи.
def display_paragraphs(page):
    paragraphs = page.content.split("\n\n")
    for i, paragraph in enumerate(paragraphs):  # Печатаем первые 200 символов каждого параграфа.
        print(f"{i + 1}. {paragraph[:200]}...")

#Запрашивает у пользователя название связанной страницы.
def search_related_page():
    related_query = input("Введите название связанной страницы: ")
    return related_query

#Получаем статью по запросу пользователя
def get_article(query):
    try:
        page = wikipedia.page(query)
        return page
    except wikipedia.exceptions.DisambiguationError as e:
        print("Найдено несколько вариантов, выберите один из них:")
        for i, option in enumerate(e.options[:3]):  # Предлагаем три наиболее подходящих варианта.
            print(f"{i + 1}. {option}")
        query = input("Введите новый запрос: ")
        return get_article(query)  # Рекурсивный вызов функции с новым запросом.
    except Exception as e:
        print(f"Ошибка: {e}")
        return None


def main():
    set_user_agent()  # Устанавливаем пользовательский агент

    wikipedia.set_lang("ru")  # Устанавливаем язык Википедии на русский.

    query = input("Введите запрос для поиска на Википедии: ")  # Запрашиваем запрос у пользователя.

    while True:
        page = get_article(query)  # Получаем статью по запросу.

        if page:
            print(f"\nСтатья: {page.title}\n\n{page.content[:1000]}...\n")  # Выводим заголовок и начало статьи.

            while True:
                # Запрашиваем у пользователя, что он хочет делать с найденной статьей.
                action = input("Выберите действие:\n1. Листать параграфы\n2. Перейти на связанную страницу\n3. Выйти\n")

                if action == "1":  # Листать параграфы
                    display_paragraphs(page)  # Показываем параграфы статьи.
                    input("Нажмите Enter для продолжения...")  # Ждем от пользователя продолжения.

                elif action == "2":  # Переход на связанную страницу
                    query = search_related_page()  # Получаем название связанной страницы.
                    break  # Переходим к следующей итерации с новым запросом.

                elif action == "3":  # Выходим из программы
                    print("Выход из программы.")
                    return

                else:
                    print("Неверный выбор, попробуйте еще раз.")

        else:
            print("Не удалось найти статью. Попробуйте снова.")
            query = input("Введите новый запрос: ")  # Запрашиваем новый запрос.


if __name__ == "__main__":
    main()  # Запускаем программу.
