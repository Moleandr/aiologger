# aiologger


## Example 1
```Python
@dp.message_handler(commands=['start'], state='*')
@backend.handler_log()
async def test_command_1(message: types.Message):
	pass
```
OUT
```
[2021-09-25 11:10:28,015] (I:backend.aiologger.logger) MESS [test_command_1] [None] [UID=222222222] [data="/start"] [attachment=None]
```

## Example 2
```Python
@dp.message_handler(commands=['start'], state='*')
@backend.handler_log(extended=True)
async def test_command_2(message: types.Message):
	pass
```
OUT
```
[2021-09-25 11:19:44,895] (I:backend.aiologger.logger) MESS [frontend.default_handlers.test_command_2] [state = None]
{'chat': {'first_name': 'first_name',
          'id': 222222222,
          'last_name': 'last_name',
          'type': 'private',
          'username': 'username'},
 'date': 1632554384,
 'entities': [{'length': 6, 'offset': 0, 'type': 'bot_command'}],
 'from': {'first_name': 'first_name',
          'id': 222222222,
          'is_bot': False,
          'language_code': 'ru',
          'last_name': 'last_name',
          'username': 'username'},
 'message_id': 15510,
 'text': '/start'}
```

