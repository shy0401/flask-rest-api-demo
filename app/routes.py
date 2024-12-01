from flask import Blueprint, jsonify
from .models import Job
from . import db

main_bp = Blueprint('main', __name__, url_prefix='/api')

@main_bp.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    result = [
        {
            "id": job.id,
            "company": job.company,
            "title": job.title,
            "link": job.link,
            "location": job.location,
            "experience": job.experience,
            "education": job.education,
            "employment_type": job.employment_type,
            "deadline": job.deadline,
            "sector": job.sector,
            "salary": job.salary
        }
        for job in jobs
    ]
    return jsonify(result)
