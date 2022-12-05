import app
from flask import json
import unittest
import requests

from mockito import when, mock, unstub

class TestSearch(unittest.TestCase):
    print("inside TEST class")

    def test_add_stu(self):  

        response = mock({"data":"added successfull"})
        when(requests).post('http://127.0.0.1:5000/add', strict = False ).thenReturn(response)

        data1 =  {
            "role": "admin",
            "user": "selva"
        }
        response = app.add_stu().post(
            '/add',
            json = data1,
            content_type='application/json',
        )
        print("running add_stu test")
        print(response)
        self.assertEqual(response.get_json(), {
            "data": "added successfully"
        })
        unstub()
if __name__ == '__main__':
    unittest.main()