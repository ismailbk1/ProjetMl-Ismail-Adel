from flask import Flask
from flask import request
import requests
import base64
app = Flask(__name__)

@app.route('/predict',methods=['POST'])
def upload_svm_model():
    print("function in the upload point work fine ")
    data = request.get_json()
    encoded_svm_model = data.get("encoded_svm_model")
    #decoding the model and saving it
    with open("./svm_model.joblib","wb") as decoded_svm_file:
      decoded_svm_file.write(base64.b64decode(encoded_svm_model))

    return "Model uploaded successfuly"


if __name__ == "__main__" :
  app.run(debug=True,host="0.0.0.0",port=5003)

