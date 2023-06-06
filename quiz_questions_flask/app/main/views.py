import config
from app.db_data import add_questions_data_to_db, get_all_questions_from_db
from flask import render_template, request
from flask.views import View




class MainView(View):
    methods = ["GET", "POST"]

    def __init__(self, template_name, title):
        self.template_name = template_name
        self.title = title

    def dispatch_request(self):
        """ POST REST метод, принимающий на вход запросы
            с содержимым вида {"questions_num": integer}
        """
        result = None
        if request.method == "POST":
            try:
                add_questions_data_to_db(config.LINK,
                                         int(request.form['questions_num']))
                result = get_all_questions_from_db()
            except ValueError as e:
                print(e)
                # TODO: всплывающее окно что данные не корректны
        return render_template(self.template_name, title=self.title, result=result)


class AllView(View):
    def __init__(self, template_name, title):
        self.template_name = template_name
        self.title = title

    def dispatch_request(self):
        result = get_all_questions_from_db()
        return render_template(self.template_name, title=self.title, result=result)
