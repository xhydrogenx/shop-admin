from starlette_admin.contrib.sqla import Admin, ModelView
from models.product import Product as SQLProduct
from models.category import Category as SQLCategory
from models.user import User as SQLUser
from models.order import Order as SQLOrder
from src.database import engine
from starlette.applications import Starlette

app = Starlette()

admin = Admin(engine, title="Панель администрирования")

admin.add_view(ModelView(SQLCategory))
admin.add_view(ModelView(SQLProduct))
admin.add_view(ModelView(SQLOrder))
admin.add_view(ModelView(SQLUser))

admin.mount_to(app)
