# Cущности:

# class User:
#     id
#     username
#     email
#     password_hash
#     role (client, driver)

# class Trip:
#     id
#     driver_id (Foreign Key to User)
#     origin
#     destination
#     date_time
#     available_slots
#     price
#     status (available, booked, completed)
#     is_group_trip (boolean)

# class Booking:
#     id
#     client_id (Foreign Key to User)
#     trip_id (Foreign Key to Trip)
#     num_horses
#     status (pending, confirmed, cancelled)
#     booking_date

# class Request:
#     id
#     client_id (Foreign Key to User)
#     origin
#     destination
#     preferred_date
#     num_horses
#     notes
#     status (open, matched, fulfilled)
