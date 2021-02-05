# ---------------
# Imports
# ---------------
import JMath
import check_input


# ----------------
# Calculator interface
# ----------------
print("========   \\\      //       //\\\   ==========   ||    ||")
print("      ||   ||\\\  //||      //  \\\      ||       ||    ||")
print("      ||   || \\\// ||    =======\\\     ||       ======||")
print("      //   ||      ||    //      \\\    ||       ||    ||")
print("\\\===//    ||      ||   //        \\\   ||       ||    ||\n\n")
while True:

    saved_letter = check_input.letter(
        "Mit welcher Form arbeitest du?\nTrapez <T> | Parallelogramm <P> | Dreieck <D> | Rechteck <R>\nGroß- und Kleinschreibung ist erlaubt.\nDu kannst das Programm jederzeit mit Q beenden.",
        "TPDR",
        True)

    if saved_letter == "T":
        saved_letter = check_input.letter(
            "Was willst du vom Trapez berechnen?\nFlächeninhalt <F> | Länge der Mittellinie <M> | Höhe <H>",
            "FMH",
            True)

        if saved_letter == "F":
            print("Das Trapez hat eine Oberfläche von: " + str(
                JMath.trapeze.surface(check_input.number("Bitte die Höhe eingeben."),
                                      JMath.trapeze.middle_line(
                    check_input.number(
                        "Bitte die Länge der oberen Linie eingeben."),
                    check_input.number("Bitte die Länge der unteren Linie eingeben.")))))

        elif saved_letter == "M":
            saved_letter = check_input.letter(
                "Von welchen Werten willst du die Länge der Mittellinie berechnen?\nObere und untere Linie <L> | Oberfläche und Höhe <O>",
                "OL", True)

            if saved_letter == "L":
                print("Die Länge der Mittellinie ist: " + str(
                    JMath.trapeze.middle_line(check_input.number("Bitte die Länge der oberen Linie eingeben."),
                                              check_input.number("Bitte die Länge der unteren Linie eingeben."))))

            elif saved_letter == "O":
                print(
                    "Die Länge der Mittellinie ist: " + str(JMath.trapeze.height_or_middle_line(check_input.number(
                        "Bitte die Höhe eingeben."),
                        check_input.number("Bitte den Flächeninhalt eingeben."))))

        elif saved_letter == "H":
            print("Die Höhe ist:" + str(JMath.trapeze.height_or_middle_line(check_input.number(
                "Bitte die Länge der Mittellinie eingeben."),
                check_input.number("Bitte den Flächeninhalt eingeben."))))

    elif saved_letter == "P":
        saved_letter = check_input.letter(
            "Was willst du vom Parallelogramm berechnen?\nFlächeninhalt <F> | Höhe <H> | Länge der Grundlinie <G>",
            "FHG",
            True)

        if saved_letter == "F":
            print("Der Flächeninhalt ist: " + str(
                JMath.parallelogram.surface(check_input.number("Bitte die Länge der Grundlinie eingeben."),
                                            check_input.number("Bitte die Höhe eingeben."))))
        if saved_letter == "H":
            print("Die Höhe ist: " + str(
                JMath.parallelogram.height_or_base_line(
                    check_input.number(
                        "Bitte die Länge der Grundlinie eingeben."),
                    check_input.number("Bitte den Flächeninhalt eingeben."))))

        if saved_letter == "G":
            print("Die Länge der Grundlinie ist:  " + str(
                JMath.parallelogram.height_or_base_line(check_input.number("Bitte die Höhe eingeben."),
                                                        check_input.number("Bitte den Flächeninhalt eingeben."))))

    elif saved_letter == "D":
        saved_letter = check_input.letter(
            "Was willst du vom Dreieck berechnen?\nOberfläche <O> | Höhe <H> | Länge der Grundlinie <G>",
            "OHG", True)

        if saved_letter == "O":
            print("Das Dreieck hat eine Oberfläche von: " + str(JMath.triangle.surface(check_input.number(
                "Bitte die Länge der Grundlinie eingeben."), check_input.number("Bitte die Höhe eingeben."))))

        elif saved_letter == "H":
            print("Das Dreieck hat eine Höhe von: " + str(JMath.triangle.height_or_base_line(check_input.number(
                "Bitte die Länge der Grundlinie eingeben."), check_input.number("Bitte die Oberfläche eingeben."))))

        elif saved_letter == "G":
            print("Die Länge der Grundlinie ist: " + str(JMath.triangle.height_or_base_line(check_input.number(
                "Bitte die Höhe eingeben."), check_input.number("Bitte die Oberfläche eingeben."))))

    elif saved_letter == "R":
        saved_letter = check_input.letter(
            "Was willst du vom Rechteck berechnen\nOberfläche <O> | Seitenlänge <L>", "OL", True)

        if saved_letter == "O":
            print("Das Rechteck hat eine Oberfläche von: " + str(
                JMath.rectangle.surface(check_input.number("Bitte die Länge der Seiten a oder c eingeben."),
                                        check_input.number("Bitte die Länge der Seiten b oder d eingeben."))))

        elif saved_letter == "L":
            print("Die Seitenlänge ist: " + str(JMath.rectangle.side(
                check_input.number("Bitte die Oberfläche eingeben."),
                check_input.number(
                    "Bitte die Längen der Seiten a oder c eingeben, wenn mit b oder d gerechnet wird, oder die Länge der Seiten b oder d, wenn mit a oder c gerechnet wird."))))

    print("\n\n")
