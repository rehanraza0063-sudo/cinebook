function searchMovies() {

    const search =
        document
        .getElementById("search")
        .value
        .toLowerCase();

    const movies =
        document.querySelectorAll(".movie-card");

    movies.forEach(function(movie) {

        const title =
            movie
            .getAttribute("data-title");

        if (title.includes(search)) {

            movie.style.display = "";

        } else {

            movie.style.display = "none";

        }

    });

}


function selectTime(button) {

    document
        .querySelectorAll(".showtime")
        .forEach(function(btn) {

            btn.classList.remove("selected");

        });

    button.classList.add("selected");

}


if (document.getElementById("seats")) {

    fetch("/api/seats")

        .then(response => response.json())

        .then(data => {

            createSeats(data.occupied);

        });

}


function createSeats(occupied) {

    const container =
        document.getElementById("seats");

    const rows =
        ["A","B","C","D","E","F","G","H"];


    rows.forEach(function(row) {

        for (let number = 1;
             number <= 10;
             number++) {


            const seat =
                document.createElement("button");


            const seatNumber =
                row + number;


            seat.innerText =
                number;


            seat.className =
                "seat";


            seat.dataset.seat =
                seatNumber;


            if (occupied.includes(seatNumber)) {

                seat.classList.add("occupied");

            }


            seat.onclick = function() {

                if (
                    !seat.classList
                    .contains("occupied")
                ) {

                    seat.classList
                        .toggle("selected");

                    updateSummary();

                }

            };


            container.appendChild(seat);

        }

    });

}


function updateSummary() {

    const selected =
        document.querySelectorAll(
            ".seat.selected"
        );


    const seats = [];


    selected.forEach(function(seat) {

        seats.push(
            seat.dataset.seat
        );

    });


    const ticketPrice =
        seats.length * moviePrice;


    let foodPrice = 0;


    document
        .querySelectorAll(".food")
        .forEach(function(food) {

            if (food.checked) {

                foodPrice +=
                    Number(
                        food.dataset.price
                    );

            }

        });


    const total =
        ticketPrice + foodPrice;


    document.getElementById(
        "selectedSeats"
    ).innerText =
        seats.length
        ? seats.join(", ")
        : "None";


    document.getElementById(
        "ticketPrice"
    ).innerText =
        ticketPrice;


    document.getElementById(
        "total"
    ).innerText =
        total;

}


document
    .querySelectorAll(".food")
    .forEach(function(food) {

        food.addEventListener(
            "change",
            updateSummary
        );

    });


function makeBooking() {

    const selected =
        document.querySelectorAll(
            ".seat.selected"
        );


    const seats = [];


    selected.forEach(function(seat) {

        seats.push(
            seat.dataset.seat
        );

    });


    if (seats.length === 0) {

        alert(
            "Please select at least one seat."
        );

        return;

    }


    const theatre =
        document.getElementById(
            "theatre"
        ).value;


    const selectedShow =
        document.querySelector(
            ".showtime.selected"
        );


    const showTime =
        selectedShow
        ? selectedShow.dataset.time
        : "10:00 AM";


    const foodItems = [];


    document
        .querySelectorAll(".food")
        .forEach(function(food) {

            if (food.checked) {

                foodItems.push(
                    food.dataset.price
                );

            }

        });


    const total =
        Number(
            document
            .getElementById("total")
            .innerText
        );


    if (
        !confirm(
            "Confirm payment of ₹"
            + total
            + "?"
        )
    ) {

        return;

    }


    fetch("/book", {

        method: "POST",

        headers: {
            "Content-Type":
                "application/json"
        },

        body: JSON.stringify({

            movie:
                "{{ movie.title }}",

            theatre:
                theatre,

            show_time:
                showTime,

            seats:
                seats,

            food:
                foodItems.join(", "),

            total:
                total

        })

    })

    .then(response =>
        response.json()
    )

    .then(data => {

        if (data.success) {

            window.location.href =
                "/ticket/"
                + data.booking_id;

        }

    });

}