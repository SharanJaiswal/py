# No matter if there is content in __init__.py or not, but this file assures that the enclosing folder of this file is a package.
# A python package will have __init__.py file. Also, a folder conataing the __init__.py file is a pyhton package.
# The code writtern in the __init__.py file runs whwnever the package is imported to any other script.

# To load a module, python will look in the print(sys.path):
#   directory that conatains the current python script
#   pyhton path env var
#   std lib dirs
#   Now python will look in the extra path added in the sys.path list variable
#   This added path is specific to the given script. not for the env.
#           import sys
#           sys.path.append('path_to_module')
#   website packages
#
# One can see the location of the imported module by printing print(<module>.__file__)

# If this line is not written and the shortcut is used in the importing scripts, then this will throw th ImportError
from .arith import Coords   # from .package_name_hierarchy import direct_import_entities