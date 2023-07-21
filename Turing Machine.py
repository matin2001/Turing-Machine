
def alphabet(word):
    if word == 1:
        return "blank"
    if word == 2:
        return "a"
    if word == 3:
        return "b"
    if word == 4:
        return "c"
    if word == 5:
        return "d"
    if word == 6:
        return "e"
    if word == 7:
        return "f"
    if word == 8:
        return "e"


def right_or_left(word):
    if word == 1:
        return "L"
    if word == 2:
        return "R"


turing_machine = input()
t_machine = []
machine = turing_machine.split("00")
for i in range(len(machine)):
    transition = machine[i].split("0")
    t0 = transition[0].count("1")
    t1 = transition[1].count("1")
    t2 = transition[2].count("1")
    t3 = transition[3].count("1")
    t4 = transition[4].count("1")
    a0 = "q" + str(t0-1)
    a2 = "q" + str(t2-1)
    a1 = alphabet(t1)
    a3 = alphabet(t3)
    a4 = right_or_left(t4)
    t_machine.append([a0, a1, a2, a3, a4])


current_state = t_machine[0][0]
list_of_states = []
for i in t_machine:
    list_of_states.append(i[0])
    list_of_states.append(i[2])
set_of_states = set(list_of_states)
final_state = "q" + str(len(set_of_states)-1)
#print("current_state: ", current_state)
#print("final_state: ", final_state)

#for i in t_machine:
#    print("Transition: ", i)

count = int(input())
for i in range(count):
    tape = []
    tape.append("blank")
    tape_pointer = 1
    current_state = t_machine[0][0]
    str1 = input()
    if(len(str1)==0):
        tape.append("blank")
        tape.append("blank")
        tape.append("blank")
    else:
        string = str1.split("0")
        input_string = ""
        for j in range(len(string)):
            string[j] = string[j].strip()
        for j in range(len(string)):
            tape.append(alphabet(string[j].count("1")))
    tape.append("blank")

    flag = False
    m = 0
    while(m < 100):
        error_check = True
        if (current_state == final_state):
            break
        for k in range(len(t_machine)):
            if t_machine[k][0] == current_state and tape[tape_pointer] == t_machine[k][1]:
                error_check = False
                current_state = t_machine[k][2]
                tape[tape_pointer] = t_machine[k][3]
                if t_machine[k][4] == "L":
                    tape_pointer = tape_pointer - 1
                elif t_machine[k][4] == "R":
                    tape_pointer = tape_pointer + 1
                #print("Current State: ", current_state)
                #print("Tape: ", tape)
                #print("Tape Pointer: ", tape_pointer)
                break
        if(error_check == True):
            flag = True
            break
        m = m + 1




    if flag == True:
        print("Rejected")
    else:
        if(current_state == final_state):
            print("Accepted")
        else:
            print("Rejected")








