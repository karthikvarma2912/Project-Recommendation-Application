from flask import Flask,render_template,redirect,request
import mysql.connector

app = Flask(__name__)

conn=mysql.connector.connect(host="localhost",user="root",password="2912",database="projectslist")
cursor=conn.cursor()
#--------------------------------------------------------------------------------------------------------------------
@app.route("/")
def index():
    return redirect("/frontpage")
@app.route("/frontpage")
def test():
    return render_template("frontpage.html")
#--------------------------------------------------------------------------------------------------------------------
@app.route("/ai1")
def ai1():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='AI' AND P.PLEVEL=1")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Artificial Intelligence Beginner Level')
@app.route("/ai2")
def ai2():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='AI' AND P.PLEVEL=2")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Artificial Intelligence Intermediate Level')
@app.route("/ai3")
def ai3():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='AI' AND P.PLEVEL=3")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Artificial Intelligence Advanced Level')
@app.route("/ai4")
def ai4():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='AI'")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Artificial intelligence')


@app.route("/ml1")
def ml1():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='ML' AND P.PLEVEL=1")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Machine Learning Beginner Level')
@app.route("/ml2")
def ml2():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='ML' AND P.PLEVEL=2")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Machine Learning Intermediate Level')
@app.route("/ml3")
def ml3():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='ML' AND P.PLEVEL=3")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Machine Learning Advanced Level')
@app.route("/ml4")
def ml4():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='ML'")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Machine Learning')

@app.route("/iot1")
def iot1():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='iot' AND P.PLEVEL=1")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Internet of Things Beginner Level')
@app.route("/iot2")
def iot2():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='iot' AND P.PLEVEL=2")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Internet of Things Intermediate Level')
@app.route("/iot3")
def iot3():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='iot' AND P.PLEVEL=3")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Internet of Things Advanced Level')
@app.route("/iot4")
def iot4():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='iot'")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Internet of Things')

@app.route("/bc1")
def bc1():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='bc' AND P.PLEVEL=1")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Blockchain Beginner Level')
@app.route("/bc2")
def bc2():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='bc' AND P.PLEVEL=2")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Blockchain Intermediate Level')
@app.route("/bc3")
def bc3():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='bc' AND P.PLEVEL=3")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Blockchain Advanced Level')
@app.route("/bc4")
def bc4():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='bc'")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Blockchain')

@app.route("/cc1")
def cc1():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='cc' AND P.PLEVEL=1")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Cloud Computing Beginner Level')
@app.route("/cc2")
def cc2():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='cc' AND P.PLEVEL=2")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Cloud Computing Intermediate Level')
@app.route("/cc3")
def cc3():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='cc' AND P.PLEVEL=3")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Cloud Computing Advanced Level')
@app.route("/cc4")
def cc4():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='cc'")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Cloud Computing')

@app.route("/cs1")
def cs1():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='cs' AND P.PLEVEL=1")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Cyber Security Beginner Level')
@app.route("/cs2")
def cs2():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='cs' AND P.PLEVEL=2")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Cyber Security Intermediate Level')
@app.route("/cs3")
def cs3():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='cs' AND P.PLEVEL=3")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Cyber Security Advanced Level')
@app.route("/cs4")
def cs4():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='cs'")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Cyber Security')

@app.route("/da1")
def da1():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='da' AND P.PLEVEL=1")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Data Analytics Beginner Level')
@app.route("/da2")
def da2():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='da' AND P.PLEVEL=2")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Data Analytics Intermediate Level')
@app.route("/da3")
def da3():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='da' AND P.PLEVEL=3")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Data Analytics Advanced Level')
@app.route("/da4")
def da4():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='da'")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Data Analytics')

@app.route("/dl1")
def dl1():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='dl' AND P.PLEVEL=1")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Deep Learning Beginner Level')
@app.route("/dl2")
def dl2():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='dl' AND P.PLEVEL=2")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Deep Learning Intermediate Level')
@app.route("/dl3")
def dl3():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='dl' AND P.PLEVEL=3")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Deep Learning Advanced Level')
@app.route("/dl4")
def dl4():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='dl'")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Deep Learning')

