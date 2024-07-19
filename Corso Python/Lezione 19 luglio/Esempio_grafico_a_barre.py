import matplotlib.pyplot as plt

studenti = ['Anna', 'Mara', 'Antonio', 'Giovanni']
voti = [8, 7, 5, 6]

plt.figure()
plt.bar(studenti, voti, color='orange')
plt.title('Andamento classe')
plt.xlabel('Studenti')
plt.ylabel('Voti')
plt.show()