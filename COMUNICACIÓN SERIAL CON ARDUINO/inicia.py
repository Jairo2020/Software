from tkinter import Tk, Button, Label, Radiobutton, Listbox, ttk, Menu, Toplevel, messagebox
import serial

# clase inicializadora---------------------------------------------

class Application:
    
    def __init__(self):
        self.colorFondo ="#212321"
        self.colorWidgets="#4E544E"
        self.colorLetra="white"
        # Variable relacionadas con la comunicación serial
        self.baud_rate = ["1200", "2400", "4800", "9600", "19200", "38400", "57600", "115200"]
        # 50, 75, 110, 134, 150, 200, 300, 600, 1200, 1800, 2400, 4800,
        #                  9600, 19200, 38400, 57600, 115200, 230400, 460800, 500000,
        #                  576000, 921600, 1000000, 1152000, 1500000, 2000000, 2500000,
        #                  3000000, 3500000, 4000000
        self.com_port = ["COM0", "COM1", "COM2", "COM3", "COM4", "COM5"]

    def iniciar(self, ventana):
        self.ventana = ventana
        self.ventana.configure(bg=self.colorFondo)
        self.ventana.state("zoomed")
        self.ventana.geometry("600x300")
        self.ventana.title("PRUEBA DE COMUNICACIÓN SERIAL CON ARDUINO")

        menu_panel = Menu(self.ventana)
        ventana.config(menu = menu_panel)

        filemenu = Menu(menu_panel, tearoff=0)
        filemenu.add_command(label="Nuevo")
        filemenu.add_command(label="Abrir")
        filemenu.add_command(label="Guardar")
        filemenu.add_command(label="Cerrar")
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=ventana.quit)

        editmenu = Menu(menu_panel, tearoff=0)
        editmenu.add_command(label="Cortar")
        editmenu.add_command(label="Copiar")
        editmenu.add_command(label="Pegar")

        viewmenu = Menu(menu_panel, tearoff=0)
        viewmenu.add_command(label="Grafica")
        #viewmenu.add_cascade(label="Grafica1", menu=viewmenu)

        helpmenu = Menu(menu_panel, tearoff=0)
        helpmenu.add_command(label="Ayuda")
        helpmenu.add_separator()
        helpmenu.add_command(label="Acerca de...")

        toolmenu = Menu(menu_panel, tearoff=0)
        toolmenu.add_command(label="Configurar COM", command=self.config)

        menu_panel.add_cascade(label="Archivo", menu=filemenu)
        menu_panel.add_cascade(label="Editar", menu=editmenu)
        menu_panel.add_cascade(label="Ver", menu=viewmenu)
        menu_panel.add_cascade(label="Herramientas", menu=toolmenu)
        menu_panel.add_separator()
        menu_panel.add_cascade(label="Ayuda", menu=helpmenu)


    def config(self):
        screen_config = Toplevel()
        screen_config.geometry("600x200")
        screen_config.resizable(0,0)
        screen_config.title("Configuración de puerto")
        screen_config.configure(background=self.colorFondo)

        # Etiquetas ---------------------------------------------------------------
        selec_velo = Label(screen_config, bg=self.colorWidgets, fg=self.colorLetra, text="selecciona la velocidad")
        selec_velo.place(x=20, y=20) 

        self.mosCom = Label(screen_config, bg=self.colorLetra)
        self.mosCom.configure(text="Mostrar Com")
        self.mosCom.place(x=20, y=20) 

        # lista de las velocidades ----------------------------------------------------------
        self.baudlist = ttk.Combobox(screen_config, value=self.baud_rate)
        self.baudlist.current(3)
        self.baudlist.place(x=150, y=20)

        # Listas de puertos
        self.Com = ttk.Combobox(screen_config, value=self.com_port)
        self.Com.current()
        self.Com.place(x=300, y=20)

        # botones-----------------------------------------------------------------------------
        self.aceptar = Button(screen_config, text="Aceptar",
                            bg=self.colorWidgets, fg=self.colorLetra,
                                command=self.print_baudrate(self.Com.get(), self.baudlist.get()))
        self.aceptar.place(x=500, y=20)

        # barra de progreso

        # self.progreso=ttk.Progressbar(screen_config,
        #                             length=100, mode="determinate")
        # self.progreso.place(x=10, y=50)

        # self.progreso.steep(5)

        #mostrarmas=

        screen_config.mainloop()

    def print_baudrate(self, ncom, baud_rate):
        #Configuración del puerto serial
        # ser = serial.Serial(ncom, baud_rate, timeout=1)
        # print(ser.name)
        # print(ser.baudrate)
        #print(ncom+" :"+baud_rate)

        self.mosCom.configure(text=ncom)
        self.mosCom.pack()
        # self.bar(screen_config)
        # ser.close()
    # def bar(self, screen_config):
    #     import time
    #     self.progreso["value"]=20
    #     screen_config.update_idletask()
    #     time.sleep(1)

#    def Menu_f(ventana):
#         menu_panel = Menu(self,ventana)
#         self.ventana.config(menu = menu_panel)

# def available():
#     try:
#         for 


# def Application(ventana):
#     colorFondo = "#212321"
#     ventana.geometry("600x300")
#     ventana.title("PRUEBA DE COMUNICACIÓN SERIAL CON ARDUINO")
#     ventana.configure(background=colorFondo)