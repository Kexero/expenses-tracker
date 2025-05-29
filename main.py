from fastapi import FastAPI
from router.user_router import user_router
from router.admin_router import admin_router
from router.costcategory_router import cost_category_router

app = FastAPI()

app.include_router(user_router)
app.include_router(admin_router)
app.include_router(cost_category_router)

