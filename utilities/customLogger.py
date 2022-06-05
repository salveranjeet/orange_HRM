import logging

class LogGenerator:

    @staticmethod
    def log_generator():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(filename="E:/orange_hrm/Logs/automation.log",
                            format="%(asctime)s: %(levelname)s: %(message)s",
                            datefmt="%m/%d/%Y %I:%M:%S %p")
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
