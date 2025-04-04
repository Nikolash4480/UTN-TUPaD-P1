***Trabajo Practico N°2 - Trabajo Colaborativo***

*Alumno: Nikolas Barroso*

pd: el formato en el que se ve, es porque en realidad realice el tp en la herramienta Obsidian y luego lo pase a este archivo.

### **¿Qué es GitHub?**  
GitHub es una plataforma en línea para alojar proyectos con Git. Permite colaborar en código, gestionar issues, revisar cambios con pull requests y automatizar tareas con CI/CD. Es ampliamente usado en desarrollo de software.  

### **¿Cómo crear un repositorio en GitHub?**  
- Ve a tu perfil en GitHub.  
- Haz clic en **+** > **New repository**.  
- Elige nombre, descripción y visibilidad (público/privado).  
- Opcional: Añade un archivo `README`, `.gitignore` o licencia.  
- Confirma con **Create repository**.  

### **¿Cómo crear una rama en Git?**  
```bash
git branch main   
git checkout main
# O en un solo comando:  
git checkout -b main 
```

### **¿Cómo fusionar ramas en Git?**  
1. Posiciónate en la rama destino (ej. `main`):  
   ```bash
   git checkout main
   ```  
2. Fusiona la otra rama:  
   ```bash
   git merge otra-rama
   ```  

### **¿Cómo crear un commit?**  
1. Añade los cambios al área de staging:  
   ```bash
   git add archivo.txt  # o `git add .` para todos  
   ```  
2. Guarda el commit:  
   ```bash
   git commit -m "Mensaje descriptivo"  
   ```  

### **¿Cómo enviar un commit a GitHub?**  
```bash
git push origin main  
```

### **¿Qué es un repositorio remoto?**  
Es una copia del repositorio guardada en un servidor (como GitHub). Sirve para sincronizar trabajo entre equipos.  

### **¿Cómo agregar un repositorio remoto a Git?**  
```bash
git remote add origin https://github.com/usuario/repo.git  
```

### **¿Cómo empujar cambios a un repositorio remoto?**  

1. **Confirma tus cambios:**
    `git status`
    
2. **Empuja los cambios:**
    `git push origin main`

### **¿Cómo tirar de cambios de un repositorio remoto?**  
1. **Verifica tu directorio de trabajo:**
    `git status`
    
2. **Tira de los cambios:**
    `git pull origin main`

### **¿Qué es un fork de repositorio?**  
- Un "fork" de un repositorio es una copia personal de un proyecto en GitHub. Cuando haces un fork, creas una copia del repositorio original en tu propia cuenta de GitHub. Esto te permite experimentar con cambios sin afectar el proyecto original.
### **¿Cómo crear un fork de un repositorio?**  
- Navega al repo en GitHub.  
- Haz clic en **Fork** (arriba a la derecha).  
- Elige tu cuenta como destino.  

### **¿Cómo enviar una solicitud de extracción (pull request) a un repositorio?**  
1. Trabaja en tu fork y sube cambios.  
2. En GitHub, ve a **Pull Requests** > **New Pull Request**.  
3. Selecciona las ramas a comparar y envía la solicitud.  

### **¿Cómo aceptar una solicitud de extracción?**  
Aceptar una solicitud de extracción (pull request) en GitHub es un proceso que permite fusionar cambios propuestos desde un fork o una rama en tu repositorio. Aquí te explico cómo hacerlo:

### Pasos para aceptar una solicitud de extracción:

1. **Revisa la solicitud de extracción:**
	- Ve a la pestaña "Pull requests" en tu repositorio de GitHub.
	- Selecciona la solicitud que deseas revisar.

2. **Examina los cambios:**
	- Revisa los archivos modificados y los comentarios asociados.
	- Asegúrate de que los cambios cumplen con los estándares del proyecto.

3. **Fusiona la solicitud:**
	- Si todo está bien, haz clic en el botón "Merge pull request".
	- Confirma la fusión.

4. **Cierra la solicitud:**
	- Una vez fusionada, la solicitud de extracción se cerrará automáticamente.
### **¿Qué es una etiqueta en Git?**  
Es un marcador para versiones específicas (ej. `v2.1.0`). Se usa comúnmente en releases.  

### **¿Cómo crear una etiqueta?**  
```bash
git tag -a v1.0.0 -m "Versión estable"  
git push origin v1.0.0     # Subirla a GitHub  
```
### **¿Cómo enviar una etiqueta a GitHub?**

1. **Crear la etiqueta:**
   - Primero, asegúrate de estar en la rama correcta.
   - Crea la etiqueta con un mensaje:
     ```bash
     git tag -a v1.0.0 -m "Versión 1.0.0"
     ```
   - O sin mensaje:
     ```bash
     git tag v1.0.0
     ```

2. **Subir la etiqueta:**
   - Para subir una sola etiqueta:
     ```bash
     git push origin v1.0.0
     ```
   - Para subir todas las etiquetas:
     ```bash
     git push origin --tags
     ```

