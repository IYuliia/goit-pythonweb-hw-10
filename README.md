**Technical Description of the Task**

- Implement an authentication mechanism in the application.
- Implement an authorization mechanism using JWT tokens, so that all operations with contacts are performed only by registered users.
- A user should only have access to their own contact operations.
- Implement an email verification mechanism for registered users.
- Limit the number of requests to the user route `/me`.
- Enable CORS for your REST API.
- Implement the ability to update the user's avatar (use Cloudinary service).

---

**General Requirements for the Homework**

- During registration, if a user already exists with the same email, the server should return an HTTP 409 Conflict error.
- The server should hash the password and not store it in plain text in the database.
- Upon successful user registration, the server should return an HTTP 201 Created status and the new user's data.
- For all POST operations (creating a new resource), the server should return a 201 Created status.
- During a POST operation, user authentication should be performed. The server should accept a request with user data (username and password) in the request body.
- If the user does not exist or the password does not match, it should return an HTTP 401 Unauthorized error.
- The authorization mechanism using JWT tokens should be implemented via the access token (`access_token`).
- All environment variables should be stored in the `.env` file. No sensitive data should be exposed in plain text inside the code.
- Docker Compose should be used to launch all services and databases in the application.

