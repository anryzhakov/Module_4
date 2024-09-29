# Слушатель курса Junior Python-разработчик
# Рыжаков Андрей Николаевич, anryzhakov@yandex.ru
# Домашняя работа по уроку "Пространство имен."

def test_function():
    def inner_function(s):
        print(s)

    s = str('Я в области видимости функции test_function')
    inner_function(s)

#inner_function()
test_function()