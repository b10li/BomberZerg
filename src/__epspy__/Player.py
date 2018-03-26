## NOTE: THIS FILE IS GENERATED BY EPSCRIPT! DO NOT MODITY
from eudplib import *

def _IGVA(vList, exprListGen):
    def _():
        exprList = exprListGen()
        SetVariables(vList, exprList)
    EUDOnStart(_)

def _CGFW(exprf, retn):
    rets = [ExprProxy(None) for _ in range(retn)]
    def _():
        vals = exprf()
        for ret, val in zip(rets, vals):
            ret._value = val
    EUDOnStart(_)
    return rets

def _ARR(items):
    k = EUDArray(len(items))
    for i, item in enumerate(items):
        k[i] = item
    return k

def _SRET(v, klist):
    return List2Assignable([v[k] for k in klist])

def _SV(dL, sL):
    [d << s for d, s in zip(FlattenList(dL), FlattenList(sL))]

class _ATTW:
    def __init__(self, obj, attrName):
        self.obj = obj
        self.attrName = attrName

    def __lshift__(self, r):
        setattr(self.obj, self.attrName, r)

    def __iadd__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov + v)

    def __isub__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov - v)

    def __imul__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov * v)

    def __idiv__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov / v)

    def __iand__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov & v)

    def __ior__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov | v)

    def __ixor__(self, v):
        ov = getattr(self.obj, self.attrName)
        setattr(self.obj, self.attrName, ov ^ v)

class _ARRW:
    def __init__(self, obj, index):
        self.obj = obj
        self.index = index

    def __lshift__(self, r):
        self.obj[self.index] = r

    def __iadd__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov + v

    def __isub__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov - v

    def __imul__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov * v

    def __idiv__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov / v

    def __iand__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov & v

    def __ior__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov | v

    def __ixor__(self, v):
        ov = self.obj[self.index]
        self.obj[self.index] = ov ^ v

def _L2V(l):
    ret = EUDVariable()
    if EUDIf()(l):
        ret << 1
    if EUDElse()():
        ret << 0
    EUDEndIf()
    return ret

def _MVAR(vs):
    return List2Assignable([
        v.makeL() if IsEUDVariable(v) else EUDVariable() << v
        for v in FlattenList(vs)])

def _LSH(l, r):
    if IsEUDVariable(l):  return f_bitlshift(l, r)
    else: return l << r

## NOTE: THIS FILE IS GENERATED BY EPSCRIPT! DO NOT MODITY

