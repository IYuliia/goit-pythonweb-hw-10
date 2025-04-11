
### Technical Task Description

1. **Authentication Mechanism**  
   Implement an authentication mechanism in the application.

2. **Authorization with JWT Tokens**  
   Implement authorization using JWT tokens so that all contact operations are performed only by registered users.

3. **User Access Control**  
   The user should only have access to their own contact operations.

4. **Email Verification**  
   Implement an email verification mechanism for registered users.

5. **Limit Requests**  
   Limit the number of requests to the `/me` route.

6. **Enable CORS**  
   Enable CORS for your REST API.

7. **User Avatar Update**  
   Implement the ability to update the user's avatar (use Cloudinary service).

---

### General Requirements for the Homework Assignment

- The requirements listed above are mandatory for evaluating the homework by the mentor. If any of the requirements are not met, the homework will be sent back to the student for revision without grading.
- If you have any questions or are stuck at any step, feel free to contact the mentor via Slack.
- When registering a user, if the user already exists with the same email, the server should return an HTTP 409 Conflict error.
- The server should hash passwords and not store them in plain text in the database.
- Upon successful user registration, the server should return HTTP status 201 Created along with the new user data.
- For all POST operations (creating a new resource), the server should return status 201 Created.
- During the POST operation, user authentication should occur, and the server should accept a request with user data (username and password) in the request body.
- If the user does not exist or the password does not match, HTTP 401 Unauthorized error should be returned.
- Authorization using JWT tokens should be implemented via the access token (`access_token`).
- All environment variables should be stored in the `.env` file. No confidential data should be stored directly in the code.
- Docker Compose should be used to run all services and databases in the application.
