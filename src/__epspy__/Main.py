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

# (Line 1) import Player;
import Player
# (Line 2) import Bomb;
import Bomb
# (Line 3) import Map;
import Map
# (Line 5) var GameState;
GameState = EUDVariable()
# (Line 7) function onPluginStart()
# (Line 8) {
@EUDFunc
def onPluginStart():
    # (Line 9) randomize();
    f_randomize()
    # (Line 10) LeaderBoardComputerPlayers(Disable);
    DoActions(LeaderBoardComputerPlayers(Disable))
    # (Line 11) LeaderBoardScore(Custom, "/2");
    DoActions(LeaderBoardScore(Custom, "/2"))
    # (Line 12) }
    # (Line 13) function RoundStart();

# (Line 14) function RoundEnd();
# (Line 15) function DisplayTextToAllPlayers(number);
# (Line 16) function GameEnd(player);
# (Line 17) function beforeTriggerExec()
# (Line 18) {
@EUDFunc
def beforeTriggerExec():
    # (Line 19) if(GameState == 0)
    if EUDIf()(GameState == 0):
        # (Line 20) {
        # (Line 21) RoundStart();
        RoundStart()
        # (Line 22) }
        # (Line 24) if(GameState == 1)
    EUDEndIf()
    if EUDIf()(GameState == 1):
        # (Line 25) {
        # (Line 26) Bomb.CheckBomb();
        Bomb.CheckBomb()
        # (Line 27) EUDPlayerLoop()();
        EUDPlayerLoop()()
        # (Line 28) var player = getcurpl();
        player = EUDVariable()
        player << (f_getcurpl())
        # (Line 29) if(player < 6)
        if EUDIf()(player >= 6, neg=True):
            # (Line 30) {
            # (Line 31) Player.PlaceBomb(Player.GetPlayerEpd(player));
            Player.PlaceBomb(Player.GetPlayerEpd(player))
            # (Line 32) Player.FollowLocation(player);
            Player.FollowLocation(player)
            # (Line 33) Player.ItemCollect(player);
            Player.ItemCollect(player)
            # (Line 34) Player.OffRide(player);
            Player.OffRide(player)
            # (Line 35) }
            # (Line 36) EUDEndPlayerLoop();
        EUDEndIf()
        EUDEndPlayerLoop()
        # (Line 37) RoundEnd();
        RoundEnd()
        # (Line 38) }
        # (Line 40) }
    EUDEndIf()
    # (Line 42) function afterTriggerExec()

# (Line 43) {
@EUDFunc
def afterTriggerExec():
    # (Line 45) SetMemory(0x6509A0, SetTo, 0);
    DoActions(SetMemory(0x6509A0, SetTo, 0))
    # (Line 46) }
    # (Line 47) function RoundStart()

# (Line 48) {
@EUDFunc
def RoundStart():
    # (Line 49) Map.ClearMap();
    Map.ClearMap()
    # (Line 50) Map.GetMap();
    Map.GetMap()
    # (Line 51) Map.Render();
    Map.Render()
    # (Line 53) EUDPlayerLoop()();
    EUDPlayerLoop()()
    # (Line 54) var player = getcurpl();
    player = EUDVariable()
    player << (f_getcurpl())
    # (Line 55) if(player < 6) //P1~P6
    if EUDIf()(player >= 6, neg=True):
        # (Line 56) Player.InitPlayer(player);
        Player.InitPlayer(player)
        # (Line 57) EUDEndPlayerLoop();
    EUDEndIf()
    EUDEndPlayerLoop()
    # (Line 58) GameState = 1; // <------------------
    GameState << (1)
    # (Line 59) }
    # (Line 61) function RoundEnd()

