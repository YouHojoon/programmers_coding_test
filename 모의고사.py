def solution(answers):
    person_1 = [1,2,3,4,5]
    person_2 = [2,1,2,3,2,4,2,5]
    person_3 = [3,3,1,1,2,2,4,4,5,5]
    persons = [person_1, person_2, person_3]
    answer = []
    
    for person in persons:
        correct_sum = 0
        for i, a in enumerate(answers):
            if person[i % len(person)] == a:
                correct_sum += 1
        answer.append(correct_sum)
        
    max_value = max(answer)
    return [i + 1 for (i, v) in enumerate(answer) if v == max_value]

    
