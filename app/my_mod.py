def enlarge(n):
    """ This is a docstring.
    This function enlarges a number.
    Pass in n as a parameter.
    Returns a larger version of the number.
    """
    return float(n) * 100



if __name__ == "__main__":


    x = input("Please input a number: ")
    result = enlarge(x)
    print(result)