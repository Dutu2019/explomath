import tkinter as tk
import pygame as pygame

pygame.mixer.init()
pygame.mixer.set_num_channels(64)


def play_sound(sound):
    sound_effect = pygame.mixer.Sound(sound)
    channel = pygame.mixer.find_channel()
    if channel:
        channel.play(sound_effect)

def stop_sound(channel):
    if channel:
        channel.stop()

root = tk.Tk()

root.title("Python Piano")
root.geometry("930x240")
root.resizable(False, False)
root.configure(background="white")

global current_channel
current_channel = pygame.mixer.find_channel()


def on_button_press(sound):
    current_channel = play_sound(sound)

def on_button_release():
    stop_sound(current_channel)

#This variable makes sure a key cannot be pressed more than once, preventing spamming notes while holding a key
key_states = {key: False for key in ["C", "Cs", "D", "Ds", "E", "F", "Fs", "G", "Gs", "A", "As", "B", "C2", "Cs2", "D2", "Ds2", "E2", "F2", "Fs2", "G2", "Gs2", "A2", "As2", "B2", "C3"]}

#Picks which song gets played
song_number = 1

#Octave of notes that gets used by keyboard inputs
octave = 1

def press_button(button, key, sound=None):
    if not key_states[key]:
        button.config(relief="sunken")
        # on_button_press(sound)
        key_states[key] = True 

def release_button(button, key):
    button.config(relief="raised")
    # on_button_release()
    key_states[key] = False

