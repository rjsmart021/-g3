import text_utils as tu


def main():
    s = input("Enter String: ")
    reversed_string = tu.reverse_string(s)
    capitalized_string = tu.capitalize_text(s)

    print("Reversed String is: ", reversed_string)
    print("Capitalized String is: ", capitalized_string)


if __name__ == "__main__":
    main()
