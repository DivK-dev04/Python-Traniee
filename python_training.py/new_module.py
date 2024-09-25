import my_module
my_module.greeting("NHZ")                               #use the syntax: module_name.function_name

import platform                                         #built-in modules
x = platform.system()
print(x)

import platform

x = dir(platform)
print(x)