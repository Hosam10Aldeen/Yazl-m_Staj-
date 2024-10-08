from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mssql.information_schema import views

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
 # oldugumuz path'ta olusturacak
db = SQLAlchemy(app) # flask api ve veritabani arasindaki iletisim ve etkilesimleri olusturabilmek icin

class VideoModel(db.Model): #modelimizde sutunlari ekleme
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name={name}, views={views}, likes={likes})"

video_put_args = reqparse.RequestParser() #gelen istek verilerinin ayrıştırılması,burada bolumleri: adi,goruntulemeler,begenmeler
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the video", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of the video" )
video_update_args.add_argument("views", type=int, help="Views of the video" )
video_update_args.add_argument("likes", type=int, help="Likes of the video" )

resource_fields = {
                    'id':fields.Integer,
                    'name':fields.String,
                    'views':fields.Integer,
                    'likes':fields.Integer
                    } # cagirilan objenin getirilecek sututnlari(bolumleri)
class Video(Resource):
    @marshal_with(resource_fields)
    def get(self,video_id):
        result = VideoModel.query.filter_by(id=video_id).first() #veritabanindan id sutunuyla objeleri siralayarak bir obje getirme
        if not result:
            abort(404, message="Could not find video with that id")
        return result

    @marshal_with(resource_fields)
    def put(self,video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="this video id is already exist")

        video = VideoModel(id=video_id,name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201

    @marshal_with(resource_fields)
    def patch(self,video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Could not find video with that id,can not update")
        if args['name']: #name kismi bos degilse name kismini guncelleyemeye izin verecek
            result.name = args['name']
        if args['views']:
            result.views = args['views']
        if args['likes']:
            result.likes = args['likes']

        db.session.commit()
        return result

    def delete(self,video_id):
        abort_if_video_id_doesnt_exist(video_id)
        del videos[video_id]
        return '', 204 # delete isleminden sonra 204 status kodu donecek bize bu da no content yani icerik yok anlamina gelir

# api.add_resource(HelloWorld, "/helloworld/<string:ad>/<int:yas>") # parametre olusturmak ve kullanicidan veri almak
api.add_resource(Video, "/video/<int:video_id>")
if __name__ == "__main__":
    app.run(debug=True)
