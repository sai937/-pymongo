from flask import Flask,jsonify,request,render_template
from flask.ext.pymongo import PyMongo
import sys
import pandas as pd
import os

app=Flask(__name__)

app.config['MONGO_DBNAME']='NewCompany'
app.config['MONGO_URI']='mongodb://localhost:27017/NewCompany'
mongo=PyMongo(app)

reload(sys)
sys.setdefaultencoding('utf-8')

@app.route('/')
def home():
    return render_template("humannetwork.html")

@app.route('/fourlakh',methods=['GET','POST'])
def get_limit_data():
    if request.method=='POST':
        if request.form['submit'] == 'dosomethingbabai':
            #specialties = request.form.get('sp')
            headquarters = request.form.get('hq')# here i'm splliting the data which is coming from form 
            
        #for j in city:
           # global y
           # y=j.split(",")

            category = request.form.get('cat')
        
            industry = request.form.get('ind')
            size     = request.form.get('siz')
        
       
            fourlakh=mongo.db.fourlakh.find({"industry":industry,"category":category,"size":size,"$text":{"$search":headquarters}}).count()  
            #fourlakh=mongo.db.fourlakh.find({"$and":[{"country":country},{"category":category},{"industry":industry},{"$text":{"$search":city}}]}).count()   
            converting = str(fourlakh)
        
            print(converting)
            return render_template('humannetwork.html',result=converting)

        
        elif request.form["submit"] == 'doanythingbabai':

             #specialties = request.form.get('sp')
             headquarters = request.form.get('hq')
             size         = request.form.get('siz')
             category = request.form.get('cat')
        
             industry = request.form.get('ind')
             output=[]
             for item in mongo.db.fourlakh.find({"industry":industry,"category":category,"size":size,"$text":{"$search":headquarters}}):
                 output.append({"name":item['name'],"category":item['category'],"size":item['size'],"website":item['website'],"overview":item['overview'],"callback":item['callback'],"child_url":item['child_url'],"city":item['city'],"country":item['country'],"employees_on_linkedin":item['employees_on_linkedin'],"followers":item['followers'],"founded":item['founded'],"hq":item['hq'],"image_url":item['image_url'],"industry":item['industry'],"last_visited":item['last_visited'],"linkedin_id":item['linkedin_id'],"parent_url":item['parent_url'],"specialties":item['specialties'],"url":item['url']})
             df=pd.DataFrame(output)#converting json to a csv file
             df.to_csv('country_city.csv',index=False)    
             return " Your file Successfully Downloaded"
             #return jsonify({'result':output})  this line will diplay the output as json in a browser

        elif request.form["submit"] == 'previewdatababai':

             #specialties = request.form.get('sp')
             headquarters = request.form.get('hq')
             size         = request.form.get('siz')
             category = request.form.get('cat')
        
             industry = request.form.get('ind')
             output=[]
             for item in mongo.db.fourlakh.find({"industry":industry,"category":category,"size":size,"$text":{"$search":headquarters}}):
                 output.append({"name":item['name'],"category":item['category'],"size":item['size'],"website":item['website'],"overview":item['overview'],"callback":item['callback'],"child_url":item['child_url'],"city":item['city'],"country":item['country'],"employees_on_linkedin":item['employees_on_linkedin'],"followers":item['followers'],"founded":item['founded'],"hq":item['hq'],"image_url":item['image_url'],"industry":item['industry'],"last_visited":item['last_visited'],"linkedin_id":item['linkedin_id'],"parent_url":item['parent_url'],"specialties":item['specialties'],"url":item['url']})
             
             return jsonify({'result':output})  #this line will preview the data when user clicks preview button     
        else:
            return " I think you have to change the code sai"    

    else:
        return "I think you searched a wrong Query Try Again"


if __name__==('__main__'):  
    app.run(debug=True)             