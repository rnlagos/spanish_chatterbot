# Spanish Chatterbot with teaching forms

I just refactor the chatterbot code, now can speak in spanish and you can teach the bot.|| He retocado el código de Chatterbot para que entienda el español.

![Spanish Chatterbot](https://tasarte.app/PDF/mongui_b.png)

The original code is here: 'https://github.com/gunthercox/chatterbot', I add the forms in the html template, refactor app.py to add the functionality and add some lines in the CSS file. || El código original lo puedes encontrar aquí: 'https://github.com/gunthercox/chatterbot', he añadido los campos en el template del html y añadido algo de código en el archivo app.py y en los estilos CSS.

Once the question and answer form is filled in, the output data (json) must be processed so that the bot understands it (yaml). For that we will use sed. || Para enseñar al bot, una vez que se rellenan los capos de pregunta y respuesta y se envía el formulario, se genera un archivo json que hay que convertir a yml para que lo entienda el bot, he usado sed para hacerlo.

1.- Format the json file and make a .bak file. || Formateo el json y hago un backup.

``sudo sed -i.bak -e 's/^.*nta":/- -/' -e 's/^.*esta":/  -/' -e 's/,$//' -e 's/{$//' -e 's/}$//' -e 's/#.*//;/^$/d' file.json``

2.-  Make a copy in yaml format. || Convierto el json a yml.

``sudo sed -n '/categories/,$w learn.yml' file.json``

3.- We need now to make a symlink for the corpus. || Hago un symlink a la carpeta con el archivo yaml (chatterbot_corpus/data/spanish)

``sudo ln -s /var/www/html/chatbot/learn.yml /usr/local/lib/python3.8/dist-packages/chatterbot_corpus/data/spanish/learn.yml``

You can automate all of this with a .sh file and a cron job. || Puedes automatizarlo con un .sh y un cron.

I do it just for fun and learn. You can see it in action: https:bot.tasarte.app.
