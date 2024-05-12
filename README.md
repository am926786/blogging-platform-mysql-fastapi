# blogging-platform-mysql-fastapi
# Tool- VS Code, MySQL
# Install FastAPI and pymysql using pip if you haven't already installed them using VS Code terminal:
pip install fastapi pymysql 

# Create a new Python file:
You can create a new Python file (e.g., blog_api.py) and paste the provided Python code into it.

# Configure MySQL connection details:
Replace 'localhost', 'username', 'password', and 'blog' with your MySQL server details in the code.
Ensure that you have MySQL installed and running, and create a database named 'blog' as mentioned in the SQL queries provided earlier.
SQL query-
CREATE TABLE posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL
);

CREATE TABLE comments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    post_id INT NOT NULL,
    text TEXT NOT NULL,
    FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE
);

CREATE TABLE likes_dislikes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    post_id INT NOT NULL,
    is_like BOOLEAN NOT NULL,
    FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE
);

# Run the Python script or notebook cell:
If you're using a Python file, you can run it from the command line or an integrated development environment (IDE) like VSCode or PyCharm.
Access the FastAPI endpoints:
Once the FastAPI application is running, you can access the endpoints by visiting http://localhost:8000 in your web browser or using tool like Postman to make HTTP requests.

# Insert-
To send a POST request to the /posts/ endpoint using Postman, follow these steps:
Open Postman and create a new request.
Set the request method to POST.
Enter the URL of the API endpoint. Assuming your FastAPI application is running locally on port 8000, the URL would be http://localhost:8000/posts/.
Switch to the "Body" tab in Postman.
Select the raw option and choose JSON from the dropdown menu.
In the text area below, enter the JSON data representing the post you want to create. For example:
{
    "title": "My First Blog Post",
    "content": "This is the content of my first blog post."
}
Click on the "Send" button to send the POST request to the API endpoint.
After sending the request, you should receive a response from the API indicating that the post was created successfully, along with a status code of 200 OK. If there are any errors or issues with the request, the response will provide information about the error.

# Update-
To send a PUT request to the /posts/{post_id} endpoint using Postman to update a blog post, follow these steps:
Open Postman and create a new request.
Set the request method to PUT.
Enter the URL of the API endpoint. Assuming your FastAPI application is running locally on port 8000 and you want to update a post with ID 1, the URL would be http://localhost:8000/posts/1.
Switch to the "Body" tab in Postman.
Select the raw option and choose JSON from the dropdown menu.
In the text area below, enter the JSON data representing the updated post. For example:
{
    "title": "Updated Title",
    "content": "This is the updated content of the post."
}
Click on the "Send" button to send the PUT request to the API endpoint.
By following these steps and providing the required data in the request body, you should be able to successfully update a post using the FastAPI-based API with Postman.

# Delete-
To send a DELETE request to the /posts/{post_id} endpoint using Postman to delete a blog post, follow these steps:
Open Postman and create a new request.
Set the request method to DELETE.
Enter the URL of the API endpoint. Assuming your FastAPI application is running locally on port 8000 and you want to delete a post with ID 1, the URL would be http://localhost:8000/posts/1.
Click on the "Send" button to send the DELETE request to the API endpoint.

# Comments-
To send a POST request to the /comments/ endpoint using Postman to create a comment, follow these steps:
Open Postman and create a new request.
Set the request method to POST.
Enter the URL of the API endpoint. Assuming your FastAPI application is running locally on port 8000, the URL would be http://localhost:8000/comments/.
Switch to the "Body" tab in Postman.
Select the raw option and choose JSON from the dropdown menu.
In the text area below, enter the JSON data representing the comment you want to create. For example:
{
    "post_id": 1,
    "text": "This is a new comment on the post."
}
Replace 1 with the actual ID of the post you want to comment on, and adjust the comment text as needed.
Click on the "Send" button to send the POST request to the API endpoint.

# Likes/dislikes-
To send a POST request to the /likes_dislikes/ endpoint using Postman to record a like or dislike for a post, follow these steps:
Open Postman and create a new request.
Set the request method to POST.
Enter the URL of the API endpoint. Assuming your FastAPI application is running locally on port 8000, the URL would be http://localhost:8000/likes_dislikes/.
Switch to the "Body" tab in Postman.
Select the raw option and choose JSON from the dropdown menu.
In the text area below, enter the JSON data representing the like or dislike action you want to record. For example:
{
    "post_id": 1,
    "like": true
}
Replace 1 with the actual ID of the post for which you want to record the like or dislike, and set the like field to true for a like or false for a dislike.
Click on the "Send" button to send the POST request to the API endpoint.
