# Fundamentos-Flask
Fundamentos del framework Flask-Python.
Crear un entorno virtual de Pyton.

<py -m venv <virtualenvironmetname>> <.\virtualenvironmetname\Scripts\activate>

# Comandos útiles de Git

1. git init
2. git add <filename> / . = all
3. git status
4. git config --global user.email 'stivendiazh@gmail.com'
5. git config --global user.name 'StivenDz'
6. git commit (i-texto escrito/esc/:/wq) / git commit -m 'comentario'
7. git log (muestra el historial)/ git log --oneline
8. git checkout -- <filaname> / git checkout -- . (revierte el cambio realizado por el ultimo)/(es como un ctrl+z)
9. git diff <filename> (muestra la diferencia entre un cambio no guardado y el ultimo guardado)
10. git branch (muestra las ramas)
11. git branch <newbranchname> (crea una nueva rama)
12. git checkout <branchname> (cambio de rama/version)
13. git remote add origin <url>
14. git push -u origin <branchname> (envia el repositorio temporal/loacl al repositorio de github/remoto)
15. git reset --hard #registro: Apunto a la versión con registro digitado y todas las versiones posteriores a esa se borran
16. git commit --amend (para cambiar el mensaje del ultimo commit realizado)
17. git commit -am 'mensaje' (es la fusion de git add y git commit/dos pasos en 1)
18. git reset --mixed f52f3da (Viajamos al commit en específico f52f3da)
19. git reset --hard f52f3da (Viajamos al commit en específico f52f3da y eliminamos los cambios futuros)
20. git reflog (Muestra todos los cambios incluso si borramos los commit)
21. git reset --hard f52f3da (Viajamos al commit en específico f52f3da y podemos restaurar los archivos)
22. git mv <nombreOriginal.vue> <nombreNuevo.vue> (ambiar nombre)
23. git rm <nombreArchivo.vue> (eliminar un archivo)
24. git branch -d <nombreRama> (eliminar una rama)

# GITHUB 
  
25. git remote add origin https://github.com/bluuweb/tutorial-github.git (una sola vez/para enlazar)
26. git push -u origin <master>  (una sola vez/para enviar)
27. git remote -v (nos muestra en que repositorios remotos estamos enlazados)
28. git push (subimos todos los archivos a nuestro repositorio remoto)
29. git pull (bajar los cambios que hemos realizado en github al repositorio local)
30. git fetch (nos muestra la diferencia entre las archivos que tenemos en el repositorio remoto/github y en el repositorio local)
31. git clone https://github.com/bluuweb/tutorial-github.git nombreCarpeta (para clonar un repositorio/decargar)
  
# Comandos útiles de Linux
      <variaciones>(def)((how))
  
32. pwd (print working directory)
33. uname (impirmira informacion del dispositivo)
34. cd <cd ../cd/cd-> (change directory)
35. ls <-R/-a/-al> (all archivos en subdirectorios/all archivos ocultos/all archivos con detalles)
36. cp (copiar archivos del directorio actual a un directorio diferente)((cp docx.txt /home/documentos/imagenes))
37. mv (mover archivos/cambiar nombre del archivo)((mv docx.txt /home/documentos/textos)/(mv docx.txt doc.pdf))
38. mkdir <-p>(crear nuevo directorio/crear un directorio entre 2 existentes)((mkdir Musica/Nuevoarchivo)/(mkdir -p Musica/2020/Nuevoarchivo))
39. rmdir (delete/remove directory)
40. touch (crea un archivo)((touch app.py))
41. locate -i (localizar un archivo)((locate -i escuela*nota))(cualquier archivo que contenga la palabra escuela y nota)
42. find <-name/-type d -name> (busca archivos y directorios/ubica un archivo dentro de un directorio dado)((find /home/ -name notas.txt))
43. grep (busca el texto de un archivo)((grep azul notepad.txt))(buscará ña palabra azul en el archivo)
44. sudo (te permite realizar tareas que requieren permisos de admin)
45. df <-m/para ver en mb> (para obtener un informe sobre el usp del espacio en el disco del sistema)((df -m))
46. du <-h/verlo en todas las medidas> (verificar cuanto espacio ocupa un archivo o un directorio)
47. wget (decgarga archivos de internet)((wget url))
48. top (mostrara los procesos en ejecucion y la cantidad de CPU que utiliza ese proceso)
49. history (muestra los comandos utilizados que ingresaste anteriormente)
50. man (te muestra como utilizar un comando)((man ls))
51. hostname <-l>(nombre de tu host/(-l)red)
