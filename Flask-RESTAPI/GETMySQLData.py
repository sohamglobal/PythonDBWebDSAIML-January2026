from flask import Flask,jsonify
import pymysql

app=Flask(__name__)

@app.route('/patients',methods=['GET'])
def getallpatients():
    con=pymysql.connect(host='pymyservice-mysql-python-0226.g.aivencloud.com',port=17577,user='praffull',password='AVNS_wBJdNDhkoHduUD3Z3z2',database='sharayudb')
    curs=con.cursor()
    curs.execute("select * from patients")
    data=curs.fetchall()
    curs.close()
    con.close()
    return jsonify(data)

app.run(debug=True)

