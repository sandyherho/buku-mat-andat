# Mengimpor NumPy
import numpy as np

# Mendeklarasikan matriks
A = np.eye(3,3)
B = np.array([[2,1,2],[1,2,8]])
C = np.array([1,-1,1])
D = np.array([[1,2], [8,1]])
E = np.array([[1,0], [0,1], [0,0], [2,1]])
F = np.array([[2,1,1,2],[1,2,2,1]])

# Jawaban
print('Jumlah baris A: {}, Jumlah kolom A: {}.'. format(np.shape(A)[0], np.shape(A)[-1]))
print('Jumlah baris B: {}, Jumlah kolom B: {}.'. format(np.shape(B)[0], np.shape(B)[-1]))
print('Jumlah baris C: {}, Jumlah kolom C: {}.'. format(np.shape(C)[0], np.shape(C)[-1]))
print('Jumlah baris D: {}, Jumlah kolom D: {}.'. format(np.shape(D)[0], np.shape(D)[-1]))
print('Jumlah baris E: {}, Jumlah kolom E: {}.'. format(np.shape(E)[0], np.shape(E)[-1]))
print('Jumlah baris F: {}, Jumlah kolom F: {}.'. format(np.shape(F)[0], np.shape(F)[-1]))