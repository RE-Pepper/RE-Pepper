

# Class FireBall



[**ClassList**](annotated.md) **>** [**FireBall**](class_fire_ball.md)





* `#include <FireBall.h>`



Inherits the following classes: al::MapObjActor


































## Public Functions

| Type | Name |
| ---: | :--- |
|   | [**FireBall**](#function-fireball) (const sead::SafeString & name) <br> |
| virtual void | [**attackSensor**](#function-attacksensor) (al::HitSensor \* me, al::HitSensor \* other) <br> |
|  void | [**exeShot**](#function-exeshot) () <br> |
| virtual void | [**init**](#function-init) (const al::ActorInitInfo & info) <br> |
| virtual bool | [**receiveMsg**](#function-receivemsg) (u32 msg, al::HitSensor \* other, al::HitSensor \* me) <br> |




























## Public Functions Documentation




### function FireBall 

```C++
FireBall::FireBall (
    const sead::SafeString & name
) 
```




<hr>



### function attackSensor 

```C++
virtual void FireBall::attackSensor (
    al::HitSensor * me,
    al::HitSensor * other
) 
```




<hr>



### function exeShot 

```C++
void FireBall::exeShot () 
```




<hr>



### function init 

```C++
virtual void FireBall::init (
    const al::ActorInitInfo & info
) 
```




<hr>



### function receiveMsg 

```C++
virtual bool FireBall::receiveMsg (
    u32 msg,
    al::HitSensor * other,
    al::HitSensor * me
) 
```




<hr>

------------------------------
The documentation for this class was generated from the following file `Game/backup/include/Enemy/FireBall.h`

