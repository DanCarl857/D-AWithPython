def fibonacci():
    a = 0
    b = 1
    while True:
        yield a

        # yes I know we can just have a, b = b, a+b :-)
        future = a + b
        a = b
        b = future