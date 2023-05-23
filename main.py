
import pickle
from flask import Flask,render_template,request

app=Flask(__name__)
model=pickle.load(open("model.pkl","rb"))

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        prediction = model.predict([features])
        if prediction == 0:
            result = '⚠️The water is non potable and harmful for drinking🚱'
        else:
            result = ' ✅ The water is potable ✅'
        return render_template('index.html', prediction_text=f"{result}")

    except Exception as e:
        print(str(e))
        return render_template("index.html", prediction_text=f"Something went wrong!! Kindly Check Values")

if __name__=="__main__":
    app.run(debug=True)
