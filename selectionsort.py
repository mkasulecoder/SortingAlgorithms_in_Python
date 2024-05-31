"""
 * An Selection sort algorithm that focuses on sorting a list of items
 * in both ascending and descending order. The larger the dataset, the in-efficient the algo works
 * Time complexity = O(n^2)
 * @author Mark Kasule
"""


# sort arr in ascending order
def ascendingSort(num_list, size):
    # Use range(array length) to Loop through the list using indices just like traditional loops in Java
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if num_list[min_index] > j:
                min_index = j

        # Flip first and second values
        temp = num_list[min_index]
        num_list[min_index] = num_list[i]
        num_list[i] = temp


def descendingSort(num_list, size):
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if (num_list[min_index] < j):
                min_index = j

        # Flip first and second values
        temp = num_list[min_index]
        num_list[min_index] = num_list[i]
        num_list[i] = temp


# Main method to sort a list of values
def main():
    num_list = [3, 4, 6, 2, 7, 1, 99, 5]
    num_length = len(num_list)

    # print list before sorting
    print("Original order", num_list)

    # Print ascending order of list
    ascendingSort(num_list, num_length)
    print("Ascending order", num_list)

    # Print descending order of list
    descendingSort(num_list, num_length)
    print("Descending order", num_list)

    # Print list of values
    for value in num_list:
        print(value, end=" ")


if __name__ == '__main__':
    main()
