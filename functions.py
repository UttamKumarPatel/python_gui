
def gettodos(filename='todos.txt'):
    """
        Reads the todos from the 'todos.txt' file and returns them as a list of strings.
    """
    with open(filename, 'r') as file:
        todos = file.readlines()
    return todos


def writetodos(todos,filename='todos.txt'):
    """
        Writes the list of todos to the 'todos.txt' file.
    """
    with open(filename, 'w') as file:
        file.writelines(todos)
print(__name__)
if __name__=='__main__':
    print(help(gettodos))
    print("Hello!")