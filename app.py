from flask import Flask

app = Flask('flask')

@app.route('/')
def root():
    return 'eu quero'

app.run()

    
