FROM node:lts-alpine

WORKDIR /app

COPY package*.json ./

RUN npm i

RUN npm install

COPY . .

EXPOSE 5173

#CMD ["npm", "run", "dev"]
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
