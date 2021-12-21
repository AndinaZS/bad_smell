csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""

def get_users_list(csv):
    data = get_data(csv)
    data = get_sorted_data(data)
    data = get_filter_data(data)
    return data

def get_data(line: str):
    data = [elem.split(';') for elem in line.split('\n')]
    return data

def get_sorted_data(data: list):
    data.sort(key=lambda x: int(x[1]))
    return data

def get_filter_data(data: list):
    return list(filter(lambda x: int(x[1]) > 10, data))


if __name__ == '__main__':
    print(get_users_list(csv))
