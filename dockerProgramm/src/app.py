from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI
# from routing.goods import router as goods_router
# from routing.brands import router as brands_router
# from routing.categories import router as categories_router
# from routing.promoblocks_new import router as promoblock_new_router
# from routing.promoblocks_sale import router as promoblock_sale_router
# from routing.basket import router as basket_router
# from routing.favorites import router as favorites_router
# from routing.clients import router as clients_router
# from routing.colors import router as colors_router
# from routing.orders import router as orders_router
# from routing.managers import router as manager_router
# from routing.loyalty import router as loyalty_router
# from routing.countries import router as country_router
# from tasks import check_clients, pereodic_parse_date, pereodic_parse_orders
# from config import Config
# from hmac_middleware import HMACMiddleware

from routing.main import router as main
app = FastAPI(
    openapi_url="/core/openapi.json", docs_url="/core/docs"
)

# app.add_middleware(HMACMiddleware)
app.include_router(main)
# scheduler = AsyncIOScheduler()
# # Запуск при старте. После выполнения job удаляется из списка
# scheduler.add_job(check_clients, 'date')
# scheduler.add_job(pereodic_parse_date, 'date')
# scheduler.add_job(pereodic_parse_orders, 'date')

# # Запуск по интервалам и cron'у
# scheduler.add_job(check_clients, 'interval', minutes=int(Config.CHECK_CLIENTS_INTERVAL))
# scheduler.add_job(pereodic_parse_date, 'cron', hour=int(Config.PARSING_TIME), timezone="Europe/Moscow")
# scheduler.add_job(pereodic_parse_orders, 'interval', minutes=int(Config.PARSING_ORDERS_INTERVAL))
# scheduler.start()

# app.add_middleware(HMACMiddleware)
# app.include_router(goods_router)
# app.include_router(brands_router)
# app.include_router(categories_router)
# app.include_router(promoblock_new_router)
# app.include_router(colors_router)
# app.include_router(promoblock_sale_router)
# app.include_router(basket_router)
# app.include_router(clients_router)
# app.include_router(orders_router)
# app.include_router(manager_router)
# app.include_router(loyalty_router)
# app.include_router(country_router)
# app.include_router(favorites_router)
