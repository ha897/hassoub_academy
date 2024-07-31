from flask import Flask, render_template, request, redirect, url_for
import json, requests
"""
تطبيق الحالات الجوية
"""
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")



@app.route('/view', methods=['post'])
def view():
    api_key = "e2f0628b95e58526aaa63dcf4dc2fef7"
    url1 = "https://api.openweathermap.org/data/2.5/weather?"
    if request.method == 'POST':
        city_name = request.form['city'].strip()
        # &units-metric لكي يطلع بيانات بالنظام المتري
        if request.form['unit'] == 'metric':
            # complete_url = "https://api.openweathermap.org/data/2.5/weather?q=oman&units=metric&appid=e2f0628b95e58526aaa63dcf4dc2fef7" 
            complete_url = url1 + "q=" + city_name + "&units=metric" + "&appid=" + api_key 
        else: 
            complete_url = url1 + "q=" + city_name + "&appid=" + api_key 

        Data = requests.get(complete_url)

        json_data_wether = json.loads(Data.text)

        if json_data_wether["cod"] == "404":
            return render_template('error.html', cityName=request.form['city'])
        return render_template('view.html', data=json_data_wether, unit= request.form['unit'])
    return redirect('home')
    


if  __name__ == '__main__':
    app.run(debug=True)