from ops.add import add
from ops.avg import avg
from ops.divide import divide
from ops.floor_divide import floor_divide
from ops.max import max
from ops.minimum import minimum
from ops.multiply import multiply
from ops.power import power
from ops.root import root
from ops.subtract import subtract
from ops.mod import mod
from ops.fact import fact
from ops.percent import percent

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
    "floor_divide": floor_divide,
    "mod": mod,
    "fact": fact,
    "percent": percent
}
