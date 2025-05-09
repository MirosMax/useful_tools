def size_to_large(size):
    '''
    Функция принимает размер файла в байтах и возвращает строку в самых крупных единицах измерения
    с округлением до целых

    Единицы измерения:
    1 KB (Kilobyte) = 1,024 Bytes
    1 MB (Megabyte) = 1024 KB = 1,048,576 Bytes
    1 GB (Gigabyte) = 1024 MB = 1,048,576 KB = 1,073,741,824 Bytes
    1 TB (Terabyte) = 1024 GB = 1,048,576 MB = 8,388,608 KB = 1,099,511,627,776 Bytes
    1 PB (Petabyte) = 1024 TB = 1,048,576 GB = 1,073,741,824 MB = 1,099,511,627,776 KB = 1,125,899,906,842,624 Bytes
    1 EB (Exabyte) = 1024 PB = 1,048,576 TB = 1,073,741,824 GB = 1,099,511,627,776 MB = 1,125,899,906,842,624 KB = 1,152,921,504,606,846,976 Bytes
    1 ZB (ZettaByte) = 1024 EB = 1,048,576 PB = 1,073,741,824 TB = 1,099,511,627,776 GB = 1,125,899,906,842,624 MB = 1,152,921,504,606,846,976 KB = 1,180,591,620,717,411,303,424 Bytes
    1 YB (Yottabyte) = 1,000 ZB = 1,048,576 EB = 1,073,741,824 PB = 1,099,511,627,776 TBz = 1,125,899,906,842,624 GB = 1,152,921,504,606,846,976 MB = 1,180,591,620,717,411,303,424 KB = 1,208,925,819,614,629,174,706,176 Bytes
    '''

    measure = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']
    count = 0
    while size >= 1024:
        size /= 1024
        count += 1
    return f'{round(size)} {measure[count]}'


if __name__ == '__main__':
    print(size_to_large(11258996842624))
    print(size_to_large(77777777777))
    print(size_to_large(1800))
    print(size_to_large(1125000000008996842624))
    print(size_to_large(1125899684262479165498435498))