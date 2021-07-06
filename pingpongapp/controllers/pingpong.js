const { response } = require("express");
const fs = require("fs");
const { request } = require("http");
const path = require("path");

const pingpongRouter = require("express").Router();
const directory = __dirname + "/../files";
if (!fs.existsSync(directory)) {
  fs.mkdirSync(directory);
}

const filePath = path.join(directory, "pongs.txt");

let pong = 0;

pingpongRouter.get("/", (request, response) => {
  pong += 1;
  fs.writeFile(filePath, `Ping / Pongs: ${pong}`, (err) => {
    if (err) return console.log(err);
  });
  return response.json({ pong: `${pong}` });
});

pingpongRouter.get("/pongcount", (request, response) => {
  return response.json({ pong: `${pong}` });
});

module.exports = pingpongRouter;
