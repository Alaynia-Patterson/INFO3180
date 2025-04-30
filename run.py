from app  import create_app  # Replace 'yourpackage' with your actual folder name

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
