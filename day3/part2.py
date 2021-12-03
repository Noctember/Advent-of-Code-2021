def get_rating(data, most_common):
    index = 0
    while len(data) > 1:
        counts = {"0": 0, "1": 0}
        for num in data:
            counts[num[index]] += 1
        if most_common:
            bit = "1" if counts["1"] >= counts["0"] else "0"
        else:
            bit = "0" if counts["1"] >= counts["0"] else "1"
        data = [num for num in data if num[index] == bit]
        index += 1
    return data[0]


data = open('input.txt').readlines()
data = [t.strip() for t in data]
oxygen_rating = get_rating(data, True)
co2_rating = get_rating(data, False)

oxygen_rating_int = int(oxygen_rating, 2)
co2_rating_int = int(co2_rating, 2)
print(f'Oxygen: {oxygen_rating} ({oxygen_rating_int}) CO2: {co2_rating} ({co2_rating_int}) Life support rating:'
      f' {co2_rating_int * oxygen_rating_int}')