#Convert to Dict JSON Response and Print and Booking Id AND checkin and Checkout Data

a = {
    "bookingid": 2384,
    "booking": {
        "firstname": "SANIA",
        "lastname": "MEHAN",
        "totalprice": 432,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2022-01-01",
            "checkout": "2022-01-01"
        },
        "additionalneeds": "Lunch"
    }
}
print(a["booking"]["bookingdates"]["checkin"])
print(a["booking"]["bookingdates"]["checkout"])
print(a["bookingid"])