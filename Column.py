from enum import Enum

class Column(Enum):
    AMOUNT = "TRANSACTION_AMOUNT"
    DATE = "TRANSACTION_DATE"
    NAME = "TRANSACTION_NAME"
    USAGE = "USE IN ANALYSIS"
    GROUP = "GROUP"