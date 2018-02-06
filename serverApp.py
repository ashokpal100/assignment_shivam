import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from db import connection
from werkzeug.datastructures import FileStorage
import json
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/home/ubuntu/flask/uploads'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file_data = request.files['file'].read()
    file_name = str(file.filename)
    file_path = app.config['UPLOAD_FOLDER']
    print "all files values"
    print file
    print file.filename
    print app.config['UPLOAD_FOLDER']
    print "All file types"
    print type(file)
    print type(file_name)
    try:
        c, conn = connection()
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
        file_path = file_path+"/"+file_name;
        print " file data"
        print file_name
        print file_path 
        query="""insert files(file_name, file_path, file_content) values (%s,%s,%s)"""
        c.execute(query, (file_name,file_path,file_data))
        #sqlquery = ("INSERT INTO files(file_name, file_content) VALUES (%s,%s)",(file_name,path))
        #c.execute(sqlquery)
        conn.commit()
        c.close()
        conn.close()
        #print type(getAllFiles())
        #res = "okey"
        res = getAllFiles()
        return render_template('uploaded.html',data=res)
    except Exception as e:
        print "inside exe"
        return(str(e))


def getAllFiles():
   print "inside getAllFiles"
   allData = []
   try:
        c, conn = connection()
        sqlquery = ("select file_name from files")
        c.execute(sqlquery)
        rows = c.fetchall()
        #print type(rows)
        #print rows
        res_list = [x[0] for x in rows]
        #print type(res_list)
        #print res_list
        for name in res_list:
          file_name1 = {'name':name}
          allData.append(file_name1)
          # print name        
        #print res_list
        #resp = json.dumps(res_list) 
        print allData 
        print type(allData)
        #for i in res_list:
         #  print res_list[i]
        conn.commit()
        c.close()
        conn.close()
        return (allData)
   except Exception as e:
        print "inside exe getAllFiles"
        print (str(e))
        return(str(e))



