from fileinput import filename
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL 
import re, os
from flask_mail import Mail, Message

from datetime import timedelta
from werkzeug.utils import secure_filename
import uuid as uuid





app = Flask(__name__)

app.secret_key = 'hardik secret_key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Sanskar'
app.config['MYSQL_DB'] = 'system'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

UPLOAD_FOLDER = 'static/birthpdf/'
app.config['UPLOAD_FOLDER_PDF'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024 

UPLOAD_FOLDER = 'static/userprofilepic/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'pithiyahardik95@gmail.com'
app.config['MAIL_PASSWORD'] = 'ppfrehgxhqlfoawp'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.permanent_session_lifetime = timedelta(minutes=10000000)


mysql = MySQL(app)
mail = Mail(app)
@app.route('/') 

# ================================ main page ================================================
@app.route('/login')
def login():
    if 'loggedin' in session:
        return redirect("/admindashboard")
    elif 'userloggedin' in session:
        return redirect('/userdashboard')
    else:
        return render_template("homemain.html")

# =========================== ** Admin Side All Code **===============================

# =================================== Admin login ===========================================
@app.route('/adminlogin', methods = ['GET', 'POST'])
def adminlogin():
      if request.method == 'POST':
        femail = request.form.get("email")
        fpassword = request.form.get("password")
        if not femail :
            msg = 'blank  email not allowed'
            return render_template('adminlogin.html', msg=msg)
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', femail):
            msg = 'Invalid email address !'    
            return render_template('adminlogin.html', msg=msg)
        elif not fpassword:
            msg = "blank  password not allowed"
            return render_template('adminlogin.html', msg=msg)
        elif not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', fpassword):
            msg = "Minimum eight characters, at least one uppercase letter, one lowercase letter, one number and one special character:"
            return render_template('adminlogin.html', msg=msg)
        
        else:
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM Admin_login WHERE email = % s AND password = md5(% s)', (femail, fpassword))
            hardik = cursor.fetchone()
            if hardik:
              session['loggedin'] = True
              session['id'] = hardik['Id']
              session['email'] = hardik['email']
              flash( 'Logged in successfully !' )
              return redirect('/admindashboard')
            else:
             msg = 'Incorrect admin name / password !'
             return render_template('adminlogin.html', msg=msg)
      
      return render_template("adminlogin.html")


# ==================================== Admin log out code =====================================
@app.route('/adminlogout')
def adminlogout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('email', None)
    flash("you are logout successfull ! ")
    return redirect(url_for('adminlogin'))

@app.route('/createuserinuserlist')
def createuserinuserlist():
    return render_template('create_user.html')

# ======================================== admin dashboard ===================================
@app.route('/admindashboard', methods = ['GET', 'POST'])
def admindashboard():
    if 'loggedin' in session:
        msg = session['email']
        
        if request.method == 'POST':
            if request.form['admin_button'] == 'userlist':
                return redirect('/showuser')
            else:
                return render_template('create_user.html')
    else:
        return redirect('adminlogin')
    return render_template('admindashboard.html', msg=msg)


#================================= create user page =======================================
@app.route('/createuser', methods = ['GET', 'POST'])
def createuser():
    if 'loggedin' in session:
        cur = mysql.connection.cursor()
        if request.method == 'POST':
            user_email = request.form.get('email')
            user_name = request.form.get('username')
            user_password = request.form.get('password')

            if not user_email :
                usermassage = 'blank  email not allowed'
                return render_template('create_user.html', umsg = usermassage)

            elif not re.match(r'[^@]+@[^@]+\.[^@]+', user_email):
                usermassage = 'Invalid email address !'    
                return render_template('create_user.html', umsg = usermassage)

            elif not user_name:
                usermassage = "blank user name not allowed !"
                return render_template('create_user.html', umsg = usermassage)

            elif not re.match(r'^[a-zA-Z0-9]([._-](?![._-])|[a-zA-Z0-9]){1,18}[a-zA-Z0-9]$', user_name):
                usermassage = "min 3 max 20 char,not allow special characters " 
                return render_template('create_user.html', umsg = usermassage)

            elif not user_password:
                usermassage = "blank  password not allowed"
                return render_template('create_user.html', umsg = usermassage)

            elif not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', user_password):
                usermassage = "Minimum eight characters, at least one uppercase letter, one lowercase letter, one number and one special character:"
                return render_template('create_user.html', umsg = usermassage) 

            else:

                cur.execute('SELECT * FROM User_login WHERE email = %s', [user_email])
                data = cur.fetchall()
                if data:
                    flash('already exists')
                    return redirect('/createuser')
                else:
                    sms = 'your User Name Is :'+ user_email +'\n\n'
                    sms2 = 'Your Password Is :' + user_password + '\n\n'
                    sms3 = 'Now You Can Login our System And Create Your Profile click :'+'http://127.0.0.1:5000/userlogin'
                    sms4 = sms+sms2+sms3
                    msg = Message('Hii Your User Name & Password', sender = 'pithiyahardik95@gmail.com', recipients = [user_email])
                    msg.body = sms4
                    mail.send(msg)

                    cur.execute("INSERT INTO User_login (email, user_name, password) VALUES (%s,%s,md5(%s))", (user_email, user_name, user_password))
                    mysql.connection.commit()
                    cur.close() 
                    flash("user create successfull & Send Mail !")
                    return redirect('showuser')    
        return render_template('create_user.html')
    else:
        return redirect('adminlogin')

#========================================= show user code ==================================
@app.route('/showuser', methods = ['GET','POST'])
def showuser():
    if 'loggedin' in session:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM User_login")
        data = cur.fetchall()
        cur.close()
        return render_template('user_list.html', user=data)
    else:
        return redirect('adminlogin')


# ============================= get user id ======================================
@app.route('/edit/<id>', methods=['POST', 'GET'])
def get_employee(id):
    if 'loggedin' in session:
        cur = mysql.connection.cursor()

        cur.execute('SELECT * FROM User_login WHERE id = %s', [id])
        data = cur.fetchall()
        cur.close()
        print(data[0])
        return render_template('update.html', user=data[0])
    else:
        return redirect('adminlogin')


# ================================= re set password id get===================================
@app.route('/idgetresetpassword/<id>')
def resetpassword(id):
    if 'loggedin' in session:
        cur = mysql.connection.cursor()

        cur.execute('SELECT * FROM User_login WHERE id = %s', [id])
        data = cur.fetchone()
        cur.close()
        return render_template('resetpassword.html', resetp=data)
    else:
        return redirect('adminlogin')
# ============================= edit user for admin ======================================
@app.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    if 'loggedin' in session:
        if request.method == 'POST':
        
            email = request.form.get('uemail')
            username = request.form.get('username')

            cur = mysql.connection.cursor()

            cur.execute('SELECT * FROM User_login WHERE id = %s', [id])
            data = cur.fetchall()
            cur.close()
            print(data[0])

            if not email :
                usermassage = 'blank  email not allowed'
                return render_template('update.html', user=data[0], umsg=usermassage)

            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                usermassage = 'Invalid email address !'    
                return render_template('update.html', user=data[0], umsg=usermassage)

            elif not username:
                usermassage = "blank user name not allowed !"
                return render_template('update.html', user=data[0], umsg=usermassage)

            elif not re.match(r'^[a-zA-Z0-9]([._-](?![._-])|[a-zA-Z0-9]){1,18}[a-zA-Z0-9]$', username):
                usermassage = "min 3 max 20 char,not allow special characters " 
                return render_template('update.html', user=data[0], umsg=usermassage)

            else:
                cur = mysql.connection.cursor()
                cur.execute("UPDATE User_login SET email = %s, user_name = %s WHERE Id = %s",(email, username, id) ) 
                mysql.connection.commit()
                flash("user update successfull !")
                return redirect(url_for('showuser'))
    else:
        return redirect('adminlogin')


# ============================= delete user for admin ======================================
@app.route('/delete/<string:id>', methods=['POST', 'GET'])
def delete_user(id):
    if 'loggedin' in session:
        cur = mysql.connection.cursor()

        cur.execute('DELETE FROM User_login WHERE id = {0}'.format(id))   
        mysql.connection.commit()
        flash("user delete successfull !")
        return redirect(url_for('showuser'))
    else:
        return redirect('adminlogin')

#======================================= re set password ===================================
@app.route('/resetpassword/<id>', methods = ['GET', 'POST'])
def resetpass(id):
    if 'loggedin' in session:
        if request.method == 'POST':
            password1 = request.form.get('password')
            password2 = request.form.get('repassword')

            if password1 == password2 :
                cur = mysql.connection.cursor()
                cur.execute("UPDATE User_login SET password = MD5(%s) WHERE Id = %s",(password1, id) )
                mysql.connection.commit()
                flash("user password re set successfull !")
                return redirect('/showuser')
            else:
                cur = mysql.connection.cursor()
                cur.execute("SELECT * FROM User_login WHERE id = %s", (id))
                data = cur.fetchone()
                cur.close()
                msg = "your password not match plase try agin"
                return render_template('resetpassword.html', msg =msg, resetp=data)
        
        return render_template('resetpassword.html')
    else:
        return redirect('adminlogin')
    

# ============================== admin show user profile ===================================
@app.route('/adminshowuserdata/<id>', methods=['GET','POST'])
def adminshowuserdata(id):
    if 'loggedin' in session:
        cur = mysql.connection.cursor()
        if cur.execute('SELECT * FROM User_profile WHERE user_id = %s', [id]) == 1:
            data = cur.fetchone()
            filename = data.get('img')
            birth = data.get('birthpdf')
            cur.execute('SELECT * FROM User_login WHERE Id = %s', [id])
            userdat = cur.fetchone()
            cur.close()
            return render_template('adminshowprofile.html', adminshowprofile=data,userdat=userdat,filename=filename,birth=birth)
        else:
            flash("user not fill data") 
            return redirect('/showuser')
    else:
        return redirect('adminlogin')

#================================== admin update user profile ================================
@app.route('/adminupdateprofile/<id>', methods=['GET','POST'])
def adminupdateprofile(id):
    if 'loggedin' in session:
        cur = mysql.connection.cursor()
        if cur.execute('SELECT * FROM User_profile WHERE user_id = %s', [id]) == 1:
            data = cur.fetchone()

            cur.close()
            return render_template('adminupdateprofile.html', adminshowprofile=data)
        else:
            flash("user not fill data")
            return redirect('/showuser')
    else:
        return redirect('adminlogin')
#======================= admin update user profile ========================================
@app.route('/adminupdateuserprofil/<id>', methods=['GET','POST'])
def adminupdateuserprofil(id):
    if 'loggedin' in session:
        if request.method == 'POST':
            fname = request.form.get('firstname')
            lname = request.form.get('lastname')
            dob = request.form.get('dob')
            mno = request.form.get('mno')
            gender = request.form.get('gender')
            address = request.form.get('address')
            city = request.form.get('city')
            state = request.form.get('state')
            zipcode = request.form.get('zipcode')


            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM User_profile WHERE user_id = %s', [id])
            data = cur.fetchone()
            cur.close()

            if not fname:
                msg = "blank  first name not allowed"
                return render_template('adminshowprofile.html', msg=msg, adminshowprofile=data)

            elif not re.match(r'[a-zA-Z ]+',fname):
                msg = 'only characters allowed'
                return render_template('adminshowprofile.html', msg=msg, adminshowprofile=data)

            elif not lname:
                lmsg = "blank  last name not allowed"
                return render_template('adminshowprofile.html', lmsg=lmsg, adminshowprofile=data)

            elif not re.match(r'[a-zA-Z ]+',lname):
                lmsg = 'only characters allowed'
                return render_template('adminshowprofile.html', lmsg=msg, adminshowprofile=data)

            elif not dob:
                lmsg = "blank  not allowed"
                return render_template('adminshowprofile.html', dmsg=lmsg, adminshowprofile=data)

            elif not mno:
                lmsg = "blank  not allowed"
                return render_template('adminshowprofile.html', nmsg=lmsg, adminshowprofile=data)

            elif not re.match(r'[0-9]{10}', mno):
                msg = "only 10 digits allowed"
                return render_template('adminshowprofile.html', nmsg=msg, adminshowprofile=data)

            elif not gender:
                lmsg = "blank  not allowed"
                return render_template('adminshowprofile.html', gmsg=lmsg, adminshowprofile=data)

            elif not address:
                lmsg = "blank  not allowed"
                return render_template('adminshowprofile.html', amsg=lmsg, adminshowprofile=data)

            elif not city:
                lmsg = "blank  not allowed"
                return render_template('adminshowprofile.html', cmsg=lmsg, adminshowprofile=data)

            elif not re.match(r'[a-zA-Z ]+',city):
                cmsg = 'only characters allowed'
                return render_template('adminshowprofile.html', cmsg=cmsg, adminshowprofile=data)

            elif not state:
                lmsg = "blank  not allowed"
                return render_template('adminshowprofile.html', smsg=lmsg, adminshowprofile=data)

            elif not re.match(r'[a-zA-Z ]+',state):
                msg = 'only characters allowed'
                return render_template('adminshowprofile.html', smsg=msg, adminshowprofile=data)

            elif not zipcode:
                lmsg = "blank  not allowed"
                return render_template('adminshowprofile.html', zmsg=lmsg, adminshowprofile=data)

            elif not re.match(r'[0-9]{6}', zipcode):
                msg = "only 6 digits allowed"
                return render_template('adminshowprofile.html', zmsg=msg, adminshowprofile=data)

            else:

                cur = mysql.connection.cursor()
                cur.execute("update User_profile set first_name=%s, last_name=%s, date_of_birth=%s,mobile_number=%s,gender=%s,address=%s,city=%s,state=%s,zipcode=%s,profile_updated_dt=curdate() where user_id=%s",(fname,lname,dob,mno,gender,address,city,state,zipcode,id))

                mysql.connection.commit()
                cur.close() 
                flash("user profile have successfull update ")
                return redirect('/showuser')
        return render_template('adminupdateprofile.html')
    else:
        return redirect('adminlogin')
    




#  ======================================** User Side All Code **=======================================

# ================================== User login code ==========================================
@app.route('/userlogin', methods = ['GET','POST'])
def userlogin():

     if request.method == 'POST':
        uemail = request.form.get('useremail')
        upassword = request.form.get('userpassword')

        if not uemail :
            usermassage = 'blank  email not allowed'
            return render_template('userlogin.html', umsg = usermassage)
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', uemail):
            usermassage = 'Invalid email address !'    
            return render_template('userlogin.html', umsg = usermassage)
        elif not upassword:
            usermassage = "blank  password not allowed"
            return render_template('userlogin.html', umsg = usermassage)
        elif not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', upassword):
            usermassage = "Minimum eight characters, at least one uppercase letter, one lowercase letter, one number and one special character:"
            return render_template('userlogin.html', umsg = usermassage) 
        else:    
         cursor = mysql.connection.cursor()
         cursor.execute('SELECT * FROM User_login WHERE email = % s AND password = md5(% s)', (uemail,upassword)) 
         userdata = cursor.fetchone()
         if userdata:
            session['userloggedin'] = True
            session['userid'] = userdata['Id']
            session['username'] = userdata['user_name'] 
            session['useremail'] = userdata['email']
             
            flash('You are successfully logged in')        
            return redirect(url_for('userdashboard'))
         else:
             usermassage = 'Incorrect username / password !'
             return render_template('userlogin.html', umsg = usermassage)

     return render_template("userlogin.html")

# ==================================== user log out code ===================================
@app.route('/userlogout')
def userlogout():
    session.pop('userloggedin', None)
    session.pop('userid', None)
    session.pop('username', None)
    session.pop('useremail', None)
    flash("your successfull logout:")
    return redirect(url_for('userlogin'))


#  ============================== user dashboard =====================================
@app.route('/userdashboard', methods=['GET','POST'])
def userdashboard():
    if 'userloggedin' in session:
        userid = session['userid']
        msg = session['username'] 
        msgemail = session['useremail']
        cur = mysql.connection.cursor()
        if cur.execute('SELECT * FROM User_profile WHERE user_id = %s', [userid]) == 1:
            data = cur.fetchone()
            filename = data.get('img')
            births = data.get('birthpdf')
            cur.close()
                  
            return render_template('userwelcomepage.html',msg = msg,userprofile=data,msge=msgemail,filename=filename,birth=births)
        else:
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM User_profile WHERE user_id = %s', [userid])
            data = cur.fetchone()
            cur.close()
            filename ='defoultimg.png'
            birthemty = " "
            return render_template('userwelcomepage.html',msg = msg,userprofile=data,msge=msgemail,filename=filename,birth=birthemty)

    else:
        return redirect('userlogin')

@app.route('/display/<filename>')
def display_image(filename):
	
	return redirect(url_for('static', filename='userprofilepic/' + filename), code=301)

@app.route('/show/<birth>')
def show_pdf(birth):
	
	return redirect(url_for('static', filename='birthpdf/' + birth), code=301)


# ================= check profile ==========================
@app.route('/checkuserprofile', methods=['GET','POST'])
def checkuserprofile():
    cur = mysql.connection.cursor()
    userid = session['userid']
    cur = mysql.connection.cursor()
    if cur.execute('SELECT * FROM User_profile WHERE user_id = %s', [userid]) ==1:
        flash('you are allread create your profile so you can edit your data')
        return redirect('/userdashboard')
    else:
        return redirect('/insertuserdata')
    
#==================================== user data insert ==================================================
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'pdf'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

ALLOWED_EXTENSIONS_PDF = set(['pdf']) 

def allowed_pdf(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS_PDF
    
@app.route('/insertuserdata', methods=['GET','POST'])
def insertuserdata():
    uid=session['userid']
    msgu = session['username'] 
    msgemail = session['useremail']
    if request.method == 'POST':
        fname = request.form.get('firstname')
        lname = request.form.get('lastname')
        file = request.files.get('pic')
        birth = request.files['birthCertificate']
        dob = request.form.get('dob')
        mno = request.form.get('mno')
        gender = request.form.get('gender')
        address = request.form.get('address')
        city = request.form.get('city')
        state = request.form.get('state')
        zipcode = request.form.get('zipcode')

        if not fname:
            msg = "blank  first name not allowed"
            return render_template('userfilldata.html', msg=msg)
        
        elif not re.match(r'[a-zA-Z ]+',fname):
            msg = 'only characters allowed'
            return render_template('userfilldata.html', msg=msg)

        elif not lname:
            lmsg = "blank  last name not allowed"
            return render_template('userfilldata.html', lmsg=lmsg)

        elif not re.match(r'[a-zA-Z ]+',lname):
            lmsg = 'only characters allowed'
            return render_template('userfilldata.html', lmsg=msg)

        elif not dob:
            lmsg = "blank  not allowed"
            return render_template('userfilldata.html', dmsg=lmsg)

        elif not mno:
            lmsg = "blank  not allowed"
            return render_template('userfilldata.html', nmsg=lmsg)

        elif not re.match(r'[0-9]{10}', mno):
            msg = "only 10 digits allowed"
            return render_template('userfilldata.html', nmsg=msg)

        elif not gender:
            lmsg = "blank  not allowed"
            return render_template('userfilldata.html', gmsg=lmsg)

        elif not address:
            lmsg = "blank  not allowed"
            return render_template('userfilldata.html', amsg=lmsg)

        elif not city:
            lmsg = "blank  not allowed"
            return render_template('userfilldata.html', cmsg=lmsg)

        elif not re.match(r'[a-zA-Z ]+',city):
            cmsg = 'only characters allowed'
            return render_template('userfilldata.html', cmsg=cmsg)

        elif not state:
            lmsg = "blank  not allowed"
            return render_template('userfilldata.html', smsg=lmsg)

        elif not re.match(r'[a-zA-Z ]+',state):
            msg = 'only characters allowed'
            return render_template('userfilldata.html', smsg=msg)

        elif not zipcode:
            lmsg = "blank  not allowed"
            return render_template('userfilldata.html', zmsg=lmsg)

        elif not re.match(r'[0-9]{6}', zipcode):
            msg = "only 6 digits allowed"
            return render_template('userfilldata.html', zmsg=msg)

        else:
            
            if file and allowed_file(file.filename) and  birth and allowed_pdf(birth.filename) and app.config['MAX_CONTENT_LENGTH'] == 3 * 1024 :
                files = secure_filename(file.filename)  
                births = secure_filename(birth.filename)
                

                filename = str(uuid.uuid1()) + "_" + files
                birthpdf = str(uuid.uuid1()) + "_" + births 
                file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
                birth.save(os.path.join(app.config['UPLOAD_FOLDER_PDF'],birthpdf))
                

                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO User_profile (user_id,first_name, last_name, date_of_birth,mobile_number,gender,address,city,state,zipcode,img,birthpdf,profile_updated_dt) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,curdate())",
                (uid,fname,lname,dob,mno,gender,address,city,state,zipcode,filename,birthpdf))
                mysql.connection.commit()
                cur.close() 
                flash("you have successfull create your profile")
                return redirect('/userdashboard')
            else:
                msg = 'only png and jpg allowed'
                pdf = 'only .pdf allowed'
                return render_template('userfilldata.html',name=msgu,email=msgemail,file=msg,pdf=pdf)
    return render_template('userfilldata.html',name=msgu,email=msgemail)

