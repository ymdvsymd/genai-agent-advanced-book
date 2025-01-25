import logging


def setup_logger(name, level=logging.INFO):
    """
    名前付きのロガーを作成し、コンソールにログを出力するように設定。

    Args:
        name (str): ロガー名。
        level (int): ログレベル。デフォルトはDEBUG。

    Returns:
        logging.Logger: 設定されたロガー。
    """

    logger = logging.getLogger(name)
    logger.setLevel(level)

    return logger
