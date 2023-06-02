# Blog App

## Description
Blog App is a Django REST backend project that serves as a blog website. It provides functionality for user management, blog post creation, blog categories, and blog comments. The project includes different permission levels for users, allowing them to perform specific actions based on their roles.

## Installation
To run the Blog App locally, please follow these steps:

1. Clone the repository:
```
git clone https://github.com/omer-fsdev/blog_app-django_REST.git
```

2. Navigate to the project directory:
```
cd blog-app
```

3. Create a virtual environment:
```
python3 -m venv env
```

4. Activate the virtual environment:
- For Windows:
  ```
  .\env\Scripts\activate
  ```
- For macOS and Linux:
  ```
  source env/bin/activate
  ```

5. Install the project dependencies:
```
pip install -r requirements.txt
```

6. Set up the database:
- Modify the database settings in the `settings.py` file to match your environment.
- Run the following command to migrate the database:
  ```
  python manage.py migrate
  ```

7. Start the development server:
```
python manage.py runserver
```


8. Access the application in your web browser at `http://localhost:8000`.

## Usage Guide
The Blog App provides the following features:

- User management: Users can register, login, and manage their accounts.
- Blog posts: Users can create, view, update, and delete blog posts.
- Blog categories: Users can categorize blog posts into different categories.
- Blog comments: Users can leave comments on blog posts.
- Permissions: Different users have different permission levels, enabling them to perform specific actions based on their roles.

To use the application, you can follow these steps:

1. Register a new user account.
2. Log in to your account using your credentials.
3. After logging in, obtain an authentication token by making a `POST` request to the `/auth/login/` endpoint with your username and password. The response will contain a token that you can use for subsequent requests.
4. Include the obtained token in the `Authorization` header of your requests as follows:
```
Authorization: Token <your_token>
```
6. Explore existing blog posts, categories, and comments.
7. Create new blog posts and assign them to categories.
8. Leave comments on blog posts.

Note: Token authentication is required for protected endpoints, such as creating, updating, or deleting blog posts and comments.

## API Documentation
For detailed API documentation (Swagger), please refer to the `https://localhost:8000/api/docs/`.

## Other Pertinent Information
Here are a few additional details you may find helpful:

- Technologies used: Django, Django REST Framework, Python, and PostgreSQL.
- The project follows the Model-View-Controller (MVC) architectural pattern.
- Make sure to set up proper authentication and authorization mechanisms to secure the application.
- The project includes API endpoints for interacting with the backend programmatically.
- Feel free to extend and customize the project as per your requirements.

For more details and API documentation, please refer to the codebase and relevant Django and Django REST Framework documentation.

Happy blogging!
