## Technologies used
- **Python 3.12**
- **GCI (Common Gateway Inteface)** for client-server communication
- **PostgreSQL** as the relational database
- **HTML5 & CSS3** for frontend templates
## Implemented Funcitonalities
### Data Validation
Implemented in `validators/validate_date.py`
- Checks that names contains only alplabetic characters
- Ensures email follows as a valid format
- Enforces strong password rules such as length, letters, digits
### CAPTCHA
Implemented in `validators/captcha.py`
- Random 5-character alphanumeric code
- User verification at login and registration
### Registration
Implemented in `cgi-bin/register.py`
- Validates input
- Stores user data (first name, last name, email and password) in the **PostgreSQL** database
### Login / Logout
Implemented in:
- `cgi-bin/login.py` - verifies email and password and redirects to profile page
- `cgi-bin/logout.py`- logs out the user and redirects to login page
### Profile Update
Implemented in `cgi-bin/profile.py`
- Users can edit their name, email and password
- Updates are saved in the **PostgreSQL** database using SQL `UPDATE`
### Unit Tests
Located in the `tests/` directory:
- `test_validate_data.py` and `test_captcha.py`
- Tested using Python's built-in `unittest` module
## Built-in Python Functions and Libraries Used
### Python Standard Library
- `os` module - for file path management
- `cgi` module - to handle HTML form data
- `cgitb` module - for error debugging in CGI
- `html` module - to prevent XSS
- `psycopg2` - for PostgreSQL operations
## Project File Description
### cgi-bin/
This folder contains all CGI Python scripts responsible for the application's main funtionality - registration, login and profile.
- `register.py`- Handles user registration; Insert new users into the PostgreSQL database; Displays dynamically in HTML
- `login.py`- Handles user login; Check email and password in the PostgreSQL database; Redirects users to their profile after succesful login
- `profile.py`- Displays the logged-in user's information; Allows users to update their profile data
### validators/
Contains all custom validation
- `validate_date.py` - provides validation function for user input;
  -- `validate_name(name)`- checks for valid names
  -- `validate_email(email)` - checks for valid emails
  -- `validate_password(password)` - checks for password strength
- `captcha.py`- Implements CAPTCHA logic for bot protection:
  --`generate_captcha()`- creates a random 5-character code
  --`verify_captcha()` - compares user input to the generated code
### templates/
Contains HTML templates:
- `registration_form.html` - HTML form for user registration
- `sign_in_form.html` - HTML form for login
- `profile.html` - User profile interface (details and edit)
### static/
Contains CSS stylessheets:
- `reigstration_form.css`- CSS stylesheet for registration form template
- `sign_in.css`- CSS stylesheet for log in form template
- `profile.css`- CSS stylesheet for profile page
### tests/
Contains unit tests:
- `test_validate_data.py`- test name, email and passwordd validation
- `test_captcha.py`- tests CAPTCHA generation and verification
### server.py
HTTP server for local development.
Uses http.server and CGIHTTPRequestHandle to serve the CGI scripts
Runs the project on http://localhost:8000
## Running the Aplication
1. Make sure you have **Python 3.12+** and **PostgreSQL** installed.
2. Create a database named `accounts` and a table:
   ```sql
   CREATE TABLE users (
       id SERIAL PRIMARY KEY,
       first_name VARCHAR(50),
       last_name VARCHAR(50),
       email VARCHAR(100) UNIQUE,
       password VARCHAR(100)
   );
3. Start the server - python server.py
4. Open browser and go to: http://localhost:8000/cgi-bin/register.py

