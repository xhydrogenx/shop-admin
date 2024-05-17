from starlette_admin.contrib.sqla import Admin, ModelView
from models.models_sqlalchemy import Product as SQLProduct
from models.models_sqlalchemy import Category as SQLCategory
from models.models_sqlalchemy import User as SQLUser
from models.models_sqlalchemy import Order as SQLOrder
from src.database import engine
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse

app = Starlette()


@app.route("/products", methods=["GET"])
async def get_products(request: Request):
    db = request.state.db
    products = db.query(SQLProduct).all()
    return JSONResponse(products)


@app.route("/products", methods=["POST"])
async def create_product(request: Request):
    db = request.state.db
    product_data = await request.json()
    product = SQLProduct(**product_data)
    db.add(product)
    db.commit()
    return JSONResponse(product)


@app.route("/categories", methods=["GET"])
async def get_categories(request: Request):
    db = request.state.db
    categories = db.query(SQLCategory).all()
    return JSONResponse(categories)


@app.route("/categories", methods=["POST"])
async def create_category(request: Request):
    db = request.state.db
    category_data = await request.json()
    category = SQLCategory(**category_data)
    db.add(category)
    db.commit()
    return JSONResponse(category)


@app.route("/orders", methods=["GET"])
async def get_orders(request: Request):
    db = request.state.db
    orders = db.query(SQLOrder).all()
    return JSONResponse(orders)


@app.route("/orders", methods=["POST"])
async def create_order(request: Request):
    db = request.state.db
    order_data = await request.json()
    order = SQLCategory(**order_data)
    db.add(order)
    db.commit()
    return JSONResponse(order)


@app.route("/users", methods=["GET"])
async def get_users(request: Request):
    db = request.state.db
    users = db.query(SQLUser).all()
    return JSONResponse(users)


@app.route("/users", methods=["POST"])
async def create_users(request: Request):
    db = request.state.db
    user_data = await request.json()
    user = SQLCategory(**user_data)
    db.add(user)
    db.commit()
    return JSONResponse(user)


admin = Admin(engine, title="Панель администрирования")

admin.add_view(ModelView(SQLCategory))
admin.add_view(ModelView(SQLProduct))
admin.add_view(ModelView(SQLOrder))
admin.add_view(ModelView(SQLUser))

admin.mount_to(app)
