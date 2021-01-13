import MyModule02
DF=MyModule02.getDF("nirs.xlsx","Sheet1")
DF2=MyModule02.extractDF(DF,400,300)
T=MyModule02.getS(DF2,0)
T1=T*0.1

print("確認したいデータがあるチャンネルの番号(1～47)を入力してください")
nnn=int(input())

if nnn>=1 and nnn<=47:
    S2=MyModule02.getS(DF2,nnn)
    MyModule02.drawS(T1,S2)
    
else:
    print("入力は1～47の整数です")