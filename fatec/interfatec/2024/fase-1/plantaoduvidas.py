
categories_map = {
  1: "ALGORITMOS",
  2: "BOAS PRATICAS",
  3: "DESEMPENHO",
  4: "FLUXOGRAMAS",
  5: "INTERPRETACAO DE ENUNCIADOS",
  6: "SINTAXE DA LINGUAGEM",
}
has_at_least_one_included = False

# max_students_count = int(input())
# line2 = input().split()

max_students_count = 5
students = []
# while True:
#   student = {}
#   student["name"] = line2[0]
#   student["categories"] = list(map(int, line2[1:7]))
#   student["is_included"] = False

students = [
  {
    "name": "joao",
    "categories":  [1, 2, 3, 4],
  },
   {
    "name": "maria",
    "categories":  [5, 4, 3, 2],
  },
    {
    "name": "jose",
    "categories":  [5, 1],
  },
     {
    "name": "carlos",
    "categories":  [5, 2, 1, 6, 4],
  },
      {
    "name": "ana",
    "categories":  [5],
  },
]
  

for category_number, category_name in categories_map.items():
  print("-" * 30)
  print(category_name)
  print("-" * 30)
  
  included_students_names = []
  
  if max_students_count:
    for student in students:
      if category_number in student["categories"]:
        included_students_names.append(student["name"])
        student["is_included"] = True
        has_at_least_one_included = True
        max_students_count -= 1
       
  included_students_names.sort()
  for student_name in included_students_names:
    print(student_name)
  
  print()
  
if has_at_least_one_included:     
  for student in students:
    if not student["is_included"]:
      print("-" * 30)
      print("FICA PARA A PROXIMA!")
      print("-" * 30)
       

