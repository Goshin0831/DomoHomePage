from Flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

#
class UserInfo:
    def __init__(self, number, name, age, gender, job, picture_path):
        self.number = number
        self.name = name
        self.age = age
        self.gender = gender
        self.job = job
        self.picture_path = picture_path

#データベースは仮処置とする
member_list = [
    UserInfo(0, 'taro', '男', 'Webデザイン', image/taro.jpg),
    UserInfo(1, 'gen', '男', 'コンサル', image/gen.jpg),
    UserInfo(2, 'akiko', '女', 'コーダー', image/akiko.jpg),
    UserInfo(3, 'hanako', '女', '経理', image/hanako.jpg),
    UserInfo(4, 'satoshi', '男', 'SE', image/satoshi.jpg),
    UserInfo(5, 'keiko', '女', 'データサイエンティスト', image/keiko.jpg),
    UserInfo(6, 'kenichi', '男', 'SE', image/kenichi.jpg)
]

@app.route('/') #mainPage
def main():
    return render_template('main.html')

@app.route('/mamberlist') #memberlistPage
def load_member_list():
    return render_template('member_list.html', member_list = member_list)

@app.route('/member/<int:member_number>') #Introduction of membersPage
def member_ditail(member_number):
    for member in member_list:
        if member.number == member_number:
            return render_template('member_ditail.html', member = member)
    return redirect(url_for('main'))

@app.route('/terms') #利用規約
def terms render_template('terms.html')

@app.errorhandler(404) #間違ったページに飛ぶと'main’に戻される
def redirect_main_page(error):
    return redirect(url_for('main'))

if __name__ == '__main__':
    app.run(debug=True)