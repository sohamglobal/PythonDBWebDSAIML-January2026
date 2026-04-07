from flask import Flask,request
import pymysql

app=Flask(__name__)

@app.route('/doctor/add',methods=['POST'])
def add_doctor():
    did=int(request.form.get("docid"))
    dnm=request.form.get("docnm")
    spl=request.form.get("spec")
    exp=int(request.form.get("exp"))
    dic={}
    try:
        con=pymysql.connect(host='pymyservice-mysql-python-0226.g.aivencloud.com',port=17577,user='praffull',password='AVNS_wBJdNDhkoHduUD3Z3z2',database='sharayudb')
        curs=con.cursor()
        curs.execute(f"insert into doctors values({did},'{dnm}','{spl}',{exp})")
        con.commit()
        con.close()
        dic['status']='success'
    except:
        dic['status']='failed'
    
    return dic

app.run(debug=True)
