__all__ = ['test2res']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['ModuloDexpo', 'Encodage', 'ValeurChar', 'CodageGroupSize', 'standard', 'CodageTableChar', 'Encode'])
@Js
def PyJsHoisted_standard_(entree, this, arguments, var=var):
    var = Scope({'entree':entree, 'this':this, 'arguments':arguments}, var)
    var.registers(['entree'])
    var.put('alphabet', Js('0123456789'))
    var.put('longueur', var.get('entree').get('length'))
    var.put('entree_standard', Js(''))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('longueur')):
        try:
            if (var.get('alphabet').callprop('indexOf', var.get('entree').callprop('charAt', var.get('i')))!=(-Js(1.0))):
                var.put('entree_standard', var.get('entree').callprop('charAt', var.get('i')), '+')
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('entree_standard')
PyJsHoisted_standard_.func_name = 'standard'
var.put('standard', PyJsHoisted_standard_)
@Js
def PyJsHoisted_ValeurChar_(Lettre, this, arguments, var=var):
    var = Scope({'Lettre':Lettre, 'this':this, 'arguments':arguments}, var)
    var.registers(['Lettre'])
    return var.get('CodageTableChar').callprop('indexOf', var.get('Lettre'), Js(0.0))
PyJsHoisted_ValeurChar_.func_name = 'ValeurChar'
var.put('ValeurChar', PyJsHoisted_ValeurChar_)
@Js
def PyJsHoisted_ModuloDexpo_(Base, Exposant, Modulo, this, arguments, var=var):
    var = Scope({'Base':Base, 'Exposant':Exposant, 'Modulo':Modulo, 'this':this, 'arguments':arguments}, var)
    var.registers(['ModuloBase2', 'Exposant', 'Modulo', 'Base'])
    var.put('ModuloBase2', var.get('Array').create())
    var.put('ModuloLevel', var.get('Math').callprop('max', var.get('Math').callprop('floor', (var.get('Math').callprop('log', var.get('Exposant'))/Js(0.6931471805599))), Js(1.0)))
    var.get('ModuloBase2').put('0', (var.get('Base')%var.get('Modulo')))
    #for JS loop
    var.put('Level', Js(1.0))
    while (var.get('Level')<=var.get('ModuloLevel')):
        try:
            var.get('ModuloBase2').put(var.get('Level'), ((var.get('ModuloBase2').get((var.get('Level')-Js(1.0)))*var.get('ModuloBase2').get((var.get('Level')-Js(1.0))))%var.get('Modulo')))
        finally:
                (var.put('Level',Js(var.get('Level').to_number())+Js(1))-Js(1))
    pass
    var.put('ExpoDec', var.get('Exposant'))
    var.put('Valeur', Js(1.0))
    var.put('Level', var.get('ModuloLevel'))
    while (var.get('ExpoDec')>Js(0.0)):
        if (var.get('ExpoDec')>=var.get('Math').callprop('pow', Js(2.0), var.get('Level'))):
            var.put('Valeur', ((var.get('Valeur')*var.get('ModuloBase2').get(var.get('Level')))%var.get('Modulo')))
            var.put('ExpoDec', var.get('Math').callprop('pow', Js(2.0), (var.put('Level',Js(var.get('Level').to_number())-Js(1))+Js(1))), '-')
        else:
            (var.put('Level',Js(var.get('Level').to_number())-Js(1))+Js(1))
        pass
    return var.get('Valeur')
