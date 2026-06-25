from ops.add import add
from ops.avg import avg
from ops.divide import divide
from ops.max import max
from ops.minimum import minimum
from ops.multiply import multiply
from ops.power import power
from ops.root import root
from ops.subtract import subtract

operations = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
    "power": power,
    "max": max,
    "min": minimum,
    "root": root,
    "avg": avg,
}