def bind_keyboard():
    root.bind("<KeyPress-F1>", lambda event: octave_down())
    root.bind("<KeyPress-F2>", lambda event: octave_up())
    match octave:
        case 1:
            root.bind("<KeyPress-a>", lambda event: press_button(C, "Samples/pianoC.wav", "C"))
            root.bind("<KeyRelease-a>", lambda event: release_button(C, "C"))

            root.bind("<KeyPress-w>", lambda event: press_button(Cs, "Samples/pianoC#.wav", "Cs"))
            root.bind("<KeyRelease-w>", lambda event: release_button(Cs, "Cs"))

            root.bind("<KeyPress-s>", lambda event: press_button(D, "Samples/pianoD.wav", "D"))
            root.bind("<KeyRelease-s>", lambda event: release_button(D, "D"))

            root.bind("<KeyPress-e>", lambda event: press_button(Ds, "Samples/pianoD#.wav", "Ds"))
            root.bind("<KeyRelease-e>", lambda event: release_button(Ds, "Ds"))

            root.bind("<KeyPress-d>", lambda event: press_button(E, "Samples/pianoE.wav", "E"))
            root.bind("<KeyRelease-d>", lambda event: release_button(E, "E"))

            root.bind("<KeyPress-f>", lambda event: press_button(F, "Samples/pianoF.wav", "F"))
            root.bind("<KeyRelease-f>", lambda event: release_button(F, "F"))

            root.bind("<KeyPress-t>", lambda event: press_button(Fs, "Samples/pianoF#.wav", "Fs"))
            root.bind("<KeyRelease-t>", lambda event: release_button(Fs, "Fs"))

            root.bind("<KeyPress-g>", lambda event: press_button(G, "Samples/pianoG.wav", "G"))
            root.bind("<KeyRelease-g>", lambda event: release_button(G, "G"))

            root.bind("<KeyPress-z>", lambda event: press_button(Gs, "Samples/pianoG#.wav", "Gs"))
            root.bind("<KeyRelease-z>", lambda event: release_button(Gs, "Gs"))

            root.bind("<KeyPress-y>", lambda event: press_button(Gs, "Samples/pianoG#.wav", "Gs"))
            root.bind("<KeyRelease-y>", lambda event: release_button(Gs, "Gs"))

            root.bind("<KeyPress-h>", lambda event: press_button(A, "Samples/pianoA.wav", "A"))
            root.bind("<KeyRelease-h>", lambda event: release_button(A, "A"))

            root.bind("<KeyPress-u>", lambda event: press_button(As, "Samples/pianoA#.wav", "As"))
            root.bind("<KeyRelease-u>", lambda event: release_button(As, "As"))

            root.bind("<KeyPress-j>", lambda event: press_button(B, "Samples/pianoB.wav", "B"))
            root.bind("<KeyRelease-j>", lambda event: release_button(B, "B"))

            root.bind("<KeyPress-k>", lambda event: press_button(C2, "Samples/pianoC2.wav", "C2"))
            root.bind("<KeyRelease-k>", lambda event: release_button(C2, "C2"))
        case 2:
            root.bind("<KeyPress-a>", lambda event: press_button(C2, "Samples/pianoC2.wav", "C2"))
            root.bind("<KeyRelease-a>", lambda event: release_button(C2, "C2"))

            root.bind("<KeyPress-w>", lambda event: press_button(Cs2, "Samples/pianoC#2.wav", "Cs2"))
            root.bind("<KeyRelease-w>", lambda event: release_button(Cs2, "Cs2"))

            root.bind("<KeyPress-s>", lambda event: press_button(D2, "Samples/pianoD2.wav", "D2"))
            root.bind("<KeyRelease-s>", lambda event: release_button(D2, "D2"))

            root.bind("<KeyPress-e>", lambda event: press_button(Ds2, "Samples/pianoD#2.wav", "Ds2"))
            root.bind("<KeyRelease-e>", lambda event: release_button(Ds2, "Ds2"))

            root.bind("<KeyPress-d>", lambda event: press_button(E2, "Samples/pianoE2.wav", "E2"))
            root.bind("<KeyRelease-d>", lambda event: release_button(E2, "E2"))

            root.bind("<KeyPress-f>", lambda event: press_button(F2, "Samples/pianoF2.wav", "F2"))
            root.bind("<KeyRelease-f>", lambda event: release_button(F2, "F2"))

            root.bind("<KeyPress-t>", lambda event: press_button(Fs2, "Samples/pianoF#2.wav", "Fs2"))
            root.bind("<KeyRelease-t>", lambda event: release_button(Fs2, "Fs2"))

            root.bind("<KeyPress-g>", lambda event: press_button(G2, "Samples/pianoG2.wav", "G2"))
            root.bind("<KeyRelease-g>", lambda event: release_button(G2, "G2"))

            root.bind("<KeyPress-z>", lambda event: press_button(Gs2, "Samples/pianoG#2.wav", "Gs2"))
            root.bind("<KeyRelease-z>", lambda event: release_button(Gs2, "Gs2"))

            root.bind("<KeyPress-y>", lambda event: press_button(Gs2, "Samples/pianoG#2.wav", "Gs2"))
            root.bind("<KeyRelease-y>", lambda event: release_button(Gs2, "Gs2"))

            root.bind("<KeyPress-h>", lambda event: press_button(A2, "Samples/pianoA2.wav", "A2"))
            root.bind("<KeyRelease-h>", lambda event: release_button(A2, "A2"))

            root.bind("<KeyPress-u>", lambda event: press_button(As2, "Samples/pianoA#2.wav", "As2"))
            root.bind("<KeyRelease-u>", lambda event: release_button(As2, "As2"))

            root.bind("<KeyPress-j>", lambda event: press_button(B2, "Samples/pianoB2.wav", "B2"))
            root.bind("<KeyRelease-j>", lambda event: release_button(B2, "B2"))

            root.bind("<KeyPress-k>", lambda event: press_button(C3, "Samples/pianoC3.wav", "C3"))
            root.bind("<KeyRelease-k>", lambda event: release_button(C3, "C3"))

# bind_keyboard()


def octave_up():
    global octave
    octave = 2
    NOTE_OCTAVE.config(text="oct: "+str(octave))
    bind_keyboard()

