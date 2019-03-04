def findclass(type_or_string,module_string=None):
        typeVar = type_or_string
        if isinstance(type_or_string, str):
            if module_string == None:
                typeVar = globals()[type_or_string]
            else:
                import importlib
                moduleIn = importlib.import_module(module_string)
                importlib.reload(moduleIn)
                typeVar = getattr(moduleIn ,type_or_string)
        return typeVar
