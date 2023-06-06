from flask import render_template

from . import main
from .views import AllView, MainView

TEMPLATES = {
    "main": "main.html",
    "404": "404.html",
    "all": "all_questions.html",
}

main.add_url_rule("/", view_func=MainView.as_view(name="main",
                                                  template_name=TEMPLATES["main"],
                                                  title="Главная страница"))

main.add_url_rule("/all/", view_func=AllView.as_view(name="all",
                                                     template_name=TEMPLATES["all"],
                                                     title="Все вопросы"))


# Обработчик 404 ответа сервера (переход на неизвестный url адрес)
@main.app_errorhandler(404)
def error_404(e):
    return render_template(TEMPLATES["404"])
