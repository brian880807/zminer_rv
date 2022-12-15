# 2022 Data Mining Final Project 第14組

[Original Code](https://github.com/zedshape/zminer.git)

本程式為 Z-Miner: An Efficient Method for Mining Frequent Arrangements of Event Intervals, KDD 2020 之原程式碼的改良版本。

## 組員

* M11115017 許文珊
* M11115089 郭恕
* M11115093 陳堂吉
* M11115094 李哲宇

## 實驗環境

### 硬體環境

* 作業系統：Windows 10 Professional 64-bit
* CPU：Intel® Core™ i5-12400F @ 2.50GHz
* 記憶體大小：16GB

### 軟體環境

本程式皆使用Python distribution內建的libraries，並未使用任何external libraries。

* Python 3.9.13
* sys
* csv
* time

## 資料集來源

本程式使用原程式Github所提供的Real-world datasets與Synthetic datsets。

## 執行方法

本程式透過以下指令執行(與原程式相同)：

`python ZMiner_rv.py [filename] [minSup] [epsilon] [gap] [timeout] [level] [printF] [printL]`

### 參數說明

* filename：資料集檔案名稱
* minSup：Minimum support，預設為0
* epsilon：判斷matches關係的允許誤差值，預設為0
* gap：限制follows關係的最大距離，預設為無限
* timeout：Z-Miner演算法執行時間上限(秒)，預設為10000
* level：Frequent arrangements的event數目上限，預設為無限
* printF：是否輸出簡略版csv檔案(True/False)，詳見[檔案輸出F](#檔案輸出f)，預設為False
* printL：是否輸出詳盡版csv檔案(True/False)，詳見[檔案輸出L](#檔案輸出l)，預設為False

以下為執行本程式的一個例子：

`python ZMiner_rv.py data/ASL_BU_1.txt 0.01 5 10 300 8 True False`

表示我們使用ASL_BU_1.txt資料集；minimum support設定為0.01；epsilon設定為5；gap設定為10；timeout設定為300秒；level設定為8；並且輸出簡略版csv檔，不輸出詳盡版csv檔。

## 執行結果

### Terminal 輸出

>TEST WITH [資料集檔名] DATASET<br>
>TOTAL SEQUENCE: [e-sequence總數]<br>
>TOTAL DISTINCT EVENTS: [event種類個數]<br>
>TOTAL INTERVALS: [event interval總數]<br>
>AVERAGE INTERVAL PER SEQ: [一個e-sequence的平均event interval數]<br>
>AVERAGE TIMESPAN: [一個e-sequence的平均timespan]<br>
>TEST WITH [資料集檔名] DATASET<br>
>########## Z-MINER_RV ##########<br>
>1-1. MINIMUM SUPPORT: [minSup count]<br>
>1-2. EPSILON CONSTRAINT: [epsilon]<br>
>1-4. TIMEOUT: [timeout]<br>
>1-5. LEVEL: [level]<br>
>2. NUMBER OF E-SEQUENCES: [e-sequence總數]<br>
>3. TOTAL COMPARISON COUNTS: [在initZ()與extendZ()中，檢查舊event與新event是否有frequent relation的次數]<br>
>4. TOTAL FREQUENT ARRANGEMENTS: [frequent arrangement總數]<br>
>5. TOTAL TIME CONSUMED: [Z-Miner演算法執行時間]<br>
>6. extendZ() called count: [extendZ()呼叫總次數]

### 檔案輸出F

* 輸出檔名：F_[資料集名稱]\_[minSup]\_[epsilon]\_[gap]\_[timeout].csv
* 一列表示一個frequent arrangement
* 欄位依序為該arrangement的event labels, relations, frequency

for example:

| event | relations | frequency |
|-----|-----|-----|
| ('17','10','179') | fcc | 13 |

表示..

### 檔案輸出L

* 輸出檔名：L_[資料集名稱]\_[minSup]\_[epsilon]\_[gap]\_[timeout].csv
* 一列表示一個frequent arrangement與其所在資料集中的位置
* 欄位依序為該arrangement的event labels, relations, frequency, 所在e-sequence, event interval (event label, start time, end time)

for example:

| event | relations | frequency | e-sequence | intervals |
|-----|-----|-----|-----|-----|
| ('78','98','179') | ecc | 10 | 647 | (78, 68, 2768),(98, 68, 2768),(179, 434, 801) |

表示..