### **¿Qué es un historial de Git?**

- El historial de Git es un registro cronológico de todos los cambios realizados en un proyecto. Incluye información detallada sobre cada commit, como el autor, la fecha y el mensaje descriptivo. Permite rastrear la evolución del proyecto y entender quién hizo qué cambios y cuándo.

### **¿Cómo ver el historial de Git?**

- Usa el comando:
  ```bash
  git log
  ```
- Esto muestra una lista de commits con detalles sobre cada cambio, como el autor y la fecha.
- Puedes personalizar la salida con opciones adicionales, como:
  ```bash
  git log --oneline
  ```
  para ver una versión más compacta.

### **¿Cómo buscar en el historial de Git?**

- Para buscar commits específicos, usa:
  ```bash
  git log --grep="palabra_clave"
  ```
- También puedes filtrar por autor:
  ```bash
  git log --author="nombre_autor"
  ```
- O buscar cambios en un archivo específico:
  ```bash
  git log -- archivo.txt
  ```

### **¿Cómo borrar el historial de Git?**

  ```bash
  git reset --hard HEAD~1
  ```
 
- Para eliminar commits de un repositorio remoto, necesitas forzar el push:
  ```bash
  git push origin --force
  ```
### **¿Qué es un repositorio privado en GitHub?**

- Un repositorio privado en GitHub es un espacio donde puedes almacenar y gestionar tu código sin que sea visible para el público.
- Solo las personas que invites pueden ver, clonar o contribuir al repositorio.
- Es ideal para proyectos confidenciales o propiedad intelectual que no deseas compartir abiertamente.
### **¿Cómo crear un repositorio privado en GitHub?**

1. **Crear un nuevo repositorio:**
   - Haz clic en el ícono "+" en la esquina superior derecha y selecciona "New repository".

2. **Configurar el repositorio:**
   - Elige un nombre para tu repositorio.
   - Selecciona la opción "Private" para hacerlo privado.
   - Configura otras opciones según tus necesidades y haz clic en "Create repository".
### **¿Cómo invitar a alguien a un repositorio privado en GitHub?**

1. **Accede al repositorio:**
   - Ve a la página principal del repositorio privado en GitHub.

2. **Ir a la configuración:**
   - Haz clic en la pestaña "Settings" en la parte superior.

3. **Invitar colaboradores:**
   - En el menú de la izquierda, selecciona "Manage access".
   - Haz clic en "Invite a collaborator".
   - Ingresa el nombre de usuario o la dirección de correo electrónico de la persona que deseas invitar y selecciona el nivel de acceso.
   - Haz clic en "Add (ej: "Nikolash4480") to this repository" para enviar la invitación.
### **¿Qué es un repositorio público en GitHub?**

- Un repositorio público en GitHub es un espacio donde puedes almacenar y gestionar tu código de manera que sea visible para cualquier persona en internet.
- Cualquiera puede ver, clonar y, en algunos casos, contribuir al proyecto.
- Es ideal para proyectos de código abierto y colaboraciones comunitarias.
### **¿Cómo crear un repositorio público en GitHub?**

1. **Crear un nuevo repositorio:**
   - Haz clic en el ícono "+" en la esquina superior derecha y selecciona "New repository".

2. **Configurar el repositorio:**
   - Elige un nombre para tu repositorio.
   - Selecciona la opción "Public" para hacerlo público.
   - Configura otras opciones según tus necesidades y haz clic en "Create repository".
### **¿Cómo compartir un repositorio público en GitHub?**

1. **Accede al repositorio:**
   - Ve a la página principal del repositorio público en GitHub.

2. **Copiar el enlace:**
   - Copia la URL del repositorio desde la barra de direcciones de tu navegador.

3. **Compartir el enlace:**
   - Envía el enlace a quien desees compartir el repositorio.
   - Puedes compartirlo a través de correo electrónico, redes sociales o cualquier otra plataforma.

4. **Invitar a colaboradores (opcional):**
   - Si deseas que otros contribuyan, puedes invitarlos a colaborar directamente desde la configuración del repositorio.
### 2) Realizar la siguiente actividad:
**• Crear un repositorio.** 
	1. Dale un nombre al repositorio. 
	2. Elije el repositorio sea público. 
	3. Inicializa el repositorio con un archivo. 
**• Agregando un Archivo** 
	4. Crea un archivo simple, por ejemplo, "mi-archivo.txt". 
	5. Realiza los comandos git add . y git commit -m "Agregando mi-archivo.txt" en la línea de comandos. 
	6. Sube los cambios al repositorio en GitHub con git push origin main (o el nombre de la rama correspondiente).
- **Creando Branchs** 
	1. Crear una Branch 
	2. Realizar cambios o agregar un archivo 
	3. Subir la Branch

**link del repo:** https://github.com/Nikolash4480/repo-tp2