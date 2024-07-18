
from sanic import Sanic, response
from sanic.response import json
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select
from models import Base, Sales

DATABASE_URL = "postgresql+asyncpg://avnadmin:AVNS_FZW0_aZRMtblqUqmQrl@pg-fc3b383-krishnakparthiba-eb59.c.aivencloud.com:11658/defaultdb"

app = Sanic("SalesAPI")

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

@app.listener('before_server_start')
async def setup_db(app, loop):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.route("/sales", methods=["GET"])
async def get_sales(request):
    print('hii')
    filters = {}
    location = request.args.get('location')
    if location:
        filters['location'] = location
    
    async with async_session() as session:
        query = await session.execute(select(Sales).filter_by(**filters))
        result = query.scalars().all()
        sales_list = [{"id": sale.id, "location": sale.location, "amount": sale.amount} for sale in result]
    return json(sales_list)

@app.route("/sales", methods=["POST"])
async def add_sale(request):
    data = request.json
    if not data or not data.get("location") or not data.get("amount"):
        return response.json({"error": "Invalid data"}, status=400)
    
    new_sale = Sales(location=data["location"], amount=data["amount"])
    
    async with async_session() as session:
        session.add(new_sale)
        await session.commit()
    return response.json({"message": "Sale added successfully"}, status=201)

@app.route("/sales/<sale_id:int>", methods=["DELETE"])
async def delete_sale(request, sale_id):
    async with async_session() as session:
        sale = await session.get(Sales, sale_id)
        if not sale:
            return response.json({"error": "Sale not found"}, status=404)
        await session.delete(sale)
        await session.commit()
    return response.json({"message": "Sale deleted successfully"}, status=200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