def octave_down():
    global octave
    octave = 1
    NOTE_OCTAVE.config(text="oct: "+str(octave))
    bind_keyboard()

def change_song():
    global song_number
    song_number += 1
    if song_number > 3:
        song_number = 1
    MUSIC_PICKED.config(text="Picked Song: " + str(song_number))

def music_finished():
    pygame.mixer.music.stop
    MUSIC_PLAY.config(state="normal")
    MUSIC_SELECT.config(state="normal")

def play_music():
    MUSIC_PLAY.config(state="disabled")
    MUSIC_SELECT.config(state="disabled")
    match song_number:
        #Music may not be 100% correct, made by ear
        case 1:
            #UNDERTALE - Megalovania
            root.after(0, lambda: press_button(D, "Samples/pianoD.wav", "D"))
            root.after(145, lambda: release_button(D, "D"))
            root.after(150, lambda: press_button(D, "Samples/pianoD.wav", "D"))
            root.after(300, lambda: press_button(D2, "Samples/pianoD2.wav", "D2"))
            root.after(300, lambda: release_button(D, "D"))
            root.after(550, lambda: press_button(A, "Samples/pianoA.wav", "A"))
            root.after(550, lambda: release_button(D2, "D2"))
            root.after(1000, lambda: press_button(Gs, "Samples/pianoG#.wav", "Gs"))
            root.after(1000, lambda: release_button(A, "A"))
            root.after(1250, lambda: press_button(G, "Samples/pianoG.wav", "G"))
            root.after(1250, lambda: release_button(Gs, "Gs"))
            root.after(1550, lambda: press_button(F, "Samples/pianoF.wav", "F"))
            root.after(1550, lambda: release_button(G, "G"))
            root.after(1800, lambda: press_button(D, "Samples/pianoD.wav", "D"))
            root.after(1800, lambda: release_button(F, "F"))
            root.after(1950, lambda: press_button(F, "Samples/pianoF.wav", "F"))
            root.after(1950, lambda: release_button(D, "D"))
            root.after(2100, lambda: press_button(G, "Samples/pianoG.wav", "G"))
            root.after(2100, lambda: release_button(F, "F"))
            root.after(2200, lambda: release_button(G, "G"))
            root.after(2800, music_finished)
        case 2:
            #Minecraft - Calm 1
            root.after(0, lambda: press_button(Cs, "Samples/pianoC#.wav", "Cs"))
            root.after(0, lambda: press_button(Fs, "Samples/pianoF#.wav", "Fs"))
            root.after(0, lambda: press_button(As, "Samples/pianoA#.wav", "As"))
            root.after(650, lambda: press_button(Gs, "Samples/pianoG#.wav", "Gs"))
            root.after(650, lambda: release_button(Cs, "Cs"))
            root.after(650, lambda: release_button(Fs, "Fs"))
            root.after(650, lambda: release_button(As, "As"))
            root.after(1000, lambda: press_button(Ds, "Samples/pianoD#.wav", "Ds"))
            root.after(1000, lambda: release_button(Gs, "Gs"))
            root.after(1600, lambda: press_button(Fs, "Samples/pianoF#.wav", "Fs"))
            root.after(1600, lambda: release_button(Ds, "Ds"))
            root.after(1800, lambda: release_button(Fs, "Fs"))
            root.after(2600, lambda: press_button(Cs, "Samples/pianoC#.wav", "Cs"))
            root.after(2600, lambda: press_button(Fs, "Samples/pianoF#.wav", "Fs"))
            root.after(2600, lambda: press_button(As, "Samples/pianoA#.wav", "As"))
            root.after(3250, lambda: press_button(Gs, "Samples/pianoG#.wav", "Gs"))
            root.after(3250, lambda: release_button(Cs, "Cs"))
            root.after(3250, lambda: release_button(Fs, "Fs"))
            root.after(3250, lambda: release_button(As, "As"))
            root.after(3600, lambda: press_button(Ds, "Samples/pianoD#.wav", "Ds"))
            root.after(3600, lambda: release_button(Gs, "Gs"))
            root.after(4200, lambda: press_button(Cs, "Samples/pianoC#.wav", "Cs"))
            root.after(4200, lambda: release_button(Ds, "Ds"))
            root.after(4400, lambda: release_button(Cs, "Cs"))
            root.after(4500, music_finished)
        case 3:
            #OMORI - Title 
            root.after(0, lambda: press_button(E2, "Samples/pianoE2.wav", "E2"))
            root.after(900, lambda: press_button(B, "Samples/pianoB.wav", "B"))
            root.after(900, lambda: release_button(E2, "E2"))
            root.after(1200, lambda: press_button(C2, "Samples/pianoC2.wav", "C2"))
            root.after(1200, lambda: release_button(B, "B"))
            root.after(1500, lambda: press_button(Cs2, "Samples/pianoC#2.wav", "Cs2"))
            root.after(1500, lambda: release_button(C2, "C2"))
            root.after(1900, lambda: press_button(G, "Samples/pianoG.wav", "G"))
            root.after(1900, lambda: release_button(Cs2, "Cs2"))
            root.after(3400, lambda: press_button(G2, "Samples/pianoG2.wav", "G2"))
            root.after(3400, lambda: release_button(G, "G"))
            root.after(4200, lambda: press_button(E2, "Samples/pianoE2.wav", "E2"))
            root.after(4200, lambda: release_button(G2, "G2"))
            root.after(4600, lambda: press_button(F2, "Samples/pianoF2.wav", "F2"))
            root.after(4600, lambda: release_button(E2, "E2"))
            root.after(6000, lambda: press_button(G2, "Samples/pianoG2.wav", "G2"))
            root.after(6000, lambda: release_button(F2, "F2"))
            root.after(6800, lambda: press_button(E2, "Samples/pianoE2.wav", "E2"))
            root.after(6600, lambda: release_button(G2, "G2"))
            root.after(7200, lambda: press_button(F2, "Samples/pianoF2.wav", "F2"))
            root.after(7200, lambda: release_button(E2, "E2"))
            root.after(8600, lambda: press_button(G2, "Samples/pianoG2.wav", "G2"))
            root.after(8600, lambda: release_button(F2, "F2"))
            root.after(9200, lambda: press_button(B, "Samples/pianoB.wav", "B"))
            root.after(9200, lambda: release_button(G2, "G2"))
            root.after(9600, lambda: press_button(C2, "Samples/pianoC2.wav", "C2"))
            root.after(9600, lambda: release_button(B, "B"))
            root.after(9800, lambda: release_button(C2, "C2"))
            root.after(12000, music_finished)


