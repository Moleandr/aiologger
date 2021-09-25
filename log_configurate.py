config1 = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': '[%(asctime)s] (%(levelname).1s:%(name)s) %(message)s',
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'INFO',
                'formatter': 'default',
            }
        },
        'root': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
    }

config2 = {
        'version': 1,
        'disable_existing_loggers': False,

        'formatters': {
            'default': {
                'format': '[%(asctime)s] (%(levelname).1s:%(name)s) %(message)s',
            },
        },

        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'INFO',
                'formatter': 'default',
            },
            'info_file':{
                'class': 'logging.FileHandler',
                'filename': 'logs/INFO.log',
                'level': 'INFO',
                'mode': 'w',
                'formatter': 'default',
            },
            'error_file':{
                'class': 'logging.FileHandler',
                'filename': 'logs/ERROR.log',
                'level': 'ERROR',
                'mode': 'w',
                'formatter': 'default',
            },
        },

        'root': {
            'level': 'DEBUG',
            'handlers': ['console', 'info_file', 'error_file'],
        },
    }
