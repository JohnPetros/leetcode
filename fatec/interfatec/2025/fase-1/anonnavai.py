balls = [
    23,
    12,
    26,
    20,
    12,
    23,
    20,
    26,
]

dorothy_balls = []
dagmar_balls = []

while balls:
    dorothy_balls.append(balls.pop(0))
    dagmar_balls.append(balls.pop(0))

for dorothy_ball, dagmar_ball in zip(dorothy_balls, dagmar_balls):
    total = dorothy_ball + dagmar_ball
    if dorothy_ball > dagmar_ball:
        if total > 40:
            print("DOROTHY DECIDE E A NONNA VAI")
        else:
            print("DOROTHY DECIDE")
    else:
        if total > 40:
            print("DAGMAR DECIDE E A NONNA VAI")
        else:
            print("DAGMAR DECIDE")