#Setting up the GUI for the piano

frame = tk.Frame(root, bg="black", bd=20, relief=tk.RIDGE)
frame.grid()

frame2 = tk.Frame(frame, bg="gray")
frame2.grid()

frame3 = tk.Frame(frame, bg="black", bd=20, relief=tk.RIDGE)
frame3.grid()


C = tk.Button(frame2, height=6, width=6, text="C", bg="white", fg="black")
C.grid(row=1, column=0)
C.bind("<ButtonPress-1>", lambda event: on_button_press("Samples/pianoC.wav"))
C.bind("<ButtonRelease-1>", lambda event: on_button_release())

Cs = tk.Button(frame2, height=6, width=6, text="C#", bg="black", fg="white")
Cs.grid(row=0, column=0)
Cs.bind("<ButtonPress-1>", lambda event: on_button_press("Samples/pianoC#.wav"))
Cs.bind("<ButtonRelease-1>", lambda event: on_button_release())

D = tk.Button(frame2, height=6, width=6, text="D", bg="white", fg="black")
D.grid(row=1, column=1)
D.bind("<ButtonPress-1>", lambda event: on_button_press("Samples/pianoD.wav"))
D.bind("<ButtonRelease-1>", lambda event: on_button_release())

Ds = tk.Button(frame2, height=6, width=6, text="D#", bg="black", fg="white")
Ds.grid(row=0, column=1)
Ds.bind("<ButtonPress-1>", lambda event: on_button_press("Samples/pianoD#.wav"))
Ds.bind("<ButtonRelease-1>", lambda event: on_button_release())

