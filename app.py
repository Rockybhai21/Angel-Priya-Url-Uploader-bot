#Thank you LazyDeveloper for helping developers in this journey !
#Must Subscribe On YouTube @LazyDeveloperr 

@app.route('/')
def home():
    return "Bot is running!"

def run_web():
    app.run(host="0.0.0.0", port=8080)

if __name__ == "__main__":
    threading.Thread(target=run_web).start()
