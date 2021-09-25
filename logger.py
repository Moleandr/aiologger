import logging.config
import re
import os
from pprint import pformat
from aiogram import types
from functools import wraps

from .log_configurate import config1, config2

# Инициализация настроек логгера
logging.config.dictConfig(config1)
# Получаем ссылку на объект логгера
logger = logging.getLogger(__name__)


try:
    os.mkdir('logs')
except FileExistsError:
    pass


def handler_log(extended=False):
    def decorator(handler):
        @wraps(handler)
        async def wrapper(*args, **kwargs):

            module_name = handler.__module__
            handler_name = handler.__name__
            state = await kwargs['state'].get_state() if 'state' in kwargs else None
            type_ = 'MESS' if isinstance(args[0], types.message.Message) else 'CALL'
            from_ = args[0]['from']['id']
            data = clear(args[0]['text']) if type_ == 'MESS' else clear(args[0]['data'])
            attach = get_attachment_type(args[0])

            if extended:
                log_message = f'{type_} [{module_name}.{handler_name}] [state = {state}]\n{pformat(dict(args[0]))}'
            else:
                log_message = f'{type_} [{handler_name}] [{state}] [UID={from_}] [data="{data}"] [attachment={attach}]'

            logger.info(log_message)
            result = await handler(*args, **kwargs)
            return result
        return wrapper
    return decorator


def get_attachment_type(callback):
    if 'photo' in callback:
        attach = 'photo'
    elif 'document' in callback:
        attach = 'document'
    elif 'sticker' in callback:
        attach = 'sticker'
    elif 'location' in callback:
        attach = 'location'
    elif 'poll' in callback:
        attach = 'poll'
    elif 'audio' in callback:
        attach = 'audio'
    elif 'contact' in callback:
        attach = 'contact'
    elif 'animation' in callback:
        attach = 'animation'
    else:
        attach = None
    return attach


def clear(text):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'[sm]', text)
