import string

alphabet = set(string.ascii_uppercase)
numbers = set(["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])


# plate = input()


plate = "A1234".ljust(50, "|")
plate = "12345".ljust(50, "|")
plate = "AB1234".ljust(50, "|")
plate = "ABC1234".ljust(50, "|")
plate = "ABC1D34".ljust(50, "|")
plate = "X0S0X0X0009".ljust(50, "|")

if plate[0] in alphabet and plate[1] in numbers and plate[2] in numbers and plate[3] in numbers and plate[4] in numbers:
  print("Placa muito antiga")
elif plate[0] in numbers and plate[1] in numbers and plate[2] in numbers and plate[3] in numbers and plate[4] in numbers:
  print("Placa numerica")
elif plate[0] in alphabet and plate[1] in alphabet and plate[2] in numbers and plate[3] in numbers and plate[4] in numbers:
  print("Placa AA-9999")
elif plate[0] in alphabet and plate[1] in alphabet and plate[2] in alphabet and plate[3] in numbers and plate[4] in numbers and plate[5] in numbers:
  print("Placa AAA-9999")
elif plate[0] in alphabet and plate[1] in alphabet and plate[2] in alphabet and plate[3] in numbers and plate[4] in alphabet and plate[5] in numbers and plate[6] in numbers:
  print("Placa AAA-9999")
else:
  print("Placa invalida")
