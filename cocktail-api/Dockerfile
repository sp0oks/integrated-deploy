FROM node:alpine

ADD package.json /tmp/package.json
RUN cd /tmp && \
    npm install && \
    mkdir -p /app && \
    mv /tmp/node_modules /app

WORKDIR /app
COPY . .

EXPOSE 3000

CMD ["npm", "run", "start"]