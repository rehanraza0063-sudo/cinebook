CineBook — Movie Ticket Booking Web Application

A full-stack movie ticket booking web application built as a learning project, inspired by modern cinema-booking platforms.

🎬 Features
🔎 Movie search
🎞️ Movie details and ratings
🏢 Theatre selection
🕐 Show-time selection
💺 Interactive seat selection
🍿 Food & beverage selection
💰 Automatic booking total calculation
🎟️ Digital movie ticket
📱 QR-code ticket generation
🗄️ SQLite database for bookings
📱 Responsive dark cinema-style UI
⚡ Flask backend with REST-style API endpoints
🛠️ Technologies Used
Technology	Purpose
Python	Backend programming
Flask	Web framework
SQLite	Database
HTML5	Page structure
CSS3	UI and responsive design
JavaScript	Interactive functionality
QRCode	Digital ticket QR generation
Pillow	QR-code image support
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
    └── qr/
🚀 How to Run
1. Clone the repository
git clone https://github.com/yourusername/CineBook.git
cd CineBook
2. Create a virtual environment

Windows PowerShell:

python -m venv venv
3. Activate the virtual environment
venv\Scripts\activate
4. Install dependencies
python -m pip install -r requirements.txt
5. Start the Flask server
python app.py
6. Open in your browser
http://127.0.0.1:5000
🎟️ Booking Flow
Home Page
    ↓
Select Movie
    ↓
Choose Theatre
    ↓
Choose Show Time
    ↓
Select Seats
    ↓
Choose Food
    ↓
Review Booking
    ↓
Confirm Booking
    ↓
Generate Digital Ticket
    ↓
QR Code
🗄️ Database

CineBook uses SQLite to store booking information.

The booking table contains:

Booking ID
Movie
Theatre
Show time
Selected seats
Food selection
Total amount
🔌 API Endpoints
Get occupied seats
GET /api/seats

Returns the currently occupied seats used by the demo.

Create booking
POST /book

Creates a new booking and returns a booking ID.

View ticket
GET /ticket/<booking_id>

Displays the digital ticket and generates its QR code.

📸 Screenshots

Add your project screenshots here after uploading them to GitHub:

![Home Page](screenshots/home.png)

![Movie Details](screenshots/movie.png)

![Seat Selection](screenshots/seats.png)

![Digital Ticket](screenshots/ticket.png)
🎯 Learning Objectives

This project was created to practice:

Python Flask development
Frontend and backend integration
REST API concepts
SQLite database operations
JavaScript DOM manipulation
Interactive UI development
Form/data handling
QR-code generation
Full-stack project structure
🔮 Future Improvements

Possible future versions can include:

User registration and login
My Bookings page
Admin dashboard
Real-time seat availability
Movie/date filtering
Multiple cities
Theatre management
Payment gateway integration
Email booking confirmation
Movie reviews and ratings
Production deployment
⚠️ Disclaimer

CineBook is an independent educational project created for learning and portfolio purposes. It is not affiliated with or endorsed by BookMyShow or any other movie-ticketing platform.

👨‍💻 Author

Rehan Raza Shaikh

Biomedical Engineering student interested in software development, AI/ML, data, cloud technologies, and healthcare technology.

Connect with me
LinkedIn: https://linkedin.com/in/rehan-raza-shaikh-3869a7328
GitHub: https://github.com/rehanraza0063-sudo
⭐ Project

If you find this project useful for learning, feel free to ⭐ the repository.
