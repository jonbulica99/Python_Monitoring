LOG_DIR = "log"
LOG_FORMAT = "%(asctime)s [%(filename)s:%(lineno)s - %(funcName)s()] - %(levelname)s - %(message)s"

CRON_DEFAULT_COMMAND = "client.py"
CRON_DEFAULT_CHECK = "cpu"
CRON_DEFAULT_TIME = "* * * * *"

MAIL_DEFAULT_RECIPIENT = "root@localhost"
MAIL_DEFAULT_SERVER = "localhost"
MAIL_DEFAULT_SERVER_PORT = "25"
MAIL_DEFAULT_MESSAGE = """
Hello {},

We are writing to inform you that the check {} was executed and returned the following output: {}.

Best regards
Your Monitoring system :) 
"""
