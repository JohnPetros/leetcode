def find_the_index_of_the_first_occurrence_in_a_string(
    haystack: str, needle: str
) -> int:
    needle_length = len(needle)

    for index in range(len(haystack)):
        print(haystack[index : index + needle_length])
        if haystack[index : index + needle_length] == needle:
            return index

    return -1


print(find_the_index_of_the_first_occurrence_in_a_string("helloworld", "low"))
# print(find_the_index_of_the_first_occurrence_in_a_string("sadbutsad", "sad"))
# print(find_the_index_of_the_first_occurrence_in_a_string("leetcode", "leeto"))
# print(find_the_index_of_the_first_occurrence_in_a_string("a", "a"))
