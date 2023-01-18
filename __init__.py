# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

"""
    Obtengo el modulo que fue invocado
"""

module = GetParams("module")


'''
Funciones del módulo
'''
def search(element, table):
    valuesFound = []
    positionX = 1
    positionY = 1
    for rowsX in element:
        for columnsY in rowsX:
            if columnsY == table:
                finalPosition = (positionX,positionY)
                valuesFound.append(finalPosition)
            positionX = positionX + 1
        positionY = positionY + 1
        positionX = 1
    return valuesFound

def delete(array_, option_, value_):
    if not option_ and not value_:
        raise Exception("option or value empty")

    if "," in value_:
        if option_ == "position_":
            raise Exception('Just one value')

        if option_ == "value_":
            v = value_.split(',')
            for a in v:
                array_.remove(a)
    else:
        if option_ == "position_":
            array_.pop(int(value_))

        if option_ == "value_":
            array_.remove(value_)
    return array_

def add(array_, position_, value_):
    if not value_:
        raise Exception("value empty")

    if not array_:
        raise Exception("Array field is empty")

    array_ = eval(array_)
    try:
        print(value_)
        value_ = eval(value_)
    except NameError:
        pass

    if not position_:
        print(position_)
        position_ = len(array_)
        
    position_ = int(position_)
    array_.insert(position_, value_)
    
    return array_

def filter(array_, data, condition):
    if array_:
        array_ = eval(array_)

    filtered_list = []
    

    for element in array_:
        type_ = type(element)
        if type_ == str:
            data_f = f"'{data}'"
            element_parsed = f"'{element}'"
        else:
            data_f = f"{data}"
            element_parsed = f"{element}"
        string = f"{element_parsed} {condition} {data_f}"
        print(string, eval(string))
        if eval(string):
            filtered_list.append(element)
            
    return filtered_list


try:

    if module == "searchInArray":

        varSearchValue = GetParams("varSearchValue")
        varArrayToSearch = GetParams("varArrayToSearch")
        varSelectedForResult = GetParams("varSelectedForResult")
        varArrayToSearch = eval(varArrayToSearch)

        valuesFound = search(varArrayToSearch, varSearchValue)

        SetVar(varSelectedForResult, valuesFound)

    if module == "deleteArray":

        array_ = GetParams('array_')
        print('ARRAY: ',array_)
        option_ = GetParams('option_')
        value_ = GetParams('value_')
        var_ = GetParams('var_')
        array_ = eval(array_)

        array_delete = delete(array_, option_, value_)

        SetVar(var_, array_delete)


    if module == "addArray":

        array_ = GetParams('array_')
        position_ = GetParams('position_')
        value_ = GetParams('value_')
        var_ = GetParams('var_')
        num = GetParams('num')

        array_add = add(array_, position_, value_, num)

        SetVar(var_, array_add)

        
    if module == "filter":
        array_ = GetParams('array_')
        data = GetParams('data')
        condition = GetParams('condition')
        result = GetParams('var_')

        array_filtered = filter(array_, data, condition)

        if result:
            SetVar(result, array_filtered)

    if module == "length":
        array_ = GetParams('array_')
        result = GetParams('var_')

        if array_:
            array_ = eval(array_)

        if result:
            SetVar(result, len(array_))

except Exception as e:
    PrintException()
    raise e

