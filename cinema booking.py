users={"admin":"admin123"} #admin credentials
movies={} # movies {"title": {"price": X, "date": Y, "tickets": Z}}
max_tickets_per_movie=5
from datetime import datetime

def login():
    username=input("Enter username: ")
    password=input("Enter password: ")

    if username in users and users[username]==password:
        return username
    else:
        print("Invalid credentials")
        return None
def add_movie():
    title=input("Enter movie title: ").strip()
    if title in movies:
        print("Movie already exists")
        return
    
    try:
        price=float(input("Enter ticket price: "))
        date_format= "%Y-%m-%d"
        date_str=input("Enter movie date (YYYY-MM-DD:)").strip()
        try:
            date=datetime.strptime(date_str, date_format).strftime(date_format)
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return
        movies[title]={"price": price,"date": date_str,"tickets": max_tickets_per_movie}
        print(f"Movie '{title}' added to the list")
    except ValueError:
        print("Invalid price. Please enter a number")
def remove_movie():
    if not movies:
        print("No movies to remove!")
        return
    
    view_movies()
    title=input("Enter movie title to remove: ").strip()
    if title in movies:
        del movies[title]
        print(f"Movie '{title}' removed succesfully.")
    else:
        print("Movie not found. ")
def view_movies():
    if not movies:
        print("No movies available.")
        return
    print("Currently showing: ")
    for title, details in movies.items():
        print(f"{title} , ${details['price']}  {details['date']} , Tickets left:{details['tickets']}")
def book_tickets():
    if not movies:
        print("No movies available for booking ")
        return
    view_movies()
    title=input("Enter the title of the movie you want to book: ").strip()
    if title in movies and movies[title]["tickets"]>0:
        price=movies[title]["price"]
        try:
            print(f'The ticket costs ${price}')
            amount = float(input("input payment amount: "))
            if amount<price:
                print("Insufficient amount. Booking failed")
            else:
                movies[title]["tickets"]-=1
                print(f"Booking confirmed for '{title}'. Enjoy!")
        except ValueError:
            print("Invalid payment amount. ")
    else:
        print("Movie not found or not tickets available.")
def admin_menu():
    if login()!= "admin":
        print("Access denied ")
        return
    while True:
        print("Admin Menu: ")
        print("1. Add Movie")
        print("2. Remove Movie")
        print("3. View Movies")
        print("4. Exit Admin Mode")
        choice=input("Enter your choice: ")

        if choice=="1":
            add_movie()
        elif choice=="2":
            remove_movie()
        elif choice=="3":
            view_movies()
        elif choice=="4":
            break
        else:
            print("Invalid choice. Enter again. ")
def user_menu():
    print("User Menu")
    while True:
        print("1. View Movies")
        print("2. Book Tickets")
        print("3. Exit User Mode")
        choice=input("Enter your choice: ")

        if choice=="1":
            view_movies()
        elif choice=="2":
            book_tickets()
        elif choice=="3":
            break
        else:
            print("Invalid choice. Enter again. ")
def main():
    print("Welcome to Baiskofuge Booking System!")
    while True:
        print("1. Admin Mode")
        print("2. User Mode")
        choice=input("Enter your choice: ")

        if choice=="1":
            admin_menu()
        elif choice=="2":
            user_menu()
        else:
            print("Invalid choice. Enter Again. ")


main()