# ======================================= user profile update ================================



@app.route('/updateuserprofiledata', methods=['GET','POST'])
def updateuserprofiledata():
    uid=session['userid'] 
    msgu = session['username'] 
    msgemail = session['useremail']
    if request.method == 'POST':
        fname = request.form.get('firstname')
        lname = request.form.get('lastname')
        file = request.files.get('pic')
        birth = request.files['birthCertificate']
        dob = request.form.get('dob')
        mno = request.form.get('mno')
        gender = request.form.get('gender')
        address = request.form.get('address')
        city = request.form.get('city')
        state = request.form.get('state')
        zipcode = request.form.get('zipcode')
        


        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM User_profile WHERE user_id = %s', [uid])
        data = cur.fetchone()
        cur.close()

        if not fname:
            msg = "blank  first name not allowed"
            return render_template('userprofile.html', msg=msg, userprofile=data)

        elif not re.match(r'[a-zA-Z ]+',fname):
            msg = 'only characters allowed'
            return render_template('userprofile.html', msg=msg, userprofile=data)

        elif not lname:
            lmsg = "blank  last name not allowed"
            return render_template('userprofile.html', lmsg=lmsg, userprofile=data)

        elif not re.match(r'[a-zA-Z ]+',lname):
            lmsg = 'only characters allowed'
            return render_template('userprofile.html', lmsg=msg, userprofile=data)

        elif not dob:
            lmsg = "blank  not allowed"
            return render_template('userprofile.html', dmsg=lmsg, userprofile=data)

        elif not mno:
            lmsg = "blank  not allowed"
            return render_template('userprofile.html', nmsg=lmsg, userprofile=data)

        elif not re.match(r'[0-9]{10}', mno):
            msg = "only 10 digits allowed"
            return render_template('userprofile.html', nmsg=msg, userprofile=data)

        elif not gender:
            lmsg = "blank  not allowed"
            return render_template('userprofile.html', gmsg=lmsg, userprofile=data)

        elif not address:
            lmsg = "blank  not allowed"
            return render_template('userprofile.html', amsg=lmsg, userprofile=data)

        elif not city:
            lmsg = "blank  not allowed"
            return render_template('userprofile.html', cmsg=lmsg, userprofile=data)

        elif not re.match(r'[a-zA-Z ]+',city):
            cmsg = 'only characters allowed'
            return render_template('userprofile.html', cmsg=cmsg, userprofile=data)

        elif not state:
            lmsg = "blank  not allowed"
            return render_template('userprofile.html', smsg=lmsg, userprofile=data)

        elif not re.match(r'[a-zA-Z ]+',state):
            msg = 'only characters allowed'
            return render_template('userprofile.html', smsg=msg, userprofile=data)

        elif not zipcode:
            lmsg = "blank  not allowed"
            return render_template('userprofile.html', zmsg=lmsg, userprofile=data)

        elif not re.match(r'[0-9]{6}', zipcode):
            msg = "only 6 digits allowed"
            return render_template('userprofile.html', zmsg=msg, userprofile=data)
        
        else:
            
            if file and allowed_file(file.filename)  and  birth and allowed_pdf(birth.filename) :
                files = secure_filename(file.filename)
                births = secure_filename(birth.filename)
               
                filename = str(uuid.uuid1()) + "_" + files
                birthpdf = str(uuid.uuid1()) + "_" + births 
                file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
                birth.save(os.path.join(app.config['UPLOAD_FOLDER_PDF'],birthpdf))
        
                cur = mysql.connection.cursor()
                cur.execute("update User_profile set first_name=%s, last_name=%s, date_of_birth=%s,mobile_number=%s,gender=%s,address=%s,city=%s,state=%s,zipcode=%s,profile_updated_dt=curdate(), img=%s, birthpdf=%s where user_id=%s",(fname,lname,dob,mno,gender,address,city,state,zipcode,filename,birthpdf,uid))

                mysql.connection.commit()
                cur.execute('SELECT * FROM User_profile WHERE user_id = %s', [uid])
                data = cur.fetchone()
                cur.close() 
                success = "you have successfull update your profile"
                return render_template('userwelcomepage.html',msg = msgu,userprofile=data,msge=msgemail,success=success,filename=filename,birth=birthpdf)
                
            else:
                cur = mysql.connection.cursor()
                cur.execute('SELECT * FROM User_profile WHERE user_id = %s', [uid])
                data = cur.fetchone()
                cur.close()
                msg = 'Allowed image types are -> png, jpg'
                pdf = 'only .pdf allowed'
                return render_template('userprofile.html', msgimg=msg, userprofile=data,name=msgu,email=msgemail,pdf=pdf)
    return render_template('userprofile.html')

