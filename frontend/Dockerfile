FROM node:19 as build

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 4173
EXPOSE 5173

CMD ["npm","run", "dev","--", "--host", "0.0.0.0"]
