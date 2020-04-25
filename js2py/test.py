import js2py
code1='function f(x) {return x+x;}'
f=js2py.eval_js(code1)
print(f)