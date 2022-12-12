import json


def load_json(file_name):
    """
    Загружаем данные из json
    :param file_name:
    :return: возвращаем список словарей
    """
    with open(file_name, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data


def get_posts_all():
    """
    Загружаем все посты и создаем сокрашенный пост в словаре
    :return: Возвращаем все посты в виде списка словарей
    """
    data = load_json('data/posts.json')
    for post in data:
        post['short'] = post['content'][:post['content'].find(" ", 100)]
    return data


def get_post_by_pk(pk):
    """
    Получаем пост по персональному ключу
    :param pk:
    :return: Возвращаем найденный пост по pk
    """
    data = get_posts_all()
    for post in data:
        if pk == post["pk"]:
            return post

    return None


def get_comments_all():
    """
    Загружаем все комментарии к постам
    :return: Возвращаем список комментариев
    """
    data = load_json('data/comments.json')

    return data


def load_post_by_user_name(user_name):
    """
    Получаем пользователя по имени из списка всех постов и складываем в отфильтрованный список
    :param user_name:
    :return: Возращаем отфильтрованный список
    """
    data = get_posts_all()
    post_filtered = []
    for post in data:
        if user_name.lower() == post["poster_name"].lower():
            post_filtered.append(post)

    return post_filtered


def get_comments_by_post_id(post_id):
    """
    Получаем комментарии по персональному ключу из списка всех комментариев
    :param post_id:
    :return: Возвращаем конкретные комментарии
    """
    comments = get_comments_all()
    list_of_comments = []
    for comment in comments:
        if post_id == comment["post_id"]:
            list_of_comments.append(comment)

    return list_of_comments


def search_for_posts(query):
    """
    Ищем по слову в содержании поста
    :param query:
    :return: Возвращаем пост(-ы) в которых есть искомое слово
    """
    data = get_posts_all()
    post_filtered = []
    for post in data:
        if query.lower() in post["content"].lower():
            post_filtered.append(post)

    return post_filtered