PyJsHoisted_ModuloDexpo_.func_name = 'ModuloDexpo'
var.put('ModuloDexpo', PyJsHoisted_ModuloDexpo_)
@Js
def PyJsHoisted_Encodage_(Message, E, N, this, arguments, var=var):
    var = Scope({'Message':Message, 'E':E, 'N':N, 'this':this, 'arguments':arguments}, var)
    var.registers(['Message', 'N', 'E'])
    var.put('messageNum', Js(''))
    var.put('PreSize', var.get('Math').callprop('ceil', (var.get('Math').callprop('log', var.get('N'))/var.get('Math').get('LN10'))))
    var.put('TailleGroupe', var.get('parseInt')(var.get('Groupage').get('value')))
    var.put('CodageTableChar', var.get('TableConv').get('value'))
    #for JS loop
    var.put('k', Js(0.0))
    while (var.get('k')<var.get('Message').get('length')):
        try:
            var.put('chiffre', var.get('ValeurChar')(var.get('Message').callprop('charAt', var.get('k'))))
            if (var.get('parseInt')(var.get('chiffre'))<Js(10.0)):
                var.put('chiffre', (Js('0')+var.get('chiffre')))
            pass
            var.put('messageNum', var.get('chiffre'), '+')
        finally:
                (var.put('k',Js(var.get('k').to_number())+Js(1))-Js(1))
    while ((var.get('messageNum').get('length')%var.get('TailleGroupe'))>Js(0.0)):
        var.put('messageNum', (Js('0')+var.get('messageNum')))
    var.put('MessageCode', Js(''))
    #for JS loop
    var.put('k', Js(0.0))
    while (var.get('k')<var.get('messageNum').get('length')):
        try:
            var.put('GroupeValue', var.get('parseInt')(var.get('messageNum').callprop('substring', var.get('k'), (var.get('k')+var.get('TailleGroupe'))), Js(10.0)))
            var.put('GroupePreCode', var.get('ModuloDexpo')(var.get('GroupeValue'), var.get('E'), var.get('N')))
            var.put('xx', var.get('GroupePreCode').callprop('toString'))
            while (var.get('xx').get('length')<var.get('PreSize')):
                var.put('GroupePreCode', (Js('0')+var.get('GroupePreCode')))
                var.put('xx', var.get('GroupePreCode').callprop('toString'))
            var.put('MessageCode', var.get('GroupePreCode'), '+')
            var.put('MessageCode', Js(' '), '+')
        finally:
                var.put('k', (var.get('k')+var.get('TailleGroupe')))
    pass
    return var.get('MessageCode')
PyJsHoisted_Encodage_.func_name = 'Encodage'
var.put('Encodage', PyJsHoisted_Encodage_)
@Js
def PyJsHoisted_Encode_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    var.get('Crypte').put('value', var.get('Encodage')(var.get('Texte').get('value'), var.get('E').get('value'), var.get('N').get('value')))
PyJsHoisted_Encode_.func_name = 'Encode'
var.put('Encode', PyJsHoisted_Encode_)
var.put('CodageGroupSize', Js(0.0))
var.put('CodageTableChar', Js(''))
var.put('CodageTableChar', (Js("0123456789 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ&~#|*+-\\/=%!:;?,.<>'àâçéèêëïîöôüûù")+Js('"')))
var.get('TableConv').put('value', var.get('CodageTableChar'))
pass
var.put('p', (Js(0.0) if (var.get('P').get('value')==Js('')) else var.get('P').get('value')))
var.put('q', (Js(0.0) if (var.get('Q').get('value')==Js('')) else var.get('Q').get('value')))
var.put('n', (var.get('p')*var.get('q')))
var.get('N').put('value', var.get('parseFloat')(var.get('n')))
var.put('Euler', (((var.get('n')-var.get('p'))-var.get('q'))+Js(1.0)))
var.put('e', (Js(0.0) if (var.get('E').get('value')==Js('')) else var.get('E').get('value')))
var.put('TmpNe', Js(1.0))
var.put('d', Js(1.0))
while (((var.get('d')*var.get('e'))%var.get('Euler'))!=Js(1.0)):
    var.put('TmpNe', Js(1.0), '+')
    var.put('d', var.get('Math').callprop('ceil', ((var.get('TmpNe')*var.get('Euler'))/var.get('e'))))
pass
var.get('D').put('value', var.get('parseFloat')(var.get('d')))
var.put('CodageGroupSize', var.get('Groupage').get('value'))
if ((var.get('CodageTableChar').get('length')*var.get('Math').callprop('pow', Js(100.0), (var.get('CodageGroupSize')-Js(1.0))))>var.get('n')):
    var.get('alert')(Js("P ou Q risquent d'être trop petits pour un chiffrement valable !"))
pass
pass
pass
pass
pass
pass
pass
var.get('Crypte').put('value', var.get('Encodage')(var.get('Texte').get('value'), var.get('E').get('value'), var.get('N').get('value')))
pass
pass
pass


# Add lib to the module scope
test2res = var.to_python()