# check_data
# input: line to substitute
# output: acc_count,loop_detected

def check_data(line_mod):
    infile = open('input.txt','r')
    acc_count = 0
    op_num = 0
    operation = []
    op_completed = []
    curr_op_num = 0
    loop_control = True

    with infile as f:
        for line in f:
            operation.append((op_num,[line.partition(' ')[0],str.rstrip(line.partition(' ')[2])]))
            op_num = op_num+1

    change_made = 0
    if operation[line_mod][1][0] == 'jmp' and change_made == 0:
        curr_op_acc_val = operation[line_mod][1][1]
        del operation[line_mod]
        operation.insert(line_mod,(line_mod,['nop',curr_op_acc_val]))
        change_made = 1
    if operation[line_mod][1][0] == 'nop'and change_made == 0:
        curr_op_acc_val = operation[line_mod][1][1]
        del operation[line_mod]
        operation.insert(line_mod,(line_mod,['jmp',curr_op_acc_val]))
        change_made = 1
    while loop_control:
        if curr_op_num == len(operation):
            loop_detected = 0
            return acc_count,loop_detected
        curr_op = operation[curr_op_num][1][0]
        if curr_op_num not in op_completed:
            if curr_op == 'acc':
                acc_inc = int(operation[curr_op_num][1][1])
                acc_count = acc_count + acc_inc
                op_completed.append(curr_op_num)
                curr_op_num = curr_op_num + 1
            if curr_op == 'jmp':
                op_completed.append(curr_op_num)
                curr_op_num = curr_op_num + int(operation[curr_op_num][1][1])
            if curr_op == 'nop':
                curr_op_num = curr_op_num + 1
            # print(op_completed)
        else:
            loop_detected = 1
            return acc_count,loop_detected