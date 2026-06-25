from ops.add import add
from ops.subtract import subtract
from ops.multiply import multiply
from ops.divide import divide
from ops.power import power
from ops.floor_divide import floor_divide
from ops.avg import avg
from ops.minimum import minimum
from ops.root import root

operations = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
    "power": power,
    "floor_divide": floor_divide,
    "avg": avg,
    "minimum": minimum,
    "root": root,
}
