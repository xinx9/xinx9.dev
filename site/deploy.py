import sys,os
import xml.etree.ElementTree as ET

def createService(Filename=None, Description=None, After=None, StartLimitIntervalSec=0, EnvironmentFile=None,
Type=None, User=None, WorkingDirectory=None, ExecStart=None, Restarton=None, RestartSec=0, WantedBy=None):
    f = open(Filename, 'w')
    f.write(f"[Unit]\nDescription={Description}\nAfter={After}\nStartLimitIntervalSec={StartLimitIntervalSec}\n\n[Service]\nEnvironmentFile={EnvironmentFile}\nType={Type}\nUser={User}\nWorkingDirectory={WorkingDirectory}\nExecStart={ExecStart}\nRestart-on={Restarton}\nRestartSec={RestartSec}\n\n[Install]\nWantedBy={WantedBy}\n")
    f.close()

def getSiteName(pomfile):
    tree = ET.parse(pomfile)
    root = tree.getroot()
    return  (root[1].text + "." + root[2].text) , root[2].text

site = getSiteName("pom.xml")
print(site[0] + "\n" + site[1])

createService(Filename=site[1], Description="my resume website app", 
After="network.target", Type="simple", User="site", WorkingDirectory="/usr/local/bin", 
ExecStart="ExecStart=/usr/bin/java $JAVA_OPTS -jar $EXEC_JAR", Restarton="failure", RestartSec=60, WantedBy="multi-user.target")