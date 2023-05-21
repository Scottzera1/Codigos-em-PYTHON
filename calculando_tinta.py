larg = float(input("Largura da parede: "))
alt = float(input("Altura da parede: "))

area = larg * alt
print("Sua parede tem a dimensão de {}x{} e tem área de {}m²".format(larg, alt, area))

tinta = area / 2
print("Para pinta sua parede, você precisa de {}l de tinta".format(tinta))