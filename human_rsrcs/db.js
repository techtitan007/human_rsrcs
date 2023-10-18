const sqlite3 = require('sqlite3').verbose();


const db = new sqlite3.Database('./hrms.db');


db.run(`
  CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT
  )
`);

module.exports = db;
