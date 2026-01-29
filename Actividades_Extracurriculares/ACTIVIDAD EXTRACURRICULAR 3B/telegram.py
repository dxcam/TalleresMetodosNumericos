import logging
import requests
from datetime import datetime
import sys

TOKEN = "TU_TOKEN"
CHAT_ID = "TU_CHAT_ID"

class ColorFormatter(logging.Formatter):
    colores = {
        logging.DEBUG: "\033[94m",
        logging.INFO: "\033[92m",
        logging.WARNING: "\033[93m",
        logging.ERROR: "\033[91m",
        logging.CRITICAL: "\033[95m",
    }
    reset = "\033[0m"
    def format(self, record):
        color = self.colores.get(record.levelno, self.reset)
        formato = f"%(asctime)s | %(levelname)s | %(filename)s | %(message)s"
        return f"{color}{super().format(record)}{self.reset}"

def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": mensaje}
    requests.post(url, data=data)

logger = logging.getLogger("ejemplo")
logger.setLevel(logging.DEBUG)

formato = ColorFormatter("%(asctime)s | %(levelname)s | %(filename)s | %(message)s", "%Y-%m-%d %H:%M:%S")

consola = logging.StreamHandler(sys.stdout)
consola.setFormatter(formato)
logger.addHandler(consola)

archivo = logging.FileHandler("registro.log", encoding="utf-8")
archivo.setFormatter(formato)
logger.addHandler(archivo)

class TelegramHandler(logging.Handler):
    def emit(self, record):
        enviar_telegram(self.format(record))

telegram = TelegramHandler()
telegram.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(filename)s | %(message)s"))
logger.addHandler(telegram)

logger.debug("mensaje debug")
logger.info("mensaje info")
logger.warning("mensaje advertencia")
logger.error("mensaje error")
logger.critical("mensaje crítico")