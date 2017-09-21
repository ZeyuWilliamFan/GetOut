from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_orm import Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurant.db')
DBsession = sessionmaker(bind=engine)
session = DBsession()

@app.route('/')
def Hello():
    return "Hello and welcome to the restaurant menu app."

@app.route('/restaurants/')
def restaurantList():
    restaurantList = session.query(Restaurant).all()
    return render_template('restaurantList.html', restaurantList = restaurantList)

@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    menuitems = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
    return render_template('menuTemplate.html',restaurant = restaurant, items = menuitems)

@app.route('/restaurant/<int:restaurant_id>/new/')
def newMenuItem(restaurant_id):
    return "page to create a new menu item. Task 1 complete!"

@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    return "page to edit a menu item. Task 2 complete!"

@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    return "page to delete a menu item. Task 3 complete!"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
