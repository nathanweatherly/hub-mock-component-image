FROM node:14

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . .

COPY ./bin/controller /
COPY ./bin/proxyserver /
COPY ./bin/webhook /

EXPOSE 3000
CMD [ "node", "app.js" ]