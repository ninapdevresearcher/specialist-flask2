from flask import Flask, render_template, abort
app = Flask(__name__)  # создать объект сервера


@app.route("/")  # прописать путь для этой функции
def home():  # создать функцию главной стр
    return render_template('index.html')


@app.route("/names")  # прописать путь для этой функции
def names():  # создать функцию главной стр
    # name = 'Nina'
    # return render_template('names.html', name=name) #**{'name':name})
    entities = list()
    with open('files/names.txt', encoding='utf-8') as f:
        for raw_line in f:
            entities.append(raw_line.strip())
    # что вернуть браузеру
    return render_template('names.html', entities=entities)


@app.get("/about")  # прописать путь
def about():  # создать функцию
    return "О нас"  # вернуть браузеру


@app.get("/table")
def table():
    humans = list()
    with open('files/humans.txt', encoding='utf-8') as f:
        for raw_line in f:
            data = raw_line.strip().split(';')
            humans.append({'last_name': data[0],
                           'name': data[1],
                           'middle_name': data[2]
                           })
    return render_template('table.html', humans=humans)


@app.route("/users")
def users_list():
    # показывает всех пользователей
    entities = list()
    with open('files/users.txt', encoding='utf-8') as f:
        for raw_line in f:
            data = raw_line.strip().split(';')
            entities.append(dict(zip(('login', 'last_name', 'name',
                            'middle_name', 'birth_date', 'phone'), data))
                            )
    return render_template('users_list.html', **{'entities': entities})


@app.route("/users/<login>")
def user_info(login):
    item = None
    with open('files/users.txt', encoding="utf-8") as f:
        for raw_line in f:
            data = raw_line.strip().split(';')
            if data[0] == login:
                item = dict(zip(('login', 'last_name', 'name',
                            'middle_name', 'birth_date', 'phone'), data))
                break

    if item is None:
        abort(404, f'User with login ({login}) not found')

    return render_template('user_info.html', item=item)


# @app.route("/users/<username>")
# def show_user_profile(username):
#     # показывает профиль пользователя
#     return f'User{username}'


# @app.route("/posts/<int:post_id>")
# def show_post(post_id):
#     # показывакет статью по её id
#     return f'Post{post_id}'


if __name__ == "__main__":  # если запущен отсюда
    app.run(debug=True)  # запустить сервер
