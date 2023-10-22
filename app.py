from flask import Flask ,render_template,request
import requests

app = Flask(__name__)
apikey='64533a7d124317690076001a89fc1fd8'
@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/weatherapp',methods=['POST','GET'])
def getweatherdata():
    url="https://api.openweathermap.org/data/2.5/weather"
    params = {'q' :"delhi",
          'appid' : apikey,
          'units':'metric'}
    request=requests.get(url,params=param)
    data=response.json()
    return f"data:{data}"

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5003)
    dgdd