from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI


from routing.main import router as main
from routing.carts import router as carts
from routing.group import router as group

app = FastAPI(
    openapi_url="/core/openapi.json", docs_url="/core/docs"
)


app.include_router(main)
app.include_router(carts)
app.include_router(group)