# (Line 62) {
@EUDFunc
def RoundEnd():
    # (Line 64) if(Command($Force1, AtMost, 1, '(men)') &&
    _t1 = EUDIf()
    # (Line 65) Command(7, Exactly, 0, 15) &&
    # (Line 66) Accumulate($Force1, AtLeast, 1, OreAndGas))
    if _t1(EUDSCAnd()(Command(18, AtMost, 1, '(men)'))(Command(7, Exactly, 0, 15))(Accumulate(18, AtLeast, 1, OreAndGas))()):
        # (Line 67) {//Time Counter
        # (Line 68) SetDeaths(7, Add, 1, 200);
        DoActions(SetDeaths(7, Add, 1, 200))
        # (Line 69) }
        # (Line 70) if(Deaths(7, AtLeast, 24, 200))
    EUDEndIf()
    if EUDIf()(Deaths(7, AtLeast, 24, 200)):
        # (Line 71) {
        # (Line 72) if(Command($Force1, AtMost, 1, '(men)'))
        if EUDIf()(Command(18, AtMost, 1, '(men)')):
            # (Line 73) {
            # (Line 74) EUDPlayerLoop()();
            EUDPlayerLoop()()
            # (Line 75) const player = getcurpl();
            player = f_getcurpl()
            # (Line 76) if(Command(player, Exactly, 1, '(men)'))
            if EUDIf()(Command(player, Exactly, 1, '(men)')):
                # (Line 77) {
                # (Line 78) SetScore(player, Add, 1, Custom);	// win score
                DoActions(SetScore(player, Add, 1, Custom))
                # (Line 79) DisplayTextToAllPlayers(player);
                DisplayTextToAllPlayers(player)
                # (Line 80) }
                # (Line 81) GameEnd(player);
            EUDEndIf()
            GameEnd(player)
            # (Line 82) EUDEndPlayerLoop();
            EUDEndPlayerLoop()
            # (Line 83) GameState = 0; // <------------------
            GameState << (0)
            # (Line 84) SetDeaths(7, SetTo, 0, 200);
            DoActions(SetDeaths(7, SetTo, 0, 200))
            # (Line 85) LeaderBoardScore(Custom, "/2");
            DoActions(LeaderBoardScore(Custom, "/2"))
            # (Line 86) }
            # (Line 87) else
            # (Line 88) SetDeaths(7, SetTo, 0, 200);
        if EUDElse()():
            DoActions(SetDeaths(7, SetTo, 0, 200))
            # (Line 89) }
        EUDEndIf()
        # (Line 91) }
    EUDEndIf()
    # (Line 93) function GameEnd(player)

# (Line 94) {
@EUDFunc
def GameEnd(player):
    # (Line 95) for(var i=0; i<6; i++)
    i = EUDVariable()
    i << (0)
    if EUDWhile()(i >= 6, neg=True):
        def _t2():
            i.__iadd__(1)
        # (Line 96) {
        # (Line 97) if (Score(i, Custom, Exactly, 2))
        if EUDIf()(Score(i, Custom, Exactly, 2)):
            # (Line 98) {
            # (Line 99) DisplayTextToAllPlayers(i);
            DisplayTextToAllPlayers(i)
            # (Line 100) Victory();
            DoActions(Victory())
            # (Line 101) }
            # (Line 102) }
        EUDEndIf()
        # (Line 103) }
        EUDSetContinuePoint()
        _t2()
    EUDEndWhile()
    # (Line 105) function DisplayTextToAllPlayers(number)

# (Line 106) {
@EUDFunc
def DisplayTextToAllPlayers(number):
    # (Line 107) EUDPlayerLoop()();
    EUDPlayerLoop()()
    # (Line 108) if(number == 0) DisplayText("\r\n\r\n\r\n\r\n\r\n\x13빨강이 이겼다\r\n\r\n\r\n\r\n\r\n");
    if EUDIf()(number == 0):
        DoActions(DisplayText("\r\n\r\n\r\n\r\n\r\n\x13빨강이 이겼다\r\n\r\n\r\n\r\n\r\n"))
        # (Line 109) else if(number == 1) DisplayText("\r\n\r\n\r\n\r\n\r\n\x13파랑이 이겼다\r\n\r\n\r\n\r\n\r\n");
    if EUDElseIf()(number == 1):
        DoActions(DisplayText("\r\n\r\n\r\n\r\n\r\n\x13파랑이 이겼다\r\n\r\n\r\n\r\n\r\n"))
        # (Line 110) else if(number == 2) DisplayText("\r\n\r\n\r\n\r\n\r\n\x13연두가 이겼다\r\n\r\n\r\n\r\n\r\n");
    if EUDElseIf()(number == 2):
        DoActions(DisplayText("\r\n\r\n\r\n\r\n\r\n\x13연두가 이겼다\r\n\r\n\r\n\r\n\r\n"))
        # (Line 111) else if(number == 3) DisplayText("\r\n\r\n\r\n\r\n\r\n\x13보라가 이겼다\r\n\r\n\r\n\r\n\r\n");
    if EUDElseIf()(number == 3):
        DoActions(DisplayText("\r\n\r\n\r\n\r\n\r\n\x13보라가 이겼다\r\n\r\n\r\n\r\n\r\n"))
        # (Line 112) else if(number == 4) DisplayText("\r\n\r\n\r\n\r\n\r\n\x13주황이 이겼다\r\n\r\n\r\n\r\n\r\n");
    if EUDElseIf()(number == 4):
        DoActions(DisplayText("\r\n\r\n\r\n\r\n\r\n\x13주황이 이겼다\r\n\r\n\r\n\r\n\r\n"))
        # (Line 113) else if(number == 5) DisplayText("\r\n\r\n\r\n\r\n\r\n\x13똥색이 이겼다\r\n\r\n\r\n\r\n\r\n");
    if EUDElseIf()(number == 5):
        DoActions(DisplayText("\r\n\r\n\r\n\r\n\r\n\x13똥색이 이겼다\r\n\r\n\r\n\r\n\r\n"))
        # (Line 114) EUDEndPlayerLoop();
    EUDEndIf()
    EUDEndPlayerLoop()
    # (Line 115) }
