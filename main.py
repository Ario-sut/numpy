import numpy as np

# Atribut Array: Menentukan ukuran, bentuk, konsumsi memori, dan tipe data array
# Indexing of array: Mendapatkan dan mengatur nilai elemen Array individu
# Slicing of arrays: Mendapatkan dan mengatur sub-Array yang lebih kecil di dalam Array yang lebih besar
# Reshaping of arrays: Mengubah bentuk Array yang diberikan
# Joining and splitting of array: Menggabungkan beberapa Array menjadi satu, dan memisahkan satu Array menjadi beberapa Array

def main():
    # create a numpy array of 10 elm
    arr = np.arange(10)
    print(arr)
    sum = np.sum(arr)
    print(sum)
    mean = np.mean(arr)
    print(mean)

if __name__ == "__main__":
    main()

# official web 