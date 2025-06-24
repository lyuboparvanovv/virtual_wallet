from fastapi import FastAPI




app = FastAPI(
    title="Virtual Wallet API",
    version="1.0.0",
    description="A virtual wallet app with user accounts, transactions, cards, and more."
)



@app.get("/")
def root():
    return 'Welcome page'