from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/players')
def players():
    players = [
        
        {"number": 18, "name": "Harry", "position": "Forward"},
        {"number": 7, "name": "Bret", "position": "Forward"},
        {"number": 17, "name": "Lenny", "position": "Midfielder","image":"lenny.jpg"},
        {"number": 8, "name": "Amimo", "position": "Midfielder"},
        {"number": 1, "name": "Daniel", "position": "Goalkeeper"},
        {"number": 6, "name": "Seth", "position": "Midfielder"},
        {"number": 44, "name": "Sila", "position": "Goalkeeper"},
        {"number": 75, "name": "Maxwell", "position": "Goalkeeper"},
        {"number": 14, "name": "Rex", "position": "Defender"},
        {"number": 4, "name": "Miracle", "position": "Defender"},
        {"number": 5, "name": "Frank", "position": "Defender"},
        {"number": 13, "name": "Dickens", "position": "Forward"},
        {"number": 15, "name": "Geoffrey", "position": "Striker"},
        {"number": 16, "name": "Lenox", "position": "Defender"},
        {"number": 18, "name": "Powel", "position": "Midfielder"},
        {"number": 20, "name": "Raju", "position": "Midfielder"},
        {"number": 10, "name": "Lorenzo", "position": "Forward"},
        {"number": 22, "name": "Naman", "position": "Defender"},
        {"number": 2, "name": "Nigel", "position": "Defender"},
        {"number": 9, "name": "Apompe", "position": "Forward"},
        {"number": 11, "name": "Brayo", "position": "Forward"},
        {"number": 19, "name": "Owuor", "position": "Forward"},
        {"number": 12, "name": "Kim", "position": "Defender"},
        {"number": 24, "name": "Dickson", "position": "Defender"},
        {"number": 26, "name": "Gibbs", "position": "Forward"},
    ]
    return render_template('player.html', players=players)


@app.route('/fixtures')
def fixtures():
    return render_template('fixture.html')


@app.route('/table')
def table():
    return render_template('table.html')


@app.route('/stats')
def stats():
    return render_template('stats.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)