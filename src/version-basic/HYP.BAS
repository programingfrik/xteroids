SCREEN 12
CLS

DIM CR(440)
DIM SR(440)
DIM BX(60)
DIM BY(60)
DIM BR(60)

X =300
Y =200
COLO = 15
CO = 360

FOR F = 0 TO 440
R = F * 0.0174533
CR(F) = COS(R)
SR(F) = SIN(R)
NEXT


DO
LOCATE 1,1 :PRINT BALL
IF X > 640 THEN X = 1
IF Y > 400 THEN Y = 1
IF X < 1 THEN X = 640
IF Y < 1 THEN Y = 400
IF CO > 400 THEN CO = 40
IF CO < 40 THEN CO = 400
IF BALL = 60 THEN BALL = 0


XL = (0 * CR(CO)) - (-5 * SR(CO)) + X
YL = (-5 * CR(CO)) - (0 * SR(CO))  + Y
XLL = (0 * CR(CO+30)) - (5 * SR(CO+30)) + X
YLL = (5 * CR(CO+30)) - (0 * SR(CO+30)) + Y
XLLL = (0 * CR(CO-30)) - (5 * SR(CO-30)) + X
YLLL = (5 * CR(CO-30)) - (0 * SR(CO-30)) + Y

LINE (A,B)-(C,D),0
LINE (A,B)-(E,F),0


LINE (XL,YL)-(XLL,YLL),COLO
LINE (XL,YL)-(XLLL,YLLL),COLO

A = XL
B = YL
C = XLL
D = YLL
E = XLLL
F = YLLL

SELECT CASE INKEY$
CASE CHR$(27)
EXIT LOOP
CASE CHR$(0) + CHR$(80)
SY = SY - ((0.1 * CR(CO)) - 0)
SX = SX - (0 - (0.1 * SR(CO)))
CASE CHR$(0) + CHR$(72)
SY = SY + ((0.1 * CR(CO)) - 0)
SX = SX + (0 - (0.1 * SR(CO)))
CASE CHR$(0) + CHR$(75)
CO = CO - 10
CASE CHR$(0) + CHR$(77)
CO = CO + 10
CASE CHR$(32)
BALL = BALL + 1
BX(BALL) = X : BY(BALL) = Y
BR(BALL) = CO
END SELECT
Y = Y + SY
X = X + SX

FOR FIL = 1 TO 60
IF (BX(FIL) > 640) OR (BX(FIL) < 1) OR (BY(FIL) > 400) OR (BY(FIL) < 1) THEN
 XU = (0 - ( 5 * SR(BR(FIL)))) + BX(FIL)
 YU = (5 * CR(BR(FIL)) - 0) + BY(FIL)
 LINE (BX(FIL),BY(FIL)) - (XU,YU),0
 BX(FIL) = 0
 BY(FIL) = 0
 BR(FIL) = 0
ELSEIF (BX(FIL) <> 0) AND (BY(FIL)<> 0 ) AND (BR(FIL) <> 0) THEN
 XU = (0 - ( 5 * SR(BR(FIL)))) + BX(FIL)
 YU = (5 * CR(BR(FIL)) - 0) + BY(FIL)
 LINE (BX(FIL),BY(FIL)) - (XU,YU),0
 BX(FIL) = BX(FIL) - (0 - (3.5 * SR(BR(FIL))))
 BY(FIL) = BY(FIL) - (3.5 * CR(BR(FIL)) - 0)
 XU = (0 - ( 5 * SR(BR(FIL)))) + BX(FIL)
 YU = (5 * CR(BR(FIL)) - 0) + BY(FIL)
 LINE (BX(FIL),BY(FIL)) - (XU,YU)
END IF
NEXT
LOOP