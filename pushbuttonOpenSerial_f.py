#pushbuttonOpenSerial_f.m

Port=get(gui.editPort,'string')
Baudrate=str2num(get(findobj(gcf,'Tag','editBaudrate'),'String'))
 instr = instrfind
 if not isempty(instr):
     fclose(instrfind)

if (~exist('s')):  
    s = serial(Port,'BAUDRATE',Baudrate)

else: 
    fclose(s)
    clear s
    s = serial(Port,'BAUDRATE',Baudrate)

if (strcmp(get(s,'Status'),'closed')):
    fopen(s)

