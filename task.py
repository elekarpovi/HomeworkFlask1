# Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал),
# и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# Например, создать страницы "Одежда", "Обувь" и "Куртка", используя базовый шаблон.

from flask import Flask, render_template, request, redirect
from dataclasses import dataclass

app = Flask(__name__)

@dataclass
class Product:
    name: str
    price: float
    img_link: str


clothes = [Product('dress', 40.55, 'img/clothes/dress.jpg'),
           Product('skirt', 35.20, 'img/clothes/skirt.jpg'),
           Product('blouse', 20.15, 'img/clothes/blouse.jpg'),
           Product('coat', 75.68, 'img/clothes/coat.jpg'),
           Product('trousers', 30.70, 'img/clothes/trousers.jpg')]

shoes = [Product('boots', 156.25, 'img/shoes/boots.jpg'),
         Product('trainers', 75.15, 'img/shoes/trainers.jpg'),
         Product('slippers', 21.15, 'img/shoes/slippers.jpg')]

accessories = [Product('bag', 120.20, 'img/accessories/bag.jpg'),
               Product('hat', 28.45, 'img/accessories/hat.jpg'),
               Product('belt', 34.80, 'img/accessories/belt.jpg'),
               Product('tie', 19.90, 'img/accessories/tie.jpg')]


@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html')


@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/products/clothes/')
def task_clothes():
    return render_template('clothes.html', clothes=clothes, title='Clothes')


@app.route('/products/shoes/')
def task_shoes():
    return render_template('shoes.html', shoes=shoes, title='Shoes')


@app.route('/products/accessories/')
def task_accessories():
    return render_template('accessories.html', accessories=accessories, title='Accessories')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)