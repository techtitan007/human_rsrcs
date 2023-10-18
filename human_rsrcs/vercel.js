{
  "version": 2,
  "builds": [
    { "src": "employees.js", "use": "@vercel/node" },
    { "src": "^(?!api/).*", "dest": "@vercel/static" }
  ],
  "routes": [
    { "src": "/api/(.*)", "dest": "employees.js" },
    { "src": "/(.*)", "dest": "/" }
  ]
}
