import requests
import csv
from bs4 import BeautifulSoup
import time
# url = 'https://www.myminipwny.xyz/'
for i in range(2, 751):
    url = 'https://www.myminipwny.xyz/' if i == 1 else f'https://www.myminipwny.xyz/?wpv_aux_current_post_id=888&wpv_aux_parent_post_id=888&wpv_view_count=886&wpv_paged={i}'

    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    data = []

    for card in soup.find_all('li', class_='quiz'):
        # Extract question and answer
        question_text = card.find('p').text.strip()
        answer_text = card.find('span', class_='quiz__answer').text.strip()

        # Append the data to the products list
        data.append([question_text,answer_text])

    with open('quizzes.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        if file.tell() == 0:  # If the file is empty
            writer.writerow(['Question', 'Answer'])
        writer.writerows(data)
        # for element in data:
        #     writer.writerows([{'Question': element.question_text, 'Answer': element.answer_text}])  
    
    print(i, 'page complete')
    time.sleep(5)

