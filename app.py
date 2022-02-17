# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 10:56:05 2022

@author: User
"""
from flask import Flask
app=Flask(__name__)

from flask import request, render_template

@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        NPTA=request.form.get("NPTA") 
        TLTA=request.form.get("TLTA")
        WCTA=request.form.get("WCTA")
        print(NPTA,TLTA,WCTA)
        model=load_model("bankruptcy")
        pred=model.predict([[float(NPTA),float(TLTA),float(WCTA)]])
        s="The predicted bankruptcy score is : " + str(pred)
        return(render_template("index.html",result=s))
    else:
        return(render_template("index.html",result="2"))
    
if __name__=="__main__":
    app.run()    
