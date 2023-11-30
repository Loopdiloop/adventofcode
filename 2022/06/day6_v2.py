def find_packet_signal(l):
    with open("input.txt") as f:
        for line in f:
            chars = list(line)
            for i in range(len(chars)-l):
                if len(chars[i:i+l]) == len(set(chars[i:i+l])):
                    return (i+1, chars[i:i+4])

print(f"Star 1, a signal: {find_packet_signal(4)}")
print(f"Star 2, signal boogaloo: {find_packet_signal(14)}")