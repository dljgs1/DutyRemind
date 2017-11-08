### 配置文件说明
- emails.conf 邮箱配置。存储将要按日程次序发送的邮箱,按次序编号0,1,2..
- list.conf 任务列表配置。存储每一个定时发送任务的信息。配置格式为：时间类型标识符、发送邮箱序列、发送内容文件名。
- timetype.conf 时间类型配置。存储定时发送的精确时间。配置格式为：标识符、时、分、星期。星期以位形式存储，一共七位，0代表不发，1代表发。如：day类型是1~5为1，0和6为0，即周一到周五发，周日周六不发。
- usr_info.txt 用来发邮件的账户信息，第一行填入用户名，第二行密码
### py文件说明
- main.py 含配置信息加载和主循环
- duty.py 含任务类Cduty
- emsender.py 含邮件发送类Cemail_sender

### 存在的问题
- STMP服务器目前用的是163，因此只能使用163邮箱发送


