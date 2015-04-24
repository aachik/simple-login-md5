from cpa_abs import db

engine = db.create_engine(
                "mysql+pymysql://root:aa121292@localhost/db"
            )

db.create_all()