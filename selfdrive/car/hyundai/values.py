# flake8: noqa

from cereal import car
from selfdrive.car import dbc_dict
from common.params import Params
Ecu = car.CarParams.Ecu

# Steer torque limits
class SteerLimitParams:
  params = Params()
  STEER_MAX = int(params.get('SteerMaxAdj'))   # 409 is the max, 255 is stock
  STEER_DELTA_UP = int(params.get('SteerDeltaUpAdj'))
  STEER_DELTA_DOWN = int(params.get('SteerDeltaDownAdj'))
  STEER_DRIVER_ALLOWANCE = 50
  STEER_DRIVER_MULTIPLIER = 2
  STEER_DRIVER_FACTOR = 1

class CAR:
  # genesis
  GENESIS = "GENESIS 2015-2016"
  GENESIS_G70 = "GENESIS G70 2018"
  GENESIS_G80 = "GENESIS G80 2017"
  GENESIS_G90 = "GENESIS G90 2017"
  # hyundai
  ELANTRA = "HYUNDAI ELANTRA LIMITED ULTIMATE 2017"
  ELANTRA_GT_I30 = "HYUNDAI I30 N LINE 2019 & GT 2018 DCT"
  SONATA = "HYUNDAI SONATA 2020"
  SONATA_HEV = "HYUNDAI SONATA HEV 2020"
  SONATA19 = "HYUNDAI SONATA 2019"
  SONATA19_HEV = "HYUNDAI SONATA 2019 HEV"
  KONA = "HYUNDAI KONA 2019"
  KONA_EV = "HYUNDAI KONA EV 2019"
  KONA_HEV = "HYUNDAI KONA HEV 2019"
  IONIQ_EV = "HYUNDAI IONIQ ELECTRIC LIMITED 2019"
  IONIQ_HEV = "HYUNDAI IONIQ HYBRID PREMIUM 2017"
  SANTA_FE = "HYUNDAI SANTA FE LIMITED 2019"
  PALISADE = "HYUNDAI PALISADE 2020"
  VELOSTER = "HYUNDAI VELOSTER 2019"
  GRANDEUR = "GRANDEUR IG 2017"
  GRANDEUR_HEV = "GRANDEUR IG HEV 2019"
  NEXO = "HYUNDAI NEXO"
  # kia
  FORTE = "KIA FORTE E 2018"
  OPTIMA = "KIA OPTIMA SX 2019 & 2016"
  OPTIMA_HEV = "KIA OPTIMA HYBRID 2017 & SPORTS 2019"
  SPORTAGE = "KIA SPORTAGE S 2020"
  SORENTO = "KIA SORENTO GT LINE 2018"
  STINGER = "KIA STINGER GT2 2018"
  NIRO_EV = "KIA NIRO EV 2020 PLATINUM"
  NIRO_HEV = "KIA NIRO HEV 2018"
  CEED = "KIA CEED 2019"
  CADENZA = "KIA K7 2016-2019"
  CADENZA_HEV = "KIA K7 HEV 2016-2019"

class Buttons:
  NONE = 0
  RES_ACCEL = 1
  SET_DECEL = 2
  GAP_DIST = 3
  CANCEL = 4

params = Params()
fingerprint_issued_fix = int(params.get("FingerprintIssuedFix", encoding='utf8')) == 1
fingerprint_two = int(params.get("FingerprintTwoSet", encoding='utf8')) == 1

