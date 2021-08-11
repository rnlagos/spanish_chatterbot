# Spanish Chatterbot with teaching forms

I just refactor the chatterbot code, now is in spanish and you can teach the bot.

![Spanish Chatterbot](https://tasarte.app/PDF/mongui.png)

The original code is here: 'https://github.com/gunthercox/chatterbot', I add the forms in the html template, refactor app.py to add the functionality and add some lines in the CSS file.

Once the question and answer form is filled in, the output data (json) must be processed so that the bot understands it (yaml). For that we will use sed.

1.- Format the json file and make a .bak file.

``sudo sed -i.bak -e 's/^.*nta":/- -/' -e 's/^.*esta":/  -/' -e 's/,$//' -e 's/{$//' -e 's/}$//' -e 's/#.*//;/^$/d' file.json``

2.-  Make a copy in yaml format.

``sudo sed -n '/categories/,$w learn.yml' file.json``

3.- We need now to make a symlink fot the corpus.

``sudo ln -s /var/www/html/chatbot/learn.yml /usr/local/lib/python3.8/dist-packages/chatterbot_corpus/data/spanish/learn.yml``

Yoy can automate all of this with a cron job.

I do it, just for fun and learn.