# (Line 1) import Header;
import Header
# (Line 2) import Helpers;
import Helpers
# (Line 3) import Map;
import Map
# (Line 4) import Bomb;
import Bomb
# (Line 6) const scale						= Map.scale;
scale = _CGFW(lambda: [Map.scale], 1)[0]
# (Line 8) const Computer		 			= Header.Computer;
Computer = _CGFW(lambda: [Header.Computer], 1)[0]
# (Line 9) const UnitID_Civilian 			= Header.UnitID_Player[0];
UnitID_Civilian = _CGFW(lambda: [Header.UnitID_Player[0]], 1)[0]
# (Line 10) const UnitID_Tank 				= Header.UnitID_Player[2];
UnitID_Tank = _CGFW(lambda: [Header.UnitID_Player[2]], 1)[0]
# (Line 11) const UnitID_Goliath 			= Header.UnitID_Player[1];
UnitID_Goliath = _CGFW(lambda: [Header.UnitID_Player[1]], 1)[0]
# (Line 12) const UnitID_Bomb				= Header.UnitID_Bomb;
UnitID_Bomb = _CGFW(lambda: [Header.UnitID_Bomb], 1)[0]
# (Line 13) const UnitID_Fire				= Header.UnitID_Fire;
UnitID_Fire = _CGFW(lambda: [Header.UnitID_Fire], 1)[0]
# (Line 15) const ItemList					= Header.ItemList;
ItemList = _CGFW(lambda: [Header.ItemList], 1)[0]
# (Line 16) const Item_rangeUp				= Header.Item_rangeUp;
Item_rangeUp = _CGFW(lambda: [Header.Item_rangeUp], 1)[0]
# (Line 17) const Item_speedUp				= Header.Item_speedUp;
Item_speedUp = _CGFW(lambda: [Header.Item_speedUp], 1)[0]
# (Line 18) const Item_bombNUp				= Header.Item_bombNUp;
Item_bombNUp = _CGFW(lambda: [Header.Item_bombNUp], 1)[0]
# (Line 19) const Item_rangeMax				= Header.Item_rangeMax;
Item_rangeMax = _CGFW(lambda: [Header.Item_rangeMax], 1)[0]
# (Line 20) const Item_rideTank				= Header.Item_rideTank;
Item_rideTank = _CGFW(lambda: [Header.Item_rideTank], 1)[0]
# (Line 21) const Item_rideHide				= Header.Item_rideHide;
Item_rideHide = _CGFW(lambda: [Header.Item_rideHide], 1)[0]
# (Line 23) const EPD_Players	 			= EUDArray(6);
EPD_Players = _CGFW(lambda: [EUDArray(6)], 1)[0]
# (Line 24) const MaxRange					= 5;
MaxRange = _CGFW(lambda: [5], 1)[0]
# (Line 25) const MaxBomb					= 8;
MaxBomb = _CGFW(lambda: [8], 1)[0]
# (Line 26) const PlayerSpeed				= EUDArray(6);
PlayerSpeed = _CGFW(lambda: [EUDArray(6)], 1)[0]
# (Line 28) const loc0 		= $L('loc0');
loc0 = _CGFW(lambda: [GetLocationIndex('loc0')], 1)[0]
# (Line 29) const loc 		= $L('loc');
loc = _CGFW(lambda: [GetLocationIndex('loc')], 1)[0]
# (Line 30) const loc_p1 	= $L('p1');
loc_p1 = _CGFW(lambda: [GetLocationIndex('p1')], 1)[0]
# (Line 31) const loc_p2 	= $L('p2');
loc_p2 = _CGFW(lambda: [GetLocationIndex('p2')], 1)[0]
# (Line 32) const loc_p3 	= $L('p3');
loc_p3 = _CGFW(lambda: [GetLocationIndex('p3')], 1)[0]
# (Line 33) const loc_p4 	= $L('p4');
loc_p4 = _CGFW(lambda: [GetLocationIndex('p4')], 1)[0]
# (Line 34) const loc_p5 	= $L('p5');
loc_p5 = _CGFW(lambda: [GetLocationIndex('p5')], 1)[0]
# (Line 35) const loc_p6 	= $L('p6');
loc_p6 = _CGFW(lambda: [GetLocationIndex('p6')], 1)[0]
# (Line 37) const loclist	= [loc_p1, loc_p2, loc_p3, loc_p4, loc_p5, loc_p6];
loclist = _CGFW(lambda: [_ARR(FlattenList([loc_p1, loc_p2, loc_p3, loc_p4, loc_p5, loc_p6]))], 1)[0]
# (Line 39) function SetBombWayBlock(unitEpd, bool);
# (Line 40) function IsBombWayBlocked(unitEpd);
# (Line 41) function SetRangeAtBomb(unitEpd, range);
# (Line 42) function GetRangeAtBomb(unitEpd);
# (Line 43) function SetBombTimer(unitEpd, time);
# (Line 44) function GetCurrentBN(player);
# (Line 45) function GetBombNumber(player);
# (Line 46) function GetBombRange(player);
# (Line 47) function SetBombNumber(player, number);
# (Line 48) function SetBombRange(player, number);
# (Line 49) function GetItem(player);
# (Line 52) function SetPlayerEpd(player)
# (Line 53) {
@EUDFunc
def SetPlayerEpd(player):
    # (Line 54) EPD_Players[player] = epdread_epd(EPD(0x628438));
    _ARRW(EPD_Players, player) << (f_epdread_epd(EPD(0x628438)))
    # (Line 55) }
    # (Line 57) function GetPlayerEpd(player)

# (Line 58) {
@EUDFunc
def GetPlayerEpd(player):
    # (Line 59) return EPD_Players[player];
    EUDReturn(EPD_Players[player])
    # (Line 60) }
    # (Line 62) function InitPlayerLocation(player)

