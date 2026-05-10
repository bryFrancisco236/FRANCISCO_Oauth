from flask import Flask, redirect, url_for, session, jsonify
from authlib.integrations.flask_client import OAuth
import os

app = Flask(__name__)
# In a real app, use a random secret key
app.secret_key = "SUPER_SECRET_KEY" 

oauth = OAuth(app)

# Configure GitHub OAuth
github = oauth.register(
    name='FranciscoAuth',
    client_id='Ov23liTY3cAj9xGQmSSJ', # Replace with your ID
    client_secret='3f9b78d366685abc5ac097b0dd344bf6fd238d16', # Replace with your Secret
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize',
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'},
)

# III.c.iii: Login Route
@app.route('/login')
def login():
    # We tell GitHub to send the user back to our /callback route
    redirect_uri = url_for('callback', _external=True)
    return github.authorize_redirect(redirect_uri)

# III.c.iv: Callback Route
@app.route('/callback')
def callback():
    # Exchange the code for a token
    token = github.authorize_access_token()
    # Fetch user info from GitHub API
    resp = github.get('user')
    user = resp.json()

    # Store user info in the session cookie
    session['user'] = user
    return redirect('/profile')

# III.c.v: Protected API
@app.route('/profile')
def profile():
    if 'user' not in session:
        return "Unauthorized", 401
    
    return jsonify(session['user'])

# III.c.vi: Logout Route
@app.route('/logout')
def logout():
    session.pop('user', None)
    return "Logged out successfully!"

# VII: Bonus Challenge - Secure Data Route
@app.route('/api/secure-data')
def secure_data():
    if 'user' not in session:
        return jsonify({"error": "Access Denied"}), 403
    
    return jsonify({
        "message": "This is top-secret data only for logged-in users!",
        "status": "Success"
    })

if __name__ == '__main__':
    app.run(debug=True)