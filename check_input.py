class check_input:

    @staticmethod
    def number(text_to_user: str):
        print(text_to_user)
        while True:
            try:
                input_number = input()

                if input_number.capitalize() == "Q":
                    print("Programm beenden...")
                    exit()

                input_number = float(input_number)

                if input_number <= 0:
                    raise FutureWarning

                return input_number

            except FutureWarning:
                print("The number has to be above zero.")

            except ValueError:
                print("Please enter a number above zero.")

    @staticmethod
    def letter(text_to_user: str, allowed_letters: str, capitalize: bool):
        print(text_to_user)
        while True:
            valid = False
            try:
                output_text = input()

                if output_text.capitalize() == "Q":
                    print("Programm beenden...")
                    exit()

                if capitalize:
                    output_text = output_text.capitalize()

                for i in allowed_letters:
                    if i == output_text:
                        valid = True
                        return output_text

                if not valid:
                    raise FutureWarning

            except FutureWarning:
                print("Please enter valid character.")
