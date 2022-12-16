import smtplib
import getpass


def send_email(from_addr, to_addr, subject, text, passwd, encode='utf-8'):

    # SMTP server
    server = "smtp.yandex.ru"
    port = 587

    # Формирование письма
    charser = f'Content-Type: text/plain; charset={encode}'
    mime = 'MIME-Version: 1.0'
    body = "\r\n".join(
        (f'From: {from_addr}', f'To: {to_addr}', f'Subject: {subject}', mime, charser, "", text)
    )
    print(body)

    try:
        # Connecting
        smtp = smtplib.SMTP(server, port)
        smtp.starttls()
        smtp.ehlo()
        # Login
        smtp.login(from_addr, passwd)
        # Send message
        smtp.sendmail(from_addr, to_addr, body.encode(encode))
    except Exception as err:
        print('Something went wrong')
        raise err
    finally:
        smtp.quit()



if __name__ == '__main__':
    from_addr = '1'
    to_addr = '1'
    subject = 'Тестовое письмо на паре'
    text = input('Введите текст письма: ')
    passwd = getpass.getpass(f'Пароль для {from_addr}: ')

    send_email(from_addr, to_addr, subject, text, passwd)