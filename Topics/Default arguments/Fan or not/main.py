def add_viewer(name, funs=None):
    if funs is None:
        return [name]
    else:
        funs.append(name)
        return funs
