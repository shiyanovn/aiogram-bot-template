import logging
import sys
import structlog

from aiogram_bot_template.data import config

def setup_logger() -> structlog.stdlib.BoundLogger:
    """
    Настраивает логирование в зависимости от окружения.
    В терминале логи читаемые (цветные, красивый формат).
    В контейнерах (Docker) логи сохраняются в JSON-формате.
    """

    logging.basicConfig(
        level=config.LOGGING_LEVEL,  
        format="%(asctime)s - %(levelname)s - %(message)s",
        stream=sys.stdout,
    )


    log = structlog.get_logger()

    shared_processors = [
        structlog.processors.add_log_level,  
        structlog.processors.TimeStamper(fmt="iso", utc=True),  
    ]

    if sys.stderr.isatty():
        processors = shared_processors + [structlog.dev.ConsoleRenderer()]
    else:
        processors = shared_processors + [
            structlog.processors.dict_tracebacks,
            structlog.processors.JSONRenderer(),
        ]

    structlog.configure(
        processors=processors,
        wrapper_class=structlog.stdlib.BoundLogger,
        context_class=dict,
    )

    return log
