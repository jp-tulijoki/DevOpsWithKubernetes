const express = require("express");
const app = express();
const cors = require("cors");
const http = require("http");
const pingpongRouter = require("./controllers/pingpong");

app.use(cors());
app.use(express.static("build"));
app.use(express.json());

app.use("/", pingpongRouter);

const server = http.createServer(app);

const PORT = 3000;
server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}.`);
});
