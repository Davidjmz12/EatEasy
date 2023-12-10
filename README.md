# Eatasy - Restaurant Management Web Application

## Overview
"Eatasy" is a web application designed for restaurant management, providing detailed information about each dish. The goal is to cater to individuals with dietary restrictions or different food preferences, allowing them to explore various dining options in a specific area. Each menu item can be reviewed, contributing to a general opinion that aids decision-making for both customers and restaurants.

The application has a global focus but is particularly valuable for individuals with dietary restrictions, as it allows them to filter options according to their specific needs. This concept originated from the challenges faced by people with dietary restrictions in finding reliable information about safe dining options.

## Features
- **Detailed Information**: Users can access comprehensive details about each dish, including ingredients, with a focus on allergens and intolerances.
- **Global Focus**: While the application has a worldwide perspective, it proves especially useful for those with dietary restrictions, offering tailored filtering options.
- **Restaurant Partnership**: The platform relies on a network of restaurants contributing information about their establishments. In return, Eatasy provides visibility and exposure.
- **User-Generated Content**: Users play a crucial role by sharing reviews and preferences, generating valuable information for both users and restaurants.
- **Restaurant Analytics**: Participating restaurants receive analytics and reviews in exchange for sharing their menu and basic information.

## Installation

### Prerequisites
- [Docker](https://www.docker.com/) must be installed and active on your system.

### Installation Steps (Windows)

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/eatasy.git
   cd eatasy
2. Build the Docker containers:
   ```bash
   docker-compose -f ./docker-compose.yml build
3. Launch the application:
   ```bash
   docker-compose -f ./docker-compose.yml up
4. Access the application in yout web browser:
   [http://localhost:8000/](http://localhost:8000/)
   
## Contributing
We welcome contributions to improve Eatasy. If you have suggestions, bug reports, or want to contribute code, please follow our [Contribution Guidelines](CONTRIBUTING.md).

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For inquiries, reach out to the project maintainers:
- David Jiménez Omeñaca (your-email@example.com)
- Sonia Cambrón Blanco (your-email@example.com)
- David Tizne Ondiviela (your-email@example.com)
