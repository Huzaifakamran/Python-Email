import smtplib
from tabulate import tabulate
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "<SENDER_EMAIL>"
to_emails = ["TO-EMAIL"]
cc_emails = ["CC-EMAIL"]
password = "<YOUR-PASSWORD>"

HTML = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <style type="text/css">
      table {
        background: white;
        border-radius:3px;
        border-collapse: collapse;
        height: auto;
        max-width: 900px;
        padding:5px;
        animation: float 5s infinite;
      }

      tr {
        border-top: 1px solid;
        border-bottom: 1px solid;
        border-left: 1px solid;
      }

      td {
        background:#FFFFFF;
        padding:5px;
        text-align:left;
        vertical-align:middle;
        font-weight:300;
        font-size:13px;
        border-right: 1px solid;
      }
    </style>
  </head>
  <body>
    Dear Somebody,<br> <br>
    Bla-bla-bla<br><br>
    <table>
      <tbody>
        <tr>
          <td><span style="font-weight:bold">Start Date</span></td>
          <td>Feb 4, 2023</td>
        </tr>
        <tr>
          <td><span style="font-weight:bold">End Date</span></td>
          <td>Feb 5, 2023</td>
        </tr>
                <tr>
          <td><span style="font-weight:bold">Submission Date</span></td>
          <td>Feb 3, 2023</td>
        </tr>
        <tr>
          <td><span style="font-weight:bold">Reason</span></td>
          <td>string</td>
        </tr>
                <tr>
          <td><span style="font-weight:bold">Comment</span></td>
          <td>string</td>
        </tr>
        <tr>
          <td><span style="font-weight:bold">Manager Remarks</span></td>
          <td>string</td>
        </tr>
      </tbody>
    </table>
    <br>
    <br><br>
    *** This is an auto-generated email, please do not reply ***
  </body>
</html>
"""
message = MIMEMultipart("alternative", None, [MIMEText(HTML, 'html')])
message["Subject"] = "Hi there"
message["From"] = sender_email
message["To"] = ", ".join(to_emails)
message["Cc"] = ", ".join(cc_emails)

server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.login(sender_email, password)
server.sendmail(sender_email, to_emails + cc_emails, message.as_string())
server.quit()