def dummy_function(arg1, arg2, arg3, kwarg1=None, kwarg2=True):
    """
    A dummy function for testing Sphinx documentation.

    Parameters:
    arg1 (int): The first argument, an integer value.
    arg2 (str): The second argument, a string value.
    arg3 (list): The third argument, a list of items.
    kwarg1 (float, optional): An optional keyword argument, a float value. Defaults to None.
    kwarg2 (bool, optional): An optional keyword argument, a boolean value. Defaults to True.

    Returns:
    dict: A dictionary containing the input arguments for demonstration purposes.
    """
    return {
        "arg1": arg1,
        "arg2": arg2,
        "arg3": arg3,
        "kwarg1": kwarg1,
        "kwarg2": kwarg2,
    }
