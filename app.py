from flask import Flask, render_template, request, jsonify, redirect, url_for
import sqlite3
import uuid
import qrcode
import os

app = Flask(__name__)

DATABASE = "cinebook.db"

MOVIES = [
    {
        "id": 1,
        "title": "The Last Horizon",
        "genre": "Sci-Fi / Adventure",
        "language": "English",
        "duration": "2h 18m",
        "rating": "8.6",
        "price": 220,
        "poster": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?auto=format&fit=crop&w=700&q=80",
        "description": "A crew races across a distant world to save the last human colony."
    },
    {
        "id": 2,
        "title": "Mumbai Nights",
        "genre": "Drama / Romance",
        "language": "Hindi",
        "duration": "2h 05m",
        "rating": "8.1",
        "price": 180,
        "poster": "https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?auto=format&fit=crop&w=700&q=80",
        "description": "Two strangers meet during one unforgettable night in Mumbai."
    },
    {
        "id": 3,
        "title": "Shadow Protocol",
        "genre": "Action / Thriller",
        "language": "Hindi",
        "duration": "2h 22m",
        "rating": "8.8",
        "price": 240,
        "poster": "https://images.unsplash.com/photo-1485846234645-a62644f84728?auto=format&fit=crop&w=700&q=80",
        "description": "An intelligence officer uncovers a hidden network threatening the city."
    },
    {
        "id": 4,
        "title": "Pixel Quest",
        "genre": "Animation / Family",
        "language": "English",
        "duration": "1h 48m",
        "rating": "8.3",
        "price": 160,
        "poster": "https://images.unsplash.com/photo-1515634928627-2a4e0dae3ddf?auto=format&fit=crop&w=700&q=80",
        "description": "A young gamer enters a magical digital universe."
    }
]

THEATRES = [
    "CineBook IMAX - Andheri",
    "Metro Grand Cinema - Lower Parel",
    "Skyline Multiplex - Thane"
]

SHOW_TIMES = [
    "10:00 AM",
    "01:15 PM",
    "04:30 PM",
    "07:45 PM",
    "10:30 PM"
]


def create_database():

    connection = sqlite3.connect(DATABASE)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id TEXT PRIMARY KEY,
            movie TEXT,
            theatre TEXT,
            show_time TEXT,
            seats TEXT,
            food TEXT,
            total INTEGER
        )
    """)

    connection.commit()
    connection.close()


@app.route("/")
def home():

    return render_template(
        "index.html",
        movies=MOVIES
    )


@app.route("/movie/<int:movie_id>")
def movie(movie_id):

    movie_data = None

    for movie in MOVIES:

        if movie["id"] == movie_id:
            movie_data = movie

    if movie_data is None:
        return "Movie not found", 404

    return render_template(
        "movie.html",
        movie=movie_data,
        theatres=THEATRES,
        show_times=SHOW_TIMES
    )


@app.route("/api/seats")
def seats():

    occupied = [
        "A3",
        "A4",
        "B6",
        "C2",
        "C3",
        "D7",
        "E4",
        "F5",
        "G1",
        "G2"
    ]

    return jsonify({
        "occupied": occupied
    })


@app.route("/book", methods=["POST"])
def book():

    data = request.json

    booking_id = "CB-" + uuid.uuid4().hex[:8].upper()

    movie = data["movie"]
    theatre = data["theatre"]
    show_time = data["show_time"]
    seats = ", ".join(data["seats"])
    food = data.get("food", "None")
    total = data["total"]

    connection = sqlite3.connect(DATABASE)

    connection.execute("""
        INSERT INTO bookings
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        booking_id,
        movie,
        theatre,
        show_time,
        seats,
        food,
        total
    ))

    connection.commit()
    connection.close()

    return jsonify({
        "success": True,
        "booking_id": booking_id
    })


@app.route("/ticket/<booking_id>")
def ticket(booking_id):

    connection = sqlite3.connect(DATABASE)

    connection.row_factory = sqlite3.Row

    booking = connection.execute(
        "SELECT * FROM bookings WHERE id = ?",
        (booking_id,)
    ).fetchone()

    connection.close()

    if booking is None:
        return "Booking not found", 404

    qr_folder = "static/qr"

    os.makedirs(qr_folder, exist_ok=True)

    qr_file = f"{qr_folder}/{booking_id}.png"

    qr_data = (
        f"CineBook\n"
        f"Booking: {booking['id']}\n"
        f"Movie: {booking['movie']}\n"
        f"Seats: {booking['seats']}"
    )

    qrcode.make(qr_data).save(qr_file)

    return render_template(
        "ticket.html",
        booking=booking,
        qr_file="/" + qr_file
    )


if __name__ == "__main__":

    create_database()

    app.run(
        debug=True,
        port=5000
    )