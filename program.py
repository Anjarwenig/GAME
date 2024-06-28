import random

def addition_game():
    print('''Welcome, Genius! 
          Lets play!''')
    score=0
    question=5
    
    for n in range(question):
        numb1=random.randint(1,20)
        numb2=random.randint(1,20)
        correct_Answer=numb1+numb2

        print(f'what is {numb1}+{numb2}?')
        player_answer= input('Enter your answer: ')

        if player_answer.isdigit() and int(player_answer)==correct_Answer:
            print('correct!')
            score +=1
        else:
            print(f'incorrect! the correct answer is {correct_Answer}')
    print(f'''GAME OVER!
          your score is {score}/{question}''')



def substraction():
    print('''Welcome, Genius! 
          Lets play!''')
    score=0
    question=5
    for n in range (question):
        num1=random.randint(1,20)
        num2=random.randint(1,10)
        correc_answer=num1-num2
        print(f'What is {num1}-{num2}?')
        player_answer=input('Enter your answer: ')

        if player_answer.isdigit() and int(player_answer)==correc_answer:
            print('Correct!')
            score+=1
        else:
            print(f'Incorrect! The correct answer is {correc_answer}')
    print(f'''GAME OVER!
          your score is {score}/{question}''')


def multiplication1():
    print('''Welcome, Genius! 
          Lets play!''')
    score=0
    question=5
    for n in range (question):
        num1=random.randint(1,10)
        num_set=[2,5,10]
        num2=random.choice(num_set)
        correc_answer=num1*num2
        print(f'What is {num1}*{num2}?')
        player_answer=input('Enter your answer: ')

        if player_answer.isdigit() and int(player_answer)==correc_answer:
            print('Correct!')
            score+=1
        else:
            print(f'Incorrect! The correct answer is {correc_answer}')
    print(f'''GAME OVER!
          your score is {score}/{question}''')
    



game_database={'快乐': 'happy',
               '悲伤': 'sad',
               '愤怒':'angry',
               '哭泣': 'cry',
               }
#show language by dictionary key randomly

def chinese_game():
    print('''Welcome, Genius! 
          Lets play!''')
    question=list(game_database.keys())
    random.shuffle(question)
    
    score=0

    for i in question:
        answer=input(f'''what is
                     {i}
                     in English?''')
        if answer.lower()==game_database[i]:
            print('Correct!')
            score += 1
        else:
            print(f'incorrect! the nswer is {game_database[i]}')


    print(f'''GAME OVER!
          Your score is {score}/{len(game_database)}''')








