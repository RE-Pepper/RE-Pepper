

# Class GhostPlayer



[**ClassList**](annotated.md) **>** [**GhostPlayer**](class_ghost_player.md)





* `#include <GhostPlayer.h>`



Inherits the following classes: al::MapObjActor


































## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**GhostPlayer**](#function-ghostplayer) (const sead::SafeString & name) <br> |
| virtual void | [**attackSensor**](#function-attacksensor) (al::HitSensor \* me, al::HitSensor \* other) <br> |
| virtual void | [**control**](#function-control) () <br> |
|  void | [**exeBegin**](#function-exebegin) () <br> |
|  void | [**exeHide**](#function-exehide) () <br> |
|  void | [**exeNrv5**](#function-exenrv5) () <br> |
| virtual void | [**init**](#function-init) (const al::ActorInitInfo & info) <br> |
| virtual void | [**kill**](#function-kill) () <br> |
| virtual bool | [**receiveMsg**](#function-receivemsg) (u32 msg, al::HitSensor \* other, al::HitSensor \* me) <br> |




























## Public Functions Documentation




### function GhostPlayer 

```C++
GhostPlayer::GhostPlayer (
    const sead::SafeString & name
) 
```




<hr>



### function attackSensor 

```C++
virtual void GhostPlayer::attackSensor (
    al::HitSensor * me,
    al::HitSensor * other
) 
```




<hr>



### function control 

```C++
virtual void GhostPlayer::control () 
```




<hr>



### function exeBegin 

```C++
void GhostPlayer::exeBegin () 
```




<hr>



### function exeHide 

```C++
void GhostPlayer::exeHide () 
```




<hr>



### function exeNrv5 

```C++
void GhostPlayer::exeNrv5 () 
```




<hr>



### function init 

```C++
virtual void GhostPlayer::init (
    const al::ActorInitInfo & info
) 
```




<hr>



### function kill 

```C++
virtual void GhostPlayer::kill () 
```




<hr>



### function receiveMsg 

```C++
virtual bool GhostPlayer::receiveMsg (
    u32 msg,
    al::HitSensor * other,
    al::HitSensor * me
) 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `Game/backup/include/Player/GhostPlayer.h`

