from . import db
from datetime import datetime

class Issue(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(100),nullable = False)
    description = db.Column(db.Text,nullable = False)
    status = db.Column(db.String(20),default = 'open')
    created_at = db.Column(db.DateTime,default = datetime.utcnow)
    
    def to_dict(self):
        return{
            "id":self.id,
            "title":self.title,
            "description":self.description,
            "status":self.status,
            "created_at":self.created_at.isoformat()
        }