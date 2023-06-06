import os

from app import create_app, setup_database

if __name__ == '__main__':
    # Создается экземпляр приложения
    app = create_app()

    # Проверяется наличие БД в проекте, в случае отсутствия производится настройка
    if not os.path.isfile('instance/develop.db'):  # TODO: заменить путь к файлу на переменную
        setup_database(app)

    # Запускается приложение (сервер) Flask
    # app.run(host='0.0.0.0', port='5050')
    # app.run(host='0.0.0.0')
    app.run()
