import logging

logger = logging.getLogger("consumer-demand")

logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)


def log_start(task):

    logger.info(
        f"STARTED : {task}"
    )


def log_end(task):

    logger.info(
        f"FINISHED : {task}"
    )


def log_error(task, err):

    logger.error(
        f"{task} FAILED : {err}"
    )
