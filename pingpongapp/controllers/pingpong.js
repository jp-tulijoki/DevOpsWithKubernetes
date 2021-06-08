const pingpongRouter = require("express").Router();
let pong = 0;

pingpongRouter.get("/", (request, response) => {
  pong += 1;
  return response.json({ pong: `${pong - 1}` });
});

module.exports = pingpongRouter;
