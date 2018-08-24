## Testing

### Automated Testing
- [coverage.py](https://coverage.readthedocs.io/en/coverage-4.5.1/)
    - Python code across applications is tested extensively using the **coverage.py** testing tool. **65 tests were run in development mode** (inc. 8 tests on Search feature for SQLite database) and **57 in production** (search feature test for Postgres database carried out manually). Custom code, for example provided by the Stripe payment service, was manually tested using the Stripe dashboard (also accounting for the under 90% test covergae on the Checkout app). The coverage on each of the apps is currently:
        - **Accounts** – 94%
        - **BugTickets** – 93%
        - **FeatureTickets** – 96%
        - **Cart** – 91%
        - **Checkout** – 88%
        - **Search** – (see manual testing)

To run automated testing in your local environment enter the following in the Command Line (replace ```app``` with name of the application being tested:

```$ coverage run --source=<app> manage.py test``` 

To produce a report of the coverage across a particualr app, follow the above command with:

```$ coverage report```

- [Travis CI](https://bower.io)
    - pre-deployment integration tests are carried out using the **Travis Continuous Integration** service. Integration tests were passing at time of deployment (as displayed at the head of the README file)

### Manual Testing
- The **Search** feature in development mode was based on queries of the Django provided SQLite database. The following tests (there were 8 in total) are an example of those run across the tables in which search was enabled (User, Profile, BugTicket, FeatureTicket):


    class TestSearch(TestCase):

        def setUp(self):
    
        self.user = User.objects.create_user('Tested', 'tested@mail.com', 'q0w9e8r7t7')
        self.user.save()
        login = self.client.login(username='Tested', password='q0w9e8r7t7')
        feature = FeatureTicket.objects.create(
                title='feature', 
                feature_type='Design', 
                description='this is a feature',
                created_by_id = 1
                )
    
        # Test feature search status code and page render
        def test_feature_search(self):
            response = self.client.get("/search/feature/?q={0}".format("feature"))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, "feature_listing.html")    
    
        # Test feature search with no matching results
        def test_feature_search_no_match(self):
            response = self.client.get("/search/feature/?q={0}".format("2feature2"))
            self.assertEqual(response.status_code, 200)
            messages = list(get_messages(response.wsgi_request))
            self.assertEqual(len(messages), 1)
            self.assertEqual(str(messages[0]), "Your search returned no results. Please try again.")

**Coverage ran at 94%**.

In production, however, a **Postgresql database** is used which caused these tests to fail the Travis CI test. Testing on the Postgresql database was done manually. 

Using a small sample of data (3 x users, 3 x bugtickets, 3 x featuretickets, 3 x alerts) keywords were inputted into the search form which tested if the query successfully located matching text in the fields targeted. The keywords were entered with a mixture of upper and lowercase to ensure searches were not case sensitive and the small sample enabled testing to identify keywords which appeared in a number of records and therefore produced more than one result (e.g. 'happens' in bugtickets, or 'union' in featuretickets).

- **User stories**, located in the [database schema](database_schema/db_schema.md) were used to test the functionalities of the application. This involved a step-by-step process of testing links, forms, comments, upvotes, bugticket and featureticket reports in production.

- **Password Reset** feature was tested by going through the reset process. Gmail settings had to be adjusted on two occasions - first to allow 'less secure' apps access to the account and secondly a 'Critical Security Alert' sent to the admin inbox which required a response to confirm the app's access to gmail account.

- The **Stripe** payment method had limited testing (2) in the automated testing suite. To test the payment system manually, details were entered (using Stripe's test Credit Card details) in the snAPP checkout form and the details associated with this purchase order (name, amount, date( was checked against the details provided on the Payment/Customer section of the Stripe Dashboard. 

- **JQuery** used to style the application and enhance UX was tested manually across the site. The process of triggering the effect, checking if it occured, refreshing the page and triggering again was used on each styled element.

- **Browser compatibility** - the site was viewed and tested manually across mobile, tablet, laptop and large desktop views and in the following browsers:
  - Mozilla Firefox
  - Google Chrome
  - Opera
  - Microsoft Edge

- **Unresolved bugs:**
    1. Clicking on the tab panes for displaying feature and bug charts in Chrome causes the page to 'blink'
    2. *embed* tag is not supported in Microsoft Edge preventing the pygal charts from rendering in that browser


- **The application [Can I Use](https://www.caniuse.com)** was used to check CSS code against the latest vendor prefix requirements.