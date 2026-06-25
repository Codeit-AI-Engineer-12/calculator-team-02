from ops.add import add
from ops.divide import divide
from ops.floor_divide import floor_divide
from ops.multiply import multiply
from ops.power import power
from ops.subtract import subtract

operations = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
    "power": power,
    "floor_divide": floor_divide,
}
