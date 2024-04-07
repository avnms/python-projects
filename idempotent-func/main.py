from copy import copy


def total(values: list, new_value: int) -> int:
    values.append(new_value)
    return sum(values)


def idempotent_total(values: list, new_value: int) -> int:
    temp_list = copy(values)
    temp_list.append(new_value)
    return sum(temp_list)


if __name__ == "__main__":
    values_1 = [1, 2, 3]
    print(f"values_1 original values: {values_1}")
    total_1 = total(values_1, 4)
    print(f"values_1 has been modified after the function call: {values_1}")
    print(f"total_1 is as expected: {total_1}\n")

    values_2 = [1, 2, 3]
    print(f"values_2 original values: {values_2}")
    total_2 = idempotent_total(values_2, 4)
    print(f"values_2 unchanged after the function call: {values_2}")
    print(f"total_2 is as expected: {total_2}")
