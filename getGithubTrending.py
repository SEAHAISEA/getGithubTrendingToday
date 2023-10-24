import requests
from pyquery import PyQuery as pq
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from googletrans import Translator


def sendEmail(article, dateVal):
    # 邮件配置
    smtp_server = 'smtp.qq.com'  # 邮箱服务端
    smtp_port = 465  # 邮箱端口
    sender_email = 'xxxx'  # 发送邮箱
    sender_password = 'xxxx'  # 发送邮箱的授权码
    receiver_email = 'xxxx'  # 接收邮箱
    # 创建MIMEMultipart对象
    msg = MIMEMultipart()

    # 设置邮件内容
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = dateVal + 'githubTrending'

    # 创建HTML内容
    html_content = '''
    <html>
    <body>
    {article}
    </body>
    </html>
    '''.format(article=article)

    # 创建MIMEText对象
    html_part = MIMEText(html_content, 'html')

    # 将MIMEText对象添加到MIMEMultipart对象中
    msg.attach(html_part)

    # 创建SMTP对象
    smtpObj = smtplib.SMTP_SSL(smtp_server, smtp_port)

    # 登录SMTP服务器
    smtpObj.login(sender_email, sender_password)

    # 发送邮件
    smtpObj.sendmail(sender_email, receiver_email, msg.as_string())

    # 关闭SMTP连接
    smtpObj.quit()


def getTrending():
    HEADERS = {
        'User-Agent'        : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
        'Accept'            : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding'   : 'gzip,deflate,sdch',
        'Accept-Language'   : 'zh-CN,zh;q=0.8',
        'Connection': 'close'
    }

    # 获取当前日期和时间
    # 格式化日期为字符串，包含"年"、"月"和"日"
    dateVal = datetime.datetime.now().strftime('%Y年%m月%d日')

    date_title = '''
    <div>
    <h1 style="text-align: center;color: #167df5;margin-top: 30px">githubTrending</h1>
    <h3 style="text-align: center;color: #167df5;">{dateVal}</h3>
    </div>
    '''.format(dateVal=dateVal)

    # 字符串拼接
    get_article = date_title

    # 获取trending页面信息
    url = 'https://github.com/trending'
    res_html = requests.get(url, headers=HEADERS)
    assert res_html.status_code == 200

    doc = pq(res_html.content)
    items = doc('div.Box article.Box-row')

    # 信息提取，循环拼接
    for item in items:
        i = pq(item)
        # 标题
        project_title = i(".lh-condensed a").text().replace(" ", "")
        # 说明
        project_description = i("p.col-9").text()

        # 说明翻译
        try:
            translator = Translator()
            project_description_translate = translator.translate(
                str(project_description), dest='zh-CN')
            project_description_translate = project_description_translate.text
        except Exception as e:
            project_description_translate = '翻译失败！'
        finally:
            # Stargazers-1
            stargazers_doc = i(
                'a[href="/{title}/stargazers"]'.format(title=project_title))
            # Stargazers-2
            stargazers = '   ' + stargazers_doc.text() + '  Stargazers'
            # project_starsToday
            starsToday = '   ' + i(".float-sm-right").text()
            # project_url-1
            project_url = i(".lh-condensed a").attr("href")
            # project_url-2
            project_url = "https://github.com" + project_url
            # language_name_coler
            language_name_coler = i(".repo-language-color").attr('style')

            if language_name_coler == None:
                show_name_coler = '#ffffff'
                show_name = ''
            else:
                show_name_coler = language_name_coler.replace(
                    "background-color: ", "")
                language_name = i(".repo-language-color").next().text().split()
                show_name = ''.join(str(x) for x in language_name)

            # Create a PyQuery object
            doc = pq('<div></div>')
            # Create the <article> element
            article = doc('<article>').attr(
                'style', 'border: 1px solid #aaa;width: 100%;display: flex;justify-content: center;')
            # Create the <div> element inside <article>
            div = doc('<div>').attr('style', 'width: 90%;')
            # Create the <h2> element inside <div>
            project_title_span = '<span style="font-weight: normal;">{title}</span>'.format(
                title=project_title)
            h2 = doc('<h2>').attr('style', 'color: #167df5')
            h2.append(project_title_span)
            # Create the <p> element inside <div>
            # print(type(project_description_translate))
            # print(project_description_translate)
            p1 = doc('<p>').attr('style', 'color: #262626').text(
                project_description_translate)
            p = doc('<p>').attr('style', 'color: #262626').text(
                project_description)
            # Create the first <h3> element inside <div>
            div1_attribute_value = 'color: {language_bgc};'.format(
                language_bgc=show_name_coler)
            div1 = doc('<h3>')
            div1.attr('style', div1_attribute_value)
            div1.text(show_name)
            div2 = doc('<div>').attr('style', 'margin-top: 1px;')
            div2_val = '<span>{Stargazers}</span>'.format(
                Stargazers=stargazers)
            div2.append(div2_val)
            # Create the third <div> element inside <div>
            div3 = doc('<div>').attr('style', 'margin-top: 1px;')
            div3_val = '<span>{starsToday}</span>'.format(
                starsToday=starsToday)
            div3.append(div3_val)
            # Create the final <h3> element inside <div>
            p2 = doc('<h3>').text(project_url)
            # Append all elements to construct the final HTML structure
            div.append(h2)
            div.append(p1)
            div.append(p)
            div.append(div1)
            div.append(div2)
            div.append(div3)
            div.append(p2)
            article.append(div)
            get_article += str(article)

    sendEmail(get_article, dateVal)


if __name__ == '__main__':
    getTrending()
