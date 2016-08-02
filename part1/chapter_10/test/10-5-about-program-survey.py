print("why you love programming?\n")
survey_result_filename = 'survey_result.txt'

def collect_result():
    results = []
    while True:
        reason = input('input you reason why you love program: ')
        results.append(reason)
        is_continue = input('is continue yes/no ')
        if is_continue == 'no':
            break
    return results

def write_result(filename, reason_list):
    with open(filename, 'a') as file_object:
        for line in reason_list:
            file_object.write(line + "\n")

    print('thanks you!')

# invoke 
love_program_reasons = collect_result()
write_result(survey_result_filename, love_program_reasons)