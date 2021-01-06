import requests
import logging

class VkBot:

    def __init__(self, token, v):
        """Инициализация"""
        self.token = token
        self.api = 'https://api.vk.com/method/'
        self.v = v


    def get_all_posts(self, owner_id):
        method = 'wall.get'
        params = {
            "owner_id": -owner_id,
            "extended": 0,
            "access_token": self.token,
            "v": self.v
        }
        response = requests.get(
            self.api + method, params=params
        ).json()
        return response['response']['items']
