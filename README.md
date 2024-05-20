# CSCustomWelcomer
A Discord bot that allows you to customize welcome and goodbye messages for users on your server, now ready!

### Requirements
- Python 3
- discord.py
- A bot account

### Support
[Discord](https://discord.gg/htyNZJNXPU)

### Instalacion (English Guide in progress)
#### Descarga la version mas reciente
Ve a la seccion Releases, y descarga el archivo "CSCustomWelcomer.py" de la version mas reciente del bot.
#### Crea una cuenta de bot
Ingresa al [Discord Developer Portal](https://discord.com/developers/applications/) y crea una cuenta de bot siguiendo las instrucciones a continuacion.
 - Crea una aplicacion

Pulsa el boton "New Application" en la esquina superior derecha.

<img src="https://github.com/DeltaGamesYT/cs-custom-welcomer/assets/127041376/16490d94-1dac-4945-8b97-698c82293543" width="40%" /> <br>
 - Ingresa el nombre de tu bot, y crea la aplicacion

<img src="https://github.com/DeltaGamesYT/cs-custom-welcomer/assets/127041376/6022335b-9dd4-4a2b-beed-bed7af6801d7" width="40%" /> <br>
 - Abre la seccion bot

<img src="https://github.com/DeltaGamesYT/cs-custom-welcomer/assets/127041376/e533c9a6-4a2f-4647-90e4-eb64b49dda79" width="40%" /> <br>
- Reinicia el token del bot y copialo

<img src="https://github.com/DeltaGamesYT/cs-custom-welcomer/assets/127041376/d1d26588-0de7-4949-9966-bba5b232c0d8" width="40%" /> <br>

#### Modifica las variables de configuracion
Abre el archivo con un editor de codigo, y modifica las variables como se especifica a continuacion.
 - bot_token, linea 6

Pega el token del bot que copiaste antes, guardalo como STRING
 - welcome_id, linea 8

Pega el ID del canal donde se enviaran las bienvenidas, guardalo como INT
 - leave_id, linea 10

Pega el ID del canal donde se enviaran los mensajes de salida, guardalo como INT
 - welcome_msg, linea 12

Escribe el mensaje de bienvenida. `[member.mention]` mencionara al miembro, y `[guild.name]` mostrara el nombre del servidor.
 - leave_msg, linea 15

Escribe el mensaje de salida, `[member.name]` se reemplazara por el nombre de usuario, y `[guild.name]` por el nombre del servidor.
#### Ejecuta el bot
Subelo a un servidor online, o ejecutalo en local con Python:

Instala discord.py
```
pip install discord
```
Ejecuta el bot
```
python CSCustomWelcomer.py
```