E = tk.Button(frame2, height=6, width=6, text="E", bg="white", fg="black")
E.grid(row=1, column=2)
E.bind("<ButtonPress-1>", lambda event: on_button_press("Samples/pianoE.wav"))
E.bind("<ButtonRelease-1>", lambda event: on_button_release())

F = tk.Button(frame2, height=6, width=6, text="F", bg="white", fg="black")
F.grid(row=1, column=3)
F.bind("<ButtonPress-1>", lambda event: on_button_press("Samples/pianoF.wav"))
F.bind("<ButtonRelease-1>", lambda event: on_button_release())

Fs = tk.Button(frame2, height=6, width=6, text="F#", bg="black", fg="white")
Fs.grid(row=0, column=3)
Fs.bind("<ButtonPress-1>", lambda event: on_button_press("Samples/pianoF#.wav"))
Fs.bind("<ButtonRelease-1>", lambda event: on_button_release())

G = tk.Button(frame2, height=6, width=6, text="G", bg="white", fg="black")
G.grid(row=1, column=4)
G.bind("<ButtonPress-1>", lambda event: on_button_press("Samples/pianoG.wav"))
G.bind("<ButtonRelease-1>", lambda event: on_button_release())

Gs = tk.Button(frame2, height=6, width=6, text="G#", bg="black", fg="white")
Gs.grid(row=0, column=4)
Gs.bind("<ButtonPress-1>", lambda event: on_button_press("Samples/pianoG#.wav"))
Gs.bind("<ButtonRelease-1>", lambda event: on_button_release())

A = tk.Button(frame2, height=6, width=6, text="A", bg="white", fg="black")
A.grid(row=1, column=5)
A.bind("<ButtonPress-1>", lambda event: on_button_press("Samples/pianoA.wav"))
A.bind("<ButtonRelease-1>", lambda event: on_button_release())

As = tk.Button(frame2, height=6, width=6, text="A#", bg="black", fg="white")
As.grid(row=0, column=5)
As.bind("<ButtonPress-1>", lambda event: on_button_press("Samples/pianoA#.wav"))
As.bind("<ButtonRelease-1>", lambda event: on_button_release())

B = tk.Button(frame2, height=6, width=6, text="B", bg="white", fg="black")
B.grid(row=1, column=6)
B.bind("<ButtonPress-1>", lambda event: on_button_press("Samples/pianoB.wav"))
B.bind("<ButtonRelease-1>", lambda event: on_button_release())

C2 = tk.Button(frame2, height=6, width=6, text="C2", bg="white", fg="black")
C2.grid(row=1, column=7)
C2.bind("<ButtonPress-1>", lambda event: on_button_press("Samples/pianoC2.wav"))
C2.bind("<ButtonRelease-1>", lambda event: on_button_release())

Cs2 = tk.Button(frame2, height=6, width=6, text="C#2", bg="black", fg="white")
Cs2.grid(row=0, column=7)
Cs2.bind("<ButtonPress-1>", lambda event: on_button_press("Samples/pianoC#2.wav"))
Cs2.bind("<ButtonRelease-1>", lambda event: on_button_release())

D2 = tk.Button(frame2, height=6, width=6, text="D2", bg="white", fg="black")
D2.grid(row=1, column=8)
D2.bind("<ButtonPress-1>", lambda event: on_button_press("Samples/pianoD2.wav"))
D2.bind("<ButtonRelease-1>", lambda event: on_button_release())

