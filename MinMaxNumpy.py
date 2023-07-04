import numpy as np

def main():
    # membuat array numpy
    data = np.array([1,2,3])

    # Menampilkan data
    print('Data :', data)

    # menampilkan jumlah elemen
    print('Jumlah elemen :', len(data))

    # menghitung rata2
    mean_value = np.mean(data)
    print('rata-rata : ',mean_value)

    # menghitung standar deviasi
    std_dev = np.std(data)
    print("standar deviasi :", std_dev)

    # menghitung nilai max and min
    max_value = np.max(data)
    min_value = np.min(data)

    print("Nilai max:", max_value)
    print("Nilai min:", min_value)

if __name__ == "__main__":
    main()