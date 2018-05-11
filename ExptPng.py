# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
import freetype
import numpy as np
import os
from PIL import Image

path = os.path.join(os.getcwd(), 'tyc_chars')
if not os.path.exists(path):
    os.mkdir(path)

normal_char = [65279, 21834, 38463, 22467, 25384, 21710, 21769, 21696, 30353, 30284, 34108, 30702, 33406, 30861, 29233, 38552, 38797, 27688, 23433, 20474, 25353, 26263, 23736, 33018, 26696, 32942, 26114, 30414, 20985, 25942, 29100, 32753, 34948, 20658, 22885, 25034, 28595, 33453, 25420, 25170, 21485, 21543, 31494, 20843, 30116, 24052, 25300, 36299, 38774, 25226, 32793, 22365, 38712, 32610, 29240, 30333, 26575, 30334, 25670, 20336, 36133, 25308, 31255, 26001, 29677, 25644, 25203, 33324, 39041, 26495, 29256, 25198, 25292, 20276, 29923, 21322, 21150, 32458, 37030, 24110, 26758, 27036, 33152, 32465, 26834, 30917, 34444, 38225, 20621, 35876, 33502, 32990, 21253, 35090, 21093, 34180, 38649, 20445, 22561, 39281, 23453, 25265, 25253, 26292, 35961, 40077, 29190, 26479, 30865, 24754, 21329, 21271, 36744, 32972, 36125, 38049, 20493, 29384, 22791, 24811, 28953, 34987, 22868, 33519, 26412, 31528, 23849, 32503, 29997, 27893, 36454, 36856, 36924, 40763, 27604, 37145, 31508, 24444, 30887, 34006, 34109, 27605, 27609, 27606, 24065, 24199, 30201, 38381, 25949, 24330, 24517, 36767, 22721, 33218, 36991, 38491, 38829, 36793, 32534, 36140, 25153, 20415, 21464, 21342, 36776, 36777, 36779, 36941, 26631, 24426, 33176, 34920, 40150, 24971, 21035, 30250, 24428, 25996, 28626, 28392, 23486, 25672, 20853, 20912, 26564, 19993, 31177, 39292, 28851, 30149, 24182, 29627, 33760, 25773, 25320, 38069, 27874, 21338, 21187, 25615, 38082, 31636, 20271, 24091, 33334, 33046, 33162, 28196, 27850, 39539, 25429, 21340, 21754, 34917, 22496, 19981, 24067, 27493, 31807, 37096, 24598, 25830, 29468, 35009, 26448, 25165, 36130, 30572, 36393, 37319, 24425, 33756, 34081, 39184, 21442, 34453, 27531, 24813, 24808, 28799, 33485, 33329, 20179, 27815, 34255, 25805, 31961, 27133, 26361, 33609, 21397, 31574, 20391, 20876, 27979, 23618, 36461, 25554, 21449, 33580, 33590, 26597, 30900, 25661, 23519, 23700, 24046, 35815, 25286, 26612, 35962, 25600, 25530, 34633, 39307, 35863, 32544, 38130, 20135, 38416, 39076, 26124, 29462, 22330, 23581, 24120, 38271, 20607, 32928, 21378, 25950, 30021, 21809, 20513, 36229, 25220, 38046, 26397, 22066, 28526, 24034, 21557, 28818, 36710, 25199, 25764, 25507, 24443, 28552, 37108, 33251, 36784, 23576, 26216, 24561, 27785, 38472, 36225, 34924, 25745, 31216, 22478, 27225, 25104, 21576, 20056, 31243, 24809, 28548, 35802, 25215, 36894, 39563, 31204, 21507, 30196, 25345, 21273, 27744, 36831, 24347, 39536, 32827, 40831, 20360, 23610, 36196, 32709, 26021, 28861, 20805, 20914, 34411, 23815, 23456, 25277, 37228, 30068, 36364, 31264, 24833, 31609, 20167, 32504, 30597, 19985, 33261, 21021, 20986, 27249, 21416, 36487, 38148, 38607, 28353, 38500, 26970, 30784, 20648, 30679, 25616, 35302, 22788, 25571, 24029, 31359, 26941, 20256, 33337, 21912, 20018, 30126, 31383, 24162, 24202, 38383, 21019, 21561, 28810, 25462, 38180, 22402, 26149, 26943, 37255, 21767, 28147, 32431, 34850, 25139, 32496, 30133, 33576, 30913, 38604, 36766, 24904, 29943, 35789, 27492, 21050, 36176, 27425, 32874, 33905, 22257, 21254, 20174, 19995, 20945, 31895, 37259, 31751, 20419, 36479, 31713, 31388, 25703, 23828, 20652, 33030, 30209, 31929, 28140, 32736, 26449, 23384, 23544, 30923, 25774, 25619, 25514, 25387, 38169, 25645, 36798, 31572, 30249, 25171, 22823, 21574, 27513, 20643, 25140, 24102, 27526, 20195, 36151, 34955, 24453, 36910, 24608, 32829, 25285, 20025, 21333, 37112, 25528, 32966, 26086, 27694, 20294, 24814, 28129, 35806, 24377, 34507, 24403, 25377, 20826, 33633, 26723, 20992, 25443, 36424, 20498, 23707, 31095, 23548, 21040, 31291, 24764, 36947, 30423, 24503, 24471, 30340, 36460, 28783, 30331, 31561, 30634, 20979, 37011, 22564, 20302, 28404, 36842, 25932, 31515, 29380, 28068, 32735, 23265, 25269, 24213, 22320, 33922, 31532, 24093, 24351, 36882, 32532, 39072, 25474, 28359, 30872, 28857, 20856, 38747, 22443, 30005, 20291, 30008, 24215, 24806, 22880, 28096, 27583, 30857, 21500, 38613, 20939, 20993, 25481, 21514, 38035, 35843, 36300, 29241, 30879, 34678, 36845, 35853, 21472, 19969, 30447, 21486, 38025, 39030, 40718, 38189, 23450, 35746, 20002, 19996, 20908, 33891, 25026, 21160, 26635, 20375, 24683, 20923, 27934, 20828, 25238, 26007, 38497, 35910, 36887, 30168, 37117, 30563, 27602, 29322, 29420, 35835, 22581, 30585, 36172, 26460, 38208, 32922, 24230, 28193, 22930, 31471, 30701, 38203, 27573, 26029, 32526, 22534, 20817, 38431, 23545, 22697, 21544, 36466, 25958, 39039, 22244, 38045, 30462, 36929, 25479, 21702, 22810, 22842, 22427, 36530, 26421, 36346, 33333, 21057, 24816, 22549, 34558, 23784, 40517, 20420, 39069, 35769, 23077, 24694, 21380, 25212, 36943, 37122, 39295, 24681, 32780, 20799, 32819, 23572, 39285, 27953, 20108, 36144, 21457, 32602, 31567, 20240, 20047, 38400, 27861, 29648, 34281, 24070, 30058, 32763, 27146, 30718, 38034, 32321, 20961, 28902, 21453, 36820, 33539, 36137, 29359, 39277, 27867, 22346, 33459, 26041, 32938, 25151, 38450, 22952, 20223, 35775, 32442, 25918, 33778, 38750, 21857, 39134, 32933, 21290, 35837, 21536, 32954, 24223, 27832, 36153, 33452, 37210, 21545, 27675, 20998, 32439, 22367, 28954, 27774, 31881, 22859, 20221, 24575, 24868, 31914, 20016, 23553, 26539, 34562, 23792, 38155, 39118, 30127, 28925, 36898, 20911, 32541, 35773, 22857, 20964, 20315, 21542, 22827, 25975, 32932, 23413, 25206, 25282, 36752, 24133, 27679, 31526, 20239, 20440, 26381, 28014, 28074, 31119, 34993, 24343, 29995, 25242, 36741, 20463, 37340, 26023, 33071, 33105, 24220, 33104, 36212, 21103, 35206, 36171, 22797, 20613, 20184, 38428, 29238, 33145, 36127, 23500, 35747, 38468, 22919, 32538, 21648, 22134, 22030, 35813, 25913, 27010, 38041, 30422, 28297, 24178, 29976, 26438, 26577, 31487, 32925, 36214, 24863, 31174, 25954, 36195, 20872, 21018, 38050, 32568, 32923, 32434, 23703, 28207, 26464, 31705, 30347, 39640, 33167, 32660, 31957, 25630, 38224, 31295, 21578, 21733, 27468, 25601, 25096, 40509, 33011, 30105, 21106, 38761, 33883, 26684, 34532, 38401, 38548, 38124, 20010, 21508, 32473, 26681, 36319, 32789, 26356, 24218, 32697, 22466, 32831, 26775, 24037, 25915, 21151, 24685, 40858, 20379, 36524, 20844, 23467, 24339, 24041, 27742, 25329, 36129, 20849, 38057, 21246, 27807, 33503, 29399, 22434, 26500, 36141, 22815, 36764, 33735, 21653, 31629, 20272, 27837, 23396, 22993, 40723, 21476, 34506, 39592, 35895, 32929, 25925, 39038, 22266, 38599, 21038, 29916, 21072, 23521, 25346, 35074, 20054, 25296, 24618, 26874, 20851, 23448, 20896, 35266, 31649, 39302, 32592, 24815, 28748, 36143, 20809, 24191, 36891, 29808, 35268, 22317, 30789, 24402, 40863, 38394, 36712, 39740, 35809, 30328, 26690, 26588, 36330, 36149, 21053, 36746, 28378, 26829, 38149, 37101, 22269, 26524, 35065, 36807, 21704, 39608, 23401, 28023, 27686, 20133, 23475, 39559, 37219, 25000, 37039, 38889, 21547, 28085, 23506, 20989, 21898, 32597, 32752, 25788, 25421, 26097, 25022, 24717, 28938, 27735, 27721, 22831, 26477, 33322, 22741, 22158, 35946, 27627, 37085, 22909, 32791, 21495, 28009, 21621, 21917, 33655, 33743, 26680, 31166, 21644, 20309, 21512, 30418, 35977, 38402, 27827, 28088, 36203, 35088, 40548, 36154, 22079, 40657, 30165, 24456, 29408, 24680, 21756, 20136, 27178, 34913, 24658, 36720, 21700, 28888, 34425, 40511, 27946, 23439, 24344, 32418, 21897, 20399, 29492, 21564, 21402, 20505, 21518, 21628, 20046, 24573, 29786, 22774, 33899, 32993, 34676, 29392, 31946, 28246, 24359, 34382, 21804, 25252, 20114, 27818, 25143, 33457, 21719, 21326, 29502, 28369, 30011, 21010, 21270, 35805, 27088, 24458, 24576, 28142, 22351, 27426, 29615, 26707, 36824, 32531, 25442, 24739, 21796, 30186, 35938, 28949, 28067, 23462, 24187, 33618, 24908, 40644, 30970, 34647, 31783, 30343, 20976, 24822, 29004, 26179, 24140, 24653, 35854, 28784, 25381, 36745, 24509, 24674, 34516, 22238, 27585, 24724, 24935, 21321, 24800, 26214, 36159, 31229, 20250, 28905, 27719, 35763, 35826, 32472, 33636, 26127, 23130, 39746, 27985, 28151, 35905, 27963, 20249, 28779, 33719, 25110, 24785, 38669, 36135, 31096, 20987, 22334, 22522, 26426, 30072, 31293, 31215, 31637, 32908, 39269, 36857, 28608, 35749, 40481, 23020, 32489, 32521, 21513, 26497, 26840, 36753, 31821, 38598, 21450, 24613, 30142, 27762, 21363, 23241, 32423, 25380, 20960, 33034, 24049, 34015, 25216, 20864, 23395, 20238, 31085, 21058, 24760, 27982, 23492, 23490, 35745, 35760, 26082, 24524, 38469, 22931, 32487, 32426, 22025, 26551, 22841, 20339, 23478, 21152, 33626, 39050, 36158, 30002, 38078, 20551, 31292, 20215, 26550, 39550, 23233, 27516, 30417, 22362, 23574, 31546, 38388, 29006, 20860, 32937, 33392, 22904, 32516, 33575, 26816, 26604, 30897, 30897, 25315, 25441, 31616, 20461, 21098, 20943, 33616, 27099, 37492, 36341, 36145, 35265, 38190, 31661, 20214, 20581, 33328, 21073, 39279, 28176, 28293, 28071, 24314, 20725, 23004, 23558, 27974, 27743, 30086, 33931, 26728, 22870, 35762, 21280, 37233, 38477, 34121, 26898, 30977, 28966, 33014, 20132, 37066, 27975, 39556, 23047, 22204, 25605, 38128, 30699, 20389, 33050, 29409, 35282, 39290, 32564, 32478, 21119, 25945, 37237, 36735, 36739, 21483, 31382, 25581, 25509, 30342, 31224, 34903, 38454, 25130, 21163, 33410, 26708, 26480, 25463, 30571, 31469, 27905, 32467, 35299, 22992, 25106, 34249, 33445, 30028, 20511, 20171, 30117, 35819, 23626, 24062, 31563, 26020, 37329, 20170, 27941, 35167, 32039, 38182, 20165, 35880, 36827, 38771, 26187, 31105, 36817, 28908, 28024, 23613, 21170, 33606, 20834, 33550, 30555, 26230, 40120, 20140, 24778, 31934, 31923, 32463, 20117, 35686, 26223, 39048, 38745, 22659, 25964, 38236, 24452, 30153, 38742, 31455, 31454, 20928, 28847, 31384, 25578, 31350, 32416, 29590, 38893, 20037, 28792, 20061, 37202, 21417, 25937, 26087, 33276, 33285, 21646, 23601, 30106, 38816, 25304, 29401, 30141, 23621, 39545, 33738, 23616, 21632, 30697, 20030, 27822, 32858, 25298, 25454, 24040, 20855, 36317, 36382, 38191, 20465, 21477, 24807, 28844, 21095, 25424, 40515, 23071, 20518, 30519, 21367, 32482, 25733, 25899, 25225, 25496, 20500, 29237, 35273, 20915, 35776, 32477, 22343, 33740, 38055, 20891, 21531, 23803, 20426, 31459, 27994, 37089, 39567, 21888, 21654, 21345, 21679, 24320, 25577, 26999, 20975, 24936, 21002, 22570, 21208, 22350, 30733, 30475, 24247, 24951, 31968, 25179, 25239, 20130, 28821, 32771, 25335, 28900, 38752, 22391, 33499, 26607, 26869, 30933, 39063, 31185, 22771, 21683, 21487, 28212, 20811, 21051, 23458, 35838, 32943, 21827, 22438, 24691, 22353, 21549, 31354, 24656, 23380, 25511, 25248, 21475, 25187, 23495, 26543, 21741, 31391, 33510, 37239, 24211, 35044, 22840, 22446, 25358, 36328, 33007, 22359, 31607, 20393, 24555, 23485, 27454, 21281, 31568, 29378, 26694, 30719, 30518, 26103, 20917, 20111, 30420, 23743, 31397, 33909, 22862, 39745, 20608, 39304, 24871, 28291, 22372, 26118, 25414, 22256, 25324, 25193, 24275, 38420, 22403, 25289, 21895, 34593, 33098, 36771, 21862, 33713, 26469, 36182, 34013, 23146, 26639, 25318, 31726, 38417, 20848, 28572, 35888, 25597, 35272, 25042, 32518, 28866, 28389, 29701, 27028, 29436, 24266, 37070, 26391, 28010, 25438, 21171, 29282, 32769, 20332, 23013, 37226, 28889, 28061, 21202, 20048, 38647, 38253, 34174, 30922, 32047, 20769, 22418, 25794, 32907, 31867, 27882, 26865, 26974, 20919, 21400, 26792, 29313, 40654, 31729, 29432, 31163, 28435, 29702, 26446, 37324, 40100, 31036, 33673, 33620, 21519, 26647, 20029, 21385, 21169, 30782, 21382, 21033, 20723, 20363, 20432, 30178, 31435, 31890, 27813, 38582, 21147, 29827, 21737, 20457, 32852, 33714, 36830, 38256, 24265, 24604, 28063, 24088, 25947, 33080, 38142, 24651, 28860, 32451, 31918, 20937, 26753, 31921, 33391, 20004, 36742, 37327, 26238, 20142, 35845, 25769, 32842, 20698, 30103, 29134, 23525, 36797, 28518, 20102, 25730, 38243, 24278, 26009, 21015, 35010, 28872, 21155, 29454, 29747, 26519, 30967, 38678, 20020, 37051, 40158, 28107, 20955, 36161, 21533, 25294, 29618, 33777, 38646, 40836, 38083, 20278, 32666, 20940, 28789, 38517, 23725, 39046, 21478, 20196, 28316, 29705, 27060, 30827, 39311, 30041, 21016, 30244, 27969, 26611, 20845, 40857, 32843, 21657, 31548, 31423, 38534, 22404, 25314, 38471, 27004, 23044, 25602, 31699, 28431, 38475, 33446, 21346, 39045, 24208, 28809, 25523, 21348, 34383, 40065, 40595, 30860, 38706, 36335, 36162, 40575, 28510, 31108, 24405, 38470, 25134, 39540, 21525, 38109, 20387, 26053, 23653, 23649, 32533, 34385, 27695, 24459, 29575, 28388, 32511, 23782, 25371, 23402, 28390, 21365, 20081, 25504, 30053, 25249, 36718, 20262, 20177, 27814, 32438, 35770, 33821, 34746, 32599, 36923, 38179, 31657, 39585, 35064, 33853, 27931, 39558, 32476, 22920, 40635, 29595, 30721, 34434, 39532, 39554, 22043, 21527, 22475, 20080, 40614, 21334, 36808, 33033, 30610, 39314, 34542, 28385, 34067, 26364, 24930, 28459, 35881, 33426, 33579, 30450, 27667, 24537, 33725, 29483, 33541, 38170, 27611, 30683, 38086, 21359, 33538, 20882, 24125, 35980, 36152, 20040, 29611, 26522, 26757, 37238, 38665, 29028, 27809, 30473, 23186, 38209, 27599, 32654, 26151, 23504, 22969, 23194, 38376, 38391, 20204, 33804, 33945, 27308, 30431, 38192, 29467, 26790, 23391, 30511, 37274, 38753, 31964, 36855, 35868, 24357, 31859, 31192, 35269, 27852, 34588, 23494, 24130, 26825, 30496, 32501, 20885, 20813, 21193, 23081, 32517, 38754, 33495, 25551, 30596, 34256, 31186, 28218, 24217, 22937, 34065, 28781, 27665, 25279, 30399, 25935, 24751, 38397, 26126, 34719, 40483, 38125, 21517, 21629, 35884, 25720, 25721, 34321, 27169, 33180, 30952, 25705, 39764, 25273, 26411, 33707, 22696, 40664, 27819, 28448, 23518, 38476, 35851, 29279, 26576, 25287, 29281, 20137, 22982, 27597, 22675, 26286, 24149, 21215, 24917, 26408, 30446, 30566, 29287, 31302, 25343, 21738, 21584, 38048, 37027, 23068, 32435, 27670, 20035, 22902, 32784, 22856, 21335, 30007, 38590, 22218, 25376, 33041, 24700, 38393, 28118, 21602, 39297, 20869, 23273, 33021, 22958, 38675, 20522, 27877, 23612, 25311, 20320, 21311, 33147, 36870, 28346, 34091, 25288, 24180, 30910, 25781, 25467, 24565, 23064, 37247, 40479, 23615, 25423, 32834, 23421, 21870, 38218, 38221, 28037, 24744, 26592, 29406, 20957, 23425, 25319, 27870, 29275, 25197, 38062, 32445, 33043, 27987, 20892, 24324, 22900, 21162, 24594, 22899, 26262, 34384, 30111, 25386, 25062, 31983, 35834, 21734, 27431, 40485, 27572, 34261, 21589, 20598, 27812, 21866, 36276, 29228, 24085, 24597, 29750, 25293, 25490, 29260, 24472, 28227, 27966, 25856, 28504, 30424, 30928, 30460, 30036, 21028, 21467, 20051, 24222, 26049, 32810, 32982, 25243, 21638, 21032, 28846, 34957, 36305, 27873, 21624, 32986, 22521, 35060, 36180, 38506, 37197, 20329, 27803, 21943, 30406, 30768, 25256, 28921, 28558, 24429, 34028, 26842, 30844, 31735, 33192, 26379, 40527, 25447, 30896, 22383, 30738, 38713, 25209, 25259, 21128, 29749, 27607, 21860, 33086, 30130, 30382, 21305, 30174, 20731, 23617, 35692, 31687, 20559, 29255, 39575, 39128, 28418, 29922, 31080, 25735, 30629, 25340, 39057, 36139, 21697, 32856, 20050, 22378, 33529, 33805, 24179, 20973, 29942, 35780, 23631, 22369, 27900, 39047, 23110, 30772, 39748, 36843, 31893, 21078, 25169, 38138, 20166, 33670, 33889, 33769, 33970, 22484, 26420, 22275, 26222, 28006, 35889, 26333, 28689, 26399, 27450, 26646, 25114, 22971, 19971, 20932, 28422, 26578, 27791, 20854, 26827, 22855, 27495, 30054, 23822, 33040, 40784, 26071, 31048, 31041, 39569, 36215, 23682, 20062, 20225, 21551, 22865, 30732, 22120, 27668, 36804, 24323, 27773, 27875, 35755, 25488, 27965, 29301, 25190, 38030, 38085, 21315, 36801, 31614, 20191, 35878, 20094, 40660, 38065, 38067, 21069, 28508, 36963, 27973, 35892, 22545, 23884, 27424, 27465, 26538, 21595, 33108, 32652, 22681, 34103, 24378, 25250, 27207, 38201, 25970, 24708, 26725, 30631, 20052, 20392, 24039, 38808, 25772, 32728, 23789, 20431, 31373, 20999, 33540, 19988, 24623, 31363, 38054, 20405, 20146, 31206, 29748, 21220, 33465, 25810, 31165, 23517, 27777, 38738, 36731, 27682, 20542, 21375, 28165, 25806, 26228, 27696, 24773, 39031, 35831, 24198, 29756, 31351, 31179, 19992, 37041, 29699, 27714, 22234, 37195, 27845, 36235, 21306, 34502, 26354, 36527, 23624, 39537, 28192, 21462, 23094, 40843, 36259, 21435, 22280, 39079, 26435, 37275, 27849, 20840, 30154, 25331, 29356, 21048, 21149, 32570, 28820, 30264, 21364, 40522, 27063, 30830, 38592, 35033, 32676, 28982, 29123, 20873, 26579, 29924, 22756, 25880, 22199, 35753, 39286, 25200, 32469, 24825, 28909, 22764, 20161, 20154, 24525, 38887, 20219, 35748, 20995, 22922, 32427, 25172, 20173, 26085, 25102, 33592, 33993, 33635, 34701, 29076, 28342, 23481, 32466, 20887, 25545, 26580, 32905, 33593, 34837, 20754, 23418, 22914, 36785, 20083, 27741, 20837, 35109, 36719, 38446, 34122, 29790, 38160, 38384, 28070, 33509, 24369, 25746, 27922, 33832, 33134, 40131, 22622, 36187, 19977, 21441, 20254, 25955, 26705, 21971, 20007, 25620, 39578, 25195, 23234, 29791, 33394, 28073, 26862, 20711, 33678, 30722, 26432, 21049, 27801, 32433, 20667, 21861, 29022, 31579, 26194, 29642, 33515, 26441, 23665, 21024, 29053, 34923, 38378, 38485, 25797, 36193, 33203, 21892, 27733, 25159, 32558, 22674, 20260, 21830, 36175, 26188, 19978, 23578, 35059, 26786, 25422, 31245, 28903, 33421, 21242, 38902, 23569, 21736, 37045, 32461, 22882, 36170, 34503, 33292, 33293, 36198, 25668, 23556, 24913, 28041, 31038, 35774, 30775, 30003, 21627, 20280, 36523, 28145, 23072, 32453, 31070, 27784, 23457, 23158, 29978, 32958, 24910, 28183, 22768, 29983, 29989, 29298, 21319, 32499, 30465, 30427, 21097, 32988, 22307, 24072, 22833, 29422, 26045, 28287, 35799, 23608, 34417, 21313, 30707, 25342, 26102, 20160, 39135, 34432, 23454, 35782, 21490, 30690, 20351, 23630, 39542, 22987, 24335, 31034, 22763, 19990, 26623, 20107, 25325, 35475, 36893, 21183, 26159, 21980, 22124, 36866, 20181, 20365, 37322, 39280, 27663, 24066, 24643, 23460, 35270, 35797, 25910, 25163, 39318, 23432, 23551, 25480, 21806, 21463, 30246, 20861, 34092, 26530, 26803, 27530, 25234, 36755, 21460, 33298, 28113, 30095, 20070, 36174, 23408, 29087, 34223, 26257, 26329, 32626, 34560, 40653, 40736, 23646, 26415, 36848, 26641, 26463, 25101, 31446, 22661, 24246, 25968, 28465, 24661, 21047, 32781, 25684, 34928, 29993, 24069, 26643, 25332, 38684, 21452, 29245, 35841, 27700, 30561, 31246, 21550, 30636, 39034, 33308, 35828, 30805, 26388, 28865, 26031, 25749, 22070, 24605, 31169, 21496, 19997, 27515, 32902, 23546, 21987, 22235, 20282, 20284, 39282, 24051, 26494, 32824, 24578, 39042, 36865, 23435, 35772, 35829, 25628, 33368, 25822, 22013, 33487, 37221, 20439, 32032, 36895, 31903, 20723, 22609, 28335, 23487, 35785, 32899, 37240, 33948, 31639, 34429, 38539, 38543, 32485, 39635, 30862, 23681, 31319, 36930, 38567, 31071, 23385, 25439, 31499, 34001, 26797, 21766, 32553, 29712, 32034, 38145, 25152, 22604, 20182, 23427, 22905, 22612, 29549, 25374, 36427, 36367, 32974, 33492, 25260, 21488, 27888, 37214, 22826, 24577, 27760, 22349, 25674, 36138, 30251, 28393, 22363, 27264, 30192, 28525, 35885, 35848, 22374, 27631, 34962, 30899, 25506, 21497, 28845, 27748, 22616, 25642, 22530, 26848, 33179, 21776, 31958, 20504, 36538, 28108, 36255, 28907, 25487, 28059, 28372, 32486, 33796, 26691, 36867, 28120, 38518, 35752, 22871, 29305, 34276, 33150, 30140, 35466, 26799, 21076, 36386, 38161, 25552, 39064, 36420, 21884, 20307, 26367, 22159, 24789, 28053, 21059, 23625, 22825, 28155, 22635, 30000, 29980, 24684, 33300, 33094, 25361, 26465, 36834, 30522, 36339, 36148, 38081, 24086, 21381, 21548, 28867, 27712, 24311, 20572, 20141, 24237, 33351, 36890, 26704, 37230, 30643, 21516, 38108, 24420, 31461, 26742, 25413, 31570, 32479, 30171, 20599, 25237, 22836, 36879, 20984, 31171, 31361, 22270, 24466, 36884, 28034, 23648, 22303, 21520, 20820, 28237, 22242, 25512, 39059, 33151, 34581, 35114, 36864, 21534, 23663, 33216, 25302, 25176, 33073, 40501, 38464, 39534, 39548, 26925, 22949, 25299, 21822, 25366, 21703, 34521, 27964, 23043, 29926, 34972, 27498, 22806, 35916, 24367, 28286, 29609, 39037, 20024, 28919, 23436, 30871, 25405, 26202, 30358, 24779, 23451, 23113, 19975, 33109, 27754, 29579, 20129, 26505, 32593, 24448, 26106, 26395, 24536, 22916, 23041, 24013, 24494, 21361, 38886, 36829, 26693, 22260, 21807, 24799, 20026, 28493, 32500, 33479, 33806, 22996, 20255, 20266, 23614, 32428, 26410, 34074, 21619, 30031, 32963, 21890, 39759, 20301, 28205, 35859, 23561, 24944, 21355, 30239, 28201, 34442, 25991, 38395, 32441, 21563, 31283, 32010, 38382, 21985, 32705, 29934, 25373, 34583, 28065, 31389, 25105, 26017, 21351, 25569, 27779, 24043, 21596, 38056, 20044, 27745, 35820, 23627, 26080, 33436, 26791, 21566, 21556, 27595, 27494, 20116, 25410, 21320, 33310, 20237, 20398, 22366, 25098, 38654, 26212, 29289, 21247, 21153, 24735, 35823, 26132, 29081, 26512, 35199, 30802, 30717, 26224, 22075, 21560, 38177, 29306, 31232, 24687, 24076, 24713, 33181, 22805, 24796, 29060, 28911, 28330, 27728, 29312, 27268, 34989, 24109, 20064, 23219, 21916, 38115, 27927, 31995, 38553, 25103, 32454, 30606, 34430, 21283, 38686, 36758, 26247, 23777, 20384, 29421, 19979, 21414, 22799, 21523, 25472, 38184, 20808, 20185, 40092, 32420, 21688, 36132, 34900, 33335, 38386, 28046, 24358, 23244, 26174, 38505, 29616, 29486, 21439, 33146, 39301, 32673, 23466, 38519, 38480, 32447, 30456, 21410, 38262, 39321, 31665, 35140, 28248, 20065, 32724, 31077, 35814, 24819, 21709, 20139, 39033, 24055, 27233, 20687, 21521, 35937, 33831, 30813, 38660, 21066, 21742, 22179, 38144, 28040, 23477, 28102, 26195, 23567, 23389, 26657, 32918, 21880, 31505, 25928, 26964, 20123, 27463, 34638, 38795, 21327, 25375, 25658, 37034, 26012, 32961, 35856, 20889, 26800, 21368, 34809, 25032, 27844, 27899, 35874, 23633, 34218, 33455, 38156, 27427, 36763, 26032, 24571, 24515, 20449, 34885, 26143, 33125, 29481, 24826, 20852, 21009, 22411, 24418, 37026, 34892, 37266, 24184, 26447, 24615, 22995, 20804, 20982, 33016, 21256, 27769, 38596, 29066, 20241, 20462, 32670, 26429, 21957, 38152, 31168, 34966, 32483, 22687, 25100, 38656, 34394, 22040, 39035, 24464, 35768, 33988, 37207, 21465, 26093, 24207, 30044, 24676, 32110, 23167, 32490, 32493, 36713, 21927, 23459, 24748, 26059, 29572, 36873, 30307, 30505, 32474, 38772, 34203, 23398, 31348, 38634, 34880, 21195, 29071, 24490, 26092, 35810, 23547, 39535, 24033, 27529, 27739, 35757, 35759, 36874, 36805, 21387, 25276, 40486, 40493, 21568, 20011, 33469, 29273, 34460, 23830, 34905, 28079, 38597, 21713, 20122, 35766, 28937, 21693, 38409, 28895, 28153, 30416, 20005, 30740, 34578, 23721, 24310, 35328, 39068, 38414, 28814, 27839, 22852, 25513, 30524, 34893, 28436, 33395, 22576, 29141, 21388, 30746, 38593, 21761, 24422, 28976, 23476, 35866, 39564, 27523, 22830, 40495, 31207, 26472, 25196, 20335, 30113, 32650, 27915, 38451, 27687, 20208, 30162, 20859, 26679, 28478, 36992, 33136, 22934, 29814, 25671, 23591, 36965, 31377, 35875, 23002, 21676, 33280, 33647, 35201, 32768, 26928, 22094, 32822, 29239, 37326, 20918, 20063, 39029, 25494, 19994, 21494, 26355, 33099, 22812, 28082, 19968, 22777, 21307, 25558, 38129, 20381, 20234, 34915, 39056, 22839, 36951, 31227, 20202, 33008, 30097, 27778, 23452, 23016, 24413, 26885, 34433, 20506, 24050, 20057, 30691, 20197, 33402, 25233, 26131, 37009, 23673, 20159, 24441, 33222, 36920, 32900, 30123, 20134, 35028, 24847, 27589, 24518, 20041, 30410, 28322, 35811, 35758, 35850, 35793, 24322, 32764, 32716, 32462, 33589, 33643, 22240, 27575, 38899, 38452, 23035, 21535, 38134, 28139, 23493, 39278, 23609, 24341, 38544, 21360, 33521, 27185, 23156, 40560, 24212, 32552, 33721, 33828, 33829, 33639, 34631, 36814, 36194, 30408, 24433, 39062, 30828, 26144, 21727, 25317, 20323, 33219, 30152, 24248, 38605, 36362, 34553, 21647, 27891, 28044, 27704, 24703, 21191, 29992, 24189, 20248, 24736, 24551, 23588, 30001, 37038, 38080, 29369, 27833, 28216, 37193, 26377, 21451, 21491, 20305, 37321, 35825, 21448, 24188, 36802, 28132, 20110, 30402, 27014, 34398, 24858, 33286, 20313, 20446, 36926, 40060, 24841, 28189, 28180, 38533, 20104, 23089, 38632, 19982, 23679, 31161, 23431, 35821, 32701, 29577, 22495, 33419, 37057, 21505, 36935, 21947, 23786, 24481, 24840, 27442, 29425, 32946, 35465, 28020, 23507, 35029, 39044, 35947, 39533, 40499, 28170, 20900, 20803, 22435, 34945, 21407, 25588, 36757, 22253, 21592, 22278, 29503, 28304, 32536, 36828, 33489, 24895, 24616, 38498, 26352, 32422, 36234, 36291, 38053, 23731, 31908, 26376, 24742, 38405, 32792, 20113, 37095, 21248, 38504, 20801, 36816, 34164, 37213, 26197, 38901, 23381, 21277, 30776, 26434, 26685, 21705, 28798, 23472, 36733, 20877, 22312, 21681, 25874, 26242, 36190, 36163, 33039, 33900, 36973, 31967, 20991, 34299, 26531, 26089, 28577, 34468, 36481, 22122, 36896, 30338, 28790, 29157, 36131, 25321, 21017, 27901, 36156, 24590, 22686, 24974, 26366, 36192, 25166, 21939, 28195, 26413, 36711, 38113, 38392, 30504, 26629, 27048, 21643, 20045, 28856, 35784, 25688, 25995, 23429, 31364, 20538, 23528, 30651, 27617, 35449, 31896, 27838, 30415, 26025, 36759, 23853, 23637, 34360, 26632, 21344, 25112, 31449, 28251, 32509, 27167, 31456, 24432, 28467, 24352, 25484, 28072, 26454, 19976, 24080, 36134, 20183, 32960, 30260, 38556, 25307, 26157, 25214, 27836, 36213, 29031, 32617, 20806, 32903, 21484, 36974, 25240, 21746, 34544, 36761, 32773, 38167, 34071, 36825, 27993, 29645, 26015, 30495, 29956, 30759, 33275, 36126, 38024, 20390, 26517, 30137, 35786, 38663, 25391, 38215, 38453, 33976, 25379, 30529, 24449, 29424, 20105, 24596, 25972, 25327, 27491, 25919, 24103, 30151, 37073, 35777, 33437, 26525, 25903, 21553, 34584, 30693, 32930, 33026, 27713, 20043, 32455, 32844, 30452, 26893, 27542, 25191, 20540, 20356, 22336, 25351, 27490, 36286, 21482, 26088, 32440, 24535, 25370, 25527, 33267, 33268, 32622, 24092, 23769, 21046, 26234, 31209, 31258, 36136, 28825, 30164, 28382, 27835, 31378, 20013, 30405, 24544, 38047, 34935, 32456, 31181, 32959, 37325, 20210, 20247, 33311, 21608, 24030, 27954, 35788, 31909, 36724, 32920, 24090, 21650, 30385, 23449, 26172, 39588, 29664, 26666, 34523, 26417, 29482, 35832, 35803, 36880, 31481, 28891, 29038, 25284, 30633, 22065, 20027, 33879, 26609, 21161, 34496, 36142, 38136, 31569, 20303, 27880, 31069, 39547, 25235, 29226, 25341, 19987, 30742, 36716, 25776, 36186, 31686, 26729, 24196, 35013, 22918, 25758, 22766, 29366, 26894, 38181, 36861, 36184, 22368, 32512, 35846, 20934, 25417, 25305, 21331, 26700, 29730, 33537, 37196, 21828, 30528, 28796, 27978, 20857, 21672, 36164, 23039, 28363, 28100, 23388, 32043, 20180, 31869, 28371, 23376, 33258, 28173, 23383, 39683, 26837, 36394, 23447, 32508, 24635, 32437, 37049, 36208, 22863, 25549, 31199, 36275, 21330, 26063, 31062, 35781, 38459, 32452, 38075, 32386, 22068, 37257, 26368, 32618, 23562, 36981, 26152, 24038, 20304, 26590, 20570, 20316, 22352, 24231]

