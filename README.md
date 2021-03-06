# Concussr

A responsive webapp to quickly gauge whether an athlete has suffered a concussion using a [King Devick Test](https://kingdevicktest.com/). To use this test, establish a benchmark time taken during a time when an individual has not possibly suffered head trauma. Then, after a hit to the head, this test can be used. Compare the results of the test. If the user's time has increased by five seconds or more, [there is a significant chance that the user has suffered a concussion](https://www.huffingtonpost.com/2015/03/06/child-concussion-test_n_6819206.html), or other serious head injury.

![screenshot](https://raw.githubusercontent.com/frfanizz/concussr/master/scrot.png)

## Getting Started

The following sections describe installation of Concussr

### Prerequisites

Download or clone repository. Install Python 3 and pip 3.

### Installing

Type the following code:

```
pip install --user --requirement requirements.txt
python webapp.py
```

Or, if Python3 (and pip3) are not the default versions on your machine:

```
pip3 install --user --requirement requirements.txt
python3 webapp.py
```

Use the generated address to view the site.

## Built With

* [Flask](http://flask.pocoo.org/) - A Microframework, for generating HTML from python
* [Jinja2](http://jinja.pocoo.org/docs/2.10/) - A templating language
* HTML, CSS & Javascript (Bootstrap) - Front end
* Mozilla - Voice recognition web API

## Authors

* [Adam Burns](https://github.com/adamburns) - Eye tracking
* [Francesco Fanizza](https://github.com/frfanizz) - Test generator functions, scoring of test, timer
* [Claudiu Moise](https://github.com/cnmoise) - Test layout, CSS
* [Mitch Croal](https://github.com/Artemish) - Set up page from frameworks, speech recognition API


## Acknowledgments

* [Rosetta Code](http://rosettacode.org/wiki/Rosetta_Code) - For Longest Common Subsequence samples
