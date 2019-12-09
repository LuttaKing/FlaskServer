from flask import Flask,request
import yagmail

import json

app = Flask(__name__)

@app.route('/',methods=["POST","GET"])
def postServer():
    if request.method=="POST":
        password=request.get_json()
                
        json_string = json.dumps(password)
        print("denny initialized"+json_string)

        yag=yagmail("denilsonwash@gmail.com","Luttason6")
        contents=[json_string]
        yag.send('denilsonwash@gmail.com', 'From server', contents)


        return "hello luttas you posted{}".format(password)
    
    return "<h1>YOU PERFORMED A GET REQUEST SO YOU GET THE GET PAGE</h1>"

if __name__ == '__main__':
    app.run()
