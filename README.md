<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/smeidigung/MULe">
    <img src="/static/images/MULe_banner.jpg" alt="Logo" width="400">
  </a>

<h3 align="center">MULe Website</h3>

  <p align="center">
    Website for the Mensa Ung Lejr
    <br />
    <a href="https://github.com/smeidigung/MULe"><strong>Explore the docs »</strong></a>
    <br />
    ·
    <a href="https://github.com/smeidigung/MULe/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/smeidigung/MULe/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project was created to ease the signup and management of all future danish Mensa Youth camps.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Flask][Flask.com]][Flask-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these steps.

### Prerequisites

* Python >= 3.10 - [Download & Install Python](https://www.python.org/downloads/). You need python since this project is built in Python.

### Installation

1. Fork the repository to your own GH profile

2. Clone the repository to your local machine:
   ```sh
   git clone https://github.com/smeidigung/MULe.git
   ```
3. Create a virtual environment from your bash terminal at the desired location:
  ```sh
   python -m venv .venv
   ```
4. Start your virtual environment:
  ```sh
  source .venv/Scripts/activate
  ```
  or for Unix systems
  ```sh
  source .venv/bin/activate
  ```
  
5. Install packages from the requirements file:
   ```sh
   pip install -r requirements.txt
   ```
6. Set the flask variables:
  ```sh
  export FLASK_ENV=development
  export FLASK_APP=main.py
  export DEBUG=1
  ```
7. Run the project:
  ```sh
  flask run
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap

- [x] Make site menu
- [ ] Create users
    - [ ] Save user data
    - [ ] Login to see account
    - [ ] Edit account option
- [ ] Make signup form
    - [ ] Show and edit my signup
- [ ] Refactor to clean arcitecture
- [ ] Switch to poetry for dependency management
- [ ] Unit tests
- [ ] Email verification
- [ ] Password protection
- [ ] About MULe subpage
- [ ] Website goes live

See the [open issues](https://trello.com/b/xuhzp9ku/mule-website) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Erik Smedegaard - smede_gaard@hotmail.com

Project Link: [https://github.com/smeidigung/MULe](https://github.com/smeidigung/MULe)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/smeidigung/MULe.svg?style=for-the-badge
[contributors-url]: https://github.com/smeidigung/MULe/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/smeidigung/MULe.svg?style=for-the-badge
[forks-url]: https://github.com/smeidigung/MULe/network/members
[stars-shield]: https://img.shields.io/github/stars/smeidigung/MULe.svg?style=for-the-badge
[stars-url]: https://github.com/smeidigung/MULe/stargazers
[issues-shield]: https://img.shields.io/github/issues/smeidigung/MULe.svg?style=for-the-badge
[issues-url]: https://github.com/smeidigung/MULe/issues
[linkedin-url]: https://linkedin.com/in/eriksmedegaard
[product-screenshot]: images/frontpage.jpg
[Flask.com]: static/images/flask_icon.png
[Flask-url]: https://flask.palletsprojects.com/
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com

