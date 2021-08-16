from unittest import TestCase
from app import app
from models import db, User

app.config['SQLALCHEMY_DATABASE-URI'] ='postgresql://:5433/blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

app.config['TESTING'] = True

app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toollbar']

db.drop_all()
db.create_all()

class userViewsTestCase(TestCase):
    """testcase for views for users"""


    def setUp(self):
        """add sample user"""
        User.query.delete()
        user = User(first_name="Jude", last_name="okwu",image_url="https://d3j2s6hdd6a7rg.cloudfront.net/v2/uploads/media/default/0002/15/thumb_114242_default_news_size_5.jpeg")
        db.session.add(user)
        db.session.commit()

        self.user_id = user.id

    def tearDown(self):
        """clean up after every test"""

        db.session.rollback()
    
    def test_list_users(self):
        with app.test_client() as client:
            resp = client.get("/")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Jude", html)

    def test_show_details(self):
        with app.test_client() as client:
            resp = client.get(f"/{self.user_id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Jude", html)

    def test_add_user(self):
        with app.test_client() as client:
            one_user = {"first_name": "Sadio", "last_name": "Mane", "image_url":"360_F_225334977_SkeDBY9GMtZ0VuRmX9Q2reQMpNch86xR.jpg"}
            resp = client.post("/", data=one_user)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 302)
            # self.assertIn("Sadio", html)

    def test_edit_user(self):
        with app.test_client() as client:
            resp = client.get(f"/edit/{self.user_id}")
            html = resp.get_data(as_text=True)
            
            # i need help here. please i intend to get the value in one of those input
            # and compare it.
            # self.assertIn("okwu", )