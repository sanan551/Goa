def tuple_info(t):
    print(f"Length of tuple: {len(t)}")
    if len(t) > 0:
        print(f"First element: {t[0]}")
        print(f"Last element: {t[-1]}")
    else:
        print("The tuple is empty.")


animals = ("dog", "cat", "bird", "elephant")
tuple_info(animals)
