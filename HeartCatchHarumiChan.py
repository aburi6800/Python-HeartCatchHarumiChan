import time
import tkinter
import random
import os
import csv
from PIL import Image, ImageTk, ImageDraw, ImageOps

############################################################################### 
# 初期処理
############################################################################### 

# 仮想VRAMのサイズ
VRM_WIDTH = 40
VRM_HEIGHT = 24

# ゲームの状態
GAMESTATUS_TITLE = 0
GAMESTATUS_START = 1
GAMESTATUS_GAME = 2
GAMESTATUS_MISS = 3
GAMESTATUS_GOAL = 4
GAMESTATUS_OVER = 5

# キー判定用
KEY_LEFT = "Left"
KEY_RIGHT = "Right"
KEY_SPACE = "space"
KEY_Z = "z"

# PC8001のカラーコードとRGB値の対応辞書
# 0 : 黒        RGB( 0x00, 0x00, 0x00)
# 1 : 青        RGB( 0x00, 0x00, 0xFF)
# 2 : 赤        RGB( 0xFF, 0x00, 0x00)
# 3 : マゼンタ  RGB( 0xFF, 0x00, 0xFF)
# 4 : 緑        RGB( 0x00, 0xFF, 0x00)
# 5 : シアン    RGB( 0x00, 0xFF, 0xFF)
# 6 : 黄色      RGB( 0xFF, 0xFF, 0x00)
# 7 : 白        RGB( 0xFF, 0xFF, 0xFF)
COLOR = {
    "BLACK"  : (0x00, 0x00, 0x00),
    "BLUE"   : (0x00, 0x00, 0xFF),
    "RED"    : (0xFF, 0x00, 0x00),
    "MAGENTA": (0xFF, 0x00, 0xFF),
    "GREEN"  : (0x00, 0xFF, 0x00),
    "CYAN"   : (0x00, 0xFF, 0xFF),
    "YELLOW" : (0xFF, 0xFF, 0x00),
    "WHITE"  : (0xFF, 0xFF, 0xFF),
}

# PC8001のカラーコード
COLOR_0 = "BLACK"
COLOR_1 = "BLUE"
COLOR_2 = "RED"
COLOR_3 = "MAGENTA"
COLOR_4 = "GREEN"
COLOR_5 = "CYAN"
COLOR_6 = "YELLOW"
COLOR_7 = "WHITE"

# スクリプトのパス
basePath = os.path.abspath(os.path.dirname(__file__))

# 空の仮想VRAM配列
blankRow = [0] * VRM_WIDTH
vrm = [blankRow] * VRM_HEIGHT

# PhotoImageの保存用変数
photoImage = ""

# ゲームの状態管理用
gameStatus = GAMESTATUS_TITLE

# ゲームの経過時間管理用
gameTime = 0

# キーイベント用
key = ""
keyOff = True


############################################################################### 
# メイン処理
############################################################################### 
def main():
    global gameTime, key, keyOff

    # 画面描画
    draw()

    # 処理
#    if gameStatus == GAMESTATUS_TITLE:
#        # タイトル処理
#        title()

#    else:
#        # ゲームメイン処理
#        game()		

    # 時間進行
    gameTime = gameTime + 1

    # キーリピート対策
    if keyOff == True:
        key = ""
        keyOff = False

    root.after(50, main)


############################################################################### 
# キーイベント：キー押す
############################################################################### 
def pressKey(e):
    global key, keyOff

    key = e.keysym
    keyOff = False


############################################################################### 
# キーイベント：キー離す
############################################################################### 
def releaseKey(e):
    global keyOff

    keyOff = True


############################################################################### 
# ゲーム状態変更
############################################################################### 
def changeGameStatus(status):
    global gameStatus, gameTime

    gameStatus = status
    gameTime = 0


############################################################################### 
# タイトル処理
############################################################################### 
def title():
    global key

#    if key == KEY_SPACE:
#        # ゲーム初期化
#        initializeGame()
#        changeGameStatus(GAMESTATUS_GAME)

    key = ""


############################################################################### 
# ゲーム初期化
############################################################################### 
def initializeGame():

    pass


############################################################################### 
# ラウンド初期化
############################################################################### 
def initializeRound():

    pass


############################################################################### 
# ゲーム処理
############################################################################### 
def game():

    pass


############################################################################### 
# 画面描画
############################################################################### 
def draw():
	global photoImage

    # canvasのイメージ削除
	canvas.delete("SCREEN")


	if gameStatus == GAMESTATUS_TITLE:
		# タイトル
		img_screen = drawTitle()

