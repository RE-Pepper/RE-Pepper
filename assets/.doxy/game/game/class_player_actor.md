

# Class PlayerActor



[**ClassList**](annotated.md) **>** [**PlayerActor**](class_player_actor.md)





* `#include <PlayerActor.h>`



Inherits the following classes: al::MapObjActor


















## Public Attributes

| Type | Name |
| ---: | :--- |
|  void \* | [**\_100**](#variable-_100)  <br> |
|  void \* | [**\_104**](#variable-_104)  <br> |
|  void \* | [**\_108**](#variable-_108)  <br> |
|  void \* | [**\_10C**](#variable-_10c)  <br> |
|  void \* | [**\_110**](#variable-_110)  <br> |
|  void \* | [**\_114**](#variable-_114)  <br> |
|  void \* | [**\_118**](#variable-_118)  <br> |
|  void \* | [**\_11C**](#variable-_11c)  <br> |
|  void \* | [**\_120**](#variable-_120)  <br> |
|  void \* | [**\_124**](#variable-_124)  <br> |
|  void \* | [**\_128**](#variable-_128)  <br> |
|  void \* | [**\_12C**](#variable-_12c)  <br> |
|  void \* | [**\_130**](#variable-_130)  <br> |
|  void \* | [**\_134**](#variable-_134)  <br> |
|  void \* | [**\_138**](#variable-_138)  <br> |
|  void \* | [**\_13C**](#variable-_13c)  <br> |
|  void \* | [**\_140**](#variable-_140)  <br> |
|  void \* | [**\_144**](#variable-_144)  <br> |
|  void \* | [**\_148**](#variable-_148)  <br> |
|  void \* | [**\_14C**](#variable-_14c)  <br> |
|  void \* | [**\_150**](#variable-_150)  <br> |
|  void \* | [**\_154**](#variable-_154)  <br> |
|  void \* | [**\_158**](#variable-_158)  <br> |
|  void \* | [**\_60**](#variable-_60)  <br> |
|  void \* | [**\_64**](#variable-_64)  <br> |
|  void \* | [**\_68**](#variable-_68)  <br> |
|  void \* | [**\_6C**](#variable-_6c)  <br> |
|  void \* | [**\_70**](#variable-_70)  <br> |
|  void \* | [**\_78**](#variable-_78)  <br> |
|  void \* | [**\_80**](#variable-_80)  <br> |
|  void \* | [**\_84**](#variable-_84)  <br> |
|  void \* | [**\_88**](#variable-_88)  <br> |
|  void \* | [**\_8C**](#variable-_8c)  <br> |
|  void \* | [**\_90**](#variable-_90)  <br> |
|  void \* | [**\_94**](#variable-_94)  <br> |
|  void \* | [**\_98**](#variable-_98)  <br> |
|  void \* | [**\_9C**](#variable-_9c)  <br> |
|  void \* | [**\_A0**](#variable-_a0)  <br> |
|  void \* | [**\_A8**](#variable-_a8)  <br> |
|  void \* | [**\_AC**](#variable-_ac)  <br> |
|  void \* | [**\_B0**](#variable-_b0)  <br> |
|  void \* | [**\_B4**](#variable-_b4)  <br> |
|  void \* | [**\_B8**](#variable-_b8)  <br> |
|  void \* | [**\_BC**](#variable-_bc)  <br> |
|  void \* | [**\_C0**](#variable-_c0)  <br> |
|  void \* | [**\_C4**](#variable-_c4)  <br> |
|  void \* | [**\_C8**](#variable-_c8)  <br> |
|  void \* | [**\_CC**](#variable-_cc)  <br> |
|  void \* | [**\_D0**](#variable-_d0)  <br> |
|  void \* | [**\_D4**](#variable-_d4)  <br> |
|  void \* | [**\_D8**](#variable-_d8)  <br> |
|  void \* | [**\_Dc**](#variable-_dc)  <br> |
|  void \* | [**\_E0**](#variable-_e0)  <br> |
|  void \* | [**\_E4**](#variable-_e4)  <br> |
|  void \* | [**\_E8**](#variable-_e8)  <br> |
|  void \* | [**\_EC**](#variable-_ec)  <br> |
|  void \* | [**\_F0**](#variable-_f0)  <br> |
|  void \* | [**\_F4**](#variable-_f4)  <br> |
|  void \* | [**\_F8**](#variable-_f8)  <br> |
|  void \* | [**\_FC**](#variable-_fc)  <br> |
|  [**PlayerModelHolder**](class_player_model_holder.md) \* | [**mModelHolder**](#variable-mmodelholder)  <br> |
|  [**Player**](class_player.md) \* | [**mPlayer**](#variable-mplayer)  <br> |
|  [**PlayerAnimator**](class_player_animator.md) \* | [**mPlayerAnimator**](#variable-mplayeranimator)  <br> |
















## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**PlayerActor**](#function-playeractor) (const char \* name) <br> |
| virtual void | [**attackSensor**](#function-attacksensor) (al::HitSensor \* me, al::HitSensor \* other) <br> |
| virtual void | [**control**](#function-control) () <br> |
|  [**PlayerProperty**](class_player_property.md) \* | [**getProperty**](#function-getproperty) () <br> |
| virtual void | [**initSpecial**](#function-initspecial) (const al::ActorInitInfo & info, const [**PlayerActorInitInfo**](class_player_actor_init_info.md) & playerInfo) <br> |
| virtual void | [**movement**](#function-movement) () <br> |
| virtual bool | [**receiveMsg**](#function-receivemsg) (u32 msg, al::HitSensor \* other, al::HitSensor \* me) <br> |
| virtual void | [**updateCollider**](#function-updatecollider) () <br> |
| virtual void | [**v\_64**](#function-v_64) () <br> |
| virtual void | [**v\_68**](#function-v_68) () <br> |
| virtual void | [**v\_6c**](#function-v_6c) () <br> |




























## Public Attributes Documentation




### variable \_100 

```C++
void* PlayerActor::_100;
```




<hr>



### variable \_104 

```C++
void* PlayerActor::_104;
```




<hr>



### variable \_108 

```C++
void* PlayerActor::_108;
```




<hr>



### variable \_10C 

```C++
void* PlayerActor::_10C;
```




<hr>



### variable \_110 

```C++
void* PlayerActor::_110;
```




<hr>



### variable \_114 

```C++
void* PlayerActor::_114;
```




<hr>



### variable \_118 

```C++
void* PlayerActor::_118;
```




<hr>



### variable \_11C 

```C++
void* PlayerActor::_11C;
```




<hr>



### variable \_120 

```C++
void* PlayerActor::_120;
```




<hr>



### variable \_124 

```C++
void* PlayerActor::_124;
```




<hr>



### variable \_128 

```C++
void* PlayerActor::_128;
```




<hr>



### variable \_12C 

```C++
void* PlayerActor::_12C;
```




<hr>



### variable \_130 

```C++
void* PlayerActor::_130;
```




<hr>



### variable \_134 

```C++
void* PlayerActor::_134;
```




<hr>



### variable \_138 

```C++
void* PlayerActor::_138;
```




<hr>



### variable \_13C 

```C++
void* PlayerActor::_13C;
```




<hr>



### variable \_140 

```C++
void* PlayerActor::_140;
```




<hr>



### variable \_144 

```C++
void* PlayerActor::_144;
```




<hr>



### variable \_148 

```C++
void* PlayerActor::_148;
```




<hr>



### variable \_14C 

```C++
void* PlayerActor::_14C;
```




<hr>



### variable \_150 

```C++
void* PlayerActor::_150;
```




<hr>



### variable \_154 

```C++
void* PlayerActor::_154;
```




<hr>



### variable \_158 

```C++
void* PlayerActor::_158;
```




<hr>



### variable \_60 

```C++
void* PlayerActor::_60;
```




<hr>



### variable \_64 

```C++
void* PlayerActor::_64;
```




<hr>



### variable \_68 

```C++
void* PlayerActor::_68;
```




<hr>



### variable \_6C 

```C++
void* PlayerActor::_6C;
```




<hr>



### variable \_70 

```C++
void* PlayerActor::_70;
```




<hr>



### variable \_78 

```C++
void* PlayerActor::_78;
```




<hr>



### variable \_80 

```C++
void* PlayerActor::_80;
```




<hr>



### variable \_84 

```C++
void* PlayerActor::_84;
```




<hr>



### variable \_88 

```C++
void* PlayerActor::_88;
```




<hr>



### variable \_8C 

```C++
void* PlayerActor::_8C;
```




<hr>



### variable \_90 

```C++
void* PlayerActor::_90;
```




<hr>



### variable \_94 

```C++
void* PlayerActor::_94;
```




<hr>



### variable \_98 

```C++
void* PlayerActor::_98;
```




<hr>



### variable \_9C 

```C++
void* PlayerActor::_9C;
```




<hr>



### variable \_A0 

```C++
void* PlayerActor::_A0;
```




<hr>



### variable \_A8 

```C++
void* PlayerActor::_A8;
```




<hr>



### variable \_AC 

```C++
void* PlayerActor::_AC;
```




<hr>



### variable \_B0 

```C++
void* PlayerActor::_B0;
```




<hr>



### variable \_B4 

```C++
void* PlayerActor::_B4;
```




<hr>



### variable \_B8 

```C++
void* PlayerActor::_B8;
```




<hr>



### variable \_BC 

```C++
void* PlayerActor::_BC;
```




<hr>



### variable \_C0 

```C++
void* PlayerActor::_C0;
```




<hr>



### variable \_C4 

```C++
void* PlayerActor::_C4;
```




<hr>



### variable \_C8 

```C++
void* PlayerActor::_C8;
```




<hr>



### variable \_CC 

```C++
void* PlayerActor::_CC;
```




<hr>



### variable \_D0 

```C++
void* PlayerActor::_D0;
```




<hr>



### variable \_D4 

```C++
void* PlayerActor::_D4;
```




<hr>



### variable \_D8 

```C++
void* PlayerActor::_D8;
```




<hr>



### variable \_Dc 

```C++
void* PlayerActor::_Dc;
```




<hr>



### variable \_E0 

```C++
void* PlayerActor::_E0;
```




<hr>



### variable \_E4 

```C++
void* PlayerActor::_E4;
```




<hr>



### variable \_E8 

```C++
void* PlayerActor::_E8;
```




<hr>



### variable \_EC 

```C++
void* PlayerActor::_EC;
```




<hr>



### variable \_F0 

```C++
void* PlayerActor::_F0;
```




<hr>



### variable \_F4 

```C++
void* PlayerActor::_F4;
```




<hr>



### variable \_F8 

```C++
void* PlayerActor::_F8;
```




<hr>



### variable \_FC 

```C++
void* PlayerActor::_FC;
```




<hr>



### variable mModelHolder 

```C++
PlayerModelHolder* PlayerActor::mModelHolder;
```




<hr>



### variable mPlayer 

```C++
Player* PlayerActor::mPlayer;
```




<hr>



### variable mPlayerAnimator 

```C++
PlayerAnimator* PlayerActor::mPlayerAnimator;
```




<hr>
## Public Functions Documentation




### function PlayerActor 

```C++
PlayerActor::PlayerActor (
    const char * name
) 
```




<hr>



### function attackSensor 

```C++
virtual void PlayerActor::attackSensor (
    al::HitSensor * me,
    al::HitSensor * other
) 
```




<hr>



### function control 

```C++
virtual void PlayerActor::control () 
```




<hr>



### function getProperty 

```C++
PlayerProperty * PlayerActor::getProperty () 
```




<hr>



### function initSpecial 

```C++
virtual void PlayerActor::initSpecial (
    const al::ActorInitInfo & info,
    const PlayerActorInitInfo & playerInfo
) 
```




<hr>



### function movement 

```C++
virtual void PlayerActor::movement () 
```




<hr>



### function receiveMsg 

```C++
virtual bool PlayerActor::receiveMsg (
    u32 msg,
    al::HitSensor * other,
    al::HitSensor * me
) 
```




<hr>



### function updateCollider 

```C++
virtual void PlayerActor::updateCollider () 
```




<hr>



### function v\_64 

```C++
virtual void PlayerActor::v_64 () 
```




<hr>



### function v\_68 

```C++
virtual void PlayerActor::v_68 () 
```




<hr>



### function v\_6c 

```C++
virtual void PlayerActor::v_6c () 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `Game/backup/include/Player/PlayerActor.h`

