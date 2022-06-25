def findclass(type_or_string,module_string=None,context=None):
        typeVar = type_or_string
        if isinstance(type_or_string, str):
            if module_string == None:
                #print("ATTEMPTING LOOKUP")
                try:
                    if context:
                        typeVar = context[type_or_string]
                    else:
                        typeVar = globals()[type_or_string]
                except:
                    import traceback as tb
                    tb.print_exc()
                    raise Exception("Could not load class "+str(type_or_string))
                #print("FINISHED LOOKUP" + str(typevar))
            else:
                #print("ATTEMPTING IMPORT")
                import importlib
                moduleIn = importlib.import_module(module_string)
                importlib.reload(moduleIn)
                typeVar = getattr(moduleIn ,type_or_string)
        return typeVar
