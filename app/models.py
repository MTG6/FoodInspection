from /develop/src import db


# Create a data model for the database to be setup for the app
class Insp(db.Model):
	index = db.Column(db.Integer, unique=False, nullable=False)
	city = db.Column(db.String(50), unique=False, nullable=False)
	dba_name = db.Column(db.String(120), unique=False, nullable=False)
	facility_type = db.Column(db.String(50), unique=False, nullable=False)
	inspection_date = db.Column(db.String(50), unique=False, nullable=False)
	inspection_id = db.Column(db.Integer, primary_key=True)
	inspection_type = db.Column(db.String(120), unique=False, nullable=False)
	latitude = db.Column(db.Float, unique=False, nullable=False)
	license_ = db.Column(db.String(120), unique=False, nullable=False)
	longitude = db.Column(db.Float, unique=False, nullable=False)
	results = db.Column(db.String(10), unique=False, nullable=False)
	risk = db.Column(db.String(10), unique=False, nullable=False)
	state = db.Column(db.String(2), unique=False, nullable=False)
	zip = db.Column(db.Integer, unique=False, nullable=False)
	infracs_total = db.Column(db.String(120), unique=False, nullable=False)
	infracs_minor = db.Column(db.String(120), unique=False, nullable=False)
	infracs_serious = db.Column(db.String(120), unique=False, nullable=False)
	infracs_critical = db.Column(db.String(120), unique=False, nullable=False)

	
	
    def __repr__(self):
        return '<Inspection %r>' % self.inspection_id
