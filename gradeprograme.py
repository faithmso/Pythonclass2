def score():
    try:
        score = float(input("Enter a grade between 0.0 and 1.0: "))

        if score > 1.0:
            print(f"Score is out of range")

        elif score >= 0.9:
            print(f"Your scored an A")

        elif score >= 0.8:
            print(f"You scored a B")

        elif score >= 0.7:
            print(f"You scored a C")

        elif score >= 0.6:
            print(f"You scored a D")

        else:
            print(f"You scored an E")

    except ValueError:
        print("Enter a valid integer or float")

        
score()