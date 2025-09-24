def fun(*args, **kwargs):
    # print(*args)
    # print(**kwargs)
    for key, value in kwargs.items():
        print(f'{value}: {key}')
    for arg in args:
        print(arg)
fun("COP3502C", "Prog 1", lab="Cows", lab2="Cows2")