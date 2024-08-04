📬 Django Newsletter System
Welcome to the Django Newsletter System! This project allows you to manage newsletter subscriptions, create engaging newsletters, and send them to your subscribers with ease.

Features ✨
📝 Subscription Management: Easily allow users to subscribe to your newsletter.
📰 Newsletter Creation: Create beautifully formatted newsletters using a rich text editor.
📧 Newsletter Delivery: Send newsletters to all your subscribers with a single click.

Getting Started 🚀
Prerequisites 📋
🐍 Python 3.x
🌐 Django 3.x or higher

Installation 🔧
Clone the repository:
git clone https://github.com/Bax-dev/Email_newsletter_system.git
cd django-newsletter-system

Install the dependencies:
pip install -r requirements.txt

Run database migrations:
python manage.py migrate
Start the development server:
python manage.py runserver

Access the application:
Open your browser and go to http://127.0.0.1:8000/

Usage 📚
Subscribe to the Newsletter ✍️
To subscribe to the newsletter, navigate to /subscribe/ and fill out the subscription form.

Create a Newsletter 📝
Go to /newsletter/create/
Fill out the form, including the subject and body of the newsletter.
Use the rich text editor to format your content with bold, italic, and underline options.

Submit the form to create the newsletter.

Send a Newsletter 📤
Navigate to the URL /newsletter/send/<newsletter_id>/
The newsletter will be sent to all subscribers.

License 📜
This project is licensed under the MIT License. See the LICENSE file for details.

Contributing 🤝
Contributions are welcome! Please feel free to submit a Pull Request.
