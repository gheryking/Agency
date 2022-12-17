import os

LOGGING = {
    'version':1,
    'disable_existing_loggers':False,
    'handlers':{
        'console':{
            'class': 'logging.StreamHandler',
        },
    },
    'root':{
        'handler': ['console'],
        'level':'WARNING',
    },
}