# -*- coding: utf-8 -*-
# @StartTime : 9/5/2017 17:35
# @EndTime   : 9/21/2017 17:35
# @Author    : Andy
# @Site      : 
# @File      : YYS01.py
# @Software  : PyCharm

"""This program tends to figure out Heroes of Class Zhennv in YYS with the problem which is the best choice,
        Attack Bonus or  Critical damage, based on Critical strike is 100%  """

# 使用式神 妖刀姬
# 情况1：BOSS血量远大于10万
# 假设24号位攻击加成， 6号位爆伤；
# 1-6号位均有暴击，爆伤，攻击加成等属性。
# 六星暴击副属性满17%，
# 六星攻击加成副属性满17%
# 六星爆伤副属性满22%
# 必要条件：满暴击。
#


maxCriticalDamage=0.22
maxCriticalStrike=0.17
maxCriticalAttack=0.17

#妖刀基础面板
baseAttack=3270
baseCriticalDamge=1.5
baseCritical=0.12


#初始化1-6号位主属性，
yu1=486
yu2=0.55
yu4=0.55
#平均每次副属性加成
bonusAttack=0.17/6
bonusCriticalDamage=0.22/6

# 六号位副属性加成共为5*6=30次
# 假设都有基础攻击加成，爆伤，暴击
# 需要堆暴击次数
neededCritical=1-baseCritical-0.3-bonusAttack*6
# neededCritical=1-0.12-0.3-0.17=0.41
freeAllocated=int(30-neededCritical/bonusAttack)
# 15次

# i 为分配到攻击加成上的次数，则15-i 为分配到爆伤上面的次数。
# 假设：
#   6号位爆伤的情况
#   BOSS防御500
#   攻击伤害=攻击值*防御/（防御+300）

def trueShanghai(attack):
    fangyu=500
    return attack*fangyu/(fangyu+300)

yu6Damage=0.89
maxSum=0
suoyin=-1

for i in range(0,freeAllocated):
    sumAttack=baseAttack+baseAttack*(yu2+yu4+i*bonusAttack)+yu1
    sumCriticalDamage=baseCriticalDamge+(freeAllocated-i)*bonusCriticalDamage+yu6Damage
    # 妖刀三技能，六次攻击，每次攻击造成攻击60%的伤害，20%几率概率造成自身攻击40%额外伤害
    # 针女，40%几率目标10%伤害，最高120%自身攻击力
    zhenNv=0.4*6*1.2*sumAttack
    sumX=6*trueShanghai(0.6*sumAttack*sumCriticalDamage)+zhenNv+6*0.2*sumAttack*0.4
    print(sumX,i)

    if sumX>maxSum:
        maxSum=sumX
        suoyin=i

print('baoshang')
print(maxSum,suoyin)




#  六号位暴击情况下呢？
#  攻击加成两件套，30次全分配给爆伤和攻击加成
maxSum=0
suoyin=-1
for i in range(0,30):
    sumAttack=baseAttack+baseAttack*(yu2+yu4+i*bonusAttack+0.15)+yu1
    sumCriticalDamage=baseCriticalDamge+(freeAllocated-i)*bonusCriticalDamage
    # 妖刀三技能，六次攻击，每次攻击造成攻击60%的伤害，20%几率概率造成自身攻击40%额外伤害
    # 针女，40%几率目标10%伤害，最高120%自身攻击力
    zhenNv=0.4*6*1.2*sumAttack
    sumX=6*trueShanghai(0.6*sumAttack*sumCriticalDamage)+zhenNv+6*0.2*sumAttack*0.4
    print(sumX,i)

    if sumX>maxSum:
        maxSum=sumX
        suoyin=i

print('baoji')
print(maxSum,suoyin)


#  六号位攻击加成情况下呢？
maxSum=0
suoyin=-1
for i in range(0,freeAllocated):
    sumAttack=baseAttack+baseAttack*(yu2+yu4+i*bonusAttack+0.55)+yu1
    sumCriticalDamage=baseCriticalDamge+(freeAllocated-i)*bonusCriticalDamage
    # 妖刀三技能，六次攻击，每次攻击造成攻击60%的伤害，20%几率概率造成自身攻击40%额外伤害
    # 针女，40%几率目标10%伤害，最高120%自身攻击力
    zhenNv=0.4*6*1.2*sumAttack
    sumX=6*trueShanghai(0.6*sumAttack*sumCriticalDamage)+zhenNv+6*0.2*sumAttack*0.4
    print(sumX,i)

    if sumX>maxSum:
        maxSum=sumX
        suoyin=i

print('gongji:')
print(maxSum,suoyin)




