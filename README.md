  ## ✅ **_Windows Server Monitoring System_**
***
CheckTool is an executable program to show monitoring results collected by _[DailyCheck](https://github.com/za5321/DailyCheck)_ and inserted into Database by _[ReadDailyCheck](https://github.com/za5321/ReadDailyCheck)_.<br/>
You don't have to install python in your PC to check monitoring results. CheckTool is served in exe extension so in order to build the exe file, please refer to _'How to execute CheckTool'_ at the below.<br/><br/>

📝 CheckTool is able to:<br/>
* Show check results of certain date (UI Framework: __PyQt5__)
* Connect Database:
    * Server list management (C/D)
    * System code list management (C/R/U/D)
    * System Identification code list management (C/R/U/D)
    
🔧 For the project CheckTool, you should install (I also offer _requirements.txt_):<br/>
* PyQt5: UI Framework<br/>
`pip install pyqt5`
* Pymssql: To connect Database - SQL Server (MS-SQL). My MS-SQL version is 2019.<br/>
`pip install pymssql`

🔧 How to execute CheckTool:<br/>
>   1. Install Pyinstaller - It helps build python project into exe file easily.<br/>
    `pip install pyinstaller`
>   2. Type the command line below. <br/>
    `pyinstaller --onefile --noconsole --name CheckTool --icon=icons\icon.ico --add-data=icons\*;icons --add-data=ui\*;ui --add-data=conf\*;conf`<br/>
    These options are:<br/>
    --onefile: Should you need a neat single exe file, this option is going to help you.<br/>
    --noconsole: The option prevent Windows command prompt showing up when you run CheckTool.
    --icon: You can include icon image for the program.
    --add-data: The option must be added in order to apply configuration to your executable program.<br/>
    --name: You can set the name of exe file.<br/>
>   3. After building, you can find **_'CheckTool.exe'_** at **_'dist'_** folder.
>   4. Upload **_'CheckTool.exe'_** to any PC with Windows OS.
