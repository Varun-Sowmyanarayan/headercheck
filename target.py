from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "<h1>Weak demo site</h1><p> I am deliberately missing security headers</p>"

@app.after_request
def add_headers(response):
    #only one good header, so the checker has a pass to show
    response.headers["X-Content-Type-Options"]="nosniff"
    return response
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5002)
    
