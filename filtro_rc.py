import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do circuito
R = 10e3
C = 10e-9

# Frequências
f = np.logspace(1, 5, 1000)

# Frequência angular
w = 2 * np.pi * f

# Função de transferência
H = 1 / (1 + 1j * w * R * C)

# Magnitude em dB
H_dB = 20 * np.log10(np.abs(H))

# Frequência de corte
fc = 1 / (2 * np.pi * R * C)

# Gráfico
plt.figure(figsize=(8,5))
plt.semilogx(f, H_dB)
plt.axvline(fc, linestyle='--',
            label=f'fc = {fc:.1f} Hz')

plt.title('Resposta em Magnitude do Filtro RC')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid(True, which='both')
plt.legend()

plt.show()