# (Line 63) {
@EUDFunc
def InitPlayerLocation(player):
    # (Line 64) var x, y;
    x, y = EUDCreateVariables(2)
    # (Line 65) if(player == 0) { x=1; y=1; }
    if EUDIf()(player == 0):
        x << (1)
        y << (1)
        # (Line 66) if(player == 1) { x=18; y=1; }
    EUDEndIf()
    if EUDIf()(player == 1):
        x << (18)
        y << (1)
        # (Line 67) if(player == 2) { x=1; y=11; }
    EUDEndIf()
    if EUDIf()(player == 2):
        x << (1)
        y << (11)
        # (Line 68) if(player == 3) { x=18; y=11; }
    EUDEndIf()
    if EUDIf()(player == 3):
        x << (18)
        y << (11)
        # (Line 69) if(player == 4) { x=1; y=6; }
    EUDEndIf()
    if EUDIf()(player == 4):
        x << (1)
        y << (6)
        # (Line 70) if(player == 5) { x=18; y=6; }
    EUDEndIf()
    if EUDIf()(player == 5):
        x << (18)
        y << (6)
        # (Line 72) const x2, y2 = Map.GetTileXY(x, y);
    EUDEndIf()
    x2, y2 = List2Assignable([Map.GetTileXY(x, y)])
    # (Line 73) Helpers.EUDSetLocation(loclist[player], x2, y2);
    Helpers.EUDSetLocation(loclist[player], x2, y2)
    # (Line 74) }
    # (Line 75) function InitPlayer(player)

# (Line 76) {
@EUDFunc
def InitPlayer(player):
    # (Line 77) SetPlayerEpd(player);
    SetPlayerEpd(player)
    # (Line 78) InitPlayerLocation(player);
    InitPlayerLocation(player)
    # (Line 79) CreateUnit(1, UnitID_Civilian, loclist[player]+1, player);
    DoActions(CreateUnit(1, UnitID_Civilian, loclist[player] + 1, player))
    # (Line 80) SetBombNumber(player, 1);
    SetBombNumber(player, 1)
    # (Line 81) SetBombRange(player, 1);
    SetBombRange(player, 1)
    # (Line 82) PlayerSpeed[player] = 1000;
    _ARRW(PlayerSpeed, player) << (1000)
    # (Line 83) if(Helpers.GetDeath(player, 216) == 0)
    if EUDIf()(Helpers.GetDeath(player, 216) == 0):
        # (Line 84) {
        # (Line 85) SetDeaths(player, SetTo, 1, 216);
        DoActions(SetDeaths(player, SetTo, 1, 216))
        # (Line 86) CenterView(loclist[player]+1);
        DoActions(CenterView(loclist[player] + 1))
        # (Line 87) }
        # (Line 88) }
    EUDEndIf()
    # (Line 89) function FollowLocation(player)

# (Line 90) {
@EUDFunc
def FollowLocation(player):
    # (Line 91) if(Command(player, AtLeast, 1, '(men)'))
    if EUDIf()(Command(player, AtLeast, 1, '(men)')):
        # (Line 92) MoveLocation(loclist[player]+1, '(men)', player, '20x13');
        DoActions(MoveLocation(loclist[player] + 1, '(men)', player, '20x13'))
        # (Line 93) }
    EUDEndIf()
    # (Line 94) function ItemCollect(player)

# (Line 95) {
@EUDFunc
def ItemCollect(player):
    # (Line 96) const item = GetItem(player);
    item = GetItem(player)
    # (Line 97) if(item != 0)
    if EUDIf()(item == 0, neg=True):
        # (Line 98) RemoveUnitAt(1, item, loclist[player]+1, Computer);
        DoActions(RemoveUnitAt(1, item, loclist[player] + 1, Computer))
        # (Line 99) }
    EUDEndIf()
    # (Line 101) function PlaceBomb(unitEpd)

