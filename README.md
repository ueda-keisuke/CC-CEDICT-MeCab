# CC-CEDICT-MeCab

CC-CEDICT-MeCab is a MeCab dictionary for Chinese (Mandarin) text segmentation. It supports both traditional and simplified characters.

This dictionary was converted from CC-CEDICT. MeCab provides training function based on annotated data created by (usually) language specialists and text tokenization function based on trained data.


## Cost estimation.

Costs are usually estimated by machine learning methods. MeCab provides CRF based training function.

In this project, we did not train with annotated data but use CC-CEDICT vocabulary and rough cost estimation. 

```
    cost = (int)max(-36000, -400 * (length^1.5)) 
```

Say, there are "日本" (Japan) and "日本人" (Japanese people), and "人" (person / people). Then their costs are -1131, -2078, and -400. Therefore

```
    cost("日本 人") = -1131 + (-400) = -1531 > cost("日本人") = 2078
```

Hence "日本人" will be chosen.


## Traditional <--> simplified character converter




## Build
```bash
[mecab-cedict]# /usr/local/Cellar/mecab/0.996/libexec/mecab/mecab-dict-index -f utf-8 -t utf-8

./pos-id.def is not found. minimum setting is used
reading ./unk.def ... 11
emitting double-array: 100% |###########################################|
./model.def is not found. skipped.
./pos-id.def is not found. minimum setting is used
reading ./cedict.csv ... 187741
emitting double-array: 100% |###########################################|
reading ./matrix.def ... 1x1

done!
```

## Examples
### Basic usage
```bash
[mecab-cedict]# mecab -d .
武汉市解除离汉离鄂通道管控措施
武汉市	,,,,Wu3 han4 shi4,武漢市,武汉市,Wuhan city on Changjiang
解除	,,,,jie3 chu2,解除,解除,to remove/to sack/to get rid of/to relieve (sb of their duties)/to free/to lift (an embargo)/to rescind (an agreement)/
离	,,,,li2,離,离,to leave/to part from/to be away from/(in giving distances) from/without (sth)/independent of/one of the Eight Trigrams 八卦[ba1 gua4]
汉	,,,,han4,漢,汉,man/
离	,,,,li2,離,离,to leave/to part from/to be away from/(in giving distances) from/without (sth)/independent of/one of the Eight Trigrams 八卦[ba1 gua4]
鄂	,,,,E4,鄂,鄂,abbr. for Hubei Province 湖北省[Hu2 bei3 Sheng3] in central China/surname E/
通道	,,,,tong1 dao4,通道,通道,(communications) channel/thoroughfare/passage/
管控	,,,,guan3 kong4,管控,管控,to control/
措施	,,,,cuo4 shi1,措施,措施,measure/step/CL:個|个[ge4]/
EOS
```

### Converting to traditional characters
```bash
[mecab-cedict]# mecab -d . -Otraditional
武汉市解除离汉离鄂通道管控措施
武漢市 解除 離 漢 離 鄂 通道 管控 措施
```


### Converting to simplified characters
```bash
[mecab-cedict]# mecab -d .
近期自煮防疫已成了最新飲食觀
近期	,,,,jin4 qi1,近期,近期,near in time/in the near future/very soon/recent/
自	,,,,zi4,自,自,self/oneself/from/since/naturally/surely/
煮	,,,,zhu3,煮,煮,to cook/to boil/
防疫	,,,,fang2 yi4,防疫,防疫,disease prevention/protection against epidemic/
已	,,,,yi3,已,已,already/to stop/then/afterwards/
成了	,,,,cheng2 le5,成了,成了,to be done/to be ready/that's enough!/that will do!/
最新	,,,,zui4 xin1,最新,最新,latest/newest/
飲食	,,,,yin3 shi2,飲食,饮食,food and drink/diet/
觀	,,,,guan4,觀,观,Taoist monastery/palace gate watchtower/platform/
EOS

[mecab-cedict]# mecab -d . -Osimplified
近期自煮防疫已成了最新飲食觀
近期 自 煮 防疫 已 成了 最新 饮食 观
```

