from itertools import groupby


def sient(phones):
    phones.sort(key=lambda phone: phone[0])

    for group in groupby(phones, lambda phone: phone[0]):
        print(list(group[1]))

    # for group in phones_group.values():
    #     group.sort(key=len, reverse=True)
    #     first_phone = group[0]
    #     digits_count += len(first_phone)
    #     for index in range(1, len(group)):
    #         for index, digit in enumerate(group[index]):
    #             if digit != first_phone[index]:
    #                 digits_count += 1

    # print(digits_count)


# phones_count = int(input())
# phones = []

# for _ in range(phones_count):
#     phones.append(input())


# sient(["0467123456"])
# sient(["0123456789", "0123"])
# sient(
#     [
#         "0412578440",
#         "0412199803",
#         "0468892011",
#         "112",
#         "15",
#     ]
# )
