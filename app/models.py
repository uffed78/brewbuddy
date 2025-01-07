from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Recipe(db.Model):
    """Databasmodell för sparade recept."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    bjcp_style = db.Column(db.String(100), nullable=False)
    inventory = db.Column(db.Text, nullable=False)  # JSON-struktur som text
    generated_recipe = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Konvertera recept till en dictionary för JSON-respons."""
        return {
            "id": self.id,
            "name": self.name,
            "bjcp_style": self.bjcp_style,
            "inventory": self.inventory,
            "generated_recipe": self.generated_recipe,
            "timestamp": self.timestamp.isoformat()
        }
