from flask import Blueprint, jsonify
from sqlalchemy.exc import SQLAlchemyError
from .models import Job
from . import db

# Define the Blueprint
main_bp = Blueprint('main', __name__, url_prefix='/api')

@main_bp.route('/jobs', methods=['GET'])
def get_jobs():
    try:
        # Query all jobs from the database
        jobs = Job.query.all()

        # Transform the data into a JSON-serializable list
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

        # Return the response with a 200 OK status
        return jsonify({"status": "success", "data": result}), 200

    except SQLAlchemyError as e:
        # Log the error and return a 500 Internal Server Error response
        print(f"Database error: {str(e)}")
        return jsonify({"status": "error", "message": "An error occurred while fetching jobs"}), 500
    except Exception as e:
        # Handle unexpected exceptions
        print(f"Unexpected error: {str(e)}")
        return jsonify({"status": "error", "message": "An unexpected error occurred"}), 500
