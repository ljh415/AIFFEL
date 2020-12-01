from flask import Flask, render_template, request, Response
from PIL import Image

from image_preprocessor import preprocess
from rock_scissor_paper import load_pre_model, predict_answer

model = load_pre_model()
app = Flask(__name__, template_folder="./templates/", static_url_path="/images", static_folder="images")

@app.route("/")
def index():
   return render_template('index.html')

@app.route("/healthz", methods=["GET"])
def healthCheck():
   return "", 200

@app.route("/image", methods = ['POST'])
def get_result():
   if request.method == "POST":
       width, height = 28, 28
       try:
           source = Image.open(request.files['source'])
           adjusted_image = preprocess(source, width, height)
           result = predict_answer(model, adjusted_image, width, height)
       except Exception as e:
           print("error : %s" % e)
           return Response("fail", status=400)

   return str(result)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port='81', debug=True)