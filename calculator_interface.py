# ---------------
# Imports
# ---------------

from JMath import JMath
from check_input import check_input

# ----------------
# User Interface
# ----------------

print("========   \\\      //       //\\\   ==========   ||    ||")
print("      ||   ||\\\  //||      //  \\\      ||       ||    ||")
print("      ||   || \\\// ||    =======\\\     ||       ======||")
print("      //   ||      ||    //      \\\    ||       ||    ||")
print("\\\===//    ||      ||   //        \\\   ||       ||    ||")
print("     -      S h a p e   C a l c u l a t o r      -\n\n")

saved_letter = check_input.letter(
    "What shape are you working with?\nTrapeze <T> | Parallelogram <P> | Triangle <I> | Rectangle <R>", "TPIR", True)

if saved_letter == "T":
    saved_letter = check_input.letter(
        "What do you want to calculate about the Trapeze?\nSurface Area <S> | Middle line <M> | Height <H>", "SMH",
        True)

    if saved_letter == "S":
        print("The trapeze has a surface area of: " + str(
            JMath.trapeze.surface(check_input.number("Please enter the length of the middle line."),
                                  JMath.trapeze.middle_line(
                                      check_input.number("Please enter the length of the upper line."),
                                      check_input.number("Please enter the length of the lower line.")))))

    elif saved_letter == "M":
        saved_letter = check_input.letter(
            "From what values do you want to calculate the middle line?\nUpper and lower lines <U> | Surface area and height <S>",
            "US", True)

        if saved_letter == "U":
            print("The length of the middle line is: " + str(
                JMath.trapeze.middle_line(check_input.number("Please enter the length of the first line."),
                                          check_input.number("Please enter the length of the second line."))))

        elif saved_letter == "S":
            print("The length of the middle line is: " + str(JMath.trapez.middle_line(check_input.number(
                "Please enter the length of the upper line."),
                check_input.number("Please enter the length of the lower line."))))

    elif saved_letter == "H":
        print("The height is: " + str(JMath.trapeze.height_or_middle_line(check_input.number(
            "Please enter the length of the upper line."),
            check_input.number("Please enter the length of the lower line."))))


elif saved_letter == "P":
    saved_letter = check_input.letter(
        "What do you want to calculate about the parallelogram?\nSurface area <S> | Height <H> | Base line <B>", "SHB",
        True)

    if saved_letter == "S":
        print("The surface area is: " + str(
            JMath.parallelogram.surface(check_input.number("Please enter the length of the base line."),
                                        check_input.number("Please enter height."))))
    if saved_letter == "H":
        print("The height is: " + str(
            JMath.parallelogram.height_or_base_line(check_input.number("Please enter the length of the base line."),
                                                    check_input.number("Please enter the surface area."))))

    if saved_letter == "B":
        print("The length of the base line is: " + str(
            JMath.parallelogram.height_or_base_line(check_input.number("Please enter the height"),
                                                    check_input.number("Please enter the surface area."))))

elif saved_letter == "I":
    saved_letter = check_input.letter(
        "What do you want to calculate about the triangle?\nSurface area <S> | Height <H> | Base line length <B>",
        "SHB", True)

    if saved_letter == "S":
        print("The triangle has a surface of: " + str(JMath.triangle.surface(check_input.number(
            "Please enter the length of the base line."), check_input.number("Please enter the height."))))

    elif saved_letter == "H":
        print("The triangle has a height of: " + str(JMath.triangle.height_or_base_line(check_input.number(
            "Please enter the length of the base line."), check_input.number("Please enter the surface area."))))

    elif saved_letter == "B":
        print("The triangle has a base line length of: " + str(JMath.triangle.height_or_base_line(check_input.number(
            "Please enter the length of the height."), check_input.number("Please enter the surface area."))))

elif saved_letter == "R":
    saved_letter = check_input.letter(
        "What do you want to calculate about the rectangle?\nSurface <S> | Side length <L>", "SL", True)

    if saved_letter == "S":
        print("The rectangle has a surface area of: " + str(
            JMath.rectangle.surface(check_input.number("Please enter the length of the top or bottom lines."),
                                    check_input.number("Please enter the length of the right or left lines."))))

    elif saved_letter == "L":
        print("The line has a length of: " + JMath.rectangle.side(
            check_input.number("Please enter the surface area of the rectangle."),
            check_input.number("Please enter the length of the side turned 90° to the current side.")))

input()
