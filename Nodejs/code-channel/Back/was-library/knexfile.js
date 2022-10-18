const path = require("path")
require("dotenv").config()

module.exports = {

  development:  {
    client: process.env.CLIENT,
    connection: {
      host: process.env.HOST,
      database: process.env.DB,
      user:     process.env.USER,
      password: process.env.PASSWORD
    },
    pool: {
      min: 2,
      max: 10
    },
    migrations: {
      directory: path.resolve(__dirname, "migrations")
    }
  }
};
