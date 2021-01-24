# ---------------
# Imports
# ---------------
import sys

from calculator_interface import calculator_interface

try:
    if sys.argv[1] == "-h" or "--hilfe" or "--help" or "/?" or "/h" or "/help" or "/hilfe":
        print("JMath hilfe:")
        print(
            "JMath ist eine Konsolenanwendung, die man benutzt um unterschiedliche Werte von Dreiecken, Rechtecken, Parallelogrammen oder Trapezen zu berechnen.")
        print("Um JMath zu starten, klicke doppelt auf die Datei.")

    else:
        print("Usage:\nStart without parameters: Start the program.\nStart with -h: Show help message")

except:
    calculator_interface
