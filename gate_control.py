from threading import Timer
from logger import logger

# --- Initialization ---
try:
    from gpiozero import OutputDevice
    GPIO_AVAILABLE = True
except Exception as e:
    GPIO_AVAILABLE = False
    print(f"GPIO nicht verfügbar – Dummy-Modus aktiv: {e}")

# Global variable for output pin
alarm_pin = None

if GPIO_AVAILABLE:
    try:
        alarm_pin = OutputDevice(17)  # GPIO17
    except Exception as e:
        print(f"GPIO initialization error: {e}")
        GPIO_AVAILABLE = False


def activate_pin():
    """set GPIO-pin to HIGH"""
    if not GPIO_AVAILABLE or alarm_pin is None:
        return
    
    alarm_pin.on()
    logger.info("output pin set to high")


def deactivate_pin():
    """set GPIO-pin to LOW"""
    if not GPIO_AVAILABLE or alarm_pin is None:
        return
    
    alarm_pin.off()
    logger.info("output pin set to low")


def open_gate(duration=5):
    """
    Activates the GPIO-Pin for a few seconds depending on the duration parameter
    and deactivates it afterwards (non-blocking)
    """
    logger.info("opening gate if possible")
    if not GPIO_AVAILABLE or alarm_pin is None:
        logger.error("gpio not available - opening gate cancelled")
        return

    activate_pin()

    # automatically deactivate after duration seconds
    Timer(duration, deactivate_pin).start()