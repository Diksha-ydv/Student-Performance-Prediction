from flask import Flask,request,render_template
from src.pipeline import predict_pipeline
from src.pipeline.predict_pipeline import CustomData, prediction_pipeline

application = Flask(__name__)
app = application

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict_data",methods = ["GET","POST"])
def predict_datapoint():
    if request.method=="GET":
        return render_template("home.html")
    else:
        data = CustomData(
            gender=request.form.get("gender"),
            race_ethnicity=request.form.get("ethnicity"),
            parental_level_of_education=request.form.get("parental_level_of_education"),
            lunch = request.form.get("lunch"),
            test_preparation_course=request.form.get("test_preparation_course"),
            reading_score=request.form.get("reading_score"),
            writing_score=request.form.get("writing_score")
        )
        data_df = data.get_data_as_dataframe()
        print(data_df)
        predict_pipe = prediction_pipeline()
        prediction = predict_pipe.predict(data_df)

        return render_template("home.html",results=prediction)


if __name__=="__main__":
    app.run(host="0.0.0.0",port=8000)