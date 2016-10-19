from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks') # Always says jhacks
    first, last, github = hackbright.get_student_by_github(github)
    proj_grade_tuple = hackbright.get_grades_by_github(github)
    print proj_grade_tuple

    html = render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github,
                            projinfo=proj_grade_tuple)

    return html


@app.route("/student_search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student_creator")
def student_creator():
    """Show form for creating a student."""

    return render_template("student_creator.html")


@app.route("/student_created", methods=['POST'])
def student_created():
    """Show results from student_creator."""

    fname = request.form.get("fname")
    lname = request.form.get("lname")
    github = request.form.get("github")

    hackbright.make_new_student(fname, lname, github)

    return render_template("student_created.html",
                            fname=fname,
                            lname=lname,
                            github=github)

    




if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
