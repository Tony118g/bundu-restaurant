# Testing

## Code Validation
All code written for the project has been validated. The final validation results can be seen below.

### W3C HTML Validator Final Results
All HTML code has been run through the [W3C HTML Validator](https://validator.w3.org/).

* During validation, a few problems were presented but after correcting the relevant issues, no warnings or errors were shown.

    * For more information on the warnings and errors that were presented, please go to the known Bugs section.

All pages presented the following message after validation.

![Screenshot of html validator result](documentation/testing-images/html-validation.png)

## Automated Testing

During development, I created automated tests for the main functionality of the project. I found this very beneficial in ensuring the site works as intended.

Tests were created for each app to test key features and functionality. I used [coverage](https://pypi.org/project/coverage/) to keep track of the amount of code my tests have covered and generated reports to find out which areas were untested so I could be sure to cover as much as possible.

I currently have 52 automated tests overall which all pass and provide 99% coverage for the project.

To run the automated tests, use the command - "python3 manage.py test"

![Screenshot of automated tests result](documentation/testing-images/automated-test-result.png)

![Screenshot of automated tests coverage report](documentation/testing-images/test-coverage-report.png)
