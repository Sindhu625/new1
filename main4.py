from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse

app = FastAPI()

@app.get('/json')
def get_details():
    return {
        'name': 'Sindhu',
        'age': 22
    }
    return JSONResponse(data)

@app.get('/html')
def get_details():
    html = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
         <meta charset="UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <title>My Project</title>
         <meta name="description" content="A simple HTML5 boilerplate template.">
         <meta name="author" content="Your Name">
         <!-- Open Graph for social sharing -->
         <meta property="og:title" content="My Project">
         <meta property="og:type" content="website">
         <meta property="og:description" content="A simple HTML5 boilerplate template.">
         <meta property="og:image" content="image.png">
         <!-- Favicon -->
         <link rel="icon" href="/favicon.ico">
         <!-- CSS -->
         <link rel="stylesheet" href="styles.css">
        </head>
        <body>
         <header>
          <h1>Welcome to My Project</h1>
         </header>
         <main>
          <p>This is where your content goes.</p>
         </main>
         <footer>
          <p>© 2026 My Project</p>
         </footer>
         <!-- JavaScript -->
         <!DOCTYPE html>
        <html>
        <head>
          <title>Simple HTML Form</title>
        </head>
        <body>
          <h2>Simple HTML Form</h2>
          <form action="/submit_form" method="post">
            <label for="fname">First name:</label><br>
            <input type="text" id="fname" name="fname"><br><br>
            <label for="lname">Last name:</label><br>
            <input type="text" id="lname" name="lname"><br><br>
            <label for="email">Email:</label><br>
            <input type="email" id="email" name="email"><br><br>
            <input type="submit" value="Submit">
          </form>
        </body>
        </html>
         <script src="scripts.js"></script>
        </body>
        </html>

    '''
    return HTMLResponse(html)

@app.get('/redirect')
def get_redirect():
    url = "https://www.wikipedia.org/"
    return RedirectResponse(url, status_code=302)