# ========================================= user profile show =================================
@app.route('/showuserdata')
def show():
    userid = session['userid']
    msgu = session['username'] 
    msgemail = session['useremail']
    cur = mysql.connection.cursor()
    if cur.execute('SELECT * FROM User_profile WHERE user_id = %s', [userid]) == 1:
        data = cur.fetchone()
        cur.close()
        return render_template('userprofile.html', userprofile=data,name=msgu,email=msgemail)
    else:
       
        flash("first of all you can fill your data")
        return redirect('/userdashboard')


       



        
# =========================== new admin crate ====================================================


@app.route('/adminlist', methods = ['GET','POST'])
def adminlist():
    if 'loggedin' in session:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Admin_login")
        data = cur.fetchall()
        cur.close()
        return render_template('newadmincrate.html', user=data)
    else:
        return redirect('adminlogin')

#================================ new admin add ============================================
@app.route('/crateadmin', methods=['GET','POST'])
def crateadmin():
    if 'loggedin' in session:
        cur = mysql.connection.cursor()
        if request.method == 'POST':
            aemail = request.form.get('email')
            apassword = request.form.get('password')
            cur.execute('SELECT * FROM Admin_login WHERE email = %s', [aemail]) 
            data = cur.fetchone()
            if data:
                flash('already exists')
                return redirect('crateadmin')
            else:
                cur.execute("INSERT INTO Admin_login (email, password) VALUES (%s,md5(%s))", (aemail, apassword))
                mysql.connection.commit()
                cur.close() 
                flash("Admin create successfull !")
                return redirect('adminlist')  
        return render_template('admincrate.html')
    else:
        return redirect('adminlogin')

