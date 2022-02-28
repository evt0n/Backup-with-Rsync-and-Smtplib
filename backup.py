import os
from configmail import *

logfile = '/var/log/backup/backup-'+dt+'.log'

try:
    rsync = ('rsync -rvazp --log-file='+logfile+' \
             /origem \
             /destino/bkpdestino'+dt+'/')
    #os.system(rsync)
    
    if os.system(rsync)==5888:
        raise Exception(os.popen('tail -n5 ' +logfile).read())

    else:
        try:
            with open(logfile) as f:
                mime = MIMEText(f.read(), _subtype="plain")
            mime.add_header('Content-Disposition', 'attachment', filename='backup-'+dt+'.log')
            msg.attach(mime)
 
            msg.attach(MIMEText('<strong style="color: #4cc76a">Backup - DIA '+dt+' realizado com sucesso!</strong>', 'html'))
            server.sendmail(msg['From'], msg['To'], msg.as_string())
    
        except FileNotFoundError as e:
            msg.attach(MIMEText('<strong style="color:red">Backup - DIA '+dt+'</strong><pre>'+str(e)+'</pre>', 'html'))
            server.sendmail(msg['From'], msg['To'], msg.as_string())

except Exception as e:
    msg.attach(MIMEText('<strong style="color:red">Backup - DIA '+dt+'</strong><pre>'+str(e)+'</pre>', 'html'))

    with open(logfile) as f:
        mime = MIMEText(f.read(), _subtype="plain")
    mime.add_header('Content-Disposition', 'attachment', filename='backup-'+dt+'-ERRO.log')
    msg.attach(mime)

    server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()
