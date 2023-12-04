#VODA IOAN - 917
def number_of_subspaces(k:int, n:int):
    """Generate the number of subspaces

    Args:
        k (int): number of dimensional subspaces
        n (int): number of elem from vector

    Returns:
        int: number of subspaces
    """
    den = 1
    num = 1
    for i in range(k):
        den *= (1 << n) - (1 << i)
        num *= (1 << k) - (1 << i)
    return den // num

def print_solution(file_for_output, k:int, n:int, solution_list_for_print:list):
    """Print solution.

    Args:
        file_for_output (_type_): adress for ouput file
        k (int):  number of dimensional subspaces
        n (int): number of elem from vector
        solution_list_for_print (list): list with solution
    """
    file_for_output.write("(")
    for i in range(1, k + 1):
        file_for_output.write("("+ format(solution_list_for_print[1 << (i - 1)], '0' + str(n) + 'b') + ')')
        if i < k:
            file_for_output.write(",")
    file_for_output.write(")\n")

def valid(solution_list_for_print:list, index:int):
    """Verify if is valid subspace

    Args:
        solution_list_for_print (list): solution list for print and for verification
        index (int): index for verification

    Returns:
        bool: True if is valid, else False
    """
    for i in range(1, index):
        if solution_list_for_print[i] ^ solution_list_for_print[index] == 0:
            return False
    return True

def add_in_solution_list_for_print(solution_list_for_print:list, index:int):
    """Add in solution list for print

    Args:
        solution_list_for_print (list): solution list for printing
        index (int): index for list
    """
    for i in range(1, index):
        solution_list_for_print[index + i] = solution_list_for_print[index] ^ solution_list_for_print[i]

def verification(used:list, n:int, solution_list:list):
    """Verify if is ok.

    Args:
        used (list): list with used subspaces
        n (int): number of elem from vector
        solution_list (list): solution list

    Returns:
        bool: True if is ok and false if isn't ok
    """
    for subspace in solution_list:
        same = all(subspace[i] == used[i] for i in range(1, (1 << n)))
        if same:
            return False
    return True

def back(index:int, k:int, n:int, solution_list:list, solution_list_for_print:list, file_for_output):
    """Function for generating solution.

    Args:
        index (int): index for list
        k (int):  number of dimensional subspaces
        n (int): number of elem from vector
        solution_list (list): solution list
        solution_list_for_print (list): solution list for print
        file_for_output (_type_): adrees for file
    """
    for i in range(1, 1 << n):
        solution_list_for_print[index] = i
        if valid(solution_list_for_print, index):
            add_in_solution_list_for_print(solution_list_for_print, index)
            if index == 1 << (k - 1):
                used = [False] * 70
                for i in range(1, 1 << k):
                    used[solution_list_for_print[i]] = True
                if verification(used, n, solution_list):
                    solution_list.append(used)
                    print_solution(file_for_output, k, n, solution_list_for_print)
            else:
                back(index << 1, k, n, solution_list, solution_list_for_print, file_for_output)

if __name__ == "__main__":
    while True:
        file_for_output = open("output.txt", "a")
        solution_list = []
        solution_list_for_print = [0] * 100
        k = int(input("Type k number: "))
        n = int(input("Type n number: "))
        counter = number_of_subspaces(k, n)
        file_for_output.write(f"Number of {k} dimensional subspace of the vector Z{n,k} over Z{k} is {str(counter)} \n")
        back(1, k, n, solution_list, solution_list_for_print, file_for_output)
        file_for_output.close()
        print("File has been updated.")