if fingerprint_issued_fix: # 핑거인식문제 혹은 다른차량과 핑거프린트 충돌이 나는경우 여기다가 핑거를 넣으시고 개발자 메뉴에서 핑거프린트 이슈차량 전용을 켜면 적용됩니다.
  FINGERPRINTS = {
    # genesis
    CAR.GENESIS: [{}],
    CAR.GENESIS_G70: [{}],
    CAR.GENESIS_G80: [{}],
    CAR.GENESIS_G90: [{}],
    # hyundai
    CAR.ELANTRA: [{}],
    CAR.ELANTRA_GT_I30: [{}],
    CAR.SONATA: [{}],
    CAR.SONATA_HEV: [{}],
    CAR.SONATA19: [{}],
    CAR.SONATA19_HEV: [{}],
    CAR.KONA: [{}],
    CAR.KONA_EV: [{}],
    CAR.KONA_HEV: [{}],
    CAR.IONIQ_HEV: [{}],
    CAR.IONIQ_EV: [{}],
    CAR.SANTA_FE: [{}],
    CAR.PALISADE: [{}],
    CAR.VELOSTER: [{}], 
    CAR.GRANDEUR: [{}],
    CAR.GRANDEUR_HEV: [{}],
    CAR.NEXO: [{}],
    # kia
    CAR.FORTE: [{}],
    CAR.OPTIMA: [{}],
    CAR.OPTIMA_HEV: [{}],
    CAR.SPORTAGE: [{}],
    CAR.SORENTO: [{}],
    CAR.STINGER: [{}],
    CAR.NIRO_EV: [{}],
    CAR.NIRO_HEV: [{}], 
    CAR.CEED: [{}],
    CAR.CADENZA: [{}],  
    CAR.CADENZA_HEV: [{}]
  }
else: # 핑거 프린트 이슈 없는 차량은 이곳에 넣으세요.
  FINGERPRINTS = {
    # genesis
    CAR.GENESIS: [{}],
    CAR.GENESIS_G70: [{}],
    CAR.GENESIS_G80: [{}],
    CAR.GENESIS_G90: [{}],
    # hyundai
    CAR.ELANTRA: [{}],
    CAR.ELANTRA_GT_I30: [{}],
    CAR.SONATA: [{}],
    CAR.SONATA_HEV: [{}],
    CAR.SONATA19: [{}],
    CAR.SONATA19_HEV: [{}],
    CAR.KONA: [{}],
    CAR.KONA_EV: [{}],
    CAR.KONA_HEV: [{}],
    CAR.IONIQ_HEV: [{
      68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 544: 8, 576: 8, 593: 8, 688: 5, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 6, 1173: 8, 1225: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1322: 8, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1407: 8, 1419: 8, 1427: 6, 1429: 8, 1430: 8, 1448: 8, 1456: 4, 1470:8, 1476: 8, 1535: 8
      },{
      68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 544: 8, 576:8, 593: 8, 688: 5, 832: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 6, 1173: 8, 1225: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1407: 8, 1427: 6, 1429: 8, 1430: 8, 1448: 8, 1456: 4, 1470: 8, 1476: 8, 1535: 8
      },{
      68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 544: 8, 576: 8, 832: 8, 881: 8, 882: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 6, 1173: 8, 1225: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1407: 8, 1427: 6, 1429: 8, 1430: 8, 1448: 8, 1456: 4, 1470: 8, 1476: 8, 1535: 8
    }],
    CAR.IONIQ_EV: [{}],
    CAR.SANTA_FE: [{}],
    CAR.PALISADE: [{}],
    CAR.VELOSTER: [{}],
    CAR.GRANDEUR: [{}],
    CAR.GRANDEUR_HEV: [{}],
    CAR.NEXO: [{}],
    # kia
    CAR.FORTE: [{}],
    CAR.OPTIMA: [{}],
    CAR.OPTIMA_HEV: [{}],
    CAR.SPORTAGE: [{}],
    CAR.SORENTO: [{}],
    CAR.STINGER: [{}],
    CAR.NIRO_EV: [{}],
    CAR.NIRO_HEV: [{}],
    CAR.CEED: [{}],
    CAR.CADENZA: [{}],  
    CAR.CADENZA_HEV: [{}]
  }

# Don't use these fingerprints for fingerprinting, they are still used for ECU detection
IGNORED_FINGERPRINTS = [CAR.VELOSTER, CAR.GENESIS_G70, CAR.KONA]

