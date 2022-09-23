##When importing a local python file, if the file is in the same directory, you put a . before the filename
##If the file is in a parent directory, you put .. before the filename
##If the file is in a grandparent directory, you put a . for every directory

#same directory
from .example import *

#parent directory
from ..example import *

#grandparent directory
from ....example import *