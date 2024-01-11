#!/usr/bin/env zxpy

# Ejecutar el comando curl para obtener el contenido de la página web de Google
resultado = ~"curl google.es"

# Iterar sobre cada línea en la salida del comando y mostrar el índice y el contenido
for index, line in enumerate(resultado.splitlines()):
    print(index, line)

# Resultado por consola

# ❯ zxpy ejejmplo5.py
# 0   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
# 1                                  Dload  Upload   Total   Spent    Left  Speed
# 2
# 3   0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
# 4   0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
# 5 100   218  100   218    0     0    427      0 --:--:-- --:--:-- --:--:--   427
# 6 <HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
# 7 <TITLE>301 Moved</TITLE></HEAD><BODY>
# 8 <H1>301 Moved</H1>
# 9 The document has moved
# 10 <A HREF="http://www.google.es/">here</A>.
# 11 </BODY></HTML>
