from flask import Flask, redirect, url_for,session,request,render_template,session,flash
from pymongo import MongoClient
app=Flask(__name__)

cluster=MongoClient('mongodb+srv://covid19:districts@cluster0.ilkuy.mongodb.net/covid19?retryWrites=true&w=majority')

db=cluster['Covidlist']

collection=db['Districts']

@app.route('/')
def home():
    return render_template('home.html',di=d_codes,d=d)
@app.route('/<name>')
def new(name):
    if name in d_codes:
        p=[]
        a=collection.find({'code':name})
        return render_template('testcenters.html',a=a,di=d_codes[name],d=d_codes,n=name)
    else:
        return 'Hello User'
d_codes={'adl':'ADILABAD','jl':'JAGTIAL','jn':'JANGAON','mlg':'MULUGU','jgl':'JOGULAMBA GADWAL','kmr':'KAMAREDDY','knr':'KARIMNAGAR','khm':'KHAMMAM','mhbd':'MAHABUBABAD','mhbr':'MAHABUBNAGAR','nrt':'NARAYANPET','mrl':'MANCHERIAL','mdk':'MEDAK','nkl':'NAGARKURNOOL','nlg':'NALGONDA','nml':'NIRMAL','nzb':'NIZAMABAD','pdpl':'PEDDAPALLI','srcl':'RAJANNA SIRCILLA','rgr':'RANGAREDDY','sdp':'SIDDIPET','wp':'WANAPARTHY','wlr':'WARANGAL RURAL','wlu':'WARANGAL URBAN','ybr':'YADADRI BHONGIR','bkm':'BHADRADRI KOTHAGUDEM','jbp':'JAYASHANKAR BHUPALAPALLY','kba':'KOMARAM BHEEM ASIFABAD','ghyd':'GOVERNMENT LABORATORIES','phyd':'PRIVATE LABORATORIES'}
d={'wp':'https://www.google.co.in/maps/d/u/0/embed?mid=1baZSgAbcuurWGANnKPnPXQpvhOJSmzpF'}
if __name__=='__main__':
	app.run(debug=True)
