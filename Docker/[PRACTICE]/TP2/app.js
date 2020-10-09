const express = require('express')
const redis = require('redis')

const app = express()
const client = redis.createClient({
    host: 'redis-server',
    port: 6379
})

//Set initial visits
client.set('visits', 0);

// Définit les visites initiales
client.set ( 'visites' , 0 )

//Compteur de visite
app.get ( '/' , (req, res) => {
    client.get ( 'visites' , (err, visites) => {
        res.send ( 'Le nombre de visites est : '  + visites)
        client.set ( 'visites' , parseInt (visites) +  1 )
    })
})

/*  j'écoute le 8081 */

app.listen(8081, ()=>{
    console.log("app listening on 8081 - Ok cool ça run ")
});