@app.route("/dm1")
def dm1():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='dm' AND P.PLEVEL=1")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Data Mining Beginner Level')
@app.route("/dm2")
def dm2():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='dm' AND P.PLEVEL=2")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Data Mining Intermediate Level')
@app.route("/dm3")
def dm3():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='dm' AND P.PLEVEL=3")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Data Mining Advanced Level')
@app.route("/dm4")
def dm4():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='dm'")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Data Mining')

@app.route("/ds1")
def ds1():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='ds' AND P.PLEVEL=1")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Data Science Beginner Level')
@app.route("/ds2")
def ds2():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='ds' AND P.PLEVEL=2")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Data Science Intermediate Level')
@app.route("/ds3")
def ds3():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='ds' AND P.PLEVEL=3")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Data Science Advanced Level')
@app.route("/ds4")
def ds4():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='ds'")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Data Science')

@app.route("/ip1")
def ip1():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='ip' AND P.PLEVEL=1")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Image Processing Beginner Level')
@app.route("/ip2")
def ip2():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='ip' AND P.PLEVEL=2")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Image Processing Intermediate Level')
@app.route("/ip3")
def ip3():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='ip' AND P.PLEVEL=3")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Image Processing Advanced Level')
@app.route("/ip4")
def ip4():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='ip'")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Image Processing')

@app.route("/mob1")
def mob1():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='mob' AND P.PLEVEL=1")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Mobile Application Beginner Level')
@app.route("/mob2")
def mob2():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='mob' AND P.PLEVEL=2")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Mobile Application Intermediate Level')
@app.route("/mob3")
def mob3():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='mob' AND P.PLEVEL=3")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Mobile Application Advanced Level')
@app.route("/mob4")
def mob4():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='mob'")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Mobile Application')

@app.route("/nlp1")
def nlp1():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='nlp' AND P.PLEVEL=1")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Natural Language Processing Beginner Level')
@app.route("/nlp2")
def nlp2():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='nlp' AND P.PLEVEL=2")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Natural Language Processing Intermediate Level')
@app.route("/nlp3")
def nlp3():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='nlp' AND P.PLEVEL=3")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Natural Language Processing Advanced Level')
@app.route("/nlp4")
def nlp4():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='nlp'")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Natural Language Processing')

@app.route("/net1")
def net1():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='net' AND P.PLEVEL=1")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Networks Beginner Level')
@app.route("/net2")
def net2():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='net' AND P.PLEVEL=2")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Networks Intermediate Level')
@app.route("/net3")
def net3():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='net' AND P.PLEVEL=3")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Networks Advanced Level')
@app.route("/net4")
def net4():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='net'")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Networks')

@app.route("/se1")
def se1():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='se' AND P.PLEVEL=1")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Software Engineering Beginner Level')
@app.route("/se2")
def se2():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='se' AND P.PLEVEL=2")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Software Engineering Intermediate Level')
@app.route("/se3")
def se3():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='se' AND P.PLEVEL=3")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Software Engineering Advanced Level')
@app.route("/se4")
def se4():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='se'")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Software Engineering')

@app.route("/web1")
def web1():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='web' AND P.PLEVEL=1")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Web Application Beginner Level')
@app.route("/web2")
def web2():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='web' AND P.PLEVEL=2")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Web Application Intermediate Level')
@app.route("/web3")
def web3():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='web' AND P.PLEVEL=3")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Web Application Advanced Level')
@app.route("/web4")
def web4():
    cursor.execute("SELECT D.DNAME, P.PNAME, P.PD, P.PTOOLS, L.LNAME FROM PLIST P, DOMAINNAMES D, LEVELNAMES L WHERE P.PDOMAIN=D.PDOMAIN AND L.PLEVEL=P.PLEVEL AND P.PDOMAIN='web'")
    users=cursor.fetchall()
    conn.commit()
    return render_template("nextpage.html",users=users,msg='Web Application')

@app.route("/submit",methods=["POST","GET"])
def submit():
    if request.method== "POST":
        email=request.form.get("email")
        comments=request.form.get("comments")
        rating=request.form.get("rating")
        # print(email, comments, feedback)
        cursor.execute("insert into feedback(email,rating,comments) values('{}','{}','{}')". format(email,rating,comments))
        conn.commit()
        return redirect('/')


if __name__ == "__main__" :
    app.run(debug=True)
