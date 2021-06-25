# from django.shortcuts import render
# import pyrebase
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db
#
# config = {
#     apiKey: "AIzaSyChJy3gvOtOFifeDHBd-l-49q24etJPNYs",
#     authDomain: "keton-password-manager.firebaseapp.com",
#     projectId: "keton-password-manager",
#     storageBucket: "keton-password-manager.appspot.com",
#     messagingSenderId: "245678840912",
#     appId: "1:245678840912:web:bc24e704e8ff6cca0f0555",
#     measurementId: "G-232CFZF1WJ"
# }
# firebase=pyrebase.initialize_app(config)
# authe = firebase.auth()
# database=firebase.database()
#
# def home(request):
#     day = database.child('Data').child('Day').get().val()
#     id = database.child('Data').child('Id').get().val()
#     projectname = database.child('Data').child('Projectname').get().val()
#     return render(request,"Home.html",{"day":day,"id":id,"projectname":projectname })
