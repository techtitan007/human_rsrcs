const { createServer } = require("http");
const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('hrms.db');

const server = createServer((req, res) => {
  if (req.url === '/employees') {
    
    db.all('SELECT * FROM employees', [], (err, rows) => {
      if (err) {
        console.error('Error retrieving employees:', err);
        res.statusCode = 500;
        res.end('Internal Server Error');
        return;
      }
      
      
      res.statusCode = 200;
      res.setHeader('Content-Type', 'application/json');
      res.end(JSON.stringify(rows));
    });
  } else {
    res.statusCode = 404;
    res.end('Not Found');
  }
});

server.listen(3000, () => {
  console.log('Server is running on port 3000');
});
