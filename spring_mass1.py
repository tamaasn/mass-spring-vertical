import matplotlib.pyplot as plt
import math


#Untuk testing
#massa = 0.5
#konstan = 200
#y0 = 0.1
#v0 = 0.0

def displacement(time , y0 , v0 , omega):
    return y0 * math.cos(omega * time) + (v0 / omega) * math.sin(omega * time)

def show_graph(massa , konstan , y0 , v0):
    omega = math.sqrt(konstan / massa)
    waktu = []
    for i in range(1000):
        waktu.append(i * 0.001)

    pemindahan = []

    for waktu_ in waktu:
        hasil_displacement = displacement(waktu_ , y0 , v0 , omega)
        pemindahan.append(hasil_displacement)

    plt.figure(figsize=(10,6))
    plt.plot(waktu ,pemindahan  , label="Perpindahan (m)")
    plt.title("Vertical spring mass")
    plt.xlabel("Waktu (s)")
    plt.ylabel("Perpindahan (m)")
    plt.legend()
    plt.grid(True)
    plt.show()

print("Vertical Spring Mass Akmal Sani")
massa = float(input("Massa (Kg) : "))
konstan = float(input("Konstanta pegas (N/m) : "))
y0 = float(input("Perpindahan awal(M): "))
v0 = float(input("Awal kecepatan (m/s) : "))
show_graph(massa , konstan , y0 , v0)