#=========================== admin show data ======================================
@app.route('/getadminedit/<id>', methods=['POST', 'GET'])
def get_admin(id):

    cur = mysql.connection.cursor()

    cur.execute('SELECT * FROM Admin_login WHERE id = %s', [id])
    data = cur.fetchone()
    cur.close()
    return render_template('adminedit.html', user=data)


#==================================== update admin data ================================
@app.route('/adminupdate/<id>', methods=['GET', 'POST'])
def adminupdate(id):
    if request.method == 'POST':
        aemail = request.form.get('email')
        apassword = request.form.get('password')
        cur = mysql.connection.cursor()
        cur.execute("UPDATE Admin_login SET email = %s, password = md5(%s) WHERE Id = %s",(aemail, apassword, id) ) 
        mysql.connection.commit()
        flash("user update successfull !")
        return redirect(url_for('adminlist'))


#================================ delete admin =====================================
@app.route('/admindelete/<string:id>', methods=['POST', 'GET'])
def delete_admin(id):
    cur = mysql.connection.cursor()

    cur.execute('DELETE FROM Admin_login WHERE id = {0}'.format(id))   
    mysql.connection.commit()
    flash("user delete successfull !")
    return redirect(url_for('adminlist'))


#================================ admin register ==============================
@app.route('/register')
def register():
    return render_template("registeradmin.html")

