import sys

import calculator_interface

try:
    if sys.argv[1] == "-h" or "--hilfe" or "--help" or "/?" or "/h" or "/help" or "/hilfe":
        print("JMath hilfe:")
        print(
            "JMath ist eine Konsolenanwendung, die man benutzt um unterschiedliche Werte von Dreiecken, Rechtecken, Parallelogrammen oder Trapezen zu berechnen.")
        print("Um JMath zu starten, starte die Datei ohne Startparameter")

    else:
        print("Benutzung:\nOhne Startparameter: Programm starten\nMit -h starten: Hilfe anzeigen.")

except:
    calculator_interface
