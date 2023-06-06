from typing import Optional

import requests
from .models import Questions, db, filling_a_field_in_the_db
from pydantic import BaseModel


class ApiQuestionsJson(BaseModel):
    id: int
    answer: str
    question: str
    value: Optional[int]
    airdate: str
    created_at: str
    updated_at: str
    category_id: int
    game_id: int
    invalid_count: Optional[int]
    category: dict


def add_questions_data_to_db(link: str, questions_num: int):
    """
    Функция получает кол-во вопросов которые необходимо добавить в
    базу данных и получив данные от внешнего ресурса записывает каждый
    вопрос в БД. При записи происходит отлавливание исключений,
    в т.ч. возникающих из за добавления вопроса, уникальный ID уже есть в БД.
    В случае если вопрос не получилось добавить, происходит повторный запрос к
    внешнему ресурсу до тех пор, пока полученный вопрос не будет записан в БД.
    """
    r = requests.get(url=link.format(count=questions_num))
    for i in r.json():
        # Устанавливаем flag = False
        flag = False
        try:
            question_data_to_db = filling_a_field_in_the_db(ApiQuestionsJson(**i))
            db.session.add(question_data_to_db)
            db.session.commit()
            flag = True
        except Exception as e:  # TODO: Надо отлавливать конкретное исключение возникающее при добавлении уже существующего вопроса, а при возникновении любого другого сообщения завершать цикл и выводить сообщение о невозможности выполнения  запроса.
            print(f"1e={e}")
            db.session.rollback()
            # До тех пор, пока flag не будет True, будет запрашиваться один вопрос
            # и выполняться попытка добавления вопроса в БД
            while not flag: #TODO: добавить счетчик кол-ва повторений запроса, например если за 5 запросов данные не добавились, то рейзить исключение и завершаь цикл.
                try:
                    r = requests.get(url=link.format(count=1))
                    question_data_to_db = filling_a_field_in_the_db(
                        ApiQuestionsJson(**r.json()[0]))
                    db.session.add(question_data_to_db)
                    db.session.commit()
                    flag = True
                except Exception as e:
                    print(f"2e={e}")


def get_all_questions_from_db():
    data = db.session.execute(db.select(Questions)).scalars()
    return data
