# Palabras
Taller6
1. ¿Qué diferencia existe entre aplicar lower() y modificar directamente un carácter
de la cadena?
2. ¿Por qué split() devuelve una lista y no una tupla?
3. ¿Qué resultado se obtiene con "Hola hola".lower().count("hola")?
4. ¿Qué ocurriría si se intentara ejecutar resumen[0] = 100?
5. ¿En qué situación del ejercicio sería más conveniente una lista que una tupla?

RESPUESTAS

1. Lo que hace el lower es no solo modificar un carácter sino que modifica todos los caracteres que se encuentren en el conjunto como: "PIZZA" a "pizza" entonces facilita el trabajo.
2. El método split() devuelve una lista porque su propósito principal es la manipulación sencilla o dinamica de los datos obtenidos. Las listas son mutables, lo que te permite:
   Modificar, agregar o eliminar palabras de los resultados de forma directa.
   Ordenar o invertir el orden de los elementos fácilmente.
   Si devolviera una tupla (que es inmutable), cualquier operación de edición posterior requeriría convertir los datos a una lista para ser capaces de modificarlos lo que complicaría el trabajo.
3. Lo primero que hace es bajar los holas a todos en minuscula "hola hola", despues el .count ya que tiene al hola entre parentesis busca y cuenta cuántas veces aparece exactamente la palabra "hola". Como ambas palabras ahora coinciden por completo, el conteo final es dos.
4. El resultado depende de qué tipo de estructura de datos sea resumen:
 Si resumen es una tupla (o una cadena), Python lanzará un TypeError: 'tuple'. Esto ocurre porque las tuplas son inmutables y no permiten reasignar sus elementos. Si resumen es una lista, la operación se ejecutará bien y el primer elemento de la lista cambiará su valor original por el número 100.
5. En cuando hay que manipular texto o procesar datos, una lista es más conveniente cuando:
El número de elementos cambia, Si necesitas ir guardando palabras una a una a medida que las vas encontrando en un texto (usando .append()) o necesitas limpiar o transformar los datos, Si planeas eliminar conectores (como "de", "del", "la"), ordenar las palabras alfabéticamente o corregir errores en los elementos procesados.

Descripcion: Proycto para analizar palabras.
   [Imagenes](https://github.com/Midnight-CEO/Palabras/tree/main/Fotosgithub_taller_6)
