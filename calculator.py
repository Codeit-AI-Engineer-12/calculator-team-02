from ops.add import add
from ops.subtract import subtract
from ops.multiply import multiply
from ops.divide import divide
from ops.power import power
from ops.minimum import minimum
from ops.root import root
from ops.avg import avg

operations = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
    "power": power,
    "min": minimum,
    "root": root,
    "avg": avg,
}