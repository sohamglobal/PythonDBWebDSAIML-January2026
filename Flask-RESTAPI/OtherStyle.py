from flask import Flask

app=Flask(__name__)

@app.route('/player',methods=['GET'])
def get_player():
    p={
        "name":"dominik szoboszlai",
        "age":24,
        "gender":"male",
        "club":"liverpool",
        "position":"midfielder"
    }
    return p

@app.route('/student/<course>',methods=['GET'])
def get_student(course):
    print(course)
    s={
        "rollno":786,
        "name":"sharayu",
        "course":"core java",
        "fees":4500.00
    }
    return s


if __name__=='__main__':
    app.run(debug=True)
