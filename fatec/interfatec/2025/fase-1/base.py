dm, ym = map(int, "5 12".split())
ds, ys = map(int, "3 8".split())

tempo_guarda1 = ys - ds

tempo_guarda2 = ym - dm

while tempo_guarda1 != tempo_guarda2:
    if tempo_guarda1 < tempo_guarda2:
        tempo_guarda1 += ys
    else:
        tempo_guarda2 += ym

print(tempo_guarda1)
