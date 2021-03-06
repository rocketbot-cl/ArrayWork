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
import json
"""
    Obtengo el modulo que fue invocado
"""
module = GetParams("module")


if module == "deleteArray":

    try:
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
    except Exception as e:
        PrintException()
        raise e

if module == "addArray":

    try:
        array_ = GetParams('array_')
        position_ = GetParams('position_')
        value_ = GetParams('value_')
        var_ = GetParams('var_')
        num = GetParams('num')
        array_ = eval(array_)
        print(array_,position_,value_,num)

        if not value_:
            raise Exception("value empty")

        if "," in value_:
            if not position_:
                v = value_.split(',')
                print(v)
                for a in v:
                    if num == True:
                        array_.append(int(a))
                        print('fin',array_)
                    else:
                        array_.append(a)

        if position_:
            if "," not in value_:
                b = array_[:]
                if num == True:
                    b.insert(int(position_), int(value_))
                    array_ = b
                else:
                    b.insert(int(position_), value_)
                    array_ = b
            else:
                raise Exception('Just one value')

        if not position_ and "," not in value_:
            if num == True:
                array_.append(int(value_))
            else:
                array_.append(value_)


        SetVar(var_, array_)
    except Exception as e:
        PrintException()
        raise  e

