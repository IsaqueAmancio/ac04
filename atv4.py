tempos = []
while True:
    tempo = int(input())
    if tempo < 0:
        break
    tempos.append(tempo)

media = sum(tempos) / len(tempos)

print("MEDIA: {:.2f}".format(media))

for tempo in tempos:
    if tempo < media:
        print(tempo)
