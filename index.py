from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():

    return "Welcome"


@app.route("/parity")
def parity():
    try:
        arg = request.args
        
        parity = int(arg["b1"]) ^ int(arg["b2"]) ^ int(arg["b3"]) ^ int(arg["b4"])
       
        return str(parity)
    except:
        return "Please pass the right figures"
@app.route("/permissions")
def permission():
    try:

        if request.args["code"]:
            return {
                "owner": ["read", "write", "execute"],
                "group": ["read"],
                "other": ["read"],
            }
        return "Access Denied"
    except:
        return "Problem Occured"




if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
