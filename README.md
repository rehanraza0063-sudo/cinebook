# 🎬 CineBook — Movie Ticket Booking Platform

<p align="center">
  <strong>A modern full-stack movie ticket booking web application built with Python and Flask.</strong>
</p>

<p align="center">
  Movie discovery • Theatre selection • Showtimes • Seat booking • Food ordering • Digital tickets • QR codes
</p>

---

## 📌 About the Project

**CineBook** is a full-stack movie ticket booking web application developed as a learning and portfolio project.

The application simulates the complete movie-booking experience — from discovering a movie to selecting a theatre, choosing seats, adding food, confirming the booking, and receiving a digital ticket with a QR code.

The project focuses on understanding how a real-world booking platform can connect a **frontend interface, backend server, database, APIs, and booking logic** into one application.

> ⚠️ CineBook is an independent educational project and is not affiliated with, sponsored by, or endorsed by BookMyShow or any other movie-ticketing platform.

---

## ✨ Key Features

### 🎞️ Movie Discovery
- Browse available movies
- Movie posters
- Movie genres
- Languages
- Ratings
- Duration
- Movie descriptions
- Search functionality

### 🏢 Theatre & Showtime Selection
- Select a theatre
- Choose available showtimes
- View movie-specific booking information

### 💺 Interactive Seat Booking
- Visual cinema seat layout
- Select multiple seats
- Selected-seat highlighting
- Occupied-seat indication
- Automatic ticket price calculation

### 🍿 Food & Beverage
- Add snacks and beverages
- Update food quantity
- Automatically calculate food charges
- Include food cost in the final booking amount

### 🎟️ Digital Ticket
After booking, CineBook generates a digital ticket containing:

- Booking ID
- Movie name
- Theatre
- Showtime
- Selected seats
- Food selection
- Total amount
- QR code

### 📱 Responsive Interface
The application is designed with a modern dark cinema-style interface and responsive layouts for different screen sizes.

---

# 🖥️ Application Flow

```text
                    ┌─────────────────┐
                    │    CineBook     │
                    │    Home Page    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Select a Movie  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Select Theatre  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Select Showtime │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  Select Seats   │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Add Food/Drinks │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Review Booking  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Confirm Booking │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Digital Ticket  │
                    │   + QR Code     │
                    └─────────────────┘

🛠️ Tech Stack
Technology	Used For
🐍 Python	Backend development
🌐 Flask	Web framework
🗄️ SQLite	Booking database
HTML5	Web page structure
CSS3	Styling and responsive UI
JavaScript	Interactive functionality
QRCode	Digital ticket QR generation
Pillow	Image processing for QR codes
📂 Project Structure
CineBook/
│
├── app.py
├── requirements.txt
├── cinebook.db
│
├── templates/
│   ├── index.html
│   ├── movie.html
│   └── ticket.html
│
└── static/
    ├── style.css
    ├── script.js
    │
    └── qr/
        └── generated QR codes
🚀 Getting Started
1️⃣ Clone the Repository
git clone https://github.com/yourusername/CineBook.git

Move into the project:

cd CineBook
2️⃣ Create a Virtual Environment
Windows
python -m venv venv

Activate it:

venv\Scripts\activate

You should see:

(venv)

at the beginning of your terminal.

3️⃣ Install Dependencies
python -m pip install -r requirements.txt

Or install them manually:

python -m pip install Flask qrcode Pillow
4️⃣ Run the Application
python app.py

The Flask development server will start.

Open your browser and visit:

http://127.0.0.1:5000
🎫 Example Booking

A typical booking looks like:

Movie:
The Last Horizon

Theatre:
CineBook IMAX - Andheri

Showtime:
07:45 PM

Seats:
A5, A6, A7

Food:
Popcorn + Soft Drink

Total:
₹1,020

Booking ID:
CB-A1B2C3D4

The application then generates a digital ticket with a QR code.

🗄️ Database

CineBook uses SQLite for storing booking information.

Booking Data

The application stores:

Booking ID
Movie
Theatre
Showtime
Seats
Food
Total Amount

SQLite makes the project easy to run locally without requiring a separate database server.

🔌 Backend Routes
Route	Method	Purpose
/	GET	Home page
/movie/<id>	GET	Movie details
/api/seats	GET	Retrieve occupied seats
/book	POST	Create a booking
/ticket/<booking_id>	GET	Display digital ticket
🧠 What I Learned

Building CineBook helped me understand several concepts used in real-world web applications:

Backend Development
Flask routing
HTTP requests
JSON data
API endpoints
Server-side rendering
Database
SQLite
Creating database tables
INSERT operations
SELECT queries
Storing booking information
Frontend
HTML structure
CSS layouts
Responsive design
JavaScript DOM manipulation
Interactive seat selection
Full-Stack Integration

The project helped me understand how:

Frontend
    ↓
JavaScript
    ↓
Flask API
    ↓
Python Backend
    ↓
SQLite Database
    ↓
Booking Confirmation
    ↓
Digital Ticket

works together as a complete application.

🔐 Current Project Scope

This project is currently designed as a local educational/demo application.

The payment process is simulated and does not process real financial transactions.

Similarly, the movie, theatre, showtime, and seat information are demo data.

🔮 Future Improvements

The project can be extended with more production-oriented features:

👤 User registration and login
🔐 Secure authentication
📋 My Bookings section
🎭 Admin dashboard
🎬 Dynamic movie management
🏢 Theatre management
📅 Date-based showtimes
💺 Real-time seat availability
💳 Payment gateway integration
📧 Email ticket confirmation
📱 Mobile-friendly improvements
⭐ Movie reviews and ratings
❤️ Watchlist
🔔 Booking notifications
☁️ Cloud deployment
🔄 REST API improvements
📸 Screenshots

Add screenshots of your application here.

Home Page
screenshots/home.png
Movie Details
screenshots/movie-details.png
Seat Selection
screenshots/seat-selection.png
Digital Ticket
screenshots/digital-ticket.png

Example Markdown:

![CineBook Home](screenshots/home.png)

![Movie Details](screenshots/movie-details.png)

![Seat Selection](screenshots/seat-selection.png)

![Digital Ticket](screenshots/digital-ticket.png)
🎯 Project Goals

The main goals of CineBook were to:

Build a complete full-stack application
Practice Python Flask
Understand frontend-backend communication
Work with a relational database
Implement interactive seat booking
Generate digital tickets
Understand how booking systems work
Create a portfolio-ready software project
👨‍💻 Developer
Rehan Raza Shaikh

Biomedical Engineering Student | Software Development | AI/ML | Data | Cloud

I'm interested in building software projects that combine technology with real-world applications.

🔗 Connect With Me

LinkedIn

https://linkedin.com/in/rehan-raza-shaikh-3869a7328

GitHub

https://github.com/rehanraza0063-sudo

⭐ Support

If you found this project useful or interesting, consider giving the repository a ⭐ on GitHub.

📄 License

This project is created for educational and portfolio purposes.

You are free to study, modify, and extend the project for learning.


### One important improvement

For your actual GitHub repository, I recommend adding a **`screenshots` folder**:

```text
CineBook/
├── screenshots/
│   ├── home.png
│   ├── movie-details.png
│   ├── seat-selection.png
│   └── digital-ticket.png
