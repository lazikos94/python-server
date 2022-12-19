from fastapi import FastAPI
from microservices.admin.routes.v1.Questionnaire import questionnaire_router
from microservices.admin.middlewares.PrimaryAdminMiddleware import AdminMiddleware
from config import settings

admin_app = FastAPI(
    title=settings.ADMIN_TITLE,
    description=settings.ADMIN_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    docs_url="/docs",
)

# ADD MIDDLEWARES
admin_app.add_middleware(middleware_class=AdminMiddleware)

admin_app.include_router(questionnaire_router, prefix="/questionnaire")

