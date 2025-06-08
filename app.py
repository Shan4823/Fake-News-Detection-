from flask import Flask, request, render_template
from markupsafe import escape
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer


# initlise a tfidvectorsizer
vector = TfidfVectorizer(stop_words='english', max_df=0.7)

model = pickle.load(open("PCL.pkl", 'rb'))
vector = pickle.load(open("vectorizer.pkl", 'rb'))


app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/prediction", methods=['GET', 'POST'])
def prediction():
    if request.method == "POST":
        news = request.form['news']
        predict = model.predict(vector.transform([news]))[0]
        print(predict)

        return render_template("prediction.html" , prediction_text="news headline is ->{}".format(predict))


    else:
        return render_template("prediction.html")
    news = request.form.get('news', '')

    
if __name__ == '__main__':
    app.run(debug=True)




