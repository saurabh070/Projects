# User Management System (UMS)

This is a simple User Management System (UMS) API built using Flask and SQLite. It provides endpoints to create user accounts, view users, update user passwords, and delete users or user records.

## Requirements

- Python 3.x

## Setup

1. **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**

    ```bash
    python app.py
    ```

    The application will run on `http://127.0.0.1:5000`.

## Endpoints

### Create Account

- **URL:** `/create_account`
- **Method:** `POST`
- **Description:** Creates a new user account.
- **Request Body:**

    ```json
    {
        "userid": "user1",
        "password": "abc123",
        "email": "user1@test.in"
    }
    ```

- **Response:**

    ```json
    "User account is created."
    ```

### Show Users

- **URL:** `/show`
- **Method:** `GET`
- **Description:** Retrieves all user accounts.
- **Response:**

    ```json
    {
        "user": [
            ["user1", "abc123", "user1@test.in"],
            ["user2", "pqr123", "user2@test.in"]
        ]
    }
    ```

### Update Password

- **URL:** `/update_password`
- **Method:** `POST`
- **Description:** Updates the password for a specified user.
- **Request Body:**

    ```json
    {
        "userid": "user2",
        "password": "newpassword"
    }
    ```

- **Response:**

    ```json
    "Row Updated !!!"
    ```

### Delete User

- **URL:** `/delete_row`
- **Method:** `POST`
- **Description:** Deletes a specified user account.
- **Request Body:**

    ```json
    {
        "userid": "user1"
    }
    ```

- **Response:**

    ```json
    "Row Deleted !!!"
    ```

### Delete All Records

- **URL:** `/delete_records`
- **Method:** `POST`
- **Description:** Deletes all user records.
- **Request Body:**

    ```json
    {
        "action": "delete records"
    }
    ```

- **Response:**

    ```json
    "Records Deleted !!!"
    ```

### Delete Table

- **URL:** `/delete_table`
- **Method:** `POST`
- **Description:** Deletes the entire users table.
- **Request Body:**

    ```json
    {
        "action": "delete table"
    }
    ```

- **Response:**

    ```json
    "Table Deleted !!!"
    ```

## Notes

- Ensure the SQLite database (`UMS.db`) is in the same directory as the `app.py` file.
- The table `users` will be created automatically if it does not exist when creating a user account.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