Ds2 = tk.Button(frame2, height=6, width=6, text="D#2", bg="black", fg="white")
Ds2.grid(row=0, column=8)
Ds2.bind("<ButtonPress-1>", lambda event: on_button_press("Samples/pianoD#2.wav"))
Ds2.bind("<ButtonRelease-1>", lambda event: on_button_release())

E2 = tk.Button(frame2, height=6, width=6, text="E2", bg="white", fg="black")
E2.grid(row=1, column=9)
E2.bind("<ButtonPress-1>", lambda event: on_button_press("Samples/pianoE2.wav"))
E2.bind("<ButtonRelease-1>", lambda event: on_button_release())

F2 = tk.Button(frame2, height=6, width=6, text="F2", bg="white", fg="black")
F2.grid(row=1, column=10)
F2.bind("<ButtonPress-1>", lambda event: on_button_press("Samples/pianoF2.wav"))
F2.bind("<ButtonRelease-1>", lambda event: on_button_release())

Fs2 = tk.Button(frame2, height=6, width=6, text="F#2", bg="black", fg="white")
Fs2.grid(row=0, column=10)
Fs2.bind("<ButtonPress-1>", lambda event: on_button_press("Samples/pianoF#2.wav"))
Fs2.bind("<ButtonRelease-1>", lambda event: on_button_release())

G2 = tk.Button(frame2, height=6, width=6, text="G2", bg="white", fg="black")
G2.grid(row=1, column=11)
G2.bind("<ButtonPress-1>", lambda event: on_button_press("Samples/pianoG2.wav"))
G2.bind("<ButtonRelease-1>", lambda event: on_button_release())

Gs2 = tk.Button(frame2, height=6, width=6, text="G#2", bg="black", fg="white")
Gs2.grid(row=0, column=11)
Gs2.bind("<ButtonPress-1>", lambda event: on_button_press("Samples/pianoG#2.wav"))
Gs2.bind("<ButtonRelease-1>", lambda event: on_button_release())

A2 = tk.Button(frame2, height=6, width=6, text="A2", bg="white", fg="black")
A2.grid(row=1, column=12)
A2.bind("<ButtonPress-1>", lambda event: on_button_press("Samples/pianoA2.wav"))
A2.bind("<ButtonRelease-1>", lambda event: on_button_release())

As2 = tk.Button(frame2, height=6, width=6, text="A#2", bg="black", fg="white")
As2.grid(row=0, column=12)
As2.bind("<ButtonPress-1>", lambda event: on_button_press("Samples/pianoA#2.wav"))
As2.bind("<ButtonRelease-1>", lambda event: on_button_release())

B2 = tk.Button(frame2, height=6, width=6, text="B2", bg="white", fg="black")
B2.grid(row=1, column=13)
B2.bind("<ButtonPress-1>", lambda event: on_button_press("Samples/pianoB2.wav"))
B2.bind("<ButtonRelease-1>", lambda event: on_button_release())

C3 = tk.Button(frame2, height=6, width=6, text="C3", bg="white", fg="black")
C3.grid(row=1, column=14)
C3.bind("<ButtonPress-1>", lambda event: on_button_press("Samples/pianoC3.wav"))
C3.bind("<ButtonRelease-1>", lambda event: on_button_release())

NOTE_OCTAVE = tk.Label(frame2,height=2,width=4,text="oct: "+str(octave),bg="white",fg="black",font="bold")
NOTE_OCTAVE.grid(row=0,column=13)

MUSIC_PLAY = tk.Button(frame2,height=2,width=10,text="Play Music",bg="white",fg="black",font="bold", command=play_music)
MUSIC_PLAY.grid(row=0,column=15)

MUSIC_SELECT = tk.Button(frame2,height=2,width=2,bg="red",fg="black",font="bold", command=change_song)
MUSIC_SELECT.grid(row=0,column=14)

MUSIC_PICKED = tk.Label(frame2,height=2,width=12,text="Picked Song: "+str(song_number),bg="white",fg="black",font="bold")
MUSIC_PICKED.grid(row=1,column=15)
