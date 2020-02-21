# Write a Python program to find the available built-in modules
import sys
import textwrap
class availableBuiltinModules:
    def BuiltinModules(self):
        module_name = ', '.join(sorted(sys.builtin_module_names))
        print(textwrap.fill(module_name, width=70))
avaBuildMod=availableBuiltinModules()
avaBuildMod.BuiltinModules()