import json


def make_json(content, filename='response.json'):
    """Делает json файл из словаря"""
    with open(filename, 'w') as wf:
        json.dump(content, wf, indent=2, ensure_ascii=False)


def is_exist(post_id, posts):
    """Проверяет есть ли в базе данных пост с заддным id"""
    for post in posts:
        if post['id'] == post_id:
            return True


def get_text(cfg, text):
    """Добавление текста по имеющимся тегам"""
    for tag in cfg.TAGS:
        if tag.lower() in text.lower():
            return text


def get_photos(attachments):
    """Добавление фоток"""
    for attac in filter(lambda elem: elem['type'] == 'photo', attachments):
        for sub_photo in filter(lambda elem: elem['type'] == 'y', attac['photo']['sizes']):
            yield {
                "width": sub_photo['width'],
                "height": sub_photo['height'],
                "url": sub_photo["url"]
            }
