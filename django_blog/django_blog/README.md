## Authentication System Documentation
# Overview

The authentication system in the django_blog project allows users to:

Register a new account

Log in and log out

View and edit their profile information (including email and optional profile picture/bio)

This system is built using Django’s built-in authentication framework combined with custom views and templates in the users app.

# 1.User Registration
📍 Location:

View: users/views.py → register_view

URL: /register/

Template: users/register.html

📜 Description:

The registration feature allows new users to create an account by providing:

Username

Email

Password (and confirmation)

We extend Django’s built-in UserCreationForm to include the email field and any custom validations.

Flow:

User navigates to /register/

Fills out and submits the registration form

On success → redirected to login page with a success message

On failure → errors are displayed on the form

How to Test:

✅ Go to /register/

✅ Enter new user credentials

✅ Check that the user is created in the admin panel (/admin/auth/user/)

# 2. User Login
📍 Location:

View: Uses Django’s built-in LoginView

URL: /login/

Template: users/login.html

📜 Description:

Registered users can log into the site using their username and password.

Flow:

User navigates to /login/

Submits their credentials

On success → redirected to home page or profile

On failure → error message appears

How to Test:

✅ Try logging in with valid credentials → should redirect successfully

✅ Try logging in with invalid credentials → error message should appear

# 3. User Logout
📍 Location:

View: Uses Django’s built-in LogoutView

URL: /logout/

Template: users/logout.html

📜 Description:

Users can log out, which ends their session and redirects them to a logout confirmation page or the home page.

How to Test:

✅ Login as a user

✅ Go to /logout/

✅ Try accessing a protected page (like /profile/) → should redirect to login page

# 4. Profile Management
📍 Location:

View: users/views.py → profile_view

URL: /profile/

Template: users/profile.html

Model: users/models.py → Profile

📜 Description:

Authenticated users can:

View their profile details

Update their email, bio, and profile picture (if enabled)

Flow:

User logs in

Navigates to /profile/

Can edit their details and submit changes

On success → success message and updated profile

## How to Test:

✅ Login and visit /profile/

✅ Update email and bio → refresh page to confirm changes

✅ Upload a profile picture → check media folder and profile view

🧪 Testing Checklist

✅ Registration:

 Create a new account with valid credentials

 Try registering with a username that already exists

✅ Login:

 Log in with valid credentials

 Attempt with invalid password

✅ Logout:

 Log out and confirm session ends

 Attempt to visit /profile/ after logout

✅ Profile Management:

 Update email and verify changes

 Upload a profile picture

 Submit invalid form data and check for errors