# Personal Portfolio with Blog  

## Overview  

Welcome to my personal portfolio project! This web application showcases my skills, projects, and provides an integrated blog platform where I share insights and experiences. Built with a combination of powerful technologies including Django, HTML, CSS, JavaScript, and Python, this project highlights my capabilities as a developer.  

## Technologies Used  

- **Django**: A high-level Python web framework for building web applications quickly and efficiently.  
- **HTML**: The standard markup language for creating web pages and web applications.  
- **CSS**: A style sheet language used for describing the presentation of a document written in HTML.  
- **JavaScript**: A programming language that enables interactive web pages and enhances user experience.  
- **Summernote**: A simple WYSIWYG editor for HTML that is integrated into the Django admin panel to make blog post creation intuitive.  

## Features  

- **Responsive Design**: The portfolio is designed to be fully responsive, ensuring an optimal viewing experience on various devices.  
- **Blog Functionality**: Easily create, edit, and delete blog posts using the Summernote editor in the Django admin panel.  
- **Project Showcase**: Display your projects with descriptions and links for visitors to explore.  
- **Contact Form**: A simple contact form for visitors to reach out.  

## Installation  

To set up the project locally, follow these steps:  

1. **Clone the repository**:  

   ```bash  
   git clone https://github.com/Tindae2022/tindae.git  
   cd tindae2022
2. Set up a virtual environment (optional but recommended):
    ```bash  
   python -m venv venv  
source venv/bin/activate  # On Windows use `venv\Scripts\activate`


4. Install the required packages:
   ```bash
   pip install -r requirements.txt

6. Apply migrations:
``` python manage.py migrate ```
8. Create a superuser for accessing the admin panel:
```python manage.py createsuperuser```
9. Run the development server:
```python manage.py runserver```

10. Access the application: Open your web browser and go to http://127.0.0.1:8000.

**Usage**

To create or edit blog posts, log in to the Django admin panel at http://127.0.0.1:8000/admin using the superuser account you created.
Use the Summernote editor to format your blog content easily.
Explore your portfolio and projects via the main interface.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any inquiries or feedback, feel free to reach out at [alusinelavalie80@gmail.com].

Thank you for checking out my personal portfolio! I'm excited to share my work and connect with others in the community.

   