@app.route('/registeradmin', methods=['GET','POST'])
def registeradmin():
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        aemail = request.form.get('email')
        apassword = request.form.get('password')
        cur.execute('SELECT * FROM Admin_login WHERE email = %s', [aemail]) 
        data = cur.fetchone()
        if data:
            flash('already exists')
            return redirect('/register')
        else:
            cur.execute("INSERT INTO Admin_login (email, password) VALUES (%s,md5(%s))", (aemail, apassword))
            mysql.connection.commit()
            cur.close() 
            flash("Register successfull !")
            return redirect('adminlogin')  
    return render_template('registeradmin.html')



#======================================== user password forget ============================
@app.route('/forgetpassword', methods=['GET','POST'])
def forgetpassword():
    return render_template('forgetpasswordlink.html')

@app.route('/senteemailforget', methods=['GET','POST'])
def senteemailforget():
    if request.method == 'POST':
        email = request.form.get('uemail')
        cur = mysql.connection.cursor()
        cur.execute('SELECT id FROM User_login WHERE email = %s', [email]) 
        
        data = cur.fetchone()
        if data:    
            uid=data.get('id')
            cur.close()
            udata = str(uid)

            sms = 'Click To Set New Password '+ 'http://127.0.0.1:5000/getdata/'+udata 
            msg = Message('Re Set Password', sender = 'pithiyahardik95@gmail.com', recipients = [email])
            msg.body = sms

            mail.send(msg)
            flash('Plase Check Your Mail')
            return redirect('/userlogin')
        else:
             flash('you are not velid user')
             return redirect('/userlogin')

@app.route('/getdata/<int:id>', methods=['GET','POST'])
def getdata(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM User_login WHERE id = %s', [id]) 
    data = cur.fetchone()
    cur.close()
    return render_template('userresetpassword.html',emaildata=data)

@app.route('/resetpassworduser/<id>', methods=['GET','POST'])
def resetpassworduser(id):
    if request.method == 'POST':
        password1 = request.form.get('password')
        password2 = request.form.get('repassword')
        
        if password1 == password2 :
            cur = mysql.connection.cursor()
            cur.execute("UPDATE User_login SET password = MD5(%s) WHERE Id = %s",(password1, id) )
            mysql.connection.commit()
            flash(" password re set successfull !")
            return redirect('/userlogin')
        else:
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM User_login WHERE id = %s", (id))
            data = cur.fetchone()
            cur.close()
            msg = "your password not match plase try agin"
            return render_template('userresetpassword.html', msg =msg, emaildata=data)

        


if __name__ == "__main__":
    app.run(debug=True)