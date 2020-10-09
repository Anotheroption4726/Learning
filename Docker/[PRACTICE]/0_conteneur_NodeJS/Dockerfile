# Base de l'image (trouvée ici? https://hub.docker.com/_/debian ). Cette instruction n'est utilisable qu'une seule fois dans un Dockerfile
FROM debian:9


# L'instruction RUN permet d'éxecuter une ou plusieures commande(s) dans le conteneur. Ici on ajoute NodeJS.
# ! Attention ! Il faut éviter d'utiliser trop de fois la commande RUN. Cela va créer plusieurs états dans le conteneur et donc alourdir l'image résultante.
RUN apt-get update -yq \
   && apt-get install curl gnupg -yq \
   && curl -sL https://deb.nodesource.com/setup_10.x | bash \
   && apt-get install nodejs -yq \
   && apt-get clean -y


# Copie le contenu du répertoire courant depuis la machine vers le dossier /app/ de l'image Docker en cours de construction
ADD . /app/


# Spécifie le répertoire courant pour la suite de la recette. Equivalent à une commande cd en ligne de commande. L'ensemble des commandes qui suivront seront toutes exécutées depuis le répertoire défini
WORKDIR /app

# Instruction RUN (voir plus haut). Ici on installe le package du projet Node.js
RUN npm install

# L'instruction EXPOSE permet d'indiquer le port sur lequel l'application écoute
EXPOSE 2368

# L'instruction VOLUME permet d'indiquer quel répertoire on veut partager avec le host
VOLUME /app/logs

# Cette instruction permet à notre conteneur de savoir quelle commande il doit exécuter lors de son démarrage. Cette instruction doit toujours être présente dans le Dockerfile
CMD npm run start


# docker build  -t ocr-docker-build .
# docker run -d -p 2368:2368 ocr-docker-build