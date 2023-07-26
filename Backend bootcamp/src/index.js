const express = require("express");
const app=express();
const connect=require("./config/db");
const { register, login } = require("./controllers/user.controller");
const User=require("./models//users.model");
const bcrypt = require('bcrypt');

// console.log("1234");
// const hash = bcrypt.hashSync("1234", 10);
// console.log(hash)

// console.time("1234");
// const hash = bcrypt.hashSync("1234", 10);
// console.timeEnd("1234")

// let password="1234";
// const hash = bcrypt.hashSync("1234", 10);
// //compare the password
// const compare =bcrypt.compareSync(password,hash)
// console.log(compare);


//middleware check proper json data or not
app.use(express.json())

app.get("/home",(req,res)=>{
    res.send("we are on homepage");
})

const auth=async(req,res,next)=>{
    try{

    }catch(error){

    }
    next();
}

app.post("/login",login)
app.post("/register",auth,async(req,res)=>{
    try{
        let user=await User.create(req.body);
        return res.status(200).send(user);
    }
    catch(error){
        return res.status(400).send({error:error.message})
    }
})


app.listen(8080 , async()=>{
    try{
        await connect()
        console.log("listenening at port 8080");
    }catch(error){
        console.log({error:error.message});
    }
    
})