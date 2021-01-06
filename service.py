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
    photos = []
    for attac in attachments:
        if attac['type'] == 'photo':
            for sub_photo in attac['photo']['sizes']:
                if sub_photo['type'] == 'y':
                    photos.append({
                        "width": sub_photo['width'],
                        "height": sub_photo['height'],
                        "url": sub_photo["url"]
                    })
    return photos
    