import customtkinter
import random

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
root = customtkinter.CTk()
root.geometry("400x500")
root.title("Dice App")

def roll():
    diceSide = combo_1.get()
    diceNumber = int(entry_1.get())
    modifiers = int(entry_2.get())
    output_0 = 0
    rannumber = 0

    if diceSide == "D4":
        out_1.delete("0.0",customtkinter.END)
        for i in range(diceNumber):
            rannumber = random.randint(1,4)
            rannumber_text = f'''Dice Number {i+1} : {rannumber}
'''
            out_1.insert("0.0" , rannumber_text)
            output_0 += rannumber
        output = output_0 + modifiers
        output_text = f'''Total Value : {output}
'''
        out_1.insert("0.0",output_text)

    if diceSide == "D6":
        out_1.delete("0.0",customtkinter.END)
        for i in range(diceNumber):
            rannumber = random.randint(1,6)
            rannumber_text = f'''Dice Number {i+1} : {rannumber}
'''
            out_1.insert("0.0" , rannumber_text)
            output_0 += rannumber
        output = output_0 + modifiers
        output_text = f'''Total Value : {output}
'''
        out_1.insert("0.0",output_text)

    if diceSide == "D8":
        out_1.delete("0.0",customtkinter.END)
        for i in range(diceNumber):
            rannumber = random.randint(1,8)
            rannumber_text = f'''Dice Number {i+1} : {rannumber}
'''
            out_1.insert("0.0" , rannumber_text)
            output_0 += rannumber
        output = output_0 + modifiers
        output_text = f'''Total Value : {output}
'''
        out_1.insert("0.0",output_text)

    if diceSide == "D10":
        out_1.delete("0.0",customtkinter.END)
        for i in range(diceNumber):
            rannumber = random.randint(1,10)
            rannumber_text = f'''Dice Number {i+1} : {rannumber}
'''
            out_1.insert("0.0" , rannumber_text)
            output_0 += rannumber
        output = output_0 + modifiers
        output_text = f'''Total Value : {output}
'''
        out_1.insert("0.0",output_text)

    if diceSide == "D12":
        out_1.delete("0.0",customtkinter.END)
        for i in range(diceNumber):
            rannumber = random.randint(1,12)
            rannumber_text = f'''Dice Number {i+1} : {rannumber}
'''
            out_1.insert("0.0" , rannumber_text)
            output_0 += rannumber
        output = output_0 + modifiers
        output_text = f'''Total Value : {output}
'''
        out_1.insert("0.0",output_text)

    if diceSide == "D20":
        out_1.delete("0.0",customtkinter.END)
        for i in range(diceNumber):
            rannumber = random.randint(1,20)
            rannumber_text = f'''Dice Number {i+1} : {rannumber}
'''
            out_1.insert("0.0" , rannumber_text)
            output_0 += rannumber
        output = output_0 + modifiers
        output_text = f'''Total Value : {output}
'''
        out_1.insert("0.0",output_text)

    if diceSide == "D100":
        out_1.delete("0.0",customtkinter.END)
        for i in range(diceNumber):
            rannumber = random.randint(1,100)
            rannumber_text = f'''Dice Number {i+1} : {rannumber}
'''
            out_1.insert("0.0" , rannumber_text)
            output_0 += rannumber
        output = output_0 + modifiers
        output_text = f'''Total Value : {output}
'''
        out_1.insert("0.0",output_text)

    

frame_1 = customtkinter.CTkFrame(master = root)
frame_1.pack( fill="both", pady= 12,padx= 10 ,expand=True)
label = customtkinter.CTkLabel(master=frame_1,text="Choose Your Fate",font=customtkinter.CTkFont(size=38,slant="roman"))
label.pack(pady=12 , padx=10 , fill="both" , expand=True,)
global combo_1
combo_1 = customtkinter.CTkComboBox(frame_1, values=["D4", "D6", "D8", "D10", "D12", "D20", "D100"])
combo_1.pack(pady = 12, padx=10  ,fill="x", expand=True)
global entry_1
entry_1 = customtkinter.CTkEntry(frame_1 , placeholder_text = "How many Dice are you rolling")
entry_1.pack(pady = 12 , padx = 10 , fill = "both" , expand = True)
global entry_2
entry_2 = customtkinter.CTkEntry(frame_1 , placeholder_text = "Modifiers (no modifier mean enter 0)")
entry_2.pack(pady = 12 , padx = 10 , fill = "both" , expand = True)
button = customtkinter.CTkButton(master=frame_1,text="Roll The Dice !!!!" , command = roll)
button.pack(pady=12 , padx=10 , fill="both" , expand=True)
global out_1
out_1 = customtkinter.CTkTextbox(frame_1, font = customtkinter.CTkFont(size=25, slant="roman"))
out_1.pack(pady = 12 , padx = 10 , fill = "both" , expand = False)

root.mainloop()