# (Line 102) {
@EUDFunc
def PlaceBomb(unitEpd):
    # (Line 103) const player = Helpers.GetPlayerID(unitEpd);
    player = Helpers.GetPlayerID(unitEpd)
    # (Line 105) if(Helpers.GetBuildQueue1(unitEpd) == $U('Zerg Mutalisk'))
    if EUDIf()(Helpers.GetBuildQueue1(unitEpd) == EncodeUnit('Zerg Mutalisk')):
        # (Line 106) {
        # (Line 107) if(GetBombNumber(player) > GetCurrentBN(player))
        if EUDIf()(GetBombNumber(player) <= GetCurrentBN(player), neg=True):
            # (Line 108) {
            # (Line 109) const x, y = Map.GetTileIndex(unitEpd);
            x, y = List2Assignable([Map.GetTileIndex(unitEpd)])
            # (Line 110) const x2, y2 = Map.GetTileXY(x, y);
            x2, y2 = List2Assignable([Map.GetTileXY(x, y)])
            # (Line 111) Helpers.EUDSetLocation(loc, x2, y2);
            Helpers.EUDSetLocation(loc, x2, y2)
            # (Line 113) if(Map.GetMapXY(x,y) == 0)
            if EUDIf()(Map.GetMapXY(x, y) == 0):
                # (Line 114) {
                # (Line 115) const unitEpd = epdread_epd(EPD(0x628438));
                unitEpd_1 = f_epdread_epd(EPD(0x628438))
                # (Line 116) CreateUnit(1, UnitID_Bomb, loc +1, player);
                DoActions(CreateUnit(1, UnitID_Bomb, loc + 1, player))
                # (Line 117) Bomb.NewBomb(unitEpd);			// Mark at map
                Bomb.NewBomb(unitEpd_1)
                # (Line 118) SetBombWayBlock(unitEpd, 0); 	// no collision on egg
                SetBombWayBlock(unitEpd_1, 0)
                # (Line 119) SetBombTimer(unitEpd, 10); 		// bomb timer
                SetBombTimer(unitEpd_1, 10)
                # (Line 120) const range = GetBombRange(player);
                range = GetBombRange(player)
                # (Line 121) SetRangeAtBomb(unitEpd, range); // Mark bomb range inside bom
                SetRangeAtBomb(unitEpd_1, range)
                # (Line 122) }
                # (Line 123) }
            EUDEndIf()
            # (Line 125) Helpers.ResetBuildQueue(unitEpd);
        EUDEndIf()
        Helpers.ResetBuildQueue(unitEpd)
        # (Line 126) }
        # (Line 127) }
    EUDEndIf()
    # (Line 129) function SetBombWayBlock(unitEpd, bool)

# (Line 130) {//union offset(space for rally & psi)
@EUDFunc
def SetBombWayBlock(unitEpd, bool):
    # (Line 131) Helpers.SetBuildQueue1(unitEpd, bool);
    Helpers.SetBuildQueue1(unitEpd, bool)
    # (Line 132) }
    # (Line 133) function IsBombWayBlocked(unitEpd)

# (Line 134) {//union offset(space for rally & psi)
@EUDFunc
def IsBombWayBlocked(unitEpd):
    # (Line 135) const bool = Helpers.GetBuildQueue1(unitEpd);
    bool = Helpers.GetBuildQueue1(unitEpd)
    # (Line 136) if(bool == 0)
    if EUDIf()(bool == 0):
        # (Line 137) return 0;
        EUDReturn(0)
        # (Line 138) else
        # (Line 139) return 1;
    if EUDElse()():
        EUDReturn(1)
        # (Line 140) }
    EUDEndIf()
    # (Line 141) function SetBombTimer(unitEpd, time)

