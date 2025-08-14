inputs = [
    "25.0 60.0 1",
    "28.0 40.0 1",
]

for input in inputs:
    t, u, p = list(map(float, input.split()))
    if p >= 1:
        print("NAO REGAR")
    else:
        if t > 30 and u < 50:
            print("REGAR")
        else:
            print("NAO REGAR")
