from flask import Flask
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app)

class BasicREST(Resource):
    def get(self):
        profile={
            "number":9,
            "name":"praffull",
            "codename":"ethan hunt",
            "city":"london",
            "language":"english",
            "gender":"male",
            "dob":"9 june",
            "qualification":"MBA(MC)",
            "email":"praffull@outlook.com",
            "mobile":"7391966656",
            "keyskills":["java","python","sql"],
            "hobbies":["music","movies","sports","travel"]
        }
        return profile

api.add_resource(BasicREST,"/profile")
app.run(debug=True)