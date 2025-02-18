from flask import Flask
from routes import setup_routes
from log import setup_logging

# Create the Flask app instance
def create_app():
    app = Flask(__name__)
    
    setup_logging()
    
    setup_routes(app)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)


"""
look for : create view and sql me .sql 
"""