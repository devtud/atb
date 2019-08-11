import asyncio
import os
from unittest import TestCase

from atb.bot import Bot

TEST_BOT_TOKEN = os.environ['TEST_BOT_TOKEN']
TEST_CHAT_ID = int(os.environ['TEST_CHAT_ID'])
TEST_WEBHOOK = os.environ['TEST_WEBHOOK']

bot = Bot(token=TEST_BOT_TOKEN)


class TestBot(TestCase):
    def test_send_message(self):
        loop = asyncio.get_event_loop()
        m = loop.run_until_complete(bot.send_message(chat_id=TEST_CHAT_ID, text='wazaaa'))
        print(m)

    def test_set_webhook(self):
        loop = asyncio.get_event_loop()
        r = loop.run_until_complete(bot.set_webhook(TEST_WEBHOOK))
        print(r)
