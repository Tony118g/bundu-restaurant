# Testing

## Code Validation
All code written for the project has been validated. The final validation results can be seen below.

### W3C HTML Validation Results
All HTML code has been run through the [W3C HTML Validator](https://validator.w3.org/).

* During validation, a few problems were presented but after correcting the relevant issues, no warnings or errors were shown.

    * For more information on the warnings and errors that were presented, please go to the known Bugs section.

All pages presented the following message after final validation.

![Screenshot of html validation result](documentation/testing-images/html-validation.png)

### W3C CSS Validation Results
All custom CSS code has been run through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).

* No errors were presented for custom css.
    * Warnings shown are in relation to bootstrap classes.

![Screenshot of css validation result](documentation/testing-images/css-validation-result.png)

### JSHint Validation Results
All custom javascript code has been run through [JSHint](https://jshint.com/).

* No warnings or errors were presented.

![Screenshot of JSHint result](documentation/testing-images/jshint-validation-result.png)

### CI Python Linter Validation Results
All python code written by myself for this project was developed following PEP8 guidelines and was run through the [CI Python Linter](https://pep8ci.herokuapp.com/).

* All final python files presented no warnings or errors.

![Screenshot of python validation result](documentation/testing-images/python-validation-result.png)

## Automated Testing

During development, I created automated tests for the main functionality of the project. I found this very beneficial in ensuring the site works as intended.

Tests were created for each app to test key features and functionality. I used [coverage](https://pypi.org/project/coverage/) to keep track of the amount of code my tests have covered and generated reports to find out which areas were untested so I could be sure to cover as much as possible.

I currently have 52 automated tests overall which all pass and provide 99% coverage for the project.

To run the automated tests, use the command - "python3 manage.py test"

![Screenshot of automated tests result](documentation/testing-images/automated-test-result.png)

![Screenshot of automated tests coverage report](documentation/testing-images/test-coverage-report.png)
