const express=require("express");
const router=express.Router();
const User=require("../models/users.model")

const register=async(req,res)=>{
    try{
        const{name,email,password}=req.body;

        const user=new User({
            name,email,password
        })
        await user.save();
        return res.status(201).send(user)
    }catch(error){
        return res.status(400).send({error:error.message})
    }
}

const login=async(req,res)=>{
    try{
       let user=await User.findOne({email:req.body.email});
       if(!user){
            res.send("user is not register")
       }
       if( user.password==req.body.password){
            return res.status(200).send(user);
       }
       const compare=user.checkPassword(req.body.password)
      if(!compare){
        res.send("password incorrect")
      }
      res.send("logged in successfully")
    }catch(error){
        return res.status(400).send(error)
    }
}

module.exports={register,login}
