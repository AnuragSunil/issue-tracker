from flask import Blueprint, request, jsonify
from .models import Issue
from . import db

issue_bp = Blueprint('issue', __name__)

@issue_bp.route('/issues',methods = ['GET'])

def get_issues():
    issues = Issue.query.all()
    return jsonify([issue.to_dict() for issue in issues])

@issue_bp.route('/issues',methods = ['POST'])
def create_issue():
    data = request.get_json()
    new_issue = Issue(
        title = data['title'],
        description = data['description']
    )
    db.session.add(new_issue)
    db.session.commit()
    return jsonify(new_issue.to_dict()),201

@issue_bp.route('/issues/<int:id>',methods = ['PATCH'])
def update_issue(id):
    data = request.get_json()
    issue = Issue.query.get_or_404(id)
    issue.status = data.get('status',issue.status)
    db.session.commit()
    return jsonify(issue.to_dict())

@issue_bp.route('/issues/<int:id>',methods = ['DELETE'])
def delete_issue(id):
    issue = Issue.query.get_or_404(id)
    db.session.delete(issue)
    db.session.commit()
    return jsonify({"message":"Issue deleted"})
