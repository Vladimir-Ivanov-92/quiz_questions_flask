from app import db


class Questions(db.Model):
    """1. ID вопроса, 2. Текст вопроса, 3. Текст ответа, 4. - Дата создания вопроса. """
    question_id = db.Column(db.Integer, unique=True, primary_key=True)
    question = db.Column(db.Text, nullable=True)
    answer = db.Column(db.String(300), nullable=True)
    created_at = db.Column(db.String(30), nullable=True)

    def __repr__(self):
        return f"{self.question_id}.Question:{self.question} - Answer: {self.answer}"


def filling_a_field_in_the_db(ApiQuestionsJson):
    question_data_to_db = Questions(
        question_id=ApiQuestionsJson.id,
        question=ApiQuestionsJson.question,
        answer=ApiQuestionsJson.answer,
        created_at=ApiQuestionsJson.created_at,
    )
    return question_data_to_db
