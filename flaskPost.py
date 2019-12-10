from flask import Flask,request

import json

app = Flask(__name__)

@app.route('/',methods=["POST","GET"])
def postServer():
    if request.method=="POST":
        password=request.get_json()
                
        json_string = json.dumps(password["key"])
        print("denny initialized "+ str(json_string))


        return "hello luttas you posted{}".format(password)
    
    return "<h1>YOU PERFORMED A GET REQUEST SO YOU GET THE GET PAGE</h1>"

if __name__ == '__main__':
    app.run()
