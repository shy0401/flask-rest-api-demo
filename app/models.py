from . import db

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    link = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(255))
    experience = db.Column(db.String(255))
    education = db.Column(db.String(255))
    employment_type = db.Column(db.String(255))
    deadline = db.Column(db.String(255))
    sector = db.Column(db.String(255))
    salary = db.Column(db.String(255))
