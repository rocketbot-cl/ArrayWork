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
print(module)
try:

    if module == "searchInArray":

        varSearchValue = GetParams("varSearchValue")
        varArrayToSearch = GetParams("varArrayToSearch")
        varSelectedForResult = GetParams("varSelectedForResult")
        # print("aca")
        # print(varArrayToSearch)
        # print("deberia")
        # print(eval(varArrayToSearch))
        # print("estar")
        varArrayToSearch = eval(varArrayToSearch)

        findedIn = []
        positionX = 1
        positionY = 1
        for cada in varArrayToSearch:
            for uno in cada:
                print(uno)
                if (uno == varSearchValue):
                    print("Lo hemos encontrado :)")
                    finalPosition = (positionX,positionY)
                    print(finalPosition)
                    findedIn.append(finalPosition)
                positionX = positionX + 1
            positionY = positionY + 1
            positionX = 1
        print(findedIn)

        SetVar(varSelectedForResult, findedIn)

    if module == "deleteArray":

        array_ = GetParams('array_')
        print('ARRAY: ',array_)
        option_ = GetParams('option_')
        value_ = GetParams('value_')
        var_ = GetParams('var_')
        array_ = eval(array_)

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

        SetVar(var_, array_)


    if module == "addArray":

        array_ = GetParams('array_')
        position_ = GetParams('position_')
        value_ = GetParams('value_')
        var_ = GetParams('var_')
        num = GetParams('num')
        print("working")
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

        print("insert")
        array_.insert(position_, value_)
        print("setvar")
        SetVar(var_, array_)

        
    if module == "filter":
        array_ = GetParams('array_')
        data = GetParams('data')
        condition = GetParams('condition')
        result = GetParams('var_')

        if array_:
            array_ = eval(array_)

        filtered_list = []
        if not data.isnumeric():
            data = f"'{data}'"

        for element in array_:
            if not element.isnumeric():
                element_parsed = f"'{element}'"
            string = f"{element_parsed} {condition} {data}"
            print(string)
            if eval(string):
                filtered_list.append(element)

        if result:
            SetVar(result, filtered_list)

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

