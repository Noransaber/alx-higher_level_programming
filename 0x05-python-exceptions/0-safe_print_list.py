def safe_print_list(my_list=[], x=0):

    """Write a function that prints x elements of a list"""
    try:
        counter = 0
        for ele in my_list:
            counter += 1
        if isinstance(x, int) and x <= counter:
            for i in range(x):
                print(my_list[i], end="")
            return x
    except IndexError:
        pass
    finally:
        print()
        return counter
