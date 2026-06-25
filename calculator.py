from ops.add import add
from ops.subtract import subtract
from ops.multiply import multiply
from ops.divide import divide
from ops.power import power
from ops.minimum import minimum

operations = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
    "power": power,
    "min": minimum,
}
