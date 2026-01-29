import logging
import colorlog

logger = logging.getLogger()
logger.handlers.clear()  # Elimina handlers previos
logger.setLevel(logging.DEBUG)

handler = colorlog.StreamHandler()
formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(asctime)s - %(levelname)s - %(message)s",
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    }
)
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.debug("Mensaje cyan (DEBUG)")
logger.info("Mensaje verde (INFO)")
logger.warning("Mensaje amarillo (WARNING)")
logger.error("Mensaje rojo (ERROR)")
logger.critical("Mensaje rojo fuerte (CRITICAL)")