#    else:
#        # ゲーム画面
#        img_screen = drawGame()

	# 画面イメージを拡大
	img_screen = img_screen.resize((img_screen.width * 2, img_screen.height * 2), Image.NEAREST)

	# オフスクリーンでPhotoImage生成
	photoImage = ImageTk.PhotoImage(img_screen)
	canvas.create_image((img_screen.width / 2, img_screen.height / 2), image = photoImage, tag = "SCREEN")


############################################################################### 
# タイトル画面描画
############################################################################### 
def drawTitle():

	# 画面イメージ作成
	img_screen = img_bg.copy()
	writeText(img_screen, 0, 0, (0x97, 0x20, 0x88, 0x20, 0x20, 0x20, 0x97, 0x20, 0x20, 0x20, 0x20, 0x20, 0x95, 0x8F, 0x95, 0x20, 0x20, 0x20, 0x20, 0x20, 0x80, 0x80, 0xEE), COLOR_2)
	writeText(img_screen, 0, 1, (0x97, 0x20, 0x88, 0x95, 0x95, 0x95, 0x97, 0xEF, 0x20, 0x20, 0xE9, 0x20, 0x95, 0x8F, 0x95, 0x20, 0x20, 0x20, 0x20, 0x20, 0x95, 0x8F, 0x95), COLOR_2)
	writeText(img_screen, 0, 2, (0xEE, 0x20, 0xEF, 0x20, 0x20, 0x20, 0x97, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x96, 0x20, 0x20, 0xD4, 0x20, 0xC2, 0x20, 0x95, 0x9B, 0x20), COLOR_2)

	return img_screen


############################################################################### 
# ゲーム画面描画
############################################################################### 
def drawGame():

	# オフスクリーン作成
	img_screen = img_bg.copy()

	return img_screen


############################################################################### 
# テキスト描画
# 引数		img 貼り付け先のImageデータ
#  			x テキスト座標系のx座標
#			y テキスト座標系のy座標
#			s 表示する文字データの配列（文字の場合は、文字コードに対応した文字を表示する）
#           c 文字の表示色（省略時は白）
############################################################################### 
def writeText(img, x, y, s, c=COLOR_7):

    # 指定色で塗りつぶした矩形を作成
    imgBack = Image.new("RGBA", (gPos(len(s)), 8), COLOR[c])
    
	# 文字を描画
    for i in range(len(s)):
        if isinstance(s, str):
            o = ord(s[i]) - 32
        else:
            o = s[i] - 32

        if o >= 0 and o <= len(img_font):
            imgBack.paste(img_font[o], (gPos(i), gPos(0)), img_font_mask[o])

    # 文字のパターンでマスクした画像を貼り付け
    img.paste(imgBack, (gPos(x), gPos(y)), imgBack)


############################################################################### 
# 指定されたパスの画像をロードして2倍に拡大したImageを返却する
# 引数		filepath 画像データのフルパス
# 戻り値	2倍に拡大したImageデータ
############################################################################### 
def loadImage(filePath):

	img = Image.open(filePath).convert("RGBA")
	return img


############################################################################### 
# テキスト座標系からグラフィック座標系に変換する
# 引数      value 変換する値
# 戻り値    変換後の値
############################################################################### 
def gPos(value):

	return value * 8


# Windowを生成
root = tkinter.Tk()
root.geometry(str(VRM_WIDTH * 8 * 2) + "x" + str(VRM_HEIGHT * 8 * 2))
root.title("HEART CATCH HARUMI-CHAN on Python")
root.bind("<KeyPress>", pressKey)
root.bind("<KeyRelease>", releaseKey)

# Canvas生成
canvas = tkinter.Canvas(width = (VRM_WIDTH * 8 * 2), height = (VRM_HEIGHT * 8 * 2))
canvas.pack()

# BG生成
img_bg = Image.new("RGBA", (VRM_WIDTH * 8, VRM_HEIGHT * 8), (0, 0, 0))

# フォントイメージ
img_fonts = loadImage(basePath + os.sep + "Images" + os.sep + "p8font.png")
img_font = []
img_font_mask = []
for h in range(0, img_fonts.height, 8):
    for w in range(0, img_fonts.width, 8):
        img = img_fonts.crop((w , h, w + 8, h + 8))
        # フォント画像生成
        img_font.append(img)
        # マスク画像生成
        img_font_mask.append(ImageOps.invert(img.convert("L")))

# メイン処理
main()

# ウィンドウイベントループ実行
root.mainloop()
