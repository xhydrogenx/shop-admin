from starlette_admin.contrib.sqla import Admin, ModelView
from models.models_sqlalchemy import Product as SQLProduct
from models.models_sqlalchemy import Category as SQLCategory
from src.database import get_db, engine, SessionLocal
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from loguru import logger

app = Starlette()


async def get_db(request: Request):
    db = SessionLocal()
    try:
        request.state.db = db
        yield db
    finally:
        db.close()


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
    return JSONResponse({"message": "Product created successfully"})


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


admin = Admin(engine, title="Панель администрирования")

admin.add_view(ModelView(SQLCategory))
admin.add_view(ModelView(SQLProduct))

admin.mount_to(app)
