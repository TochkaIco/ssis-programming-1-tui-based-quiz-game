import json

def create_quiz():
    name = input("Ange namn för quizzet")
    question = input("Ange fråga (q för att sluta)")

    while question != "q":
        answers = input("Ange korrekta svar på frågan (separera med : om det finns flera)")

        json_data = {
            "name" : name,
            "question" : question,
            "answers" : answers
        }

        with open("quiz.json", "a") as f:
            json.dump(json.dumps(json_data), f)



while True:
    print("1 - skapa en ett quiz")
    print("2 - svara på quiz")

    mode = int(input())

   # if mode == 1:

