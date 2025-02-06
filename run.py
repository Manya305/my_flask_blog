from app import app, db

if __name__ == '__main__':
    # Create the database tables (if they don't exist)
    with app.app_context():
        db.create_all()
    
    # Run the Flask development server
    app.run(debug=True)