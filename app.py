from flask import Flask, url_for, request
from flask_cors import CORS
import cloudinary as Cloud
import cloudinary.uploader as CloudUploader

app = Flask(__name__)
CORS(app)

Cloud.config(
    cloud_name="dowagkwkg",
    api_key="311688685377264",
    api_secret="AWZjcaXa3c-sQT-GeVvSEeeTz7k"
)


@app.route("/")
def main():
    return "Rota Principal"


@app.route("/image_edit", methods=['POST'])
def image_edit():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    img_id = upload()
    final_image = Cloud.CloudinaryImage(img_id).image(transformation=[
        {'overlay': {'font_family': "Times", 'font_size': 30,
                     'text': nome}, 'gravity': "west", 'x': 243, 'y': -43},
        {'overlay': {'font_family': "Times", 'font_size': 30,
                     'text': email}, 'gravity': "west", 'x': 243, 'y': 51},
        {'overlay': {'font_family': "Times", 'font_size': 30,
                     'text': telefone}, 'gravity': "west", 'x': 290, 'y': 142},
    ])

    return final_image


def upload():
    image_id = "prime"
    prime_img = CloudUploader.upload("prime.png", public_id="prime")
    prime_url = prime_img["url"]
    print("URL da Imagem: ", prime_url)
    return image_id
