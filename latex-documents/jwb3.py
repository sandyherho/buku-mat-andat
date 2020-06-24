# Mengimpor NumPy
import numpy as np

# Deklarasi vektor
x = np.arange(1,5)

# Menghitung norm L2
euNorm = np.linalg.norm(x)

# Menampilkan hasil
print('Norma Euklidesan dari vektor x adalah: {}'.format(euNorm))