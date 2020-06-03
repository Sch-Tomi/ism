[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![PyPI Downloads][pypi-downloads]][pypi-downloads]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/Sch-Tomi/ism">
    <img src="images/logo.jpg" alt="Logo">
  </a>

  <p align="center">
    Interactive SSH Menu
    <br />
    <a href="https://github.com/Sch-Tomi/ism"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Sch-Tomi/ism">View Demo</a>
    ·
    <a href="https://github.com/Sch-Tomi/ism/issues">Report Bug</a>
    ·
    <a href="https://github.com/Sch-Tomi/ism/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

[![ism Screen Shot][product-screenshot]](https://github.com/Sch-Tomi/ism)

The ISM project is a simple CLI script. ISM collects all your hosts from your ~/.ssh/config file, expect host that starts with a *.

The biggest advantage of ISM over similar programs ISM can handle [Include](https://man.openbsd.org/ssh_config#Include) rules.
Which is very usefull if you working with dozens of hosts.

### Built With

* [Python3](https://www.python.org/)
* [questionary](https://github.com/tmbo/questionary)

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Installation
 
1. Install by pip
```sh
pip install ism
```

2. From source
```sh
git pull https://github.com/Sch-Tomi/ism.git
cd ism
pip install . 
```

<!-- USAGE EXAMPLES -->
## Usage

After install, you can simply open ISM by ```ism``` in terminal. Use arrow keys to select a host then press ```Enter```. A SSH will open on the same terminal with the selected host.

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/Sch-Tomi/ism/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the GPLv3 License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/Sch-Tomi/ism](https://github.com/Sch-Tomi/ism)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Sch-Tomi/ism.svg?style=flat-square
[contributors-url]: https://github.com/Sch-Tomi/ism/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Sch-Tomi/ism.svg?style=flat-square
[forks-url]: https://github.com/Sch-Tomi/ism/network/members
[stars-shield]: https://img.shields.io/github/stars/Sch-Tomi/ism.svg?style=flat-square
[stars-url]: https://github.com/Sch-Tomi/ism/stargazers
[issues-shield]: https://img.shields.io/github/issues/Sch-Tomi/ism.svg?style=flat-square
[issues-url]: https://github.com/Sch-Tomi/ism/issues
[license-shield]: https://img.shields.io/github/license/Sch-Tomi/ism.svg?style=flat-square
[license-url]: https://github.com/Sch-Tomi/ism/blob/master/LICENSE.txt
[product-screenshot]: images/screenshot.gif
[pypi-downloads]: https://img.shields.io/pypi/dm/ism?style=flat-square