if fingerprint_two:
  FW_VERSIONS = {  #핑거프린트2.0부분, 차량 미인식으로 대시캠모드로 동작시 개발자메뉴에서 핑거프린트2.0 활성화 옵션을 끄고 위쪽 핑거프린트1.0에 본인차량 핑거프린트가 들어가 있는지 확인해보세요.
    # genesis
    CAR.GENESIS_G70: {
      (Ecu.fwdRadar, 0x7d0, None): [b'\xf1\x00IK__ SCC F-CUP      1.00 1.02 96400-G9100         \xf1\xa01.02',],
      (Ecu.esp, 0x7d1, None): [b'\xf1\x00\x00\x00\x00\x00\x00\x00',],
      (Ecu.engine, 0x7e0, None): [b'\xf1\x81640F0051\x00\x00\x00\x00\x00\x00\x00\x00',],
      (Ecu.eps, 0x7d4, None): [b'\xf1\x00IK  MDPS R 1.00 1.06 57700-G9420 4I4VL106',],
      (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\x00IK  MFC  AT USA LHD 1.00 1.01 95740-G9000 170920',],
      (Ecu.transmission, 0x7e1, None): [b'\xf1\x87VDJLT17895112DN4\x88fVf\x99\x88\x88\x88\x87fVe\x88vhwwUFU\x97eFex\x99\xff\xb7\x82\xf1\x81E25\x00\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  E25\x00\x00\x00\x00\x00\x00\x00SIK0T33NB2\x11\x1am\xda',],
    },
    # hyundai
    CAR.ELANTRA_GT_I30: {
      (Ecu.fwdRadar, 0x7d0, None): [b'\xf1\x00PD__ SCC F-CUP      1.00 1.01 99110-G3100         ',],
      (Ecu.esp, 0x7d1, None): [b'\xf1\x00PD ESC \x11 100 \a\x03 58910-G3AC0',],
      (Ecu.engine, 0x7e0, None): [b'\x01TPD-1A506F000H00',],
      (Ecu.eps, 0x7d4, None): [b'\xf1\x00PDu MDPS C 1.00 1.01 56310/G3690 4PDUC101',],
      (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\x00PDP LKAS AT AUS RHD 1.00 1.01 99211-G4000 v60',],
      (Ecu.transmission, 0x7e1, None): [b'\xf1\x816U2VA051\x00\x00\xf1\x006U2V0_C2\x00\x006U2VA051\x00\x00DPD0H16US0\x00\x00\x00\x00',],
    },
    CAR.SONATA: {
      (Ecu.fwdRadar, 0x7d0, None): [
        b'\xf1\x00DN8_ SCC FHCUP      1.00 1.01 99110-L1000         ',
        b'\xf1\x00DN8_ SCC FHCUP      1.00 1.00 99110-L0000         ',
        b'\xf1\x00DN8_ SCC F-CU-      1.00 1.00 99110-L0000         ',
      ],
      (Ecu.esp, 0x7d1, None): [
        b'\xf1\x00DN ESC \x01 102\x19\x04\x13 58910-L1300\xf1\xa01.02',
        b'\xf1\x8758910-L0100\xf1\x00DN ESC \x06 104\x19\x08\x01 58910-L0100\xf1\xa01.04',
      ],
      (Ecu.engine, 0x7e0, None): [
        b'HM6M2_0a0_BD0',
        b'\xf1\x87391162M003\xf1\xa0000F',
        b'\xf1\x87391162M003\xf1\xa00240',
      ],
      (Ecu.eps, 0x7d4, None): [
        b'\xf1\x8756310-L1010\xf1\x00DN8 MDPS C 1.00 1.03 56310-L1010 4DNDC103\xf1\xa01.03',
        b'\xf1\x8756310L0010\x00\xf1\x00DN8 MDPS C 1.00 1.01 56310L0010\x00 4DNAC101\xf1\xa01.01',
        b'\xf1\x8756310-L0010\xf1\x00DN8 MDPS C 1.00 1.01 56310-L0010 4DNAC101\xf1\xa01.01',
      ],
      (Ecu.fwdCamera, 0x7c4, None): [
        b'\xf1\x00DN8 MFC  AT KOR LHD 1.00 1.02 99211-L1000 190422',
        b'\xf1\x00DN8 MFC  AT USA LHD 1.00 1.00 99211-L0000 190716',
        b'\xf1\x00DN8 MFC  AT USA LHD 1.00 1.01 99211-L0000 191016',
      ],
      (Ecu.transmission, 0x7e1, None): [
        b'\xf1\x00HT6TA260BLHT6TA800A1TDN8C20KS4\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00',
        b'\xf1\x00bcsh8p54  U903\x00\x00\x00\x00\x00\x00SDN8T16NB0z{\xd4v',
      ],
    },
    CAR.SONATA_HEV: {
      (Ecu.fwdRadar, 0x7d0, None): [b'\xf1\x00DNhe SCC FHCUP      1.00 1.02 99110-L5000         ',],
      (Ecu.esp, 0x7d1, None): [b'\xf1\x8758910-L0100\xf1\x00DN ESC \x06 104\x19\x08\x01 58910-L0100\xf1\xa01.04',],
      (Ecu.engine, 0x7e0, None): [b'\xf1\x87391062J002\xf1\xa0000P',],
      (Ecu.eps, 0x7d4, None): [b'\xf1\x8756310-L5500\xf1\x00DN8 MDPS C 1.00 1.02 56310-L5500 4DNHC102\xf1\xa01.02',],
      (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\x00DN8HMFC  AT USA LHD 1.00 1.04 99211-L1000 191016',],
      (Ecu.transmission, 0x7e1, None): [b'\xf1\x00PSBG2323  E09\x00\x00\x00\x00\x00\x00\x00TDN2H20SA5\x97R\x88\x9e',],
    },
    CAR.KONA: {
      (Ecu.fwdRadar, 0x7d0, None): [b'\xf1\x00OS__ SCC F-CUP      1.00 1.00 95655-J9200         \xf1\xa01.00',],
      (Ecu.esp, 0x7d1, None): [b'\xf1\x816V5RAK00018.ELF\xf1\x00\x00\x00\x00\x00\x00\x00\xf1\xa01.05',],
      (Ecu.engine, 0x7e0, None): [b'"\x01TOS-0NU06F301J02',],
      (Ecu.eps, 0x7d4, None): [b'\xf1\x00OS  MDPS C 1.00 1.05 56310J9030\x00 4OSDC105',],
      (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\x00OS9 LKAS AT USA LHD 1.00 1.00 95740-J9300 g21',],
      (Ecu.transmission, 0x7e1, None): [b'\xf1\x816U2VE051\x00\x00\xf1\x006U2V0_C2\x00\x006U2VE051\x00\x00DOS4T16NS3\x00\x00\x00\x00',],
    },
    CAR.KONA_EV: {
      (Ecu.fwdRadar, 0x7D0, None): [b'\xf1\x00OSev SCC FNCUP      1.00 1.01 99110-K4000        \xf1\xa01.01',],
      (Ecu.esp, 0x7D1, None): [b'\xf1\xa02.06',],
      (Ecu.eps, 0x7D4, None): [
        b'\xf1\x00OS  MDPS C 1.00 1.04 56310K4000\x00 4OEDC104',
        b'\xf1\x00OS  MDPS C 1.00 1.04 56310K4050\x00 4OEDC104',
      ],
      (Ecu.fwdCamera, 0x7C4, None): [b'\xf1\x00OSE LKAS AT KOR LHD 1.00 1.00 95740-K4100 W40',],
    },
    CAR.IONIQ_HEV: {
      (Ecu.fwdRadar, 0x7d0, None): [
        b'\xf1\x00AEhe SCC F-CUP      1.00 1.00 99110-G2200         ',
        b'\xf1\x00AEhe SCC H-CUP      1.01 1.01 96400-G2000         ',
      ],
      (Ecu.engine, 0x7e0, None): [
        b'\xf1\x816H6F6051\x00\x00\x00\x00\x00\x00\x00\x00',
        b'\xf1\x816H6F2051\x00\x00\x00\x00\x00\x00\x00\x00',
      ],
      (Ecu.eps, 0x7D4, None): [
        b'\xf1\x00AE  MDPS C 1.00 1.07 56310/G2301 4AEHC107',
        b'\xf1\x00AE  MDPS C 1.00 1.01 56310/G2310 4APHC101',
      ],
      (Ecu.fwdCamera, 0x7c4, None): [
        b'\xf1\x00AEH MFC  AT EUR LHD 1.00 1.01 95740-G2600 190819',
        b'\xf1\x00AEH MFC  AT EUR LHD 1.00 1.00 95740-G2400 180222',
      ],
      (Ecu.transmission, 0x7e1, None): [
        b'\xf1\x816U3J8051\x00\x00\xf1\x006U3H1_C2\x00\x006U3J8051\x00\x00HAE0G16UL0Nd\xed:',
        b'\xf1\x816U3H1051\x00\x00\xf1\x006U3H0_C2\x00\x006U3H1051\x00\x00HAE0G16US2\x95\xa2^$',
      ],
    },
    CAR.SANTA_FE: {
      (Ecu.fwdRadar, 0x7d0, None): [b'\xf1\x00TM__ SCC F-CUP      1.00 1.02 99110-S2000         \xf1\xa01.02',],
      (Ecu.esp, 0x7d1, None): [b'\xf1\x00TM ESC \x02 100\x18\x030 58910-S2600\xf1\xa01.00',],
      (Ecu.engine, 0x7e0, None): [b'\xf1\x81606EA051\x00\x00\x00\x00\x00\x00\x00\x00',],
      (Ecu.eps, 0x7d4, None): [b'\xf1\x00TM  MDPS C 1.00 1.00 56340-S2000 8409',],
      (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\x00TM  MFC  AT USA LHD 1.00 1.00 99211-S2000 180409',],
      (Ecu.transmission, 0x7e1, None): [b'\xf1\x87SBJWAA6562474GG0ffvgeTeFx\x88\x97\x88ww\x87www\x87w\x84o\xfa\xff\x87fO\xff\xc2 \xf1\x816W3C2051\x00\x00\xf1\x006W351_C2\x00\x006W3C2051\x00\x00TTM2G24NS1\x00\x00\x00\x00',],
    },
    CAR.PALISADE: {
      (Ecu.fwdRadar, 0x7d0, None): [
        b'\xf1\x00LX2_ SCC FHCUP      1.00 1.04 99110-S8100         \xf1\xa01.04',
        b'\xf1\x00LX2  SCC FHCUP      1.00 1.04 99110-S8100         \xf1\xa01.04',
        b'\xf1\x00LX2_ SCC FHCUP      1.00 1.04 99110-S8100         \xf1\xa01.04',
      ],
      (Ecu.esp, 0x7d1, None): [
        b'\xf1\x00LX ESC \v 102\x19\x05\a 58910-S8330\xf1\xa01.02',
        b'\xf1\x00LX ESC \v 103\x19\t\x10 58910-S8360\xf1\xa01.03',
        b'\xf1\x00LX ESC \x01 103\x19\t\x10 58910-S8360\xf1\xa01.03',
        b'\xf1\x00LX ESC \x0b 102\x19\x05\x07 58910-S8330',
      ],
      (Ecu.engine, 0x7e0, None): [
        b'\xf1\x81640J0051\x00\x00\x00\x00\x00\x00\x00\x00',
        b'\xf1\x81640K0051\x00\x00\x00\x00\x00\x00\x00\x00',
      ],
      (Ecu.eps, 0x7d4, None): [
        b'\xf1\x00LX2 MDPS C 1.00 1.03 56310-S8020 4LXDC103',
      ],
      (Ecu.engine, 0x7e0, None): [b'\xf1\x81640J0051\x00\x00\x00\x00\x00\x00\x00\x00',],
      (Ecu.eps, 0x7d4, None): [b'\xf1\x00LX2 MDPS C 1.00 1.03 56310-S8020 4LXDC103',],
      (Ecu.fwdCamera, 0x7c4, None): [
        b'\xf1\x00LX2 MFC  AT USA LHD 1.00 1.03 99211-S8100 190125',
        b'\xf1\x00LX2 MFC  AT USA LHD 1.00 1.05 99211-S8100 190909',
        b'\xf1\x00LX2 MFC AT USA LHD 1.00 1.05 99211-S8100 190909',
      ],
      (Ecu.transmission, 0x7e1, None): [
        b'\xf1\x87LBLUFN650868KF36\xa9\x98\x89\x88\xa8\x88\x88\x88h\x99\xa6\x89fw\x86gw\x88\x97x\xaa\x7f\xf6\xff\xbb\xbb\x8f\xff+\x82\xf1\x81U891\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  U891\x00\x00\x00\x00\x00\x00SLX2G38NB3\xd1\xc3\xf8\xa8',
        b'\xf1\x87LDKVBN424201KF26\xba\xaa\x9a\xa9\x99\x99\x89\x98\x89\x99\xa8\x99\x88\x99\x98\x89\x88\x99\xa8\x89v\x7f\xf7\xffwf_\xffq\xa6\xf1\x81U891\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  U891\x00\x00\x00\x00\x00\x00SLX4G38NB2\xafL]\xe7',
        b'\xf1\x87LDLVBN560098KF26\x86fff\x87vgfg\x88\x96xfw\x86gfw\x86g\x95\xf6\xffeU_\xff\x92c\xf1\x81U891\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  U891\x00\x00\x00\x00\x00\x00SLX4G38NB2\xafL]\xe7',
        b'\xf1\x87LDLVBN5600981KF26\x86fff\x87vgfg\x88\x96xfw\x86gfw\x86g\x95\xf6\xffeU_\xff\x92c\xf1\x81U891\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  U891\x00\x00\x00\x00\x00\x00SLX4G38NB2\xafL]\xe7',
        b'\xf1\x87LBLUFN655162KF36\x98\x88\x88\x88\x98\x88\x88\x88x\x99\xa7\x89x\x99\xa7\x89x\x99\x97\x89g\xf7\xffwU_\xff\xe9!\xf1\x81U891\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54 U891\x00\x00\x00\x00\x00\x00SLX2G38NB3\xd1\xc3\xf8\xa8',
      ],
    },
    CAR.VELOSTER: {
      (Ecu.fwdRadar, 0x7d0, None): [b'\xf1\x00JS__ SCC H-CUP      1.00 1.02 95650-J3200         ',],
      (Ecu.esp, 0x7d1, None): [b'\xf1\x00\x00\x00\x00\x00\x00\x00',],
      (Ecu.engine, 0x7e0, None): [b'\x01TJS-JNU06F200H0A',],
      (Ecu.eps, 0x7d4, None): [b'\xf1\x00JSL MDPS C 1.00 1.03 56340-J3000 8308',],
      (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\x00JS  LKAS AT USA LHD 1.00 1.02 95740-J3000 K32',],
      (Ecu.transmission, 0x7e1, None): [b'\xf1\x816U2V8051\x00\x00\xf1\x006U2V0_C2\x00\x006U2V8051\x00\x00DJS0T16NS1\xba\x02\xb8\x80',],
    },
    # kia
    CAR.OPTIMA: {
      (Ecu.fwdRadar, 0x7d0, None): [b'\xf1\x00JF__ SCC F-CUP      1.00 1.00 96400-D4110         ',],
      (Ecu.esp, 0x7d1, None): [b'\xf1\x00JF ESC \v 11 \x18\x030 58920-D5180',],
      (Ecu.engine, 0x7e0, None): [b'\x01TJFAJNU06F201H03',],
      (Ecu.eps, 0x7d4, None): [b'\xf1\x00TM  MDPS C 1.00 1.00 56340-S2000 8409',],
      (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\x00JFA LKAS AT USA LHD 1.00 1.02 95895-D5000 h31',],
      (Ecu.transmission, 0x7e1, None): [b'\xf1\x816U2V8051\x00\x00\xf1\x006U2V0_C2\x00\x006U2V8051\x00\x00DJF0T16NL0\t\xd2GW',],
    },
    CAR.OPTIMA_HEV: {
      (Ecu.fwdRadar, 0x7d0, None): [b'\xf1\x00DEhe SCC H-CUP      1.01 1.02 96400-G5100         ',],
      (Ecu.engine, 0x7e0, None): [b'\xf1\x816H6F4051\x00\x00\x00\x00\x00\x00\x00\x00',],
      (Ecu.eps, 0x7d4, None): [b'\xf1\x00DE  MDPS C 1.00 1.09 56310G5301\x00 4DEHC109',],
      (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\x00DEP MFC  AT USA LHD 1.00 1.01 95740-G5010 170424',],
      (Ecu.transmission, 0x7e1, None): [b"\xf1\x816U3J2051\x00\x00\xf1\x006U3H0_C2\x00\x006U3J2051\x00\x00PDE0G16NS2\xf4'\\\x91",],
    },
    CAR.STINGER: {
      (Ecu.fwdRadar, 0x7d0, None): [ b'\xf1\x00CK__ SCC F_CUP      1.00 1.01 96400-J5100         \xf1\xa01.01',],
      (Ecu.engine, 0x7e0, None): [ b'\xf1\x81640E0051\x00\x00\x00\x00\x00\x00\x00\x00',],
      (Ecu.eps, 0x7d4, None): [b'\xf1\x00CK  MDPS R 1.00 1.04 57700-J5420 4C4VL104',],
      (Ecu.fwdCamera, 0x7c4, None): [b'\xf1\x00CK  MFC  AT USA LHD 1.00 1.03 95740-J5000 170822',],
      (Ecu.transmission, 0x7e1, None): [
        b'\xf1\x87VDHLG17118862DK2\x8awWwgu\x96wVfUVwv\x97xWvfvUTGTx\x87o\xff\xc9\xed\xf1\x81E21\x00\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  E21\x00\x00\x00\x00\x00\x00\x00SCK0T33NB0\x88\xa2\xe6\xf0',
        b'\xf1\x87VDHLG17000192DK2xdFffT\xa5VUD$DwT\x86wveVeeD&T\x99\xba\x8f\xff\xcc\x99\xf1\x81E21\x00\x00\x00\x00\x00\x00\x00\xf1\x00bcsh8p54  E21\x00\x00\x00\x00\x00\x00\x00SCK0T33NB0\x88\xa2\xe6\xf0',
      ],
    },
    CAR.NIRO_EV: {
      (Ecu.fwdRadar, 0x7D0, None): [
        b'\xf1\x00DEev SCC F-CUP      1.00 1.03 96400-Q4100         \xf1\xa01.03',
        b'\xf1\x00DEev SCC F-CUP      1.00 1.00 99110-Q4000         \xf1\xa01.00',
      ],
      (Ecu.esp, 0x7D1, None): [
        b'\xf1\xa01.06',
        b'\xf1\xa01.07',
      ],
      (Ecu.eps, 0x7D4, None): [
        b'\xf1\x00DE  MDPS C 1.00 1.05 56310Q4000\x00 4DEEC105',
        b'\xf1\x00DE  MDPS C 1.00 1.05 56310Q4100\x00 4DEEC105',
      ],
      (Ecu.fwdCamera, 0x7C4, None): [
        b'\xf1\x00DEE MFC  AT USA LHD 1.00 1.03 95740-Q4000 180821',
        b'\xf1\x00DEE MFC  AT EUR LHD 1.00 1.00 99211-Q4000 191211',
      ],
    },
  }

CHECKSUM = {
  "crc8": [CAR.SANTA_FE, CAR.SONATA, CAR.PALISADE, CAR.SONATA_HEV],
  "6B": [CAR.SORENTO, CAR.GENESIS],
}

FEATURES = {
  # 캔오류 관련, 오류가 발생하는 경우는 본인 차종에 맞지 않는 캔신호가 들어오기때문입니다. 대부분 이곳을 수정하면 해결되나, 부득이 판다코드를 수정해야 될수도 있습니다.
  # debug 코드가 포함되어 있으면, /data/openpilot/selfdrive/debug 안에 몇가지 툴이 들어있습니다. 실행하시면 디버그에 도움이 되실겁니다. 팟팅!!! 
  # which message has the gear
  "use_cluster_gears": set([CAR.ELANTRA, CAR.KONA, CAR.ELANTRA_GT_I30, CAR.CADENZA, CAR.GRANDEUR]),
  "use_tcu_gears": set([CAR.OPTIMA, CAR.SONATA19, CAR.VELOSTER]),

  # send LFA MFA message for new HKG models
  "send_lfa_mfa": set([]),
}

ELEC_VEH = set([CAR.IONIQ_EV, CAR.KONA_EV, CAR.NIRO_EV, CAR.NEXO])

HYBRID_VEH = set([CAR.OPTIMA_HEV, CAR.IONIQ_HEV, CAR.SONATA_HEV, CAR.CADENZA_HEV, CAR.GRANDEUR_HEV, CAR.NIRO_HEV, CAR.KONA_HEV])

DBC = {
  # genesis
  CAR.GENESIS: dbc_dict('hyundai_kia_generic', None),
  CAR.GENESIS_G70: dbc_dict('hyundai_kia_generic', None),
  CAR.GENESIS_G80: dbc_dict('hyundai_kia_generic', None),
  CAR.GENESIS_G90: dbc_dict('hyundai_kia_generic', None),
  # hyundai
  CAR.ELANTRA: dbc_dict('hyundai_kia_generic', None),
  CAR.ELANTRA_GT_I30: dbc_dict('hyundai_kia_generic', None),
  CAR.SONATA: dbc_dict('hyundai_kia_generic', None),
  CAR.SONATA_HEV: dbc_dict('hyundai_kia_generic_hybrid', None),
  CAR.SONATA19: dbc_dict('hyundai_kia_generic', None),
  CAR.SONATA19_HEV: dbc_dict('hyundai_kia_generic_hybrid', None),
  CAR.KONA: dbc_dict('hyundai_kia_generic', None),
  CAR.KONA_EV: dbc_dict('hyundai_kia_generic', None),
  CAR.KONA_HEV: dbc_dict('hyundai_kia_generic_hybrid', None),
  CAR.IONIQ_EV: dbc_dict('hyundai_kia_generic', None),
  CAR.IONIQ_HEV: dbc_dict('hyundai_kia_generic_hybrid', None),
  CAR.SANTA_FE: dbc_dict('hyundai_kia_generic', None),
  CAR.PALISADE: dbc_dict('hyundai_kia_generic', None),
  CAR.VELOSTER: dbc_dict('hyundai_kia_generic', None),
  CAR.GRANDEUR: dbc_dict('hyundai_kia_generic', None),
  CAR.GRANDEUR_HEV: dbc_dict('hyundai_kia_generic_hybrid', None),
  CAR.NEXO: dbc_dict('hyundai_kia_generic', None),
  # kia
  CAR.FORTE: dbc_dict('hyundai_kia_generic', None),
  CAR.OPTIMA: dbc_dict('hyundai_kia_generic', None),
  CAR.OPTIMA_HEV: dbc_dict('hyundai_kia_generic_hybrid', None),
  CAR.SPORTAGE: dbc_dict('hyundai_kia_generic', None),
  CAR.SORENTO: dbc_dict('hyundai_kia_generic', None),
  CAR.STINGER: dbc_dict('hyundai_kia_generic', None),
  CAR.NIRO_EV: dbc_dict('hyundai_kia_generic', None),
  CAR.NIRO_HEV: dbc_dict('hyundai_kia_generic_hybrid', None),
  CAR.CEED: dbc_dict('hyundai_kia_generic', None),
  CAR.CADENZA: dbc_dict('hyundai_kia_generic', None),
  CAR.CADENZA_HEV: dbc_dict('hyundai_kia_generic_hybrid', None),
}

STEER_THRESHOLD = 150
