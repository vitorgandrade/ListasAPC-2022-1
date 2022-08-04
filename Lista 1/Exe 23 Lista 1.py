def ritmoMedio(h, m, s, d):
    s += (h * 3600) + (m * 60)
    ritmo = s / d
    h = int(ritmo // 3600)
    m = int((ritmo % 3600) // 60)
    s = int((ritmo % 3600) % 60)
    print("%02d:%02d min/km" % (m, s))