from flask import Flask, make_response, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_cju():
    '''초기 접속 시 실행할 함수'''
    # return render_template(
    #     'index.html'
    # )

    # 쿠키 굽기(발행)
    response = make_response(
        render_template('index.html') # 템플릿 내용은 그대로 유지
    )

    if request.cookies:
        # 사용자의 쿠키 정보 읽어오기
        print('쿠키 정보가 있습니다. 방문한 적이 있습니다.')
        name = request.cookies.get('name')
        universtiy = request.cookies.get('universtiy')
        passwd = request.cookies.get('passwd')

        # 쿠키 정보 확인 -> 터미널에 출력
        print(f'name: {name}')
        print(f'university: {universtiy}')
        print(f'passwd: {passwd}')
    else:
        print('첫 방문자입니다. 쿠키를 굽습니다.')
        response.set_cookie('name', 'Hong Gil-dong') # 쿠키 굽기
        response.set_cookie('universtiy', 'Chongju University') # 또 다른 쿠키 굽기
        response.set_cookie('passwd', '1234', max_age=60*60*24*7) # 쿠키 유효 기간을 7일로 설정

    return response

if __name__=='__main__':
    # app.run()
    app.run(host='0.0.0.0', port='80', debug=True)