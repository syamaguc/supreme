import shutil


class ChromeOptions:
    CHROME_DRIVER_PATH = shutil.which("chromedriver")


class ProductDetails:
    KEYWORDS = ""
    COLOUR = ""
    SIZE = ""


class UserDetails:
    NAME = ""
    EMAIL = ""
    TELE = ""
    STATE = ""               # 半角スペース必要!!
    CITY = ""
    ADDRESS = ""
    POSTCODE = ""


class PaymentDetails:
    CARD_NUMBER = ""
    CVV = ""
    EXP_MONTH = ""                # Two digit month (i.e. January is "01")
    EXP_YEAR = ""               # Four digit year (2020)
