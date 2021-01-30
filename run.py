

from resumewebproject import create_app

app = create_app()

"Grab the app and run it"
"This conditional is only true when you run this script directly"
if __name__ == '__main__':
    app.run(debug=True)
