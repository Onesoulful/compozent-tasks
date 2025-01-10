from flask import Flask , request ,  render_template
import pickle
import numpy as np

app = Flask(__name__)

with open(r'C:\Users\maury\OneDrive\Desktop\python\dataset\stock dataset.pkl','rb') as f: 
 model = pickle.load(f)
 @app.route('/')
 def home_page():
    return render_template("index.html")
@app.route('/predict',methods=['POST'])
def predict():
    if request.method == "POST":
        data = request.form
        Open = int(data.get("Open"))
        PercentageChange = int(data.get("PercentageChange"))
        Volumeinlakhs = int(data.get("Volumeinlakhs"))
        TurnoverinCr = int(data.get("TurnoverinCr"))
        YearlyChange= int(data.get("YearlyChange"))
        MonthlyChange= int(data.get("MonthlyChange"))
        
        user_input = np.array([[Open,PercentageChange,Volumeinlakhs,TurnoverinCr,YearlyChange,MonthlyChange]])
        print(user_input)
        model_output = model.predict(user_input)
        print(model_output)
        return render_template('index.html')
        output_user = ''
        if model_output == 0:
            output_user = "Not Available"
        else:
            output_user = "Name"
        return render_template('index.html',Name = output_user)
        
    if __name__ == "__main__":
         app.run(debug=True,port=8000)