import faust

app = faust.App('hello-world-faust', broker='localhost:9092')

topic = app.topic("purchases")

@app.agent(topic)
async def purchase(purchases):
    async for purchase in purchases:
        print(purchase)

if __name__ == "_main__":
    app.main()