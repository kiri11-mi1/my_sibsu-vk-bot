import logging
from config import Config
from bot import VkBot
import service


logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

# Прототип базы)
db = []

def main():
    cfg = Config()
    bot = VkBot(cfg.TOKEN, cfg.VERSION)

    while True:
        for post in bot.get_all_posts(cfg.PUBLIC_ID):

            # Проверка на существаование в базе
            if service.is_exist(posts=db, post_id=post['id']):
                logging.info(f"Пост {post['id']} определён")
                continue

            post_data = {'id': post['id']}
            
            # Берём текст поста
            if content := service.get_text(cfg=cfg, text=post['text']):
                post_data.update({'text': content})
                logging.info(f"Пост {post['id']} подходит")
            else:
                logging.info(f"Пост {post['id']} не подходит")
                continue

            # Добавлям фотки
            post_data.update({"photos": service.get_photos(post['attachments'])})
            logging.info(f"Фотографии поста {post['id']} добавлены")

            # Добавляем в базу всю информацию о посте
            db.append(post_data)
            logging.info(f"Пост {post['id']} добавлен в базу данных")

            # Делаем json-чик, чтобы поглядеть результат
            service.make_json(db, 'database.json')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logging.info('Выключение клавишей Ctrl + C')
        exit()
