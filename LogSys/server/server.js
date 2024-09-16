const express = require('express')
const app = express()
const port = 3000

app.get("/api", (req, res) => {
    res.json({ "users": ["Hello World!"] })
})

app.listen(5000, () => { console.log("Server started on port 5000") })