class ExptPng():
    def __init__(self, path):
        self.face = freetype.Face(path)

    def get_im_prop(self, char):
        """
        :param char: <unicode>
        :return:
        """
        self.face.set_char_size(38*38)
        self.face.load_char(char)
        bitmap = self.face.glyph.bitmap
        height = bitmap.width
        width = int(len(bitmap.buffer)/height)
        bitmap_np = np.array(bitmap.buffer)
        bitmap_np = bitmap_np.reshape(width, height)
        return [bitmap_np, width, height]
    
    def bm2im(self, bitmap_np, width, height, offset):
        """
        :param bitmap_np: <np.array>
        :param size: (width, height) <tuple>
        :return:
        """
        # print('size:({}, {})'.format(width, height))
        im = Image.new('L', (28, 28))
        off = int(offset/2)
        for x in range(off, width+off):
            for y in range(off, height+off):
                value = bitmap_np[x-off, y-off]
                im.putpixel(xy=(x, y), value=(value,))
        im = im.rotate(-90)
        im = im.transpose(Image.FLIP_LEFT_RIGHT)
        return im
    
    def main(self):
        index = 0
        items = sorted([x for x in self.face.get_chars() if int(x[0]) > 0], key=lambda x: x[1])
        for char_code, _ in items[1:]:
            char = chr(char_code)
            # print(char)
            args = self.get_im_prop(char)
            im = self.bm2im(*args, offset=4)
            im.save('tyc_chars/{}_{}.png'.format(char_code, index))
            index += 1
        print('done')


if __name__ == '__main__':
    path = './woff/tyc-num.woff'
    ExptPng(path).main()

