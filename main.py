# Data type class TreeNode () to store the parent and the state of the node

class TreeNode:
    def __init__(self, parent=0, state='1234567890abcdef'):
        self.parent = parent
        self.state = state
        self.blank_tile_location = self.state.find('0')

    def __str__(self):
        return f"Parent node : {self.parent} \nState: \n{self.state[0:4]}\n{self.state[4:8]}\n{self.state[8:12]}\n{self.state[12:16]} "

# Function possible_child_states takes the node as input and returns the possible childs for the input node
def possible_child_states(tn=TreeNode()):
    zero_location = tn.blank_tile_location
    # Top action move
    if zero_location != 0 and zero_location != 1 and zero_location != 2 and zero_location != 3:
        tpart_1 = tn.state[0: zero_location - 4]
        tpart_2 = tn.state[zero_location]
        tpart_3 = tn.state[zero_location - 3: zero_location]
        tpart_4 = tn.state[zero_location - 4]
        tpart_5 = tn.state[zero_location + 1:]

        tpart = tpart_1 + tpart_2 + tpart_3 + tpart_4 + tpart_5
    else:
        tpart = None
    # Bottom action move
    if zero_location != 12 and zero_location != 13 and zero_location != 14 and zero_location != 15:
        bpart_1 = tn.state[0: zero_location]
        bpart_2 = tn.state[zero_location + 4]
        bpart_3 = tn.state[zero_location + 1: zero_location + 4]
        bpart_4 = tn.state[zero_location]
        bpart_5 = tn.state[zero_location + 5:]

        bpart = bpart_1 + bpart_2 + bpart_3 + bpart_4 + bpart_5
    else:
        bpart = None
    # Left action move
    if zero_location != 0 and zero_location != 4 and zero_location != 8 and zero_location != 12:
        lpart_1 = tn.state[0: zero_location - 1]
        lpart_2 = tn.state[zero_location]
        lpart_3 = tn.state[zero_location - 1]
        lpart_4 = tn.state[zero_location + 1:]

        lpart = lpart_1 + lpart_2 + lpart_3 + lpart_4
    else:
        lpart = None
    # Right action move
    if zero_location != 3 and zero_location != 7 and zero_location != 11 and zero_location != 15:
        rpart_1 = tn.state[0: zero_location]
        rpart_2 = tn.state[zero_location + 1]
        rpart_3 = tn.state[zero_location]
        rpart_4 = tn.state[zero_location + 2:]

        rpart = rpart_1 + rpart_2 + rpart_3 + rpart_4
    else:
        rpart = None

    return [tpart, bpart, lpart, rpart]  # Order [top, bottom, left, right]

# Function takes input from the user to create an input state
def input_state():
    i = 1
    state = ''
    possible_inputs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    possible_input_values = possible_inputs
    while True:
        start_state = input(
            f"Enter the value {i} of the start state. You are yet to enter these values{possible_inputs}")
        if start_state not in possible_input_values:
            print("Invalid value. Enter a valid value")
            continue
        if start_state in state:
            print("You have already entered this value")
            continue

        state = state + start_state
        possible_inputs.remove(start_state)
        i+=1
        print(state)
        if len(state) == 16:
            break

    return state

# Explores all the states until a goal state is reached. Prints the output to the text file
def tree_builder():
    f = open('test.txt', 'w')
    nodes_list = [TreeNode(None, input_state())]
    f.write(f"The input state is {nodes_list[0]} \n")
    iterator = 0
    goal_not_found = True
    
    while goal_not_found:
        x = nodes_list[iterator]
        if x.state == '123456789abcdef0':
            # If finput state is goal
            f.write(f'Goal State Found. The index is {iterator} \n')
            break
        for child_state in possible_child_states(x):
            
            if child_state is not None and child_state not in nodes_list:
                # If teh child state is valid or is not visited
                nodes_list.append(TreeNode(iterator, child_state))

            if child_state == '123456789abcdef0':
                # If the child state is goal
                f.write(f'Goal State Found. The parent is {iterator} \n')
                goal_not_found = False
                break

        iterator += 1
    i = 0
    for n in nodes_list:
        # printing all the nodes
        f.write(f"The {i}th index of nodes_list is \n {n} \n")
        i+=1
    
    f.write('Path to Goal is below:\n')
    a = -1
    path_list = []
    # Backtracking to find the optimum state
    while True:
        path_list.append(nodes_list[a])
        
        a = nodes_list[a].parent
        
        if a == None:
            break
        
    path_list.reverse()
    for n in path_list:
        # Prints to file
        f.write(f"{n}")
        
    f.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tree_builder()
