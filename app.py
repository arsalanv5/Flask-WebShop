from flask import Flask, render_template, request, redirect, url_for, session
from models import db, User, Product, CartItem

app = Flask(__name__)
app.secret_key = "supersecret"

#  DATABASE 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///webshop.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

#  ROUTES 
@app.route("/")
def home():
    return render_template("home.html")

#  REGISTER 
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if User.query.filter_by(username=username).first():
            return "Username already exists"

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))

    return render_template("register.html")

#  LOGIN 
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username, password=password).first()

        if user:
            session["user_id"] = user.id
            return redirect(url_for("dashboard"))

        return "Invalid credentials"

    return render_template("login.html")

#  DASHBOARD 
@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))

    user = User.query.get(session["user_id"])
    return render_template("dashboard.html", user=user)

# LOGOUT 
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

#  PRODUCTS 
@app.route("/products")
def show_products():
    products = Product.query.all()
    return render_template("products.html", products=products)

# ADD TO CART 
@app.route("/add_to_cart/<int:pid>")
def add_to_cart(pid):
    if "user_id" not in session:
        return redirect(url_for("login"))

    user = User.query.get(session["user_id"])
    product = Product.query.get(pid)

    if product and product.stock > 0:
        product.stock -= 1
        item = CartItem.query.filter_by(user_id=user.id, product_id=product.id).first()
        if item:
            item.quantity += 1
        else:
            item = CartItem(user_id=user.id, product_id=product.id, quantity=1)
            db.session.add(item)
        db.session.commit()

    return redirect(url_for("show_products"))

#  CART 
@app.route("/cart")
def show_cart():
    if "user_id" not in session:
        return redirect(url_for("login"))

    user = User.query.get(session["user_id"])
    items = CartItem.query.filter_by(user_id=user.id).all()
    total = sum(item.product.price * item.quantity for item in items)
    return render_template("cart.html", cart=items, total=total)

# REMOVE FROM CART 
@app.route("/remove_from_cart/<int:item_id>")
def remove_from_cart(item_id):
    item = CartItem.query.get(item_id)
    if item:
        item.product.stock += item.quantity
        db.session.delete(item)
        db.session.commit()
    return redirect(url_for("show_cart"))

#  CHECKOUT 
@app.route("/checkout")
def checkout():
    if "user_id" not in session:
        return redirect(url_for("login"))

    user = User.query.get(session["user_id"])
    items = CartItem.query.filter_by(user_id=user.id).all()
    total = sum(item.product.price * item.quantity for item in items)

    if user.balance >= total:
        user.balance -= total
        for item in items:
            db.session.delete(item)
        db.session.commit()
        return "Checkout successful!"
    else:
        return "Not enough balance"

#  ADMIN 
@app.route("/admin", methods=["GET", "POST"])
def admin():
    if "user_id" not in session:
        return redirect(url_for("login"))

    user = User.query.get(session["user_id"])
    if user.username != "admin":
        return redirect(url_for("login"))

    if request.method == "POST":
        name = request.form["name"]
        price = float(request.form["price"])
        stock = int(request.form["stock"])
        product = Product(name=name, price=price, stock=stock)
        db.session.add(product)
        db.session.commit()

    products = Product.query.all()
    return render_template("admin.html", products=products)

#  RUN APP 
if __name__ == "__main__":
    
    with app.app_context():
        db.create_all()
    app.run(debug=True)
