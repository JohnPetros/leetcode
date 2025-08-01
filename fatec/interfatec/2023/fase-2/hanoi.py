disks_count = 6
current_movement = "1 0 0 1 1 1"


def hanoi(disks_count):
    return 2**disks_count - 1


binary = current_movement.replace(" ", "")
decimal = int(binary, 2)

print(hanoi(disks_count) - decimal)
