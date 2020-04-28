from config import app, db, func

class Dojo(db.Model):
    __tablename__ = 'dojos'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(45))
    city = db.Column(db.String(45))
    state = db.Column(db.String(45))
    created_at = db.Column(db.DateTime, server_default = func.now())
    updated_at = db.Column(db.DateTime, server_default = func.now(), onupdate = func.now())

class Ninja(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    dojo_id = db.Column(db.Integer, db.ForeignKey("dojos.id", ondelete = "cascade"))
    dojo = db.relationship('Dojo', foreign_keys=[dojo_id], backref = "dojos_ninjas")
    created_at = db.Column(db.DateTime, server_default = func.now())
    updated_at = db.Column(db.DateTime, server_default = func.now(), onupdate = func.now())
    
    def name(self):
        return self.first_name + " " + self.last_name
