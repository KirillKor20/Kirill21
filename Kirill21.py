def test_function():
    print('Я работаю')
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()


test_function()