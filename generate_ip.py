def generate_ip():
    # функция генерирует случайный ip-адрес
    import random

    new_ip = []
    for _ in range(4):
        num = random.randrange(256)
        new_ip.append(str(num))
    return '.'.join(new_ip)


if __name__ == '__main__':
    print(generate_ip())
    print(generate_ip())
    print(generate_ip())
    print(generate_ip())
    print(generate_ip())