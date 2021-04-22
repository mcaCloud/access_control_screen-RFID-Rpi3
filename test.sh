#!/bin/bash
#The “#!” combo is called a shebang by most Unix geeks.
#This is used by the shell to decide which interpreter to run the rest of the script, and ignored by the shell that actually runs the script.

# This is just an example. It simply prints all passed parameters and sleeps
# 5 seconds.
#
# Any action tile (eg. any tile with no sub items) will trigger this script.
# The names of the pages and of the clicked tile will be passed as arguments.
# Use those to decide what to do.

#$1, $2, $3, ... parámetros de posición que hacen referencia al primer, segundo, tercer, etc. parámetro pasado al script.

#$_, el último argumento pasado al último comando ejecutado (justo después de arrancar la shell, este valor guarda la ruta absoluta del comando que inicio la shell).
#$#, número total de argumentos pasados al script actual.
#$*, la lista completa de argumentos pasados al script. Esta valor es una cadena de texto.
#$@, la lista completa de argumentos pasados al script. Esta valor es una lista.
#$-, la lista de opciones de la shell actual.
#$$, el PID de la shell actual.
#$IFS, el separador utilizado para delimitar los campos.
#$?, el código de salida del pipe más reciente (es decir, de la última vez que se encadenaron varios comandos mediante el carácter pipe que se escribe como |).
#$!, el PID del último comando ejecutado en segundo plano.
#$0, el nombre de la shell o del script de shell.
## run while loop to display date and hostname on screen ##
comment="kellnerCall"
myVar="${@: -1}"
echo $comment $myVar > /home/pi/pimenu/txt_containers_bash/kellnerCall.txt
sleep 3
exit N
