def findSchedules(workHours, dayHours, pattern):
    from itertools import product
    count_question_mark = pattern.count('?')
    numbers = pattern.replace('?', '')
    answer_list = []
    existing_totol_working_hours = 0
    for n in pattern:
        if n != '?':
            existing_totol_working_hours += int(n) 
    left_hours = workHours - existing_totol_working_hours
    all_posible_number = ''.join(str(i) for i in list(range(dayHours + 1)))
    all_posible_combination_list = list(product(all_posible_number, repeat=count_question_mark))
    for all_posible_combination in all_posible_combination_list:
        tmp_sum = 0
        answer_string = ''
        for i in all_posible_combination:
            tmp_sum += int(i)
        if tmp_sum == left_hours:
            idx = 0
            for m in pattern:
                if m == '?':
                    answer_string += all_posible_combination[idx]
                    idx += 1
                else:
                    answer_string += m
            answer_list.append(answer_string)
    return answer_list


if __name__ == '__main__':
    # test_case1
    # workHours = 56
    # dayHours = 8
    # pattern = '???8???'
    # ans = ['8888888']

    # test_case2
    # workHours = 24
    # dayHours = 4
    # pattern = '08??840'
    # ans = ['0804840', '0813840', '0822840', '0831840', '0840840']

    # test_case3
    workHours = 3
    dayHours = 2
    pattern = '??2??00'
    ans = ['0020100', '0021000', '0120000', '1020000']

    my_ans = findSchedules(workHours, dayHours, pattern)
    print('my_ans:', my_ans)
    assert my_ans == ans