# (Line 142) {
@EUDFunc
def SetBombTimer(unitEpd, time):
    # (Line 143) SetMemoryEPD(unitEpd + 0x114/4, SetTo, time);
    DoActions(SetMemoryEPD(unitEpd + 0x114 // 4, SetTo, time))
    # (Line 144) }
    # (Line 145) function GetBombRange(player)

# (Line 146) {
@EUDFunc
def GetBombRange(player):
    # (Line 147) for(var i = 0; i<12; i++)
    i = EUDVariable()
    i << (0)
    if EUDWhile()(i >= 12, neg=True):
        def _t2():
            i.__iadd__(1)
        # (Line 148) if(Accumulate(player, Exactly, i, Gas))
        if EUDIf()(Accumulate(player, Exactly, i, Gas)):
            # (Line 149) return i;
            EUDReturn(i)
            # (Line 150) }
        EUDEndIf()
        EUDSetContinuePoint()
        _t2()
    EUDEndWhile()
    # (Line 151) function SetBombRange(player, number)

# (Line 152) {
@EUDFunc
def SetBombRange(player, number):
    # (Line 153) SetResources(player, SetTo, number, Gas);
    DoActions(SetResources(player, SetTo, number, Gas))
    # (Line 154) }
    # (Line 155) function GetCurrentBN(player)

# (Line 156) {
@EUDFunc
def GetCurrentBN(player):
    # (Line 157) for(var i = 0; i<12; i++)
    i = EUDVariable()
    i << (0)
    if EUDWhile()(i >= 12, neg=True):
        def _t2():
            i.__iadd__(1)
        # (Line 158) if(Command(player, Exactly, i, UnitID_Bomb))
        if EUDIf()(Command(player, Exactly, i, UnitID_Bomb)):
            # (Line 159) return i;
            EUDReturn(i)
            # (Line 161) }
        EUDEndIf()
        EUDSetContinuePoint()
        _t2()
    EUDEndWhile()
    # (Line 162) function GetBombNumber(player)

# (Line 163) {
@EUDFunc
def GetBombNumber(player):
    # (Line 164) for(var i = 0; i<12; i++)
    i = EUDVariable()
    i << (0)
    if EUDWhile()(i >= 12, neg=True):
        def _t2():
            i.__iadd__(1)
        # (Line 165) if(Accumulate(player, Exactly, i, Ore))
        if EUDIf()(Accumulate(player, Exactly, i, Ore)):
            # (Line 166) return i;
            EUDReturn(i)
            # (Line 167) }
        EUDEndIf()
        EUDSetContinuePoint()
        _t2()
    EUDEndWhile()
    # (Line 168) function SetBombNumber(player, number)

# (Line 169) {
@EUDFunc
def SetBombNumber(player, number):
    # (Line 170) SetResources(player, SetTo, number, Ore);
    DoActions(SetResources(player, SetTo, number, Ore))
    # (Line 171) }
    # (Line 173) function GetRangeAtBomb(unitEpd)

# (Line 174) {
@EUDFunc
def GetRangeAtBomb(unitEpd):
    # (Line 175) return dwread_epd(unitEpd + 0xFC/4);
    EUDReturn(f_dwread_epd(unitEpd + 0xFC // 4))
    # (Line 176) }
    # (Line 178) function SetRangeAtBomb(unitEpd, range)

# (Line 179) {//union offset(space for rally & psi)
@EUDFunc
def SetRangeAtBomb(unitEpd, range):
    # (Line 180) dwwrite_epd(unitEpd + 0xFC/4, range);
    f_dwwrite_epd(unitEpd + 0xFC // 4, range)
    # (Line 181) }
    # (Line 183) function GetItem(player)

# (Line 184) {
@EUDFunc
def GetItem(player):
    # (Line 185) for(var i=0; i<6; i++)
    i = EUDVariable()
    i << (0)
    if EUDWhile()(i >= 6, neg=True):
        def _t2():
            i.__iadd__(1)
        # (Line 186) {
        # (Line 187) const item = ItemList[i];
        item = ItemList[i]
        # (Line 188) if(Bring(Computer, AtLeast, 1, item, loclist[player]+1))
        if EUDIf()(Bring(Computer, AtLeast, 1, item, loclist[player] + 1)):
            # (Line 189) {
            # (Line 191) if(item == Item_rangeUp)
            if EUDIf()(item == Item_rangeUp):
                # (Line 192) {
                # (Line 193) const bombRange = GetBombRange(player);
                bombRange = GetBombRange(player)
                # (Line 194) if(bombRange < MaxRange)
                if EUDIf()(bombRange >= MaxRange, neg=True):
                    # (Line 195) {
                    # (Line 196) DisplayText("\x07[ Range + ]");
                    DoActions(DisplayText("\x07[ Range + ]"))
                    # (Line 197) SetBombRange(player, bombRange+1);
                    SetBombRange(player, bombRange + 1)
                    # (Line 198) return item;
                    EUDReturn(item)
                    # (Line 199) }
                    # (Line 200) return 0;
                EUDEndIf()
                EUDReturn(0)
                # (Line 201) }
                # (Line 203) if(item == Item_speedUp)
            EUDEndIf()
            if EUDIf()(item == Item_speedUp):
                # (Line 204) {
                # (Line 205) if(MemoryEPD(GetPlayerEpd(player) + 0x034 /4, AtMost, 1900) || PlayerSpeed[player] > 1900)
                if EUDIf()(EUDSCOr()(MemoryEPD(GetPlayerEpd(player) + 0x034 // 4, AtMost, 1900))(PlayerSpeed[player] <= 1900, neg=True)()):
                    # (Line 206) {
                    # (Line 207) DisplayText("\x07[ Speed + ]");
                    DoActions(DisplayText("\x07[ Speed + ]"))
                    # (Line 208) SetMemoryEPD(GetPlayerEpd(player) + 0x034 /4, Add, 100);
                    DoActions(SetMemoryEPD(GetPlayerEpd(player) + 0x034 // 4, Add, 100))
                    # (Line 209) PlayerSpeed[player] = PlayerSpeed[player] + 100;
                    _ARRW(PlayerSpeed, player) << (PlayerSpeed[player] + 100)
                    # (Line 210) return item;
                    EUDReturn(item)
                    # (Line 211) }
                    # (Line 212) return 0;
                EUDEndIf()
                EUDReturn(0)
                # (Line 213) }
                # (Line 215) if(item == Item_bombNUp)
            EUDEndIf()
            if EUDIf()(item == Item_bombNUp):
                # (Line 216) {
                # (Line 217) const bombNumber = GetBombNumber(player);
                bombNumber = GetBombNumber(player)
                # (Line 218) if(bombNumber < MaxBomb)
                if EUDIf()(bombNumber >= MaxBomb, neg=True):
                    # (Line 219) {
                    # (Line 220) DisplayText("\x07[ Bomb + ]");
                    DoActions(DisplayText("\x07[ Bomb + ]"))
                    # (Line 221) SetBombNumber(player, bombNumber+1);
                    SetBombNumber(player, bombNumber + 1)
                    # (Line 222) return item;
                    EUDReturn(item)
                    # (Line 223) }
                    # (Line 224) return 0;
                EUDEndIf()
                EUDReturn(0)
                # (Line 225) }
                # (Line 227) if(item == Item_rangeMax)
            EUDEndIf()
            if EUDIf()(item == Item_rangeMax):
                # (Line 228) {
                # (Line 229) const bombRange = GetBombRange(player);
                bombRange = GetBombRange(player)
                # (Line 230) if(bombRange < MaxRange)
                if EUDIf()(bombRange >= MaxRange, neg=True):
                    # (Line 231) {
                    # (Line 232) DisplayText("\x07[ Range ++ ]");
                    DoActions(DisplayText("\x07[ Range ++ ]"))
                    # (Line 233) SetBombRange(player, bombRange+2);
                    SetBombRange(player, bombRange + 2)
                    # (Line 234) return item;
                    EUDReturn(item)
                    # (Line 235) }
                    # (Line 236) return 0;
                EUDEndIf()
                EUDReturn(0)
                # (Line 237) }
                # (Line 239) if(item == Item_rideTank)
            EUDEndIf()
            if EUDIf()(item == Item_rideTank):
                # (Line 240) {
                # (Line 241) if(Command(player, Exactly, 1, UnitID_Civilian))
                if EUDIf()(Command(player, Exactly, 1, UnitID_Civilian)):
                    # (Line 242) {
                    # (Line 243) PlayerSpeed[player] = dwread_epd(GetPlayerEpd(player) + 0x034 /4);
                    _ARRW(PlayerSpeed, player) << (f_dwread_epd(GetPlayerEpd(player) + 0x034 // 4))
                    # (Line 244) RemoveUnit(UnitID_Civilian, player);
                    DoActions(RemoveUnit(UnitID_Civilian, player))
                    # (Line 245) SetPlayerEpd(player);
                    SetPlayerEpd(player)
                    # (Line 246) const chance = Helpers.GetRandom(0,2);
                    chance = Helpers.GetRandom(0, 2)
                    # (Line 247) if(chance == 1)
                    if EUDIf()(chance == 1):
                        # (Line 248) {
                        # (Line 249) CreateUnit(1, UnitID_Tank, loclist[player]+1, player);
                        DoActions(CreateUnit(1, UnitID_Tank, loclist[player] + 1, player))
                        # (Line 250) SetDeaths(player, SetTo, 1, UnitID_Tank);
                        DoActions(SetDeaths(player, SetTo, 1, UnitID_Tank))
                        # (Line 251) }
                        # (Line 252) else
                        # (Line 253) {
                    if EUDElse()():
                        # (Line 254) CreateUnit(1, UnitID_Goliath, loclist[player]+1, player);
                        DoActions(CreateUnit(1, UnitID_Goliath, loclist[player] + 1, player))
                        # (Line 255) SetDeaths(player, SetTo, 1, UnitID_Goliath);
                        DoActions(SetDeaths(player, SetTo, 1, UnitID_Goliath))
                        # (Line 256) }
                        # (Line 257) return item;
                    EUDEndIf()
                    EUDReturn(item)
                    # (Line 258) }
                    # (Line 259) return 0;
                EUDEndIf()
                EUDReturn(0)
                # (Line 261) }
                # (Line 262) if(item == Item_rideHide)
            EUDEndIf()
            if EUDIf()(item == Item_rideHide):
                # (Line 263) {
                # (Line 264) if(1)
                if EUDIf()(1):
                    # (Line 265) {
                    # (Line 269) DisplayText("\x07똥을 밟았다.");
                    DoActions(DisplayText("\x07똥을 밟았다."))
                    # (Line 270) return item;
                    EUDReturn(item)
                    # (Line 271) }
                    # (Line 272) return 0;
                EUDEndIf()
                EUDReturn(0)
                # (Line 274) }
                # (Line 275) }
            EUDEndIf()
            # (Line 276) }
        EUDEndIf()
        # (Line 277) }
        EUDSetContinuePoint()
        _t2()
    EUDEndWhile()
    # (Line 279) function OffRide(player)

# (Line 280) {
@EUDFunc
def OffRide(player):
    # (Line 281) if(Command(player, Exactly, 0, '(men)'))
    if EUDIf()(Command(player, Exactly, 0, '(men)')):
        # (Line 282) {
        # (Line 283) if(Helpers.GetDeath(player, UnitID_Tank) > 0 || Helpers.GetDeath(player, UnitID_Goliath) > 0)
        if EUDIf()(EUDSCOr()(Helpers.GetDeath(player, UnitID_Tank) <= 0, neg=True)(Helpers.GetDeath(player, UnitID_Goliath) <= 0, neg=True)()):
            # (Line 284) {
            # (Line 285) if(Bomb.boom == 0)
            if EUDIf()(Bomb.boom == 0):
                # (Line 286) {
                # (Line 287) SetPlayerEpd(player);
                SetPlayerEpd(player)
                # (Line 288) CreateUnit(1, UnitID_Civilian, loclist[player]+1, player);
                DoActions(CreateUnit(1, UnitID_Civilian, loclist[player] + 1, player))
                # (Line 289) SetMemoryEPD(GetPlayerEpd(player) + 0x034 /4, SetTo, PlayerSpeed[player]);
                DoActions(SetMemoryEPD(GetPlayerEpd(player) + 0x034 // 4, SetTo, PlayerSpeed[player]))
                # (Line 290) SetDeaths(player, SetTo, 0, UnitID_Tank);
                DoActions(SetDeaths(player, SetTo, 0, UnitID_Tank))
                # (Line 291) SetDeaths(player, SetTo, 0, UnitID_Goliath);
                DoActions(SetDeaths(player, SetTo, 0, UnitID_Goliath))
                # (Line 292) }
                # (Line 293) }
            EUDEndIf()
            # (Line 294) }
        EUDEndIf()
        # (Line 295) }
    EUDEndIf()
