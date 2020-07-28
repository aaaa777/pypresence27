# -*- coding: utf-8 -*-
from presence27.presence import Presence
import time


RPC = Presence(737286157456506940)

RPC.connect()

RPC.update(state="三段目表示", details="二段目表示",
		   
		   # 開始時間 (○時間プレイ中)
		   #start = int(time.time()),
		   
		   # 終了時間 (残時間表示)
		   # end = int(time.time()) + 900, 
		   
		   # 登録済み表示画像名と表示名
		   #large_image = '登録済み大画像名', large_text = '大画像マウスオーバー表示テキスト', 
		   #small_image = '登録済み小画像名', small_text = '小画面マウスオーバー表示テキスト',
		   
		   # 参加、観戦ボタン等
		   #join = 'join_secret',
		   #spectate = 'spectate_secret',
		   #match = 'match_secret',

		   # パーティサイズ指定 (分子,分母)
		   #party_size = [1, 3]
		   )

time.sleep(3600)