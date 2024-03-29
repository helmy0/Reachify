<p align="center">
  <img src="static/imgs/network.png" width="250" alt="Reachify CRM Logo">
</p>

# Reachify CRM

Reachify is a powerful Customer Relationship Management (CRM) web application built with Django. It's designed to streamline the process of managing customer interactions and data, empowering businesses to efficiently handle their relationships with clients.

## Features

- **Customer Tracking**: Easily manage and track customer details to better understand and serve your client base.
- **Product Inventory**: Keep track of your product inventory, including stock levels and availability.
- **Order Status**: Monitor and update order statuses to ensure smooth transactions and customer satisfaction.
- **Authentication & Authorization**: Customers access their personalized dashboard showcasing their respective order models. Meanwhile, administrators have an overarching dashboard providing an overview of all orders.
  
## Technologies Used

- **Django**: A high-level Python web framework for rapid development and clean, pragmatic design.
- **HTML/CSS**: Standard languages for building the structure and styling of web pages.
- **JavaScript**: Used for adding interactivity and dynamic features to the application.
- **AWS RDS**: Connected django backend to AWS RDS PostgreSQL.
- **AWS S3#**: Used S3 bucket to serve the static files (CSS & Imgs)


## Getting Started

To get started with Reachify, follow these steps:

1. Clone the repository: `git clone <repository-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start the development server: `python manage.py runserver`